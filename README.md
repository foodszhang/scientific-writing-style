# scientific-writing-style

An open Agent Skill for **scientific manuscript structure, evidence, and prose**.

Version 0.2 expands the original writing-layer skill into a manuscript workflow that first checks whether the paper's scientific argument is structurally sound, then improves the writing.

It focuses on problems generic LLM rewriting often misses:

- problem → gap → contribution → method → experiment → result → discussion alignment;
- section roles and section-size balance;
- reproducibility of simulated, experimental, and in vivo protocols;
- evidence traceability from prose claims to tables/figures/analyses;
- domain-paper patterning from relevant published literature;
- precise word choice;
- stable technical terminology;
- contribution and evidence verbs;
- claim-strength preservation;
- sentence and paragraph information flow;
- optional IEEE house style.

The goal is not to make prose sound more sophisticated. The goal is to make a manuscript **scientifically legible, evidence-traceable, reproducible, field-appropriate, and precise**.

## What is included

```text
scientific-writing-style/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── manuscript-audit.md
│   ├── section-role-and-budget.md
│   ├── domain-paper-patterning.md
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

## Three working modes

### 1. Wording mode

Use for local sentence/paragraph editing.

The skill:
- freezes technical content;
- preserves claim strength;
- repairs terminology, grammar, information flow, and concision;
- prefers minimal-diff revision.

### 2. Section mode

Use for a complete Introduction, Methods subsection, Experimental Setup, Results, Discussion, or Conclusion.

The skill first checks:
- what the section is supposed to do;
- whether the current section actually does it;
- whether material is missing or belongs elsewhere;
- whether the section is over- or under-developed.

When useful, it then patterns the section against 2–3 relevant published papers by extracting their rhetorical structure and field terminology without copying prose.

### 3. Manuscript mode

Use for full-paper revision.

The default workflow is:

```text
story map
    ↓
contribution–evidence matrix
    ↓
section-role + size audit
    ↓
reproducibility + evidence traceability
    ↓
domain-paper patterning
    ↓
structural repair
    ↓
section rewriting
    ↓
wording/style pass
    ↓
final alignment gate
```

This order matters. A polished Discussion that only repeats Results is still a weak Discussion; a polished in vivo paragraph that omits how the reference mask was constructed is still unreproducible.

## Section-size diagnostics

`references/section-role-and-budget.md` includes both relative manuscript proportions and a TMI-like 9–10 page planning profile.

The ranges are **diagnostic, not prescriptive**. They are used to ask:
- Is Methods long because the method truly needs explanation, or because implementation detail is displacing Results/Discussion?
- Is Discussion short because the evidence is simple, or because interpretation and prior-work comparison are missing?
- Is Conclusion concise, or simply incomplete?

## Contribution–evidence alignment

Every claimed contribution should be traceable across:

```text
Introduction
   ↓
Methods
   ↓
direct experiment / ablation
   ↓
Results
   ↓
Discussion
   ↓
Conclusion
```

If a claimed contribution disappears from any stage, the skill flags the gap before polishing prose.

## Domain-paper patterning

The skill does not maintain a phrase bank.

Instead, for field-appropriate drafting it extracts from relevant papers:
- section order;
- paragraph functions;
- opening/transition logic;
- terminology;
- evidence presentation;
- Discussion structure.

It then adapts the rhetorical skeleton, not the copyrighted sentences.

## Reproducibility and evidence checks

The manuscript audit covers:
- simulated-data generation;
- in vivo/experimental acquisition;
- train/validation/test separation;
- comparator fairness;
- reference-mask / ground-truth construction;
- metric definitions and matching rules;
- confidence intervals and statistical tests;
- traceability of every important result in prose.

## Optional linter

A dependency-free advisory linter still flags common style risks:

```bash
python scripts/style_lint.py manuscript.tex --ieee
```

You can also provide a terminology map:

```bash
python scripts/style_lint.py manuscript.tex \
  --ieee \
  --terminology assets/terminology.example.json
```

The linter is intentionally secondary. Structural and scientific audits require reasoning and cannot be reduced to regex.

## Installing as an Agent Skill

Copy the complete `scientific-writing-style` folder into the skills directory recognized by the agent client. The folder name should remain `scientific-writing-style` because it matches the `name` in `SKILL.md`.

Clients differ in how they import personal skills. Keep the instruction body and repository structure; adapt only client-specific metadata/install location when required.

## Recommended manuscript workflow

For an existing paper:

```text
full manuscript audit
        ↓
fix blocking scientific/reproducibility issues
        ↓
repair section structure
        ↓
compare key sections with field papers
        ↓
revise prose
        ↓
venue/LaTeX/style check
        ↓
final reviewer read
```

For a single sentence or paragraph, use wording mode and do not force the full workflow.

## Sources and copyright

This repository contains original guidance synthesized from publicly available writing resources and manuscript practice.

It does **not** copy or bundle a proprietary phrase bank, journal manual, or published-paper prose. Domain-paper patterning extracts rhetorical functions and terminology, not sentences.

See `references/source-notes.md`.

## Status

`0.2.0` — manuscript-audit release.

Major additions:
- full manuscript audit;
- contribution–evidence matrix;
- section role and size budgets;
- reproducibility audit;
- result/evidence traceability;
- domain-paper patterning;
- stronger Results/Discussion distinction;
- regression cases based on real manuscript-review failures.

## License

MIT. See `LICENSE`.
