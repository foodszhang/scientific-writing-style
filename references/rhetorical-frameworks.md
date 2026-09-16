# Rhetorical Frameworks for Scientific Manuscripts

These are **functional frameworks**, not fill-in-the-blank templates. A section can omit, merge, or reorder moves when the science or venue requires it.

## Title

A strong title usually identifies the research object/problem and the distinctive method, mechanism, data condition, or finding.

Prefer informative noun phrases over promotional framing. Avoid leading with `A Novel ...` unless the venue or field convention strongly supports it.

Useful title patterns include:

- `[Method or mechanism] for [task/problem]`
- `[Task/problem] via [method or principle]`
- `[Property or phenomenon] in [system/setting]`
- `[Method]: [specific purpose or setting]`

Use the field's canonical terms. A title should not introduce synonyms for concepts named differently in the body.

## Abstract

Default move sequence:

1. **Problem/context:** identify the specific scientific or technical problem.
2. **Gap/need:** state what remains difficult, missing, or insufficient.
3. **Response:** state what the study does.
4. **Method:** give only the methodological detail needed to understand the contribution.
5. **Results:** report the central quantitative or qualitative findings with scope.
6. **Meaning:** state the supported implication without expanding beyond the evidence.

For short engineering abstracts, context and gap may be compressed into one or two sentences. Results should carry more information than generic claims such as `achieves superior performance`.

Do not repeat the Introduction's broad motivation. Do not spend scarce abstract space on textbook definitions.

## Introduction

A practical move sequence:

1. **Establish the problem territory.** What problem matters, and in what setting?
2. **Narrow to the technical difficulty.** What property makes the problem hard?
3. **Position prior approaches.** Group them by relevant mechanism or assumption, not by paper-by-paper chronology unless chronology matters.
4. **Identify the unresolved limitation.** State the limitation at the level needed to motivate this work.
5. **State the research response.** What does this paper do about that limitation?
6. **State contributions.** Describe concrete contributions, not praise words.
7. **Optionally preview evidence or organization.** Use only if useful.

A contribution statement should answer `what changed technically?`, not merely `what components exist?`

Weak contribution:

> We introduce a novel framework with three modules.

Stronger structure:

> We formulate X so that Y is separated from Z, develop A to realize this separation, and evaluate the resulting method under B and C.

This is a structure example, not a phrase template to copy mechanically.

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
2. identify what it handles well;
3. identify the limitation relevant to this paper;
4. connect that limitation to the present design choice.

Do not convert Related Work into a sequence of mini-abstracts.

## Methods

A Methods section should make the pipeline reproducible and the rationale legible.

Recommended local pattern for each component:

1. **Role:** what subproblem does this component solve?
2. **Input/state:** what quantities enter?
3. **Operation:** what is computed?
4. **Output:** what is produced?
5. **Constraint/interface:** how does it connect to the next component?
6. **Rationale:** include only the rationale needed to understand the design.

Introduce notation before using it. Keep the same symbol for the same quantity. Do not alternate between conceptual and implementation names without explicitly mapping them.

Avoid explaining an equation twice: once symbolically and again by narrating every symbol in prose. Explain the relationship and any non-obvious terms.

## Experimental Setup

The reader should be able to answer:

- What data were used and how were they obtained or constructed?
- What split or evaluation population was used?
- What preprocessing and normalization were applied?
- What baselines or controlled variants were compared?
- What was held fixed across comparisons?
- What metrics and thresholds were used?
- What implementation/training details materially affect reproducibility?

Prefer concrete procedural statements over `we constructed a dataset` or `standard preprocessing was applied` when the construction or preprocessing matters.

## Results

A strong results paragraph often follows:

1. **Question/comparison:** what is being tested?
2. **Main finding:** what happened?
3. **Evidence:** give the relevant numbers, intervals, or observations.
4. **Scope:** state where the result applies.
5. **Limited interpretation:** explain what the result supports, not what it merely invites the reader to believe.

Prefer:

> Method A increased Dice from X to Y on the fixed test set.

Over:

> Method A achieved remarkable and significantly superior reconstruction performance.

When a table already contains all values, prose should identify the pattern or contrast, not transcribe every cell.

## Discussion

A practical move sequence:

1. restate the principal finding in interpretive terms;
2. explain a plausible mechanism or reason, clearly separating evidence from interpretation;
3. compare with prior work where the comparison is valid;
4. identify limitations and boundary conditions;
5. state implications or next steps at the strength supported by the study.

Do not use Discussion to introduce major unreported results.

## Conclusion

A conclusion should close the paper, not re-run the abstract.

Useful sequence:

1. problem and response in compressed form;
2. central supported result;
3. implication within scope;
4. one concrete limitation or next step if needed.

Avoid generic closing claims such as `This work paves the way for...` unless a specific next capability follows from the results.

## Figure and Table Captions

A caption should let the reader understand the figure/table's role without searching the body for basic definitions.

Include, as needed:

- what is shown;
- experimental condition or population;
- meaning of panels, lines, symbols, or error bars;
- what statistical summary is plotted;
- abbreviations not already obvious from the figure itself.

Do not make the caption a second Results paragraph.

## Reviewer Responses

Use a compact structure:

1. acknowledge the concrete issue, not the reviewer's status;
2. state the action taken;
3. state where it was changed;
4. explain briefly if the suggestion was only partly adopted or not adopted.

Avoid performative gratitude in every response and avoid defensive rhetoric.
