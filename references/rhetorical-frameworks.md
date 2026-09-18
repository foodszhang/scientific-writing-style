# Rhetorical Frameworks for Scientific Manuscripts

These are **functional frameworks**, not fill-in-the-blank templates. A section can omit, merge, or reorder moves when the science or venue requires it.

Before using these frameworks for a full section, consult:

- `section-role-and-budget.md` for the section's actual job and diagnostic size;
- `manuscript-audit.md` for evidence/reproducibility checks;
- `domain-paper-patterning.md` when field-specific published-paper structure should guide the revision.

## Title

A strong title usually identifies the research object/problem and the distinctive method, mechanism, data condition, or finding.

Prefer informative noun phrases over promotional framing. Avoid leading with `A Novel ...` unless the venue or field convention strongly supports it.

Useful structural patterns include:

- `[Method or mechanism] for [task/problem]`
- `[Task/problem] via [method or principle]`
- `[Property or phenomenon] in [system/setting]`
- `[Method]: [specific purpose or setting]`

Use the field's canonical terms. A title should not introduce synonyms for concepts named differently in the body.

## Abstract

Default move sequence:

1. **Problem/context:** identify the specific scientific or technical problem.
2. **Gap/need:** state what remains difficult, missing, or insufficient.
3. **Aim/response:** state what the study does.
4. **Method:** give only the methodological detail needed to understand the contribution.
5. **Results:** report the central quantitative or qualitative findings with scope.
6. **Meaning:** state the supported implication without expanding beyond the evidence.

For short engineering abstracts, context and gap may be compressed into one or two sentences. Results should carry more information than generic claims such as `achieves superior performance`.

A named module should normally be paired with its function/problem, not merely listed.

Do not repeat the Introduction's broad motivation. Do not spend scarce abstract space on textbook definitions.

## Introduction

A practical move sequence:

1. **Establish the problem territory.** What problem matters, and in what setting?
2. **Narrow to the technical difficulty.** What property makes the problem hard?
3. **Position prior approaches.** Group them by relevant mechanism, assumption, representation, or measurement regime.
4. **Identify the unresolved limitation.** State the limitation at the level needed to motivate this work.
5. **State the research aim/response.** What does this paper do about that limitation?
6. **State contributions.** Describe concrete, parallel, testable contributions.
7. **Optionally preview evidence or organization.**

A contribution statement should answer `what changed technically?`, not merely `what components exist?`.

The gap should map directly to the method. Do not criticize limitations that the paper does not address.

Weak contribution:

> We introduce a novel framework with three modules.

Stronger structure:

> We formulate X so that Y is separated from Z, develop A to realize this separation, and evaluate the resulting method under B and C.

This is a structure example, not a phrase template.

## Related Work

Organize around distinctions that matter to the present problem:

- modeling assumption;
- measurement regime;
- representation;
- supervision;
- optimization/inference strategy;
- spatial/temporal scale;
- validation setting.

For each group:

1. state the shared approach;
2. identify what it handles;
3. identify the limitation relevant to this paper;
4. connect that limitation to the present design choice.

Do not convert Related Work into a sequence of mini-abstracts.

## Methods

A Methods section should make the pipeline **conceptually legible and reproducible**.

Recommended section order:

1. task/problem formulation and framework overview;
2. principal component A;
3. principal component B;
4. integration/output/training objective;
5. implementation details.

For the opening overview, establish before dense notation:
- task;
- input;
- output;
- data flow;
- relationship to the overview figure.

Recommended local pattern for each component:

1. **Role:** what subproblem does this component solve?
2. **Input/state:** what quantities enter?
3. **Operation:** what is computed?
4. **Output:** what is produced?
5. **Constraint/interface:** how does it connect to the next component?
6. **Rationale:** only what is needed to understand the design.

Introduce notation before using it. Keep the same symbol for the same quantity.

Avoid explaining an equation twice: once symbolically and again by narrating every symbol. Explain the relationship and non-obvious terms.

Do not let implementation detail substitute for the scientific idea.

## Experimental Setup

The reader should be able to answer:

- What data were used and how were they obtained or constructed?
- What population/split was evaluated?
- What preprocessing and normalization were applied?
- What acquisition/simulation settings matter?
- What baselines or controlled variants were compared?
- What was held fixed across comparisons?
- How was the evaluation reference or ground truth constructed?
- What metrics and thresholds were used?
- What statistical procedure was used?
- What training/checkpoint-selection details materially affect reproducibility?

A useful ordering is:

`data/acquisition → comparator protocol → metrics/statistics → targeted analyses`

For in vivo or experimental work, prioritize actual biological/acquisition details over generic computational narration.

Prefer concrete procedural statements over `we constructed a dataset` or `standard preprocessing was applied`.

## Results

A strong Results paragraph often follows:

1. **Question/comparison:** what is being tested?
2. **Main finding:** what happened?
3. **Evidence:** relevant numbers, intervals, or observations.
4. **Scope:** where the result applies.
5. **Limited interpretation:** what the result supports.

Prefer:

> Method A increased Dice from X to Y on the fixed test set.

Over:

> Method A achieved remarkable and significantly superior reconstruction performance.

When a table already contains all values, prose should identify the pattern or contrast, not transcribe every cell.

Every prose number should be traceable to a table, figure, or explicitly described analysis.

Representative images illustrate behavior; they do not replace population-level statistics.

## Discussion

Discussion should answer **why the results matter and what they mean**, not merely repeat them.

For each major result, a practical move sequence is:

1. **Importance:** why was this experiment/result important to the paper's argument?
2. **Finding:** state the relevant observation in interpretive rather than tabular terms.
3. **Explanation:** give a plausible mechanism/reason, clearly separating interpretation from direct evidence.
4. **Prior work:** compare with or contextualize the result using relevant published work.
5. **Evidence boundary:** state what the result supports and what it does not establish.
6. **Implication:** connect the interpretation to the broader method/problem.

A multi-paragraph Discussion often works well as:

- positioning paragraph;
- one paragraph per major technical contribution/mechanism;
- measured/external-data paragraph;
- limitations/future-work paragraph.

Do not use Discussion to introduce major unreported results.

Do not begin and end every paragraph by re-reporting metrics. If prior literature is absent from the Discussion, check whether the section is functioning as a second Results section.

## Conclusion

A conclusion should close the paper, not re-run the Abstract or Discussion.

Useful sequence:

1. problem/aim and study response in compressed form;
2. principal technical contribution(s);
3. strongest supported result/evidence;
4. implication within scope.

For a full-length engineering paper, one very short paragraph may be insufficient if it cannot mention both method and evidence.

Avoid generic closing claims such as `This work paves the way for...` unless a specific next capability follows from the results.

## Figure and Table Captions

A caption should let the reader understand the figure/table's role without searching the body for basic definitions.

Include, as needed:

- what is shown;
- experimental condition/population;
- meaning of panels, lines, symbols, or error bars;
- statistical summary;
- abbreviations not already obvious.

Do not make the caption a second Results paragraph.

## Reviewer Responses

Use a compact structure:

1. acknowledge the concrete issue;
2. state the action taken;
3. state where it was changed;
4. explain briefly if the suggestion was partly adopted or not adopted.

Avoid performative gratitude in every response and avoid defensive rhetoric.
