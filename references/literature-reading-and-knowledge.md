# Literature Reading and Knowledge Accumulation

Use this workflow when the user asks to read, study, summarize, compare, or learn from scientific papers with the intention of improving later writing.

The goal is not only to summarize a paper. The goal is to convert each paper into **reusable, source-traceable scientific knowledge**.

## Core principle

A paper-reading pass should produce structured assets that can be reused later:

```text
paper
  ↓
paper card
  ↓
domain terminology / accepted expressions
  ↓
equation registry
  ↓
claim & evidence ledger
  ↓
section/rhetorical pattern notes
  ↓
project/domain knowledge base
```

Do not rely on memory alone if durable accumulation is desired. Persist the distilled knowledge in a repository, project workspace, or other user-approved storage.

## 1. Paper card

For each paper, record:

- full citation;
- task/problem;
- modality/domain;
- data and validation setting;
- central method idea;
- section organization;
- main contributions;
- main equations or models;
- principal findings;
- limitations explicitly stated by the authors;
- what the paper can legitimately support in a later manuscript;
- what it cannot support.

Use `knowledge/templates/paper-card.md`.

## 2. Terminology extraction

Extract **field-recognized terminology**, not ornamental wording.

Useful categories:

- object/task terms;
- measurement/acquisition terms;
- physical quantities;
- reconstruction/inference terms;
- evaluation terms;
- anatomical/experimental terms;
- mechanism names;
- common problem descriptions.

For every term, record:

- canonical term;
- precise meaning;
- section/context where it is used;
- source paper(s);
- accepted alternatives;
- misleading or ambiguous alternatives to avoid.

Example structure:

| Canonical term | Meaning | Typical context | Sources | Avoid/confusable |
| --- | --- | --- | --- | --- |
| boundary fluorescence measurements | measured fluorescence information on tissue boundary | Introduction / forward model / Methods | Paper A, Paper B | projection data if acquisition is not a projection process |

Do not store long verbatim sentences as a phrase bank. Short technical expressions and terminology are acceptable; longer rhetorical wording should be paraphrased into a reusable pattern.

## 3. Accepted-expression extraction

Capture **industry/field-recognized ways of saying things** at the level of concepts and collocations.

Good:
- `severely ill-posed inverse problem`
- `surface fluorescence measurements`
- `source localization and morphology recovery`
- `finite-element mesh`
- `anatomical prior`

Avoid storing:
- full multi-sentence passages;
- distinctive prose copied from one paper;
- persuasive wording that is not a field convention.

For each expression, track how many independent sources use or support the same wording/concept. Prefer expressions seen across multiple papers.

## 4. Equation registry

For every equation that may matter later, record:

- equation name/role;
- mathematical form;
- symbol definitions;
- assumptions;
- derivation source;
- what quantity it predicts/relates;
- whether the current project uses it exactly, approximately, or only as a reference model;
- limitations or boundary conditions;
- downstream conclusion enabled by the equation.

Use `knowledge/templates/equation-registry.md`.

Do not copy derivations unnecessarily. Preserve the mathematical relation and explain its role.

## 5. Claim and evidence ledger

For each important conclusion from a paper, record:

- claim;
- evidence type;
- population/dataset/condition;
- quantitative support;
- statistical support if present;
- author-stated limitation;
- strength of claim that can be safely reused.

Example:

| Claim | Evidence | Scope | Safe reuse |
| --- | --- | --- | --- |
| graph-based topology improves morphology recovery | ablation + simulated/in vivo comparison | tested meshes and datasets | supports motivation for topology-aware modeling, not universal superiority |

This prevents later writing from citing a paper for a stronger claim than it actually supports.

## 6. Rhetorical/section pattern notes

Extract how the paper **organizes information**, not the sentences themselves.

For each major section, note:

- section order;
- paragraph function;
- opening move;
- transition logic;
- where equations are introduced;
- where implementation detail is placed;
- how figures/tables are discussed;
- how Discussion differs from Results;
- how limitations are framed.

Store this in the paper card or domain pack.

## 7. Cross-paper synthesis

After reading several papers in the same subfield, update a **domain pack**.

The domain pack should contain:

- canonical terminology;
- recurring physical/model equations;
- standard experimental protocol categories;
- common evaluation metrics;
- common section structures;
- recurring scientific claims and their evidence;
- disagreements or terminology differences across papers.

Do not force consensus when the literature differs. Record the alternatives and the papers that use them.

## 8. Source hierarchy

When later writing from scratch, use this precedence:

1. verified project-specific facts/data;
2. project profile / frozen author decisions;
3. directly read source papers;
4. domain pack synthesized from multiple papers;
5. general scientific-writing guidance;
6. generic model knowledge.

Never silently replace a project fact with a field convention.

## 9. Persistent update rule

When a new paper changes the preferred terminology or scientific framing:

1. update the paper card;
2. update the domain lexicon;
3. note the old term and why it was superseded;
4. update the project profile only if the user accepts the change.

This creates a stable history instead of allowing terminology to drift between writing sessions.
