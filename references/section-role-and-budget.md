# Section Roles and Size Budgets

This file defines **diagnostic defaults**, not journal rules. Venue instructions and the scientific content always take precedence.

The goal is to prevent two common failures:

1. a section is present but does not perform its actual rhetorical/scientific job;
2. one section consumes space that should be carrying evidence or interpretation elsewhere.

Use relative proportions first. Page counts are secondary because figures, equations, and tables distort page length.

## Default manuscript budget

For a full-length engineering or medical-imaging paper, a useful starting profile is:

| Section | Primary job | Typical share of main narrative | Typical paragraph count / size |
| --- | --- | ---: | --- |
| Title | Identify problem + distinctive method/finding | — | usually 8–18 words |
| Abstract | Problem → response → method → evidence → meaning | — | commonly 150–250 words; many IEEE venues cap at 250 |
| Introduction | Establish importance, prior approaches, exact gap, study response, contributions | 12–18% | often 4–6 substantive paragraphs |
| Methods | Make the proposed method understandable and reproducible | 30–40% | overview + 2–5 technical subsections + implementation |
| Experimental Setup | Define data, protocol, comparators, metrics, statistics | 10–15% | often 3–5 compact subsections |
| Results | Answer the experimental questions with evidence | 20–30% | main comparison + ablations/mechanism + external/measured data |
| Discussion | Explain what the results mean, why, how they relate to prior work, and where they stop | 12–18% | often 4–6 paragraphs |
| Conclusion | Close the paper: problem, response, strongest evidence, scoped implication | 2–4% | commonly 120–220 words in an 8–10 page engineering paper |

These are starting ranges, not acceptance criteria.

### TMI-like 9–10 page diagnostic profile

For a dense IEEE Transactions-style manuscript with several figures/tables, the following is a practical planning aid:

- Introduction: about 1.2–1.8 pages
- Methods: about 3.0–4.0 pages
- Experimental setup + Results: about 2.5–3.5 pages
- Discussion: about 0.8–1.4 pages
- Conclusion: about 0.15–0.35 pages, usually around 120–220 words

Do not force a manuscript into these ranges. Use them to detect imbalance. A 4.5-page Methods section may be justified if the method is mathematically dense; a 0.5-page Discussion may be too short if the paper makes several mechanistic claims.

## Section-by-section role checks

### Title

**Job:** tell the reader what the paper is about and what is distinctive.

Must answer at least two of:
- What task/problem?
- What method/mechanism?
- What setting/modality?
- What distinctive property or finding?

Failure signals:
- title contains only method names;
- title uses vague praise instead of a technical distinction;
- title introduces terminology not used consistently in the paper.

### Abstract

**Job:** compress the entire paper into one evidence-bearing argument.

Recommended move order:
1. specific problem/context;
2. unresolved difficulty;
3. study aim/response;
4. only the method details needed to understand the contribution;
5. central quantitative evidence;
6. scoped implication.

Audit questions:
- Can a reader state the exact problem after the first 2–3 sentences?
- Does each named module have a clear problem/function?
- Are the most important results numerical rather than adjectival?
- Does the final sentence stay within the tested scope?

### Introduction

**Job:** justify the study and make the contribution logically inevitable.

A strong Introduction normally contains:
1. field/problem significance;
2. technical difficulty;
3. prior approaches grouped by mechanism or assumption;
4. unresolved gap relevant to the present work;
5. study aim and design response;
6. contributions at matched conceptual granularity.

Audit questions:
- Does the first paragraph end with the actual unresolved problem, not just background?
- Is prior work grouped for a reason, rather than listed chronologically?
- Is the gap something the proposed method actually addresses?
- Does every contribution correspond to a Method component and later evidence?

### Methods

**Job:** let a domain reader understand the computational/experimental logic and reproduce the method at the intended level.

Recommended hierarchy:
1. problem formulation and framework overview;
2. one subsection per principal technical component;
3. reconstruction/output/training objective;
4. implementation details.

Every main component should answer:
- Why is this component needed?
- What enters it?
- What is computed?
- What leaves it?
- How does it connect to the next stage?
- Which equations/constraints are essential to understanding the design?

A Methods section should not begin with symbols before the task, inputs, outputs, and data flow are clear.

### Experimental Setup

**Job:** make the evaluation reproducible and fair.

Must specify, as applicable:
- dataset/population and how it was created/acquired;
- inclusion/exclusion or source-generation protocol;
- train/validation/test split;
- preprocessing and normalization;
- acquisition/simulation settings;
- comparison methods and exact adaptation;
- what was held fixed across methods;
- evaluation reference / ground-truth construction;
- metrics and component-matching rules;
- statistical tests, confidence intervals, multiplicity correction;
- training/selection protocol.

If a reader cannot reconstruct how a sample, reference mask, metric, or comparator result was produced, the setup is incomplete.

### Results

**Job:** answer predefined questions using figures, tables, and statistics.

Recommended paragraph pattern:
1. question/comparison;
2. main finding;
3. key evidence;
4. scope;
5. limited interpretation.

Audit questions:
- Can every number in prose be traced to a table, figure, or stated analysis?
- Are subgroup numbers explained relative to the overall result?
- Does prose identify the pattern instead of reading every table cell?
- Are mechanistic claims separated from direct observations?

### Discussion

**Job:** interpret the evidence, not repeat it.

A strong Discussion usually does four things:
1. states the important finding in interpretive terms;
2. explains a plausible reason/mechanism;
3. compares that interpretation with relevant prior work;
4. defines limitations, boundary conditions, and implications.

For each major experimental claim, ask:
- Why was this result important?
- What did the experiment actually show?
- Why might this result occur?
- Which prior work supports, contrasts with, or contextualizes the interpretation?
- What does the result support, and what does it not establish?

Failure signals:
- paragraph is a compressed Results section;
- no prior work is discussed;
- mechanism is asserted without evidence;
- Discussion introduces new results;
- limitations are generic or disconnected from the method.

### Conclusion

**Job:** close the argument, not repeat the Abstract.

Recommended sequence:
1. problem + study response;
2. principal technical contribution(s);
3. strongest supported evidence;
4. scoped implication.

For a full-length engineering paper, a conclusion under ~100 words is often too compressed to do all four jobs; a conclusion over ~250 words often starts repeating the Discussion.

## Budget audit

When reviewing a full manuscript, report:

- current section size;
- recommended diagnostic range;
- whether the section is **underdeveloped**, **balanced**, or **overweight**;
- what function is missing or taking too much space;
- what should move to another section rather than simply be deleted.

Never cut Methods or Experimental Setup merely to hit a page target if doing so makes the paper non-reproducible.
