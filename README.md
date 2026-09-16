# scientific-writing-style

A small, open Agent Skill for **scientific prose rather than scientific judgment**.

It focuses on the problems that generic LLM rewriting often handles poorly:

- precise word choice;
- stable technical terminology;
- contribution and evidence verbs;
- claim-strength preservation;
- sentence information flow;
- paragraph architecture;
- section-level rhetorical frameworks;
- anti-inflation / anti-template writing;
- an optional IEEE house-style overlay.

The goal is not to make prose sound more sophisticated. The goal is to make it **clearer, more conventional, more precise, and less likely to change the science while editing the English**.

## What is included

```text
scientific-writing-style/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── rhetorical-frameworks.md
│   ├── word-choice.md
│   ├── sentence-paragraph.md
│   ├── anti-patterns.md
│   ├── ieee-overlay.md
│   └── source-notes.md
├── scripts/
│   └── style_lint.py
├── assets/
│   └── terminology.example.json
└── evals/
    └── evals.json
```

`SKILL.md` follows the open Agent Skills convention: a skill is a directory with YAML-frontmatter metadata and Markdown instructions. The detailed references are loaded only when needed.

## Core behavior

The skill tells an agent to:

1. identify the communicative job of the text;
2. freeze technical invariants;
3. use conventional scientific wording rather than decorative synonyms;
4. preserve claim strength;
5. apply section-aware rhetorical structure;
6. make the smallest revision that solves the writing problem.

A central rule is:

> Never replace a precise technical term merely to avoid lexical repetition.

Another is:

> Do not rewrite an acceptable sentence merely to make it different.

## Optional linter

A dependency-free advisory linter flags common risks:

```bash
python scripts/style_lint.py manuscript.tex --ieee
```

You can also provide a terminology map:

```bash
python scripts/style_lint.py manuscript.tex \
  --ieee \
  --terminology assets/terminology.example.json
```

Warnings are deliberately advisory. Scientific context decides whether a phrase is actually wrong.

## Installing as an Agent Skill

Agent clients use different skill directories. Copy the whole `scientific-writing-style` folder into the skills directory recognized by your client. The folder name must remain `scientific-writing-style` because it matches the `name` in `SKILL.md`.

The format is intentionally simple enough to work with clients that support the open `SKILL.md` Agent Skills convention. If a client has additional metadata requirements, keep the instruction body and adapt only the frontmatter/install location.

## Recommended use

Use this skill **after or alongside scientific reasoning**, not instead of it.

A productive manuscript workflow is:

```text
scientific reasoning / content decisions
        ↓
scientific-writing-style
        ↓
venue-specific formatting / LaTeX checks
        ↓
final reviewer read
```

For an existing manuscript, prefer minimal-diff editing. For a new section, use the rhetorical framework as a planning scaffold, then write natural prose rather than filling a phrase template.

## Sources and copyright

This repository contains original guidance synthesized from publicly available writing resources, especially:

- University of Manchester Academic Phrasebank (function-first / rhetorical-move organization);
- Microsoft Writing Style Guide (simple, precise, consistent wording);
- Google Developer Documentation Style Guide and Technical Writing materials (information flow, sentence/paragraph clarity);
- IEEE Editorial Style Manual for Authors (optional IEEE overlay).

The repository **does not copy or bundle** the Manchester phrase inventory or the IEEE manual. External sources remain under their own terms. See `references/source-notes.md`.

## Status

`0.1.0` — usable first version. The next useful step is evaluation on real manuscript edits, especially false positives from the linter and cases where a generic prose rule conflicts with field convention.

## License

MIT. See `LICENSE`.
