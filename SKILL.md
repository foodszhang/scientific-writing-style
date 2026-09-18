---
name: scientific-writing-style
description: Read and distill scientific literature into reusable domain knowledge, audit and plan manuscripts, draft sections from scratch, and revise scientific prose with section-aware structure, evidence traceability, reproducibility checks, domain-paper patterning, precise terminology, restrained claim strength, and an optional IEEE overlay. Use for literature reading, paper cards, terminology/equation/claim accumulation, full-manuscript review, section planning, from-scratch drafting, abstracts, introductions, methods, experiments, results, discussions, conclusions, captions, reviewer responses, and wording-focused revision. Preserve verified equations, numbers, citations, method names, and scientific meaning unless the user explicitly asks to change them.
license: MIT
metadata:
  version: "0.4.0"
  scope: "evidence-governed read-to-write scientific manuscript workflow"
---

# Scientific Writing Style

This skill is a **read-to-write scientific manuscript workflow**, not only a prose polisher.

It supports six modes:

1. **Standards-governance mode** — record, verify, scope, adopt, revise, or retire reusable writing rules.
2. **Literature mode** — read papers and convert them into reusable, source-traceable knowledge.
3. **Project-planning mode** — freeze the manuscript story, contribution hierarchy, terminology, evidence boundaries, and section blueprints.
4. **From-scratch drafting mode** — write a section from a stable blueprint rather than generating a new framing every turn.
5. **Audit/revision mode** — review and repair a complete section or manuscript before polishing.
6. **Wording mode** — perform local sentence/paragraph edits with minimal scientific change.

The central rules are:

> Do not make a manuscript merely sound more scientific. Make sure each section performs the job required for the scientific argument.

> Do not rely on fresh generation when durable project knowledge already exists. Load the project profile, domain pack, paper cards, equation registry, and claim ledger first.

## Use When

- Recording and validating teacher, reviewer, collaborator, or model feedback before turning it into a reusable writing rule.\n- Reading, studying, summarizing, or comparing scientific papers for future writing.
- Building a persistent field lexicon, equation/model registry, claim/evidence ledger, or paper-card library.
- Planning a manuscript from the beginning.
- Drafting an Abstract, Introduction, Methods, Experimental Setup, Results, Discussion, or Conclusion from scratch.
- Reviewing or revising a full scientific manuscript.
- Auditing whether contributions are actually supported by methods and experiments.
- Checking reproducibility, comparator fairness, metric definitions, and evidence traceability.
- Comparing section structure with published papers in the same field.
- Improving word choice, sentence flow, terminology, captions, or reviewer responses.
- Compressing a manuscript without deleting information needed to understand or reproduce the work.
- Applying IEEE-specific language and formatting conventions.

## Source-of-Truth Hierarchy

When sources disagree, use this precedence unless the user explicitly changes it:

1. verified project-specific facts/data;
2. accepted project profile and decision ledger;
3. directly read source papers/files;
4. domain pack synthesized from multiple papers;
5. venue instructions and generic scientific-writing guidance;
6. generic model knowledge.

Never silently replace a project fact with a field convention.

## Writing-Rule Precedence

Scientific correctness is non-negotiable. Within scientifically correct expression, use this order when writing rules conflict:

1. current formal venue/publisher/reporting requirements;
2. accepted manuscript-specific decisions in the project profile;
3. ADOPTED Living Writing Standards within their stated scope;
4. strong, relevant community convention;
5. context-dependent editorial preference;
6. individual preference.

A teacher, reviewer, collaborator, or model comment is not automatically a universal rule. When the rule itself is in question, use `references/living-writing-standards.md`.

## Mode Selection

### Standards-governance mode

Use when a writing comment or preference may become reusable guidance.

Read `references/living-writing-standards.md` and use `knowledge/templates/writing-standard-entry.md`.

Record the original comment separately from the interpreted concern. Assign one lifecycle status:

`RAW → SUPPORTED / CONDITIONAL / DISPUTED → ADOPTED → RETIRED`

Use external verification proportionate to the risk. Do not search 5–10 papers for a trivial grammar issue; do inspect formal guidance and comparable papers for consequential, contestable, or venue-specific rules. Seek counterexamples before promoting a rule into the core references.

### Literature mode

Use when the user asks to read or learn from papers.

Read `references/literature-reading-and-knowledge.md`.

For each relevant paper, extract:

- task/problem;
- method structure;
- data/evaluation setting;
- canonical terminology and short accepted expressions;
- important equations/models and assumptions;
- main findings and quantitative support;
- author-stated limitations;
- what the paper can safely support later;
- section/rhetorical structure.

Persist durable knowledge when the user wants accumulation:

- paper card;
- domain lexicon;
- equation registry;
- claim/evidence ledger;
- domain pack.

Do not build a copied phrase bank. Store terminology, short technical collocations, mathematical relations, paraphrased rhetorical patterns, and structured conclusions.

### Project-planning mode

Use before writing a new manuscript or after a major conceptual revision.

Create or update:

- project profile;
- contribution–evidence matrix;
- terminology lock;
- section-role/size plan;
- section blueprints;
- decision ledger.

Read:

- `knowledge/templates/project-profile.md`
- `knowledge/templates/section-blueprint.md`
- `references/section-role-and-budget.md`

Once accepted, do not silently change the central gap, contribution order, method names, or terminology later.

### From-scratch drafting mode

Use when the user asks to write a section from the beginning.

Read `references/from-scratch-drafting.md`.

Before prose, load:

- project profile;
- relevant domain pack;
- relevant paper cards;
- equation registry;
- claim ledger;
- verified results;
- section blueprint.

Draft in two passes:

1. **scientific skeleton** — correct logic, evidence, citations, terminology;
2. **publication prose** — field-standard wording, sentence flow, compression, venue style.

Do not invent missing experimental facts merely to complete a polished draft.

### Audit/revision mode

Use for full-paper revision, reviewer-style assessment, or substantial section repair.

Run `references/manuscript-audit.md` before line editing.

Check:

- problem → gap → aim → contributions;
- contribution → method → experiment → result → discussion → conclusion;
- section role and size balance;
- reproducibility;
- comparator fairness;
- evidence traceability;
- terminology ontology;
- Discussion depth and evidence boundaries.

If the section structure is wrong, rewrite from the blueprint instead of patching it sentence by sentence.

### Wording mode

Use when the user asks only for local wording, grammar, compression, terminology, or tone.

Do:
- freeze scientific structure/evidence;
- make the smallest revision that solves the wording problem;
- preserve claim strength.

Do not:
- trigger a full manuscript audit unless a scientific ambiguity blocks the edit.

## Literature-to-Writing Workflow

For long projects, use this durable sequence:

```text
read paper(s)
   ↓
paper cards
   ↓
domain lexicon + accepted expressions
   ↓
equation registry
   ↓
claim/evidence ledger
   ↓
cross-paper domain pack
   ↓
project profile
   ↓
section blueprint
   ↓
draft from scratch
   ↓
audit against evidence + project decisions
   ↓
wording/venue pass
```

This workflow is designed to reduce repeated rewriting and terminology drift.

## Manuscript Workflow

1. **Identify target and venue.**
2. **Load or create the project profile.**
3. **Freeze verified scientific invariants.**
4. **Build the story map.**
5. **Run the contribution–evidence audit.**
6. **Run the section-role and size audit.**
7. **Run reproducibility and evidence-traceability checks.**
8. **Pattern against relevant published papers when appropriate.**
9. **Repair scientific structure.**
10. **Create/update section blueprints.**
11. **Draft or revise.**
12. **Apply wording/claim-strength rules.**
13. **Apply venue overlay.**
14. **Run final alignment and terminology checks.**
15. **Record any accepted conceptual/terminology change in the decision ledger.**

## Structural Gates

### Gate 0 — Knowledge base

For a literature-grounded drafting task, pass only if:
- required source papers have been read or their absence is explicit;
- project facts are separated from field conventions;
- important equations/claims are traceable to sources;
- canonical terminology is defined.

### Gate 1 — Introduction

Pass only if:
- the opening establishes the research problem and significance;
- technical difficulty is explicit;
- prior work is grouped for a reason;
- the gap is one the proposed method actually addresses;
- the aim responds directly to the gap;
- contributions are parallel and testable.

### Gate 2 — Methods

Pass only if:
- task, inputs, outputs, and data flow are understandable before dense equations;
- every principal component has a stated role;
- notation is introduced before use;
- component interfaces are explicit;
- implementation detail does not replace conceptual explanation.

### Gate 3 — Experimental Setup

Pass only if a domain reader can reconstruct:
- how data/samples were obtained;
- how training/validation/test data were separated;
- what each comparator received;
- how references/ground truth were produced;
- how metrics/statistics were computed.

### Gate 4 — Results

Pass only if:
- every major numerical claim is traceable;
- main comparisons identify comparator and metric;
- subgroup results are related to overall results;
- representative examples are not treated as population-level proof;
- observation is distinguishable from interpretation.

### Gate 5 — Discussion

Pass only if major findings are discussed through:
- importance;
- observation;
- plausible explanation;
- relation to prior work;
- evidence boundary/implication.

A Discussion that only repeats Results or re-describes modules does not pass.

### Gate 6 — Conclusion

Pass only if it contains:
- problem/aim in compressed form;
- central technical response;
- strongest supported evidence;
- scoped implication.

## Section Size Discipline

Use `references/section-role-and-budget.md` diagnostically, not as a rigid quota.

When a section is too long:
1. remove duplicate explanation;
2. move content to the section whose job it actually serves;
3. remove low-value implementation detail;
4. compress wording;
5. only then consider deleting qualifiers/reproducibility details.

When a section is too short:
- add missing scientific function, not filler.

## Domain-Paper Patterning

Read `references/domain-paper-patterning.md`.

When field-appropriate writing matters:

1. inspect 2–3 high-relevance papers;
2. record section order, paragraph functions, terminology, equation placement, and evidence presentation;
3. compare those functions with the current section;
4. adapt the structure, not the sentences;
5. never invent details to imitate the references.

## Persistent Knowledge Rules

### Paper cards
Use `knowledge/templates/paper-card.md`.

### Domain lexicon
Use `knowledge/templates/domain-lexicon.md`.

Track:
- canonical term;
- meaning;
- context;
- independent sources;
- accepted alternatives;
- terms to avoid.

### Equation registry
Use `knowledge/templates/equation-registry.md`.

Track:
- mathematical form;
- assumptions;
- symbols;
- source;
- project usage;
- conclusion enabled;
- limitations.

### Claim/evidence ledger
Use `knowledge/templates/claim-ledger.md`.

Track:
- claim;
- evidence type;
- population/condition;
- quantitative/statistical support;
- safe later wording;
- overclaim to avoid.

### Domain pack
Use `knowledge/templates/domain-pack.md`.

A domain pack synthesizes multiple public papers and should not contain unpublished project facts.

### Living Writing Standards
Use `references/living-writing-standards.md` and `knowledge/templates/writing-standard-entry.md`.

Use this layer for reusable writing-rule provenance, evidence, scope, confidence, status, and verification history. Do not store manuscript-specific wording decisions here when they belong in the project profile.

### Project profile
Use `knowledge/templates/project-profile.md`.

Treat it as the source of truth for manuscript-specific decisions.

## Consistency Lock

When a project profile exists:

- do not switch terminology for stylistic variety;
- do not reorder contributions between Abstract, Introduction, Discussion, and Conclusion;
- do not change the scientific gap from one writing session to another;
- do not change method/module names without recording the decision;
- do not upgrade `suggests` to `demonstrates` unless evidence changes;
- do not introduce a new citation-dependent claim without source support.

If a better formulation emerges, state the proposed change explicitly and update the decision ledger only after acceptance.

## Rules

### A. Meaning preservation

- Never change a quantitative value, sign, unit, threshold, sample size, equation, citation, or method name merely to improve style.
- Never strengthen epistemic force during polishing.
- Never replace a precise technical term merely to avoid repetition.
- When a wording change could alter technical meaning, retain the original meaning and flag the ambiguity.

### B. Word choice

- Prefer the shortest word that preserves intended scientific meaning.
- Prefer specific verbs over vague verb-noun shells.
- Use one canonical term for one concept.
- Avoid prestige words unless operationalized by evidence.
- Treat `significant` as statistical in quantitative contexts unless clearly defined otherwise.
- Prefer neutral technical verbs when evidence strength is uncertain.

### C. Contribution verbs

| Verb | Use when |
| --- | --- |
| `propose` | putting forward a method, model, criterion, or hypothesis |
| `develop` | building or working out a method/system substantially |
| `design` | specifying an architecture, procedure, experiment, or mechanism |
| `formulate` | expressing a problem, objective, model, or constraint |
| `derive` | obtaining a result through mathematical/logical steps |
| `implement` | realizing a specified method in software/hardware |
| `evaluate` | measuring performance or behavior under stated conditions |
| `validate` | testing against a defined validity criterion/reference/intended use |
| `verify` | checking conformance to a known property/specification |
| `present` | neutrally describing material without claiming invention |
| `introduce` | bringing in a genuinely new concept/term/component/formulation; not a default synonym for `propose` |

### D. Evidence verbs

Use strength deliberately:

`is consistent with` / `suggests` → `indicates` → `shows` → `demonstrates` → `establishes`

Do not vary these merely for style.

### E. Sentence and paragraph design

- Give each sentence one main proposition.
- Keep subject and main verb easy to locate.
- Place scope restrictions next to the claims they qualify.
- Give each paragraph one dominant communicative job.
- Keep evidence adjacent to the claim it supports.
- Use transitions only when they encode a real relation.

### F. Scientific tone

- Prefer restrained, evidence-bearing prose.
- Avoid unsupported praise and generic scene-setting.
- Avoid ornamental synonym rotation.
- Distinguish direct results, author interpretation, and editorial inference.

### G. Minimal revision

In wording mode:
1. fix technical ambiguity;
2. fix unnatural/incorrect usage;
3. fix information flow;
4. remove unnecessary words;
5. stop.

In planning, drafting, or audit modes, structural correctness takes precedence over minimal-diff editing.

## Output Formats

### Standards-governance mode
Return, as appropriate:
1. original comment;
2. interpreted underlying concern;
3. verification evidence and counterexamples;
4. assessment;
5. current operational rule;
6. scope/confidence/last-verified date;
7. status change and decision history.

### Literature mode
Return, as appropriate:
1. paper card;
2. terminology additions;
3. equation/model additions;
4. claim/evidence additions;
5. rhetorical pattern notes;
6. domain-pack updates;
7. unresolved questions.

### Full-manuscript audit
Return:
1. story map;
2. blocking findings;
3. section-role and size audit;
4. contribution–evidence matrix;
5. reproducibility/evidence-traceability findings;
6. terminology findings;
7. revision order.

### From-scratch section drafting
Return:
1. section blueprint;
2. any missing evidence/source warnings;
3. draft;
4. consistency check against project profile.

## Edge Cases

- **User requests wording only:** stay in wording mode.\n- **Teacher/reviewer says a phrase is wrong:** record the concern first; do not universalize it without checking scope and evidence when the rule is consequential or disputed.
- **User asks to read only one supplied paper:** do not generalize one paper's terminology into a field-wide convention without qualification.
- **Reference paper unavailable:** do not invent its wording, equation, protocol, or conclusion.
- **Ambiguous claim strength:** choose the weaker defensible wording.
- **Journal conflict:** current venue instructions take precedence.
- **Field-specific terminology:** established field usage overrides generic prose preferences.
- **Space-limited venues:** compress redundancy before deleting reproducibility, scope, or evidence boundaries.
- **LaTeX input:** preserve commands, labels, citations, math, and protected capitalization unless explicitly asked to edit them.
- **Public knowledge repository:** do not store unpublished project facts unless the user explicitly wants them public.

## References

Read as needed:

- `references/living-writing-standards.md` — evidence-governed lifecycle for reusable writing rules.\n- `knowledge/templates/writing-standard-entry.md` — standard record for RAW/SUPPORTED/CONDITIONAL/DISPUTED/ADOPTED/RETIRED rules.\n- `references/literature-reading-and-knowledge.md` — paper reading and durable knowledge extraction.
- `references/from-scratch-drafting.md` — stable blueprint-first drafting.
- `references/manuscript-audit.md` — scientific/evidence/reproducibility audit.
- `references/section-role-and-budget.md` — section roles and diagnostic size ranges.
- `references/domain-paper-patterning.md` — learn field structure without copying prose.
- `references/rhetorical-frameworks.md` — section-level rhetorical frameworks.
- `references/word-choice.md` — lexical precision and claim-strength verbs.
- `references/sentence-paragraph.md` — sentence and paragraph architecture.
- `references/anti-patterns.md` — inflated, vague, and AI-like prose patterns.
- `references/ieee-overlay.md` — IEEE house-style layer.
- `knowledge/README.md` — persistent knowledge architecture.
- `references/source-notes.md` — provenance and design notes.

Optional checker:

```bash
python scripts/style_lint.py path/to/manuscript.tex --ieee
```

The checker is advisory. Literature synthesis, structural audit, and scientific consistency require reasoning and cannot be reduced to regex warnings.
