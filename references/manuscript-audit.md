# Scientific Manuscript Audit

Use this audit **before sentence-level polishing** when reviewing a full manuscript or a substantial section.

The audit is intended to catch the kinds of problems that polished English can hide: missing scientific logic, unclear evidence chains, unreproducible experiments, and claims that cannot be traced to reported results.

## 1. Story map

Write one sentence for each item:

1. **Problem:** What scientific/technical problem is the paper solving?
2. **Why difficult:** What property makes it hard?
3. **Gap:** What do existing methods not adequately address?
4. **Response:** What is the central design idea?
5. **Contributions:** What changed technically?
6. **Evidence:** What experiments test each contribution?
7. **Meaning:** What do the results support?
8. **Boundary:** What do the results not establish?

If any answer requires several unrelated sentences, the manuscript likely lacks a stable central story.

## 2. Contribution–evidence matrix

Create one row per claimed contribution.

| Problem/gap | Contribution | Method location | Direct experiment | Result/evidence | Discussion interpretation | Conclusion mention |
| --- | --- | --- | --- | --- | --- | --- |
| ... | ... | ... | ... | ... | ... | ... |

A contribution is incomplete when:
- it has no dedicated Method explanation;
- it has no direct evaluation, controlled comparison, or mechanism analysis;
- the Results do not report evidence for it;
- the Discussion does not interpret the evidence;
- the Conclusion claims it more strongly than the Results support.

## 3. Section-role audit

Use `section-role-and-budget.md`.

For each section report:
- intended role;
- current role actually performed;
- missing rhetorical/scientific moves;
- redundant material that belongs elsewhere;
- size balance.

Do not start rewriting until the major section-role failures are identified.

## 4. Evidence traceability audit

For every important quantitative or comparative claim, identify its evidence source.

Check:
- every prose number appears in a table, figure, equation, or explicitly described analysis;
- subgroup values are related clearly to overall values;
- `best`, `highest`, `lowest`, `improved`, and `significant` claims identify the comparison set and metric;
- confidence intervals and p-values match the stated analysis;
- claims about a mechanism are supported by a direct ablation/targeted analysis rather than only overall performance;
- descriptive small-cohort results are not presented as inferential evidence;
- representative figures are not treated as population-level proof.

If a number cannot be traced, either add its source/context or remove it.

## 5. Reproducibility audit

### Simulated/computational data
Check:
- anatomy/domain definition;
- source/target generation;
- optical/physical/model parameters;
- noise model;
- normalization;
- sample count;
- split and randomization;
- forward simulator / solver;
- evaluation grid/resolution.

### In vivo / experimental data
Check:
- animal/sample/cell model;
- number, sex/age if relevant;
- inoculation / preparation;
- agent/probe administration route and timing;
- acquisition hardware and settings;
- registration/calibration;
- reference-mask or ground-truth construction;
- ethics approval;
- which data are used for training, validation, and testing.

Do not call a manually delineated or anatomically inferred reference a direct physical ground truth unless it truly is one.

### Comparator fairness
Check:
- each baseline has an individual citation;
- task adaptation is described method-by-method when needed;
- input views/data, train/validation/test partitions, normalization, grid, checkpoint selection, and postprocessing are matched where intended;
- animal-specific or case-specific training is clearly attributed to all relevant methods.

## 6. Terminology and concept audit

Build a small ontology before polishing.

For each concept specify:
- canonical term;
- allowed short form;
- terms to avoid;
- whether the distinction is physical, computational, or evaluative.

Examples of distinctions that often matter:
- measurement vs response vs profile vs distribution;
- source distribution vs source strength vs fluorescence yield;
- reference mask vs ground truth;
- framework vs method vs module;
- validation vs evaluation;
- association vs causation.

One concept should not silently change names across sections.

## 7. Discussion-depth audit

For each major result, create a five-part note:

1. **Why this experiment matters**
2. **What was observed**
3. **Why the result may occur**
4. **How prior work contextualizes it**
5. **What the result supports / does not support**

A Discussion paragraph that contains only items 2 and 5 is usually too close to a Conclusion.

## 8. Severity levels

Report findings as:

- **Blocking:** threatens scientific interpretation, reproducibility, or claim validity.
- **Major:** substantially reduces clarity, evidence traceability, or section function.
- **Minor:** wording, formatting, local ambiguity, or presentation polish.

Fix in that order.

## 9. Final manuscript gate

Before calling the manuscript structurally ready, verify:

- [ ] The problem, gap, aim, and contributions use the same conceptual vocabulary.
- [ ] Every contribution maps to Method → Experiment → Result → Discussion.
- [ ] Experimental setup is reproducible at the intended level.
- [ ] Every important numerical claim is traceable.
- [ ] Results distinguish observation from interpretation.
- [ ] Discussion compares with prior work and states evidence boundaries.
- [ ] In vivo / external data claims match the cohort size and training protocol.
- [ ] Conclusion does not exceed the evidence.
- [ ] Section sizes are balanced for the target venue.
- [ ] Only after these checks is sentence-level style polishing considered final.
