#!/usr/bin/env python3
"""Measure landing page copy so the skill does not have to estimate.

Reports sentence count, mean and maximum sentence length, the position of every
long sentence, passive-voice candidates, hedges and the word-frequency table.
Every number here is counted. The judgement belongs in the skill.

Usage:
    python3 readability_report.py page.txt
    python3 readability_report.py page.txt --long 30 --mean 18
    cat page.txt | python3 readability_report.py -
    python3 readability_report.py before.txt --compare after.txt

Thresholds are this pack's own defaults for landing page copy, chosen to be
useful rather than derived from published research: a sentence over 35 words is
flagged long, and a mean over 20 words is flagged. Neither has an external
source. Override with --long and --mean, and prefer a measured comparison
between two versions over any absolute number.

Below MIN_SENTENCES_FOR_MEAN sentences the mean is not a stable measurement and
is reported without a verdict.

Exit codes:
    0  measured
    2  input unreadable, or empty where content was required

Stdlib only. No network.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from dataclasses import dataclass, field

MIN_SENTENCES_FOR_MEAN = 10
MAX_TABLE_ROWS = 40
# Below this the frequency table is a list of words that each appear once.
MIN_WORDS_FOR_FREQUENCY = 150

# Forms of "to be" that mark a passive when followed by a participle.
BE_FORMS = {
    "is", "are", "was", "were", "be", "been", "being", "am",
    "isn't", "aren't", "wasn't", "weren't",
}

IRREGULAR_PARTICIPLES = {
    "built", "made", "given", "taken", "seen", "known", "shown", "done",
    "written", "driven", "found", "held", "kept", "left", "lost", "paid",
    "run", "sent", "set", "spent", "told", "understood", "won", "chosen",
    "brought", "bought", "caught", "dealt", "felt", "led", "meant", "met",
}

# Two different vagueness classes, counted separately. Intensifiers inflate a
# claim; hedges retract it. A landing page usually has a hedge problem.
INTENSIFIERS = {
    "actually", "basically", "essentially", "simply", "just", "really",
    "very", "quite", "truly", "literally", "seamlessly", "effortlessly",
    "holistically", "robustly", "extremely", "incredibly", "massively",
}

EPISTEMIC_HEDGES = {
    "perhaps", "maybe", "may", "might", "could", "possibly", "probably",
    "arguably", "seems", "seem", "appears", "appear", "likely", "generally",
    "typically", "usually", "often", "sometimes", "somewhat", "fairly",
    "relatively", "roughly", "approximately", "potentially",
    "tends", "tend",
}
# Deliberately NOT hedges: "can", "should", "about", "around". They are ordinary
# modals and prepositions in landing page copy ("you can cancel any time"), and
# counting them produced a false positive on every page that had no hedging at all.

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "been", "but", "by", "can",
    "do", "does", "for", "from", "get", "has", "have", "how", "in", "into",
    "is", "it", "its", "of", "on", "or", "our", "out", "so", "that", "the",
    "their", "them", "then", "there", "these", "they", "this", "to", "up",
    "was", "we", "were", "what", "when", "which", "who", "will", "with",
    "you", "your", "i", "if", "not", "no", "all", "more", "most", "than",
    "one", "two", "any", "each", "also", "about", "over", "under",
}

# Abbreviations that end in a period without ending a sentence. Without this the
# sentence count inflates and the mean drops, which is the number the skill acts
# on: "Trusted by Dr. Smith and approx. 4 000 teams." would count as three.
ABBREVIATIONS = [
    "dr", "mr", "mrs", "ms", "prof", "sr", "jr", "st",
    "inc", "ltd", "llc", "co", "corp", "dept", "est",
    "approx", "etc", "vs", "fig", "no", "vol", "ed", "al",
]

# Carry periods inside them and are followed by a capital often enough that the
# trailing period must be protected too, or "e.g. Shopify" splits into two.
FULLY_DOTTED_ABBREVIATIONS = ["e.g", "i.e"]

# Also carry interior periods, but here only the interior ones are protected: the
# final period is left as a candidate terminator, because "…in the U.K. Contact
# us." really is two sentences and protecting that period would merge them.
DOTTED_ABBREVIATIONS = ["a.m", "p.m", "u.s", "u.k", "u.a.e"]

SENTINEL = ""  # private-use codepoint, restored after splitting

# Latin terminators plus the ideographic full stop, question and exclamation
# marks, so a page in Chinese or Japanese is measured rather than reported empty.
# A Latin terminator only ends a sentence when what follows could start one: this
# is what keeps "in the U.S. and" together while still splitting "the U.K. Contact".
# Any uppercase codepoint, not just A-Z: a page in Polish, Turkish, French or
# German collapses into one sentence when the lookahead is ASCII-only, which
# inflates both numbers the skill acts on.
_UPPER = "".join(
    chr(c) for c in range(0x2500) if chr(c).isupper()
)
SENTENCE_SPLIT = re.compile(
    r"(?<=[。！？])\s*"
    r"|(?<=[.!?])[ \t]*\n+\s*"
    r"|(?<=[.!?])\s+(?=[\"'“‘(\[]?[" + re.escape(_UPPER) + r"0-9])"
    r"|(?<=[.!?])\s*(?=[㐀-䶿一-鿿぀-ヿ가-힯])"
    r"|\n{2,}\s*"
)

# \w with Unicode, plus the typographic apostrophe and hyphen, so "Zürich" and
# "don't" are one word each and the frequency table is not full of fragments.
WORD = re.compile(r"[^\W\d_][\w’'\-]*", re.UNICODE)

# CJK has no spaces, so count ideographs as words when there are no Latin words.
CJK = re.compile(r"[㐀-䶿一-鿿぀-ヿ가-힯]")


@dataclass
class Sentence:
    index: int
    text: str
    words: list[str] = field(default_factory=list)

    @property
    def length(self) -> int:
        return len(self.words)


@dataclass
class Report:
    sentences: list[Sentence]
    long_threshold: int
    mean_threshold: float
    script: str = "latin"

    @property
    def count(self) -> int:
        return len(self.sentences)

    @property
    def word_count(self) -> int:
        return sum(s.length for s in self.sentences)

    @property
    def mean_length(self) -> float:
        if not self.sentences:
            return 0.0
        return round(self.word_count / self.count, 1)

    @property
    def max_length(self) -> int:
        return max((s.length for s in self.sentences), default=0)

    @property
    def longest(self) -> Sentence | None:
        if not self.sentences:
            return None
        return max(self.sentences, key=lambda s: s.length)

    @property
    def long_sentences(self) -> list[Sentence]:
        return [s for s in self.sentences if s.length > self.long_threshold]

    @property
    def mean_is_stable(self) -> bool:
        return self.count >= MIN_SENTENCES_FOR_MEAN

    @property
    def mean_verdict(self) -> str:
        if not self.mean_is_stable:
            return (
                f"not adjudicated, only {self.count} "
                f"{'sentence' if self.count == 1 else 'sentences'} "
                f"(needs {MIN_SENTENCES_FOR_MEAN} for the mean to be stable)"
            )
        if self.mean_length > self.mean_threshold:
            return f"over the {self.mean_threshold} flag"
        return f"within the {self.mean_threshold} flag"

    @property
    def passive_candidates(self) -> list[tuple[Sentence, str]]:
        found: list[tuple[Sentence, str]] = []
        for s in self.sentences:
            lowered = [w.lower() for w in s.words]
            for i, word in enumerate(lowered[:-1]):
                if word not in BE_FORMS:
                    continue
                nxt = lowered[i + 1]
                if nxt.endswith("ly") and i + 2 < len(lowered):
                    nxt = lowered[i + 2]
                if nxt in IRREGULAR_PARTICIPLES or (
                    nxt.endswith("ed") and len(nxt) > 4
                ):
                    found.append((s, f"{word} {nxt}"))
                    break
        return found

    def _count(self, vocabulary: set[str]) -> Counter:
        c: Counter = Counter()
        for s in self.sentences:
            for w in s.words:
                lw = w.lower()
                if lw in vocabulary:
                    c[lw] += 1
        return c

    @property
    def intensifiers(self) -> Counter:
        return self._count(INTENSIFIERS)

    @property
    def hedges(self) -> Counter:
        return self._count(EPISTEMIC_HEDGES)

    @property
    def frequency(self) -> Counter:
        c: Counter = Counter()
        for s in self.sentences:
            for w in s.words:
                lw = w.lower()
                if lw not in STOPWORDS and len(lw) > 2:
                    c[lw] += 1
        return c


def protect_abbreviations(text: str) -> str:
    # Fully protected dotted forms first, trailing period included.
    for abbr in FULLY_DOTTED_ABBREVIATIONS:
        pattern = re.compile(r"\b" + re.escape(abbr) + r"\.", re.I)
        text = pattern.sub(lambda m: m.group(0).replace(".", SENTINEL), text)
    # Then interior-only forms, so "U.S." keeps its inner dot and nothing else.
    for abbr in DOTTED_ABBREVIATIONS:
        head, _, tail = abbr.rpartition(".")
        pattern = re.compile(r"\b" + re.escape(head) + r"\." + re.escape(tail), re.I)
        text = pattern.sub(lambda m: m.group(0).replace(".", SENTINEL), text)
    # Then the single-token abbreviations, whose trailing period never ends a
    # sentence. Substituting on the match rather than mangling the pattern is what
    # the first version got wrong, and why these silently never matched.
    for abbr in ABBREVIATIONS:
        pattern = re.compile(r"\b" + re.escape(abbr) + r"\.", re.I)
        text = pattern.sub(lambda m: m.group(0).replace(".", SENTINEL), text)
    return text


def restore_abbreviations(text: str) -> str:
    return text.replace(SENTINEL, ".")


def tokenize(text: str) -> tuple[list[str], str]:
    """Return the word list and which script it was counted in.

    CJK characters satisfy `\\w`, so a naive word regex happily reports a whole
    Chinese clause as one word. Tokens made entirely of ideographs are therefore
    excluded from the word list, and when nothing else is left the text is
    counted in ideographs instead.
    """
    words = [w for w in WORD.findall(text) if not all(CJK.match(c) for c in w)]
    if words:
        return words, "latin"
    ideographs = CJK.findall(text)
    if ideographs:
        return ideographs, "cjk"
    return [], "latin"


def parse(text: str, long_threshold: int, mean_threshold: float) -> Report:
    protected = protect_abbreviations(text.strip())
    raw = [p.strip() for p in SENTENCE_SPLIT.split(protected) if p.strip()]
    sentences: list[Sentence] = []
    script = "latin"
    for chunk in raw:
        restored = restore_abbreviations(chunk)
        words, chunk_script = tokenize(restored)
        if not words:
            continue
        if chunk_script == "cjk":
            script = "cjk"
        sentences.append(
            Sentence(index=len(sentences) + 1, text=restored, words=words)
        )
    return Report(sentences, long_threshold, mean_threshold, script)


def truncate(text: str, limit: int = 90) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1] + "…"


def table(rows: list[str], header: list[str], label: str) -> list[str]:
    out = [f"### {label}", "", header[0], header[1]]
    shown = rows[:MAX_TABLE_ROWS]
    out += shown
    if len(rows) > MAX_TABLE_ROWS:
        out.append("")
        out.append(f"Showing {len(shown)} of {len(rows)} rows.")
    out.append("")
    return out


def render(r: Report, label: str = "") -> str:
    if r.count == 0:
        return (
            "No sentences found. The file contained no words this tool could "
            "tokenize; check that it is text rather than markup or binary."
        )

    unit = "ideographs" if r.script == "cjk" else "words"
    lines = [
        f"## Measurement{f' - {label}' if label else ''}",
        "",
        f"- Sentences: {r.count}",
        f"- {unit.capitalize()}: {r.word_count}",
        f"- Mean sentence length: {r.mean_length} {unit}, {r.mean_verdict}",
        f"- Longest sentence: {r.max_length} {unit}"
        + (
            f", over the {r.long_threshold} flag"
            if r.max_length > r.long_threshold
            else f", under the {r.long_threshold} flag"
        ),
        f"- Sentences over {r.long_threshold} {unit}: {len(r.long_sentences)}",
        f"- Passive-voice candidates: {len(r.passive_candidates)}",
        f"- Epistemic hedges: {sum(r.hedges.values())}",
        f"- Intensifiers: {sum(r.intensifiers.values())}",
        "",
    ]
    if r.script == "cjk":
        lines += [
            "Counted as ideographs because no Latin words were found. Sentence "
            "length in ideographs is not comparable to a word count.",
            "",
        ]

    if r.long_sentences:
        lines += table(
            [f"| {s.index} | {s.length} | {truncate(s.text)} |" for s in r.long_sentences],
            ["| # | Words | Sentence |", "|---|---|---|"],
            "Long sentences",
        )

    if r.passive_candidates:
        lines += table(
            [
                f"| {s.index} | {match} | {truncate(s.text, 70)} |"
                for s, match in r.passive_candidates
            ],
            ["| # | Match | Sentence |", "|---|---|---|"],
            "Passive-voice candidates",
        )

    if r.hedges:
        pairs = ", ".join(f"{w} x{n}" for w, n in r.hedges.most_common())
        lines += [
            "### Epistemic hedges",
            "",
            pairs,
            "",
            "These retract the claim. On a landing page they are usually the more "
            "expensive of the two classes.",
            "",
        ]

    if r.intensifiers:
        pairs = ", ".join(f"{w} x{n}" for w, n in r.intensifiers.most_common())
        lines += ["### Intensifiers", "", pairs, "", "These inflate the claim.", ""]

    top = r.frequency.most_common(12) if r.word_count >= MIN_WORDS_FOR_FREQUENCY else []
    if not top and r.word_count < MIN_WORDS_FOR_FREQUENCY:
        lines += [
            f"Frequency table suppressed: {r.word_count} words is under the "
            f"{MIN_WORDS_FOR_FREQUENCY} needed for repetition to mean anything.",
            "",
        ]
    if top:
        lines += table(
            [f"| {w} | {n} |" for w, n in top],
            ["| Word | Count |", "|---|---|"],
            "Most frequent content words",
        )

    longest = r.longest
    if longest:
        lines += [
            "### Hardest sentence on the page",
            "",
            f'"{truncate(longest.text, 400)}" ({longest.length} {unit})',
            "",
        ]

    return "\n".join(lines)


def render_compare(a: Report, b: Report, name_a: str, name_b: str) -> str:
    rows = [
        ("Sentences", a.count, b.count),
        ("Words", a.word_count, b.word_count),
        ("Mean sentence length", a.mean_length, b.mean_length),
        ("Longest sentence", a.max_length, b.max_length),
        ("Long sentences", len(a.long_sentences), len(b.long_sentences)),
        ("Passive candidates", len(a.passive_candidates), len(b.passive_candidates)),
        ("Epistemic hedges", sum(a.hedges.values()), sum(b.hedges.values())),
        ("Intensifiers", sum(a.intensifiers.values()), sum(b.intensifiers.values())),
    ]
    out = [
        "## Comparison",
        "",
        f"| Metric | {name_a} | {name_b} | Direction |",
        "|---|---|---|---|",
    ]
    for metric, va, vb in rows:
        if vb < va:
            direction = "easier"
        elif vb > va:
            direction = "harder"
        else:
            direction = "unchanged"
        out.append(f"| {metric} | {va} | {vb} | {direction} |")
    out += [
        "",
        "Fewer words and shorter sentences is easier to read, not automatically "
        "better. A short sentence that says nothing is a vagueness defect, which "
        "this helper cannot measure.",
        "",
    ]
    if not (a.mean_is_stable and b.mean_is_stable):
        out += [
            f"At least one version has under {MIN_SENTENCES_FOR_MEAN} sentences, so "
            "the mean comparison is not stable. Compare the raw counts instead.",
            "",
        ]
    return "\n".join(out)


def read_source(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    with open(path, encoding="utf-8-sig") as fh:
        return fh.read()


def read_source_or_fail(path: str) -> str:
    """Raises OSError for both unreadable files and undecodable bytes, so the
    caller's one handler covers what the docstring promises."""
    try:
        return read_source(path)
    except UnicodeDecodeError as exc:
        raise OSError(f"not decodable as UTF-8 text: {exc}") from exc


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description="Measure landing page copy readability mechanics."
    )
    ap.add_argument("file", help="text file with the page copy, or - for stdin")
    ap.add_argument("--compare", help="second file to compare against")
    ap.add_argument(
        "--long", type=int, default=35,
        help="word count above which a sentence is flagged long (default 35, this "
             "pack's own default, no external source)",
    )
    ap.add_argument(
        "--mean", type=float, default=20.0,
        help="mean sentence length above which the page is flagged (default 20, this "
             "pack's own default, no external source)",
    )
    args = ap.parse_args(argv)

    if args.long < 1:
        print("--long must be at least 1 word", file=sys.stderr)
        return 2
    if args.mean <= 0:
        print("--mean must be greater than zero", file=sys.stderr)
        return 2

    if args.compare and args.file == "-" and args.compare == "-":
        print(
            "Cannot read both documents from stdin; the second would always parse "
            "as empty and every metric would read as an improvement.",
            file=sys.stderr,
        )
        return 2

    try:
        first = parse(read_source_or_fail(args.file), args.long, args.mean)
    except OSError as exc:
        print(f"Cannot read {args.file}: {exc}", file=sys.stderr)
        return 2

    if not args.compare:
        print(render(first))
        return 0 if first.count else 2

    try:
        second = parse(read_source_or_fail(args.compare), args.long, args.mean)
    except OSError as exc:
        print(f"Cannot read {args.compare}: {exc}", file=sys.stderr)
        return 2

    if not second.count:
        print(
            f"{args.compare} contains no measurable sentences, so a comparison would "
            "report improvement across the board. Supply both versions as text.",
            file=sys.stderr,
        )
        return 2

    print(render(first, label=args.file))
    print(render(second, label=args.compare))
    print(render_compare(first, second, args.file, args.compare))
    return 0


if __name__ == "__main__":
    sys.exit(main())
