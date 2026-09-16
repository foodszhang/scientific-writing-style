# Word Choice and Lexical Precision

## 1. Terminology stability

The core rule is simple:

> One concept, one canonical term, unless a genuine distinction requires two terms.

Do not rotate among `method`, `framework`, `architecture`, `scheme`, `pipeline`, and `strategy` merely to avoid repetition. If they denote different levels, define that hierarchy explicitly.

Maintain stable names for:

- methods and variants;
- datasets and data splits;
- variables and physical quantities;
- stages/modules/components;
- metrics;
- anatomical or experimental regions;
- assumptions and constraints.

## 2. Prefer precise simple words

When meaning is unchanged, prefer the simpler conventional form:

| Prefer | Usually avoid when meaning is identical |
| --- | --- |
| use | utilize |
| to | in order to |
| because | due to the fact that |
| before | prior to |
| after | subsequent to |
| many/several | a large number of |
| about/approximately | in the vicinity of |
| show/report | give an indication of |
| measure | perform a measurement of |
| analyze | perform an analysis of |

These are preferences, not blind substitutions. Domain-specific senses override them.

## 3. Method and contribution verbs

### propose
Use for a method, model, hypothesis, criterion, or formulation that the paper puts forward. `Propose` does not by itself prove novelty.

### develop
Use when the work actually builds, derives, or works out a method/system beyond merely presenting it.

### design
Use for deliberately specified architectures, protocols, acquisition schemes, losses, experiments, or mechanisms.

### formulate
Use for mathematical problems, optimization objectives, probabilistic models, or explicit conceptual formulations.

### derive
Use when a result follows from mathematical/logical manipulation.

### introduce
Use when a concept, term, mechanism, representation, or component is genuinely brought into the work. Avoid as an ornamental default for any contribution.

### present
A useful neutral verb when invention is not the point.

### implement
Means realization, not invention or validation.

## 4. Evaluation verbs

### evaluate
Measure performance or behavior under stated conditions. This is the safe default for benchmark experiments.

### validate
Use when the experiment tests validity against a defined reference, intended use, criterion, or independent evidence. Ordinary benchmarking is not automatically validation.

### verify
Check whether a known property, identity, specification, derivation, or implementation condition holds.

### test
Broad and neutral. Good when the exact epistemic status does not require a stronger word.

## 5. Evidence-strength verbs

From weaker to stronger, roughly:

`is consistent with` / `suggests` → `indicates` → `shows` → `demonstrates` → `establishes`

This is not a stylistic ladder. Choose based on evidence strength and scope.

- **suggests**: limited, indirect, noisy, or exploratory evidence.
- **indicates**: evidence points toward the claim but may not be decisive.
- **shows**: direct support for the stated result under the reported conditions.
- **demonstrates**: strong evidence for the stated phenomenon or capability.
- **establishes**: strong, usually convergent or formal support that justifies treating the conclusion as settled within a defined scope.

Do not upgrade verbs during polishing.

## 6. High-risk evaluation words

These words are often legitimate but must be operationalized.

### significant / significantly
If statistical inference is intended, connect the word to a test, interval, or model. If only numerical magnitude is intended, report the magnitude or use a more precise descriptor.

### robust
Specify robustness to what: noise, initialization, parameter variation, domain shift, missing views, perturbations, or something else.

### efficient
Specify the resource: time, memory, FLOPs, sample count, acquisitions, or energy.

### accurate
Name the error/accuracy metric and evaluation setting.

### effective
State the outcome it improves.

### comprehensive
Use only when coverage is actually broad relative to a defined scope.

### novel
Prefer stating the concrete new element. Use `novel` only when novelty is materially relevant and reasonably supported.

### first
Requires a scoped literature claim. Qualify by task, modality, setting, date, or other boundary when necessary.

### state-of-the-art
Requires a defined benchmark, comparator set, metric, and time context. Prefer the measured result over the label.

## 7. Comparison language

Prefer explicit comparisons:

- `A increased X from ... to ...`
- `A reduced Y by ... relative to B`
- `A and B were similar within ...`
- `A improved X on dataset D but not on dataset E`

Avoid unqualified:

- `better performance`
- `superior results`
- `large improvement`
- `more robust`

If the metric direction is not obvious, write it explicitly.

## 8. Causal language

Do not convert association into causation during revision.

Use:

- `is associated with` for association;
- `coincides with` for temporal or observational co-occurrence;
- `may arise from` for plausible mechanism;
- `is caused by` / `leads to` only when the design or derivation supports causality.

## 9. Scope and hedging

Hedges should encode actual uncertainty, not politeness.

Useful forms include:

- `may` for possibility;
- `can` for capability or possible outcome;
- `suggests` for limited evidence;
- `under the tested conditions` for empirical scope;
- `in this dataset` / `for the evaluated cases` for population scope;
- `approximately` for numerical approximation.

Avoid stacking hedges (`may possibly suggest that...`) unless distinct uncertainties really exist.
