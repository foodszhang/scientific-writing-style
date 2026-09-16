---
name: scientific-writing-style
description: Write and revise English scientific and technical prose with precise word choice, stable terminology, concise sentences, coherent paragraphs, section-aware rhetorical structure, and an optional IEEE house-style overlay. Use for manuscripts, abstracts, titles, captions, methods, results, discussions, conclusions, reviewer responses, and wording-focused revision. Preserve technical meaning, numbers, equations, citations, and claim strength unless the user explicitly asks to change them.
license: MIT
metadata:
  version: "0.1.0"
  scope: "scientific prose and manuscript style"
---

# Scientific Writing Style

A writing-layer skill for scientific and technical prose. It is intentionally narrower than a scientific reviewer: its main job is **how to say the intended content clearly, conventionally, and precisely**, not whether the science is correct.

## Use When

- Drafting or rewriting scientific manuscript prose in English.
- Improving word choice, sentence structure, paragraph flow, section titles, captions, or abstract wording.
- Converting literal, translated, inflated, or AI-sounding prose into conventional scientific English.
- Compressing text without changing technical meaning.
- Standardizing terminology across a manuscript.
- Choosing among verbs such as `propose`, `develop`, `formulate`, `derive`, `evaluate`, `validate`, `verify`, `show`, `suggest`, and `demonstrate`.
- Applying IEEE-specific language and formatting conventions when the target venue is an IEEE journal, transaction, or letter.

## Don't Use When

- The primary task is judging scientific validity, novelty, experimental design, or statistical correctness. Perform a scientific review first, then use this skill for wording.
- The user asks for citation discovery or literature verification. Use literature-search and source-verification tools instead.
- The user asks for creative, promotional, conversational, legal, or marketing writing.
- The user requests a journal-specific rule that conflicts with this skill. The target journal's current author instructions take precedence.

## Workflow

1. **Identify the writing job.** Determine the target section, venue, audience, and whether the user wants drafting, polishing, compression, or a wording audit.
2. **Freeze invariants.** Treat equations, numbers, units, citations, variable names, named methods, dataset names, and explicit scientific claims as immutable unless the user asks to change them.
3. **Assign a communicative function.** For each sentence or paragraph, identify its job: background, gap, purpose, method, observation, comparison, interpretation, limitation, implication, or transition.
4. **Choose conventional wording.** Prefer the simplest precise verb and the established technical term. Do not manufacture lexical variety.
5. **Repair sentence information flow.** Make the actor/action or object/relation easy to find; keep qualifiers near the claims they limit; split overloaded sentences.
6. **Repair paragraph structure.** Give each paragraph one dominant communicative job and a visible route through it.
7. **Apply the section framework.** Consult `references/rhetorical-frameworks.md` for the relevant manuscript section.
8. **Apply the lexical and prose rules.** Consult `references/word-choice.md` and `references/sentence-paragraph.md` when wording is uncertain.
9. **Apply an optional venue overlay.** For IEEE venues, consult `references/ieee-overlay.md` after the prose is scientifically clear.
10. **Run an anti-pattern pass.** Remove inflated, vague, formulaic, or persuasion-heavy language using `references/anti-patterns.md`.
11. **Preserve meaning on output.** By default, return the smallest revision that solves the writing problem. Do not silently strengthen claims.

## Rules

### A. Meaning preservation

- Never change a quantitative value, sign, unit, threshold, sample size, equation, citation, or method name merely to improve style.
- Never strengthen epistemic force during polishing. `suggests` must not become `demonstrates`; `associated with` must not become `causes`; `improves on this dataset` must not become `generalizes better`.
- Never replace a precise technical term merely to avoid repetition.
- When a wording change could alter technical meaning, retain the original meaning and flag the ambiguity instead of guessing.

### B. Word choice

- Prefer the shortest word that preserves the intended scientific meaning: usually `use` rather than `utilize`, and `to` rather than `in order to`.
- Prefer specific verbs over vague verb-noun shells: `we measured` over `we performed a measurement of` when both mean the same thing.
- Use one canonical term for one concept. Lexical repetition is acceptable when terminological stability matters.
- Do not use prestige words as decoration. Words such as `novel`, `robust`, `efficient`, `effective`, `accurate`, `comprehensive`, `significant`, and `state-of-the-art` need an explicit basis in the surrounding text.
- Treat `significant` as statistical when the context is quantitative; if no statistical inference is intended, use a more exact description.
- Prefer a neutral technical verb over a stronger rhetorical verb when evidence strength is uncertain.

### C. Contribution verbs

Use verbs according to what was actually done:

| Verb | Use when |
| --- | --- |
| `propose` | putting forward a new method, model, criterion, or hypothesis |
| `develop` | building or working out a method/system substantially |
| `design` | specifying an architecture, procedure, experiment, or mechanism |
| `formulate` | expressing a problem, objective, model, or constraint mathematically/conceptually |
| `derive` | obtaining a result through mathematical or logical steps |
| `implement` | realizing a specified method in software/hardware |
| `evaluate` | measuring performance or behavior under stated conditions |
| `validate` | testing against a defined validity criterion, reference, or intended use |
| `verify` | checking conformance to a known property, specification, or derivation |
| `present` | neutrally describing material without claiming invention |
| `introduce` | bringing in a genuinely new concept, term, component, or formulation; not a default synonym for `present` or `propose` |

### D. Evidence verbs

- `suggest` / `indicate`: use for limited or indirect evidence.
- `show`: use for a result directly supported by the reported analysis.
- `demonstrate`: reserve for stronger evidence that clearly establishes the stated phenomenon under the tested conditions.
- `establish`: use sparingly for a conclusion supported strongly enough to function as a settled result within the stated scope.
- Do not vary these verbs only for style; they encode different claim strengths.

### E. Sentence design

- Give each sentence one main proposition. A second proposition is acceptable when its logical relation is immediately clear.
- Put the grammatical subject and main verb close enough that the reader can identify the sentence skeleton without holding a long modifier in memory.
- Place conditions, scope restrictions, and uncertainty markers next to the claims they qualify.
- Prefer active voice when the actor matters. Use passive voice when the object/process is the natural topic or the actor is irrelevant; do not mechanically convert Methods prose to active voice.
- Use explicit nouns after vague demonstratives when needed: `this discrepancy`, `this result`, `this constraint`, not bare `this` when the referent could be ambiguous.
- Avoid noun stacks when their internal relation is unclear. Unpack the relation with a preposition or clause.
- Avoid repeated sentence templates across a paragraph.

### F. Paragraph design

- Give each paragraph one dominant communicative function.
- Put the paragraph's route early: the reader should know what the paragraph is about before encountering details.
- Arrange sentences so that known/contextual information leads into new information when possible.
- Keep evidence adjacent to the claim it supports.
- Do not add a transition merely because a paragraph lacks one. Use `however`, `therefore`, `moreover`, and similar connectors only when the logical relation actually requires them.
- A paragraph may end with a result, interpretation, limitation, or forward link; do not force a summary sentence after every paragraph.

### G. Scientific tone

- Prefer precise and restrained prose over persuasive or promotional prose.
- Avoid telling the reader that something is `obvious`, `clear`, `remarkable`, or `interesting`; state the evidence or consequence instead.
- Avoid empty scene-setting such as `In recent years, X has attracted increasing attention` unless the trend itself matters and is supported.
- Avoid meta-writing such as `It is worth noting that` when the sentence can state the point directly.
- Avoid formulaic three-part lists, paired `not only ... but also ...`, and ornamental synonym rotation unless they serve the content.

### H. Minimal-revision default

When revising existing prose:

1. fix technical ambiguity;
2. fix unnatural or incorrect usage;
3. fix information flow;
4. remove unnecessary words;
5. stop.

Do not rewrite an acceptable sentence merely to make it different.

## Examples

- `We introduce a reconstruction method and validate its performance on the test set.`  
  If the work actually builds a method and only benchmarks it, prefer: `We develop a reconstruction method and evaluate it on the test set.`

- `In order to effectively utilize the available measurements, we perform the construction of a multiview feature representation.`  
  Prefer: `To use the available measurements, we construct a multiview feature representation.`

- `The proposed framework demonstrates significantly better robustness.`  
  Do not polish this blindly. Ask what `significantly`, `better`, and `robustness` mean operationally. If the evidence is only a numerical improvement under one perturbation, report that result directly.

- `Our framework employs a coarse representation. The architecture then transfers the estimate to the voxel domain. The proposed scheme predicts a residual.`  
  If all three nouns refer to the same method, keep one canonical term rather than rotating `framework`, `architecture`, and `scheme`.

- `The measurements were acquired from seven views.`  
  Keep passive voice if acquisition is the topic and the actor is irrelevant. Do not convert to `We acquired...` solely because active voice is generally preferred.

## Edge Cases

- **User requests aggressive rewriting:** preserve scientific meaning first; larger structural changes are allowed only within the requested scope.
- **Non-native but technically correct phrasing:** prefer conventional scientific English, not idiomatic flourish.
- **Ambiguous claim strength:** choose the weaker defensible wording and surface the ambiguity.
- **Journal conflict:** follow the current journal instructions over this skill.
- **Field-specific terminology:** established field usage overrides general-language preferences. Do not replace technical `utilization`, `activation`, `registration`, `significance`, or similar terms when they carry domain-specific meanings.
- **Space-limited venues:** compress redundancy before deleting qualifiers, experimental conditions, or causal/epistemic boundaries.
- **LaTeX input:** preserve commands, labels, citations, math, and protected capitalization unless the user explicitly requests LaTeX edits.

## References

Read these only as needed:

- `references/rhetorical-frameworks.md` — section-level writing frameworks.
- `references/word-choice.md` — lexical precision, claim-strength verbs, and terminology stability.
- `references/sentence-paragraph.md` — sentence and paragraph architecture.
- `references/anti-patterns.md` — common inflated and AI-like prose patterns.
- `references/ieee-overlay.md` — optional IEEE house-style layer.
- `references/source-notes.md` — source provenance and design notes.

Optional deterministic checker:

```bash
python scripts/style_lint.py path/to/manuscript.tex --ieee
```

The checker is advisory. A warning is not automatically an error.
