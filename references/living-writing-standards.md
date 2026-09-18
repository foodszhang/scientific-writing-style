# Living Writing Standards

Use this layer to govern **writing rules themselves**. It is not a second style guide and not a project-specific decision log.

Its job is to answer:

- Where did a writing rule come from?
- What problem was the original comment actually pointing to?
- Is the rule supported by official guidance, community practice, or only preference?
- In what scope does it apply?
- How confident are we?
- Has later evidence changed the rule?

The central principle is:

> A reviewer, teacher, collaborator, or model comment is evidence that a writing problem may exist; it is not automatically a universal rule.

## 1. Rule lifecycle

Every writing-standard entry must have one status.

### RAW

A newly received comment or observation. Record it faithfully without generalizing it.

Example:

> Teacher comment: `introduce` is inaccurate in the contribution statement.

Do **not** immediately convert this into:

> Never use `introduce`.

### SUPPORTED

External evidence indicates that the rule is broadly consistent with formal guidance or strong community practice.

### CONDITIONAL

The concern is valid only under identifiable conditions.

Example:

> `introduce` is acceptable for genuinely new concepts, terms, components, or formulations, but a more specific verb is usually preferable for a concrete technical operation.

### DISPUTED

The proposed rule conflicts with substantial high-quality evidence, has clear counterexamples, or is mainly an individual preference presented too broadly.

### ADOPTED

The project currently treats the rule as active guidance.

ADOPTED means "use this rule now within its stated scope," not "universally true forever."

### RETIRED

The rule is no longer active because stronger evidence, venue changes, or project changes superseded it.

Keep the history instead of deleting it.

## 2. Required record format

Use `knowledge/templates/writing-standard-entry.md`.

Every substantial entry should distinguish:

- original comment;
- trigger example;
- interpreted underlying concern;
- external verification;
- assessment;
- current rule;
- examples;
- scope;
- confidence;
- last verified;
- decision history.

Do not blur the original comment with the later interpretation.

## 3. Evidence model

### Scientific correctness is non-negotiable

No style preference or venue convention may justify a scientifically false, misleading, or unsupported statement.

### Formal requirements are mandatory within scientifically correct expression

Current journal, publisher, ethics, reporting, and submission requirements override ordinary stylistic preferences.

### Strong community convention

Repeated practice across recent, relevant, high-quality papers can support a writing convention when no formal rule exists.

Prefer evidence from:
1. the target venue;
2. the same or closely related subfield;
3. recent articles whose section function is comparable.

### Context-dependent editorial preference

Choices such as heading granularity, transition density, or active/passive balance may depend on section function, page pressure, and local flow.

### Individual preference

Teacher, collaborator, reviewer, or author preferences may be adopted when they do not conflict with stronger evidence, but must not be mislabeled as field-wide rules.

## 4. Verification workflow

For a new or disputed rule:

```text
Record
  ↓
Interpret
  ↓
Check formal guidance when relevant
  ↓
Inspect comparable published practice
  ↓
Seek counterexamples
  ↓
Assess scope and confidence
  ↓
Adopt / keep conditional / dispute / retire
```

### Verification intensity

Do **not** run a literature audit for every trivial wording issue.

Use lightweight handling for low-risk, stable prose issues such as:
- obvious redundancy;
- term inconsistency;
- empty meta-writing;
- unclear noun stacks;
- grammatical errors.

Use external verification for high-impact or contestable issues such as:
- venue-specific structure;
- citation placement and citation ranges;
- statistical-reporting language;
- contribution wording with novelty implications;
- table/figure conventions;
- claims such as `significant`, `robust`, `generalizable`, `clinically relevant`;
- whether a teacher/reviewer preference should become a reusable rule.

When external paper sampling is needed, start with 2–3 highly relevant papers. Expand toward 5–10 only when practice is mixed, the decision is consequential, or confidence remains low.

## 5. Promotion into the core skill

A Living Standard may be promoted into a stable reference file such as:
- `references/word-choice.md`;
- `references/sentence-paragraph.md`;
- `references/rhetorical-frameworks.md`;
- `references/ieee-overlay.md`.

Promotion is appropriate when:
- the rule is repeatedly useful;
- its scope is clear;
- evidence is strong enough;
- important counterexamples are understood;
- the wording can be applied without hiding the original conditions.

Do not promote RAW opinions directly into core rules.

## 6. Separation from project decisions

Living Standards and Project Profiles serve different purposes.

### Living Standard

Answers:

> What writing rule is supported, under what conditions, and why?

Example:

> Prefer a specific contribution verb over `introduce` when describing a concrete operation; retain `introduce` for genuinely new concepts or formulations.

### Project decision

Answers:

> What does this manuscript use?

Example:

> In the current manuscript, the three contribution bullets use `formulate`, `develop`, and `design`.

Store the first in the Living Standards registry. Store the second in the project profile / decision ledger.

## 7. Recommended categories

- Paper Architecture
- Paragraph Architecture
- Vocabulary
- Contribution
- Claim Strength
- Citation
- Method
- Experimental Setup
- Results
- Discussion
- Figure/Table
- Section Structure
- Statistical Reporting
- Venue-Specific Style

## 8. High-value registries

Maintain focused rule families instead of isolated comments.

### Contribution verbs

Track conditions for:
- `introduce`
- `propose`
- `develop`
- `design`
- `formulate`
- `derive`
- `present`

### Evidence / claim verbs

Track the evidential gradient among:
- `is consistent with`
- `suggests`
- `indicates`
- `shows`
- `demonstrates`
- `establishes`

### High-risk adjectives and claims

Track conditions for:
- `novel`
- `significant`
- `robust`
- `generalizable`
- `effective`
- `superior`
- `clinically relevant`
- `clinical potential`

### Citation standards

Track:
- claim-local citation placement;
- grouped citation ranges;
- author-naming vs passive citation;
- representative-work citation;
- negative contrast claims;
- protocol inheritance terms such as `reproduced`, `adapted`, `followed`, `based on`, and `similar to`.

## 9. Default interpretation rule

When a teacher or reviewer says that wording "is bad," do not ask only whether the phrase appears in published papers.

Identify the underlying failure mode, for example:
- semantic mismatch;
- insufficient information;
- excessive claim strength;
- bibliography-style narration;
- section-role confusion;
- terminology instability;
- unsupported generalization.

The final rule should describe the failure mode and the conditions under which the alternative is preferable.

## 10. Update discipline

Each active rule should record:
- status;
- scope;
- confidence;
- last verified date.

Revisit rules when:
- a target venue changes;
- repeated counterexamples appear;
- a new project exposes an edge case;
- the original rule causes overcorrection;
- a reviewer/teacher preference is found to be narrower than first assumed.

The goal is not to create more rules. The goal is to maintain a small set of **evidence-governed, revisable, traceable scientific-writing decisions**.
