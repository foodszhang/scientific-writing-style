#!/usr/bin/env python3
"""Advisory linter for common scientific-writing style risks.

No third-party dependencies. It intentionally reports warnings rather than
rewriting text. The agent or author must decide whether each warning applies.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


PATTERNS = [
    (r"\bin order to\b", "wordiness", "Consider 'to' if the meaning is unchanged."),
    (r"\butili[sz]e(?:d|s|ing)?\b", "word-choice", "Consider 'use' unless 'utilize' has a specific technical sense."),
    (r"\bdue to the fact that\b", "wordiness", "Consider 'because' if causality is intended."),
    (r"\bit (?:is|should be) (?:worth|important) (?:noting|to note) that\b", "meta-writing", "State the point directly if possible."),
    (r"\bit can be (?:seen|observed) that\b", "meta-writing", "State the observation directly if possible."),
    (r"\b(?:obviously|clearly|remarkably|remarkable|groundbreaking|unprecedented)\b", "rhetorical-strength", "Check whether the evaluative word is necessary and evidenced."),
    (r"\bstate[- ]of[- ]the[- ]art\b", "scope-claim", "Verify benchmark, comparator set, metric, and time scope."),
    (r"\b(?:novel|first)\b", "novelty-claim", "Verify that the novelty/priority claim is scoped and supported."),
    (r"\b(?:robust|robustness)\b", "operationalize", "Specify robustness to what perturbation or condition."),
    (r"\b(?:efficient|efficiency)\b", "operationalize", "Specify the resource: time, memory, compute, samples, acquisitions, etc."),
    (r"\bsignificant(?:ly)?\b", "statistical-language", "Check whether statistical significance is intended; otherwise report magnitude precisely."),
    (r"\bplays? (?:a|an) (?:crucial|vital|pivotal|important) role\b", "importance-filler", "Prefer the concrete consequence or function."),
    (r"\bhas attracted (?:considerable|significant|increasing) attention\b", "scene-setting", "Keep only if the trend itself matters and is supported."),
    (r"\bdespite these (?:advancements|advances),? (?:several )?challenges remain\b", "generic-gap", "Name the actual unresolved limitation."),
    (r"\bto address the aforementioned (?:issues|challenges|limitations)\b", "generic-transition", "Name the specific issue directly."),
    (r"\bpaves? the way for\b", "generic-implication", "State the concrete supported implication or omit."),
]

IEEE_BRITISH = {
    "behaviour": "behavior",
    "behaviours": "behaviors",
    "centre": "center",
    "centres": "centers",
    "polarisation": "polarization",
    "optimisation": "optimization",
    "normalisation": "normalization",
    "localisation": "localization",
    "modelling": "modeling",
}

LATEX_COMMAND = re.compile(r"\\[A-Za-z@]+(?:\*?)")


def strip_latex_comments(text: str) -> str:
    lines = []
    for line in text.splitlines():
        # Preserve escaped percent signs.
        line = re.split(r"(?<!\\)%", line, maxsplit=1)[0]
        lines.append(line)
    return "\n".join(lines)


def line_number(text: str, pos: int) -> int:
    return text.count("\n", 0, pos) + 1


def lint(text: str, ieee: bool = False):
    clean = strip_latex_comments(text)
    warnings = []
    for pattern, category, message in PATTERNS:
        for m in re.finditer(pattern, clean, flags=re.IGNORECASE):
            warnings.append((line_number(clean, m.start()), category, m.group(0), message))

    if ieee:
        for british, american in IEEE_BRITISH.items():
            for m in re.finditer(rf"\b{re.escape(british)}\b", clean, flags=re.IGNORECASE):
                warnings.append(
                    (line_number(clean, m.start()), "ieee-spelling", m.group(0), f"IEEE generally prefers American spelling: '{american}'.")
                )
    return sorted(warnings, key=lambda x: (x[0], x[1], x[2].lower()))


def check_terminology(text: str, config_path: Path):
    cfg = json.loads(config_path.read_text(encoding="utf-8"))
    warnings = []
    for canonical, variants in cfg.get("canonical_terms", {}).items():
        seen = []
        for term in [canonical, *variants]:
            if re.search(rf"(?<!\w){re.escape(term)}(?!\w)", text, flags=re.IGNORECASE):
                seen.append(term)
        if len(seen) > 1:
            warnings.append((0, "terminology", ", ".join(seen), f"Multiple variants detected; consider canonical term '{canonical}' if they denote the same concept."))
    return warnings


def main() -> int:
    p = argparse.ArgumentParser(description="Advisory scientific-writing style linter")
    p.add_argument("path", type=Path)
    p.add_argument("--ieee", action="store_true", help="Enable a small IEEE-specific spelling pass")
    p.add_argument("--terminology", type=Path, help="JSON file based on assets/terminology.example.json")
    args = p.parse_args()

    text = args.path.read_text(encoding="utf-8", errors="replace")
    warnings = lint(text, ieee=args.ieee)
    if args.terminology:
        warnings.extend(check_terminology(text, args.terminology))

    if not warnings:
        print("No advisory style warnings found.")
        return 0

    for line, category, phrase, message in sorted(warnings, key=lambda x: (x[0], x[1])):
        loc = f"line {line}" if line else "document"
        print(f"{loc}: [{category}] {phrase!r} — {message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
