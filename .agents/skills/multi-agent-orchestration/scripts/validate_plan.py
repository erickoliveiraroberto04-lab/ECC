#!/usr/bin/env python3
"""Validate the declared structure and guardrails of a JSON orchestration plan."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import defaultdict, deque
from pathlib import Path
from typing import Any


ID_PATTERN = re.compile(r"^[a-z][a-z0-9_-]{0,63}$")
TAG_PATTERN = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
APPROVAL_REQUIRED_TAGS = {"consequential", "deploy", "external-mutation"}
MAX_TIMEOUT_SECONDS = 86_400
MAX_ATTEMPTS = 10
MAX_RETRY_BACKOFF_SECONDS = 3_600


def nonempty_text(value: Any, label: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty string")
        return ""
    return value.strip()


def optional_text(value: Any, label: str, errors: list[str]) -> str | None:
    if value is None:
        return None
    text = nonempty_text(value, label, errors)
    return text or None


def string_list(value: Any, label: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{label} must be an array")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        text = nonempty_text(item, f"{label}[{index}]", errors)
        if text:
            result.append(text)
    if len(result) != len(set(result)):
        errors.append(f"{label} contains duplicates")
    return result


def bounded_number(
    value: Any,
    label: str,
    errors: list[str],
    *,
    minimum: float,
    maximum: float,
) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        errors.append(f"{label} must be a number")
        return None
    result = float(value)
    if not math.isfinite(result):
        errors.append(f"{label} must be finite")
        return None
    if not minimum <= result <= maximum:
        errors.append(f"{label} must be between {minimum:g} and {maximum:g}")
        return None
    return result


def bounded_integer(
    value: Any,
    label: str,
    errors: list[str],
    *,
    minimum: int,
    maximum: int,
) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int):
        errors.append(f"{label} must be an integer")
        return None
    if not minimum <= value <= maximum:
        errors.append(f"{label} must be between {minimum} and {maximum}")
        return None
    return value


def topological_order(tasks: dict[str, dict[str, Any]]) -> tuple[list[str], list[str]]:
    indegree = {task_id: 0 for task_id in tasks}
    children: dict[str, list[str]] = defaultdict(list)
    errors: list[str] = []
    for task_id, task in tasks.items():
        for dependency in task["depends_on"]:
            if dependency not in tasks:
                errors.append(f"task {task_id!r} depends on unknown task {dependency!r}")
                continue
            if dependency == task_id:
                errors.append(f"task {task_id!r} cannot depend on itself")
                continue
            indegree[task_id] += 1
            children[dependency].append(task_id)
    if errors:
        return [], errors

    queue = deque(sorted(task_id for task_id, degree in indegree.items() if degree == 0))
    order: list[str] = []
    while queue:
        current = queue.popleft()
        order.append(current)
        for child in sorted(children[current]):
            indegree[child] -= 1
            if indegree[child] == 0:
                queue.append(child)
    if len(order) != len(tasks):
        errors.append("task graph contains a dependency cycle")
    return order, errors


def ancestors(task_id: str, tasks: dict[str, dict[str, Any]], memo: dict[str, set[str]]) -> set[str]:
    if task_id in memo:
        return memo[task_id]
    result: set[str] = set()
    for dependency in tasks[task_id]["depends_on"]:
        if dependency in tasks:
            result.add(dependency)
            result.update(ancestors(dependency, tasks, memo))
    memo[task_id] = result
    return result


def write_conflicts(tasks: dict[str, dict[str, Any]]) -> list[str]:
    writers: dict[str, list[str]] = defaultdict(list)
    for task_id, task in tasks.items():
        for target in task["writes"]:
            writers[target].append(task_id)
    memo: dict[str, set[str]] = {}
    warnings: list[str] = []
    for target, task_ids in sorted(writers.items()):
        for index, left in enumerate(task_ids):
            for right in task_ids[index + 1 :]:
                left_before_right = left in ancestors(right, tasks, memo)
                right_before_left = right in ancestors(left, tasks, memo)
                if not left_before_right and not right_before_left:
                    warnings.append(
                        f"parallel tasks {left!r} and {right!r} both declare write target {target!r}"
                    )
    return warnings


def base_result(errors: list[str], warnings: list[str], **extra: Any) -> dict[str, Any]:
    result: dict[str, Any] = {
        "structurally_valid": not errors,
        "strict_pass": not errors and not warnings,
        "scope": (
            "Declared-plan structural checks only. This does not verify runtime isolation, "
            "authorization, approval authenticity, task behavior, or successful execution."
        ),
        "errors": errors,
        "warnings": warnings,
    }
    result.update(extra)
    return result


def validate_plan(source: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    if not isinstance(source, dict):
        return base_result(["plan must be an object"], [])
    nonempty_text(source.get("objective"), "objective", errors)
    raw_tasks = source.get("tasks")
    if not isinstance(raw_tasks, list) or not raw_tasks:
        return base_result(errors + ["tasks must be a non-empty array"], warnings, task_count=0)

    tasks: dict[str, dict[str, Any]] = {}
    for index, raw_task in enumerate(raw_tasks):
        label = f"tasks[{index}]"
        if not isinstance(raw_task, dict):
            errors.append(f"{label} must be an object")
            continue
        task_id = nonempty_text(raw_task.get("id"), f"{label}.id", errors)
        if task_id and not ID_PATTERN.fullmatch(task_id):
            errors.append(f"{label}.id must match {ID_PATTERN.pattern}")
        if task_id in tasks:
            errors.append(f"duplicate task id {task_id!r}")
            continue
        nonempty_text(raw_task.get("owner"), f"{label}.owner", errors)
        nonempty_text(raw_task.get("description"), f"{label}.description", errors)
        nonempty_text(raw_task.get("output_contract"), f"{label}.output_contract", errors)
        dependencies = string_list(raw_task.get("depends_on"), f"{label}.depends_on", errors)
        writes = string_list(raw_task.get("writes"), f"{label}.writes", errors)

        raw_tags = raw_task.get("tags", [])
        tags = string_list(raw_tags, f"{label}.tags", errors)
        for tag in tags:
            if not TAG_PATTERN.fullmatch(tag):
                errors.append(f"{label}.tags entry {tag!r} must match {TAG_PATTERN.pattern}")

        approval_ref = optional_text(raw_task.get("approval_ref"), f"{label}.approval_ref", errors)
        timeout = bounded_number(
            raw_task.get("timeout_seconds"),
            f"{label}.timeout_seconds",
            errors,
            minimum=0.001,
            maximum=MAX_TIMEOUT_SECONDS,
        )
        max_attempts = bounded_integer(
            raw_task.get("max_attempts"),
            f"{label}.max_attempts",
            errors,
            minimum=1,
            maximum=MAX_ATTEMPTS,
        )
        retry_backoff = bounded_number(
            raw_task.get("retry_backoff_seconds"),
            f"{label}.retry_backoff_seconds",
            errors,
            minimum=0,
            maximum=MAX_RETRY_BACKOFF_SECONDS,
        )
        retry_contract = optional_text(
            raw_task.get("retry_contract"), f"{label}.retry_contract", errors
        )

        if timeout is None and "timeout_seconds" not in raw_task:
            warnings.append(
                f"task {task_id or label!r} omits timeout_seconds; strict plans must bound task duration"
            )
        if max_attempts is None and "max_attempts" not in raw_task:
            warnings.append(
                f"task {task_id or label!r} omits max_attempts; strict plans must bound retries"
            )
        if max_attempts is not None and max_attempts > 1 and retry_contract is None:
            warnings.append(
                f"task {task_id or label!r} allows retries but omits retry_contract "
                "(idempotency, status check, and retryable errors)"
            )
        if retry_backoff is not None and (max_attempts is None or max_attempts == 1):
            warnings.append(
                f"task {task_id or label!r} declares retry_backoff_seconds without multiple attempts"
            )

        if task_id:
            tasks[task_id] = {
                "depends_on": dependencies,
                "writes": writes,
                "tags": tags,
                "approval_ref": approval_ref,
                "timeout_seconds": timeout,
                "max_attempts": max_attempts,
                "retry_backoff_seconds": retry_backoff,
                "retry_contract": retry_contract,
            }

    order, graph_errors = topological_order(tasks)
    errors.extend(graph_errors)

    approvals: dict[str, str] = {}
    approval_points = source.get("approval_points", [])
    if not isinstance(approval_points, list):
        errors.append("approval_points must be an array when provided")
    else:
        for index, point in enumerate(approval_points):
            label = f"approval_points[{index}]"
            if not isinstance(point, dict):
                errors.append(f"{label} must be an object")
                continue
            approval_id = nonempty_text(point.get("id"), f"{label}.id", errors)
            if approval_id and not ID_PATTERN.fullmatch(approval_id):
                errors.append(f"{label}.id must match {ID_PATTERN.pattern}")
            if approval_id in approvals:
                errors.append(f"duplicate approval point id {approval_id!r}")
                continue
            task_id = nonempty_text(point.get("before_task"), f"{label}.before_task", errors)
            nonempty_text(point.get("reason"), f"{label}.reason", errors)
            if task_id and task_id not in tasks:
                errors.append(f"{label}.before_task references unknown task {task_id!r}")
            if approval_id:
                approvals[approval_id] = task_id

    for task_id, task in tasks.items():
        risk_tags = sorted(APPROVAL_REQUIRED_TAGS.intersection(task["tags"]))
        approval_ref = task["approval_ref"]
        if risk_tags and approval_ref is None:
            errors.append(
                f"task {task_id!r} has approval-required tag(s) {risk_tags!r} but no approval_ref"
            )
        if approval_ref is not None:
            if approval_ref not in approvals:
                errors.append(
                    f"task {task_id!r} approval_ref {approval_ref!r} does not reference an approval point"
                )
            elif approvals[approval_ref] != task_id:
                errors.append(
                    f"task {task_id!r} approval_ref {approval_ref!r} points before task "
                    f"{approvals[approval_ref]!r}"
                )

    if not graph_errors:
        warnings.extend(write_conflicts(tasks))
    return base_result(
        errors,
        warnings,
        task_count=len(tasks),
        topological_order=order,
        approval_required_tags=sorted(APPROVAL_REQUIRED_TAGS),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON orchestration plan")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on warnings, including parallel write conflicts and omitted execution bounds",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        source = json.loads(args.input.read_text(encoding="utf-8"))
        result = validate_plan(source)
        print(json.dumps(result, indent=2, sort_keys=True))
        if not result["structurally_valid"]:
            return 1
        return 1 if args.strict and not result["strict_pass"] else 0
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
