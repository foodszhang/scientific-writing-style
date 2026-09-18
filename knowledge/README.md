# Knowledge Architecture

This directory defines how long-term literature knowledge should be stored for reuse in later manuscript drafting.

## Three layers

### 1. Core skill

Generic manuscript reasoning and writing rules.

Lives in:
- `SKILL.md`
- `references/`

### 2. Domain pack

Public-literature-derived knowledge for a field such as FMT, BLT, optical tomography, medical image reconstruction, etc.

A domain pack may contain:
- paper cards;
- canonical terminology;
- accepted expressions;
- equation/model registry;
- common metrics;
- common experimental protocol patterns;
- cross-paper disagreements;
- rhetorical patterns.

A domain pack should not contain unpublished project facts.

### 3. Project profile

Private/project-specific source of truth.

Contains:
- exact problem/gap;
- contribution hierarchy;
- method names;
- terminology decisions;
- verified data/results;
- evidence boundaries;
- author/reviewer preferences;
- decision history.

Do not publish a project profile in a public repository if it contains unpublished or sensitive work.

## Recommended durable workflow

```text
read paper
   ↓
paper card
   ↓
update domain lexicon / equation registry / claim ledger
   ↓
update project profile only when the new information is accepted
   ↓
build section blueprint
   ↓
draft from scratch
   ↓
audit against project profile and evidence
```

## Templates

- `templates/paper-card.md`
- `templates/equation-registry.md`
- `templates/project-profile.md`
- `templates/section-blueprint.md`

## Copyright / source discipline

Store:
- citations;
- terminology;
- short technical expressions;
- equations/models needed for scientific understanding;
- paraphrased rhetorical patterns;
- structured summaries and conclusions.

Do not build a repository of copied paragraphs or long distinctive passages from published papers.
