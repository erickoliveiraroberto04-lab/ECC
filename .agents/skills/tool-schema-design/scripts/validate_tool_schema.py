#!/usr/bin/env python3
"""Check common structural and review-worthy properties of an agent tool schema."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path
from typing import Any


NAME_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_-]{0,63}$")
JSON_TYPES = {"array", "boolean", "integer", "null", "number", "object", "string"}
BOUNDED_NUMBER_NAME = re.compile(
    r"(?:^|_)(?:amount|count|days|hours|limit|max|minutes|page_size|quantity|results|seconds|timeout)(?:$|_)",
    re.IGNORECASE,
)
COMMAND_PROPERTY_NAMES = {
    "code",
    "command",
    "command_line",
    "executable",
    "script",
    "shell",
    "shell_command",
}
PRIVILEGE_PROPERTY_NAMES = {
    "admin",
    "allow_privileged",
    "as_root",
    "elevate",
    "privileged",
    "root",
    "run_as_admin",
    "sudo",
}
CREDENTIAL_NAMES = {
    "api_key",
    "auth_token",
    "bearer_token",
    "client_secret",
    "credential",
    "password",
    "passwd",
    "private_key",
    "refresh_token",
    "secret",
    "session_token",
    "token",
}
LOCATION_NAMES = {"directory", "endpoint", "file", "host", "path", "uri", "url"}
RISKY_TOOL_NAME_PATTERN = re.compile(
    r"^(?:run|execute|exec)[_-]?(?:shell|command|script|code)(?:$|_)", re.IGNORECASE
)


def validate_type(value: Any, path: str, errors: list[str]) -> None:
    if isinstance(value, str):
        if value not in JSON_TYPES:
            errors.append(f"{path}.type has unsupported value {value!r}")
        return
    if isinstance(value, list) and value:
        if any(not isinstance(item, str) or item not in JSON_TYPES for item in value):
            errors.append(f"{path}.type array contains an unsupported value")
        if len(value) != len(set(value)):
            errors.append(f"{path}.type array contains duplicates")
        return
    errors.append(f"{path}.type must be a JSON type string or non-empty array")


def schema_includes(schema: dict[str, Any], type_name: str) -> bool:
    schema_type = schema.get("type")
    return schema_type == type_name or (
        isinstance(schema_type, list) and type_name in schema_type
    )


def validate_bound_pair(
    schema: dict[str, Any],
    path: str,
    errors: list[str],
    minimum_key: str,
    maximum_key: str,
    *,
    integers: bool,
) -> None:
    values: dict[str, float] = {}
    for key in (minimum_key, maximum_key):
        if key not in schema:
            continue
        value = schema[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            errors.append(f"{path}.{key} must be {'an integer' if integers else 'a number'}")
            continue
        if integers and not isinstance(value, int):
            errors.append(f"{path}.{key} must be an integer")
            continue
        numeric = float(value)
        if not math.isfinite(numeric) or numeric < 0:
            errors.append(f"{path}.{key} must be a finite non-negative value")
            continue
        values[key] = numeric
    if minimum_key in values and maximum_key in values:
        if values[minimum_key] > values[maximum_key]:
            errors.append(f"{path}.{minimum_key} cannot exceed {maximum_key}")


def has_closed_or_pattern_constraint(schema: dict[str, Any]) -> bool:
    pattern = schema.get("pattern")
    restrictive_pattern = isinstance(pattern, str) and pattern.strip() not in {
        "",
        ".*",
        ".+",
        "^.*$",
        "^.+$",
    }
    return bool(
        "const" in schema
        or (isinstance(schema.get("enum"), list) and schema["enum"])
        or restrictive_pattern
    )


def name_is_or_ends_with(normalized: str, terms: set[str]) -> bool:
    return normalized in terms or any(normalized.endswith(f"_{term}") for term in terms)


def review_property(
    schema: dict[str, Any],
    path: str,
    property_name: str,
    required_property: bool,
    warnings: list[str],
) -> None:
    normalized = property_name.casefold().replace("-", "_")
    is_string = schema_includes(schema, "string")

    if (
        name_is_or_ends_with(normalized, COMMAND_PROPERTY_NAMES)
        and is_string
        and not has_closed_or_pattern_constraint(schema)
    ):
        warnings.append(
            f"{path} exposes free-form command, shell, script, or code execution; replace it "
            "with a bounded operation enum or isolate it behind an explicitly sandboxed runtime"
        )
    if normalized in PRIVILEGE_PROPERTY_NAMES or name_is_or_ends_with(
        normalized, {"admin", "privileged", "root", "sudo"}
    ):
        warnings.append(
            f"{path} exposes a caller-controlled privilege or elevation parameter; derive privilege server-side"
        )
    if name_is_or_ends_with(normalized, CREDENTIAL_NAMES):
        warnings.append(
            f"{path} appears to accept credentials or secrets; obtain them from trusted server-side context"
        )
    if is_string and name_is_or_ends_with(normalized, LOCATION_NAMES):
        if not has_closed_or_pattern_constraint(schema):
            warnings.append(
                f"{path} appears to accept an arbitrary URL, host, endpoint, file, directory, or path; "
                "use an enum, restrictive pattern, opaque identifier, and runtime allowlist/sandbox"
            )

    if is_string and not has_closed_or_pattern_constraint(schema):
        portable_format = schema.get("format") in {"date", "date-time", "time", "uuid"}
        if "maxLength" not in schema and not portable_format:
            warnings.append(f"{path} should define maxLength for bounded model input")
        if required_property and "minLength" not in schema and not portable_format:
            warnings.append(f"{path} is required and should define minLength or a pattern")

    if schema_includes(schema, "array"):
        if "maxItems" not in schema:
            warnings.append(f"{path} should define maxItems for bounded model input")
        if required_property and "minItems" not in schema:
            warnings.append(f"{path} is required and should define minItems")

    if (schema_includes(schema, "integer") or schema_includes(schema, "number")) and BOUNDED_NUMBER_NAME.search(normalized):
        if "minimum" not in schema:
            warnings.append(f"{path} appears numerically bounded but omits minimum")
        if "maximum" not in schema:
            warnings.append(f"{path} appears numerically bounded but omits maximum")


def validate_schema(
    schema: Any,
    path: str,
    errors: list[str],
    warnings: list[str],
    *,
    property_name: str | None = None,
    required_property: bool = False,
) -> None:
    if not isinstance(schema, dict):
        errors.append(f"{path} must be an object")
        return

    combinators = [key for key in ("oneOf", "anyOf", "allOf") if key in schema]
    if "type" not in schema and not combinators and "$ref" not in schema:
        errors.append(f"{path} must declare type, a composition keyword, or $ref")
    if "type" in schema:
        validate_type(schema["type"], path, errors)
    if property_name is not None:
        description = schema.get("description")
        if not isinstance(description, str) or not description.strip():
            warnings.append(f"{path} should have a non-empty description")
        review_property(schema, path, property_name, required_property, warnings)

    if "pattern" in schema and not isinstance(schema["pattern"], str):
        errors.append(f"{path}.pattern must be a string")
    validate_bound_pair(schema, path, errors, "minLength", "maxLength", integers=True)
    validate_bound_pair(schema, path, errors, "minItems", "maxItems", integers=True)

    for key in ("minimum", "maximum"):
        if key in schema:
            value = schema[key]
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
                errors.append(f"{path}.{key} must be a finite number")
    if all(key in schema for key in ("minimum", "maximum")):
        lower, upper = schema["minimum"], schema["maximum"]
        if (
            isinstance(lower, (int, float))
            and not isinstance(lower, bool)
            and isinstance(upper, (int, float))
            and not isinstance(upper, bool)
            and math.isfinite(lower)
            and math.isfinite(upper)
            and lower > upper
        ):
            errors.append(f"{path}.minimum cannot exceed maximum")

    for keyword in combinators:
        branches = schema[keyword]
        if not isinstance(branches, list) or not branches:
            errors.append(f"{path}.{keyword} must be a non-empty array")
        else:
            for index, branch in enumerate(branches):
                validate_schema(branch, f"{path}.{keyword}[{index}]", errors, warnings)

    includes_object = schema_includes(schema, "object")
    if includes_object or "properties" in schema or "required" in schema:
        properties = schema.get("properties", {})
        if not isinstance(properties, dict):
            errors.append(f"{path}.properties must be an object")
            properties = {}

        required = schema.get("required", [])
        if not isinstance(required, list) or any(not isinstance(item, str) for item in required):
            errors.append(f"{path}.required must be an array of strings")
            required_names: set[str] = set()
        else:
            required_names = set(required)
            if len(required) != len(required_names):
                errors.append(f"{path}.required contains duplicates")
            for name in required:
                if name not in properties:
                    errors.append(f"{path}.required references undeclared property {name!r}")

        for name, child in properties.items():
            if not isinstance(name, str) or not name:
                errors.append(f"{path}.properties keys must be non-empty strings")
                continue
            validate_schema(
                child,
                f"{path}.properties.{name}",
                errors,
                warnings,
                property_name=name,
                required_property=name in required_names,
            )

        if "additionalProperties" not in schema:
            warnings.append(f"{path} should set additionalProperties to false")
        elif not isinstance(schema["additionalProperties"], (bool, dict)):
            errors.append(f"{path}.additionalProperties must be a boolean or schema")
        elif schema["additionalProperties"] is not False:
            warnings.append(
                f"{path}.additionalProperties is permissive; strict model-facing schemas should reject unknown fields"
            )
            if isinstance(schema["additionalProperties"], dict):
                validate_schema(
                    schema["additionalProperties"],
                    f"{path}.additionalProperties",
                    errors,
                    warnings,
                )

    if schema_includes(schema, "array"):
        if "items" not in schema:
            errors.append(f"{path}.items is required for arrays")
        else:
            validate_schema(schema["items"], f"{path}.items", errors, warnings)

    if "enum" in schema:
        values = schema["enum"]
        if not isinstance(values, list) or not values:
            errors.append(f"{path}.enum must be a non-empty array")
        else:
            encoded = [json.dumps(value, sort_keys=True) for value in values]
            if len(encoded) != len(set(encoded)):
                errors.append(f"{path}.enum contains duplicates")


def unwrap_tool(source: Any, errors: list[str]) -> dict[str, Any]:
    if not isinstance(source, dict):
        errors.append("document must be an object")
        return {}
    if source.get("type") == "function":
        function = source.get("function")
        if not isinstance(function, dict):
            errors.append("function wrapper must contain a function object")
            return {}
        return function
    return source


def validate_tool(source: Any) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []
    tool = unwrap_tool(source, errors)

    name = tool.get("name")
    if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
        errors.append(f"name must match {NAME_PATTERN.pattern}")
    else:
        if any(character.isupper() for character in name):
            warnings.append("lowercase tool names are more portable across providers")
        if RISKY_TOOL_NAME_PATTERN.search(name):
            warnings.append(
                "tool name indicates general command, shell, script, or code execution; "
                "prefer bounded operation-specific tools and an explicit sandbox"
            )

    description = tool.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("description must be a non-empty string")
    elif len(description.strip()) < 20:
        warnings.append("description may be too short to guide reliable tool selection")
    elif re.search(r"\b(?:arbitrary|any)\s+(?:shell\s+)?command\b", description, re.IGNORECASE):
        warnings.append("description advertises arbitrary command execution")

    parameters = tool.get("parameters")
    if parameters is None:
        errors.append("parameters is required")
    else:
        validate_schema(parameters, "parameters", errors, warnings)
        if isinstance(parameters, dict) and parameters.get("type") != "object":
            errors.append("parameters.type must be object")

    warnings = list(dict.fromkeys(warnings))
    return {
        "structurally_valid": not errors,
        "strict_pass": not errors and not warnings,
        "validation_scope": (
            "Common JSON-shape and heuristic review checks only. Passing does not certify "
            "semantic safety, authorization, provider compatibility, sandboxing, or implementation behavior."
        ),
        "tool_name": name if isinstance(name, str) else None,
        "errors": errors,
        "warnings": warnings,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON tool definition")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail on review findings as well as structural errors",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        source = json.loads(args.input.read_text(encoding="utf-8"))
        result = validate_tool(source)
        print(json.dumps(result, indent=2, sort_keys=True))
        if not result["structurally_valid"]:
            return 1
        return 1 if args.strict and not result["strict_pass"] else 0
    except (OSError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
