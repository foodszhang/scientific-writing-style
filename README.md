# scientific-writing-style

An open Agent Skill for **read-to-write scientific manuscript work**.

Version 0.4 expands the project into an evidence-governed workflow that starts at literature reading, accumulates field knowledge, plans the manuscript, drafts from a frozen blueprint, audits the evidence chain, and only then performs wording/style revision.

## What it now does

### 1. Literature reading
Turns papers into reusable, source-traceable knowledge:

- paper cards;
- field terminology and short accepted expressions;
- equation/model registry;
- claim/evidence ledger;
- section/rhetorical pattern notes;
- cross-paper domain packs.

### 3. Project planning
Builds a stable source of truth for one manuscript:

- problem;
- technical difficulty;
- exact gap;
- contribution hierarchy;
- method/module names;
- terminology lock;
- verified results;
- evidence boundaries;
- reviewer/author decisions;
- section size plan;
- section blueprints.

### 4. From-scratch drafting
Writes from the project profile + domain pack + paper cards rather than inventing a new framing each turn.

### 5. Manuscript audit
Checks:

- problem → gap → contribution → method → experiment → result → discussion → conclusion;
- contribution–evidence alignment;
- section role and size balance;
- reproducibility;
- comparator fairness;
- metric/statistical definitions;
- prose-number traceability;
- Discussion depth;
- claim strength.

### 6. Wording/style
Retains the original strengths:

- precise word choice;
- stable terminology;
- contribution/evidence verbs;
- sentence and paragraph flow;
- claim-strength preservation;
- optional IEEE overlay.

## Knowledge architecture

```text
scientific-writing-style/
├── SKILL.md
├── references/
│   ├── living-writing-standards.md\n│   ├── literature-reading-and-knowledge.md
│   ├── from-scratch-drafting.md
│   ├── manuscript-audit.md
│   ├── section-role-and-budget.md
│   ├── domain-paper-patterning.md
│   ├── rhetorical-frameworks.md
│   ├── word-choice.md
│   ├── sentence-paragraph.md
│   ├── anti-patterns.md
│   ├── ieee-overlay.md
│   └── source-notes.md
├── knowledge/
│   ├── README.md
│   └── templates/
│       ├── writing-standard-entry.md\n│       ├── paper-card.md
│       ├── domain-lexicon.md
│       ├── equation-registry.md
│       ├── claim-ledger.md
│       ├── domain-pack.md
│       ├── project-profile.md
│       └── section-blueprint.md
├── scripts/
│   └── style_lint.py
├── assets/
│   └── terminology.example.json
└── evals/
    └── evals.json
```

## Recommended long-project workflow

```text
read papers
   ↓
paper cards
   ↓
domain terminology / equations / conclusions
   ↓
cross-paper domain pack
   ↓
project profile
   ↓
section role + size plan
   ↓
section blueprint
   ↓
draft from scratch
   ↓
evidence/reproducibility audit
   ↓
wording + venue pass
   ↓
decision ledger update
```

This order is meant to reduce oscillation between drafts. Once a project profile is accepted, the skill should not silently rename the problem, change the contribution order, switch terminology, or strengthen claims in a later session.

## Section-size diagnostics

`references/section-role-and-budget.md` includes both relative manuscript proportions and a TMI-like 9–10 page planning profile.

The ranges are **diagnostic, not prescriptive**. The skill asks whether a section performs its real scientific job, not merely whether it is the right length.

## Domain-paper patterning

The skill does not build a copied phrase bank.

Instead, it extracts from relevant papers:

- section order;
- paragraph functions;
- technical terminology;
- equation placement;
- evidence presentation;
- Discussion structure;
- limitations;
- safe claim scope.

The resulting knowledge is stored as structured notes, not copied prose.

## Evidence-governed writing rules

Teacher/reviewer/collaborator feedback is treated as a hypothesis about writing quality, not automatically as a field-wide rule. Reusable rules are tracked in `references/living-writing-standards.md` with status, scope, evidence, counterexamples, confidence, and verification date.

Low-risk wording issues can be handled directly. Consequential or disputed issues should be checked against formal guidance and comparable papers before promotion into stable core guidance.

## Persistent project consistency

For long manuscripts, the recommended source hierarchy is:

1. verified project facts/data;
2. accepted project profile and decision ledger;
3. directly read source papers;
4. domain pack;
5. venue/style rules;
6. generic model knowledge.

This prevents a new writing session from silently overriding decisions made earlier.

## Optional linter

The dependency-free linter remains useful for local style risks:

```bash
python scripts/style_lint.py manuscript.tex --ieee
```

The linter is secondary. Literature synthesis, scientific structure, reproducibility, and evidence traceability require reasoning.

## Installing

Copy the complete `scientific-writing-style` folder into the skills directory recognized by the agent client.

Clients differ in how they import personal skills. Keep the repository structure and instruction body; adapt only client-specific metadata/install location when required.

## Status

`0.4.0` — evidence-governed read-to-write workflow.

Major additions since v0.1:

- literature knowledge accumulation;
- field lexicon / accepted-expression tracking;
- equation/model registry;
- claim/evidence ledger;
- domain packs;
- project source-of-truth profiles;
- blueprint-first from-scratch drafting;
- section roles and size diagnostics;
- contribution–evidence matrices;
- reproducibility and comparator audits;
- result/evidence traceability;
- stronger Results vs Discussion distinction;
- regression cases based on real manuscript-review failures.

## License

MIT. See `LICENSE`.
