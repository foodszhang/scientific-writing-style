# Sentence and Paragraph Architecture

## Sentence skeleton

A reader should be able to locate the sentence's main subject and verb quickly.

When revising a difficult sentence:

1. identify the main proposition;
2. identify who/what performs or exhibits the main action/relation;
3. move long setup material away from the subject-verb gap where possible;
4. attach conditions and qualifiers to the claim they limit;
5. split the sentence if two independent propositions compete for attention.

## One main proposition per sentence

A scientific sentence may contain subordinate detail, but it should not make the reader resolve several equally important claims at once.

Split when a sentence simultaneously:

- defines a method;
- reports a result;
- interprets the result;
- and states an implication.

Those functions usually deserve separate sentences.

## Information order

Prefer an information path that moves from context to new content.

Common useful patterns:

- known object → new property;
- prior result → contrast/new result;
- experimental condition → observation;
- observation → interpretation;
- limitation → design response.

Do not force a single template across the manuscript. The principle is continuity, not sameness.

## Conditions and qualifiers

Keep scope restrictions close to their target.

Potentially ambiguous:

> The method improved Dice using seven views in all cases.

Possible intended meanings differ: seven views might describe the method, the evaluation, or the cases. Rewrite so the scope is explicit.

## Active and passive voice

Active voice is useful when the actor is meaningful:

> We trained the model on 2400 cases.

Passive voice is useful when the process/object is the topic or the actor is irrelevant:

> The model was trained for 50 epochs.

Do not treat passive voice as an error category in scientific Methods sections.

## Nominalization

Nominalizations are common and sometimes useful in technical writing, especially for established concepts (`optimization`, `registration`, `reconstruction`). The problem is not the noun form itself but unnecessary verb-noun shells.

Prefer:

> We evaluated the model.

Over:

> We performed an evaluation of the model.

But retain established technical nouns when they name a process or object in the field.

## Noun stacks

Long chains such as `multiview boundary evidence fusion module` can hide the relation among concepts.

Possible repairs:

- add a preposition: `module for fusing multiview boundary evidence`;
- introduce the concept once, then use a short stable name;
- split taxonomy from function.

## Demonstratives

Bare `this` is risky when several preceding ideas are plausible referents.

Prefer:

- `this discrepancy`;
- `this constraint`;
- `this improvement`;
- `this observation`.

## Parallelism

Parallel items should have parallel grammar and comparable conceptual granularity.

Weak:

> The method improves reconstruction, lower memory use, and is robust to noise.

Repair by aligning the forms and verifying that all three claims are supported.

## Sentence length

Do not impose a universal word limit. Use length as a diagnostic: if the reader must retain several nested clauses before reaching the main verb, restructure the sentence.

Short sentences are not automatically clear; a sequence of very short sentences can become choppy. Combine only when the logical relation is clear.

## Paragraph architecture

A paragraph normally needs a visible communicative center.

Possible patterns:

### Background paragraph
`topic → relevant facts → narrowing distinction → link to problem`

### Method paragraph
`role → operation → interface/constraint → rationale`

### Results paragraph
`comparison/question → finding → numerical evidence → scope/interpretation`

### Discussion paragraph
`finding → explanation → relation to prior work → limitation/implication`

These are patterns, not mandatory sentence counts.

## Paragraph openings

The first sentence should usually orient the reader. Avoid opening with a detail that only becomes meaningful later.

Useful opening functions:

- name the technical issue;
- state the comparison;
- identify the component's role;
- state the finding being explained.

Avoid generic openers that could begin almost any paper.

## Paragraph endings

End where the communicative job is complete. Good endings may:

- report the key result;
- interpret the result;
- expose the remaining limitation;
- motivate the next component.

Do not add `Therefore, this method is effective` as a compulsory closing sentence.

## Transitions

Use explicit connectors only when they encode a real relation:

- contrast: `however`, `whereas`, `in contrast`;
- consequence: `therefore`, `thus`, `consequently`;
- addition: often no connector is needed;
- specification: `specifically`, `in particular` when the next statement narrows the previous one.

Repeated `Moreover`, `Furthermore`, and `Additionally` often mask weak paragraph structure.

## Compression order

When space is limited, remove in this order:

1. duplicate statements;
2. meta-writing and throat-clearing;
3. redundant adjectives/adverbs;
4. repeated explanations already visible in figures/tables;
5. low-value implementation detail that is available elsewhere.

Preserve, as long as possible:

- scope restrictions;
- experimental conditions;
- quantitative results;
- definitions needed for interpretation;
- limitations that prevent overclaiming.
