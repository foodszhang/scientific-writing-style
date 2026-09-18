---
name: scientific-writing-style
description: Audit, plan, draft, and revise English scientific manuscripts with section-aware structure, evidence traceability, reproducibility checks, domain-paper patterning, precise word choice, stable terminology, restrained claim strength, and an optional IEEE overlay. Use for full-manuscript review, section restructuring, abstracts, introductions, methods, experiments, results, discussions, conclusions, captions, reviewer responses, and wording-focused revision. Preserve equations, numbers, citations, method names, and scientific meaning unless the user explicitly asks to change them.
license: MIT
metadata:
  version: "0.2.0"
  scope: "scientific manuscript audit, structure, and prose"
---

# Scientific Writing Style

This skill supports three levels of work:

1. **Wording mode** — local sentence/paragraph polishing without changing scientific structure.
2. **Section mode** — restructure and rewrite one manuscript section so that it performs its scientific/rhetorical job.
3. **Manuscript mode** — audit the complete problem → contribution → method → experiment → result → discussion → conclusion chain before polishing.

The central rule is:

> Do not make a manuscript merely sound more scientific. Make sure each section performs the job required for the scientific argument, then improve the prose.

## Use When

- Reviewing or revising a full scientific manuscript.
- Drafting or restructuring an Abstract, Introduction, Methods, Experimental Setup, Results, Discussion, or Conclusion.
- Auditing whether contributions are actually supported by methods and experiments.
- Checking whether experiments are reproducible and comparisons are fair.
- Comparing section structure with published papers in the same field.
- Improving word choice, sentence flow, terminology, captions, or reviewer responses.
- Compressing a manuscript without deleting the information needed to understand or reproduce the work.
- Applying IEEE-specific language and formatting conventions.

## Mode Selection

### Wording mode

Use when the user asks only for local wording, grammar, compression, terminology, or tone.

Do:
- freeze the scientific structure and evidence;
- make the smallest revision that solves the wording problem;
- preserve claim strength.

Do not:
- expand into a manuscript review unless a scientific ambiguity blocks the edit.

### Section mode

Use when the user asks to rewrite or improve a complete section.

Before drafting:
1. identify the section's actual job;
2. compare the current text against `references/section-role-and-budget.md`;
3. identify missing moves and misplaced material;
4. when useful and sources are available, use `references/domain-paper-patterning.md` to inspect 2–3 relevant published papers;
5. then rewrite.

### Manuscript mode

Use for full-paper revision, reviewer-style assessment, or requests such as "what is wrong with this paper?"

Run `references/manuscript-audit.md` before sentence-level polishing.

Do not begin with line editing if blocking structural, evidence, or reproducibility problems are present.

## Manuscript Workflow

1. **Identify target and venue.**
   - target journal/conference;
   - manuscript type;
   - current page/word constraints;
   - requested level of intervention.

2. **Freeze scientific invariants.**
   - equations;
   - quantitative values;
   - units;
   - citations;
   - variable names;
   - dataset/method names;
   - explicit claims.
   
   Change them only when the user asks for scientific revision or when a verified inconsistency must be surfaced.

3. **Build the story map.**
   Summarize:
   - problem;
   - technical difficulty;
   - gap;
   - study response;
   - contributions;
   - evidence;
   - interpretation;
   - evidence boundary.

4. **Run the contribution–evidence audit.**
   Every contribution should map to:
   `Introduction → Methods → direct experiment → Results → Discussion → Conclusion`.

5. **Run the section-role and size audit.**
   Read `references/section-role-and-budget.md`.
   Report:
   - intended role;
   - role actually performed;
   - missing moves;
   - redundant/misplaced material;
   - size balance.

6. **Run reproducibility and evidence traceability checks.**
   Read `references/manuscript-audit.md`.
   Verify:
   - data/acquisition/simulation protocol;
   - train/validation/test separation;
   - reference/ground-truth construction;
   - comparator fairness;
   - metrics/statistics;
   - every important prose number is traceable to reported evidence;
   - descriptive and inferential claims are not mixed.

7. **Pattern against published papers when appropriate.**
   Read `references/domain-paper-patterning.md`.
   Extract rhetorical structure and field terminology, not copyrighted wording.

8. **Repair scientific structure before prose.**
   Move, add, merge, or delete material only to make section function and evidence flow correct.

9. **Assign communicative functions.**
   For each paragraph/sentence: background, gap, purpose, method, observation, comparison, interpretation, limitation, implication, or transition.

10. **Apply rhetorical frameworks.**
    Read `references/rhetorical-frameworks.md`.

11. **Apply wording rules.**
    Read `references/word-choice.md` and `references/sentence-paragraph.md`.

12. **Apply the venue overlay.**
    For IEEE venues, read `references/ieee-overlay.md`.

13. **Run the anti-pattern pass.**
    Read `references/anti-patterns.md`.

14. **Run final alignment.**
    Confirm:
    - same problem/gap vocabulary across Abstract and Introduction;
    - same contribution hierarchy across Introduction, Methods, Discussion, and Conclusion;
    - results do not claim more than the experiments test;
    - Discussion interprets rather than repeats Results;
    - Conclusion stays within the evidence;
    - terminology is stable throughout.

## Structural Gates

### Gate 1 — Introduction

Pass only if:
- the opening establishes the research problem and why it matters;
- the technical difficulty is explicit;
- prior work is grouped for a reason;
- the gap is one the proposed method actually addresses;
- the aim responds directly to that gap;
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
- how metrics and statistical comparisons were computed.

### Gate 4 — Results

Pass only if:
- every major numerical claim is traceable;
- main comparisons identify the comparator and metric;
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

A Discussion that only repeats numerical results and restates method components does not pass.

### Gate 6 — Conclusion

Pass only if it contains:
- problem/aim in compressed form;
- central technical response;
- strongest supported evidence;
- scoped implication.

Do not use the Conclusion to introduce new results, new limitations, or stronger claims.

## Section Size Discipline

Use `references/section-role-and-budget.md` as a diagnostic, not a rule.

When a section is too long:
1. remove duplicated explanation;
2. move material to the section whose job it actually serves;
3. remove low-value implementation detail;
4. compress wording;
5. only then consider deleting scientific qualifiers or reproducibility details.

When a section is too short:
- add missing scientific function, not filler.

## Domain-Paper Patterning

When the user asks for field-appropriate writing, or when the manuscript sounds structurally unlike published work:

1. inspect 2–3 high-relevance papers;
2. record section order, paragraph functions, terminology, and evidence presentation;
3. compare those functions with the current section;
4. adapt the structure, not the sentences;
5. never invent details to imitate the references.

## Rules

### A. Meaning preservation

- Never change a quantitative value, sign, unit, threshold, sample size, equation, citation, or method name merely to improve style.
- Never strengthen epistemic force during polishing.
- Never replace a precise technical term merely to avoid repetition.
- When a wording change could alter technical meaning, retain the original meaning and flag the ambiguity.

### B. Word choice

- Prefer the shortest word that preserves the intended scientific meaning.
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

Do not vary these verbs merely for style.

### E. Sentence design

- Give each sentence one main proposition.
- Keep the grammatical subject and main verb easy to locate.
- Place conditions and scope restrictions next to the claims they qualify.
- Use active/passive voice according to information structure, not dogma.
- Avoid ambiguous bare demonstratives and unclear noun stacks.

### F. Paragraph design

- Give each paragraph one dominant communicative job.
- Put the route early.
- Keep evidence adjacent to the claim it supports.
- Use explicit transitions only when they encode a real logical relation.
- Do not force a summary sentence at every paragraph end.

### G. Scientific tone

- Prefer restrained, evidence-bearing prose over persuasion.
- Do not tell the reader something is obvious, remarkable, or important when the evidence/consequence can be stated.
- Avoid generic scene-setting and canned gap language.
- Avoid ornamental synonym rotation.

### H. Minimal revision

In wording mode:
1. fix technical ambiguity;
2. fix unnatural/incorrect usage;
3. fix information flow;
4. remove unnecessary words;
5. stop.

In section/manuscript mode, structural repair takes precedence over minimal-diff editing.

## Output Format for Full-Manuscript Review

Unless the user requests another format, return:

1. **Story map**
2. **Blocking findings**
3. **Section-role and size audit**
4. **Contribution–evidence matrix**
5. **Reproducibility/evidence-traceability findings**
6. **Terminology findings**
7. **Revision order**
8. revised text only after the audit priorities are clear

## Edge Cases

- **User requests wording only:** stay in wording mode.
- **User requests aggressive rewriting:** structural changes are allowed, but preserve scientific facts.
- **Ambiguous claim strength:** choose the weaker defensible wording and surface the ambiguity.
- **Journal conflict:** current venue instructions take precedence.
- **Field-specific terminology:** established field usage overrides generic prose preferences.
- **Space-limited venues:** compress redundancy before deleting reproducibility, scope, or evidence boundaries.
- **LaTeX input:** preserve commands, labels, citations, math, and protected capitalization unless explicitly asked to edit them.
- **Reference paper unavailable:** do not invent its wording or protocol; say what could not be verified.

## References

Read as needed:

- `references/manuscript-audit.md` — full scientific/evidence/reproducibility audit.
- `references/section-role-and-budget.md` — section roles, expected content, and diagnostic size ranges.
- `references/domain-paper-patterning.md` — how to learn structure from published papers without copying prose.
- `references/rhetorical-frameworks.md` — section-level rhetorical frameworks.
- `references/word-choice.md` — lexical precision and claim-strength verbs.
- `references/sentence-paragraph.md` — sentence and paragraph architecture.
- `references/anti-patterns.md` — inflated, vague, and AI-like prose patterns.
- `references/ieee-overlay.md` — IEEE house-style layer.
- `references/source-notes.md` — provenance and design notes.

Optional checker:

```bash
python scripts/style_lint.py path/to/manuscript.tex --ieee
```

The checker is advisory. Structural and scientific audits require reasoning and cannot be reduced to regex warnings.
