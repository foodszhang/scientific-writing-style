# Scientific-Prose Anti-Patterns

These are warning patterns, not a blacklist. Retain a phrase when it is the clearest accurate choice.

## Empty importance claims

Often removable:

- `plays a crucial/vital/pivotal role`
- `is of great importance`
- `has attracted considerable attention`
- `is an important research topic`

Repair: state the concrete consequence, use, or unresolved problem.

## Meta-writing

Usually replace the wrapper with the actual point:

- `It is worth noting that ...`
- `It should be noted that ...`
- `It can be seen that ...`
- `It is important to mention that ...`

## Inflated novelty or praise

Flag for evidence:

- `novel`
- `groundbreaking`
- `remarkable`
- `excellent`
- `superior`
- `promising`
- `state-of-the-art`
- `unprecedented`

The best repair is usually a specific technical distinction or measured result.

## AI-like generic transitions

Watch repeated use of:

- `Moreover,`
- `Furthermore,`
- `Additionally,`
- `Notably,`
- `Importantly,`
- `Specifically,`

A connector should express a logical relation, not merely decorate a sentence boundary.

## Formulaic gap language

Examples of weak generic structure:

- `Despite these advancements, several challenges remain.`
- `However, existing methods still suffer from several limitations.`
- `To address the aforementioned issues, we propose ...`

These patterns are not forbidden, but they should be replaced when the actual limitation can be named directly.

## Ornamental synonym rotation

Warning pattern:

> method → framework → architecture → scheme → paradigm

If these words denote the same object, choose one canonical term. If they denote distinct levels, define the distinction.

## Overloaded contribution lists

Warning pattern:

> Our main contributions are threefold: first..., second..., third...

This is acceptable when the three contributions are genuinely separable. Do not force every paper into exactly three contributions or make one contribution consist only of `extensive experiments` unless the evaluation design itself is a contribution.

## Double claims

Warning pattern:

> The module improves feature fusion and enhances reconstruction accuracy.

If `enhances reconstruction accuracy` is a downstream empirical effect, separate mechanism from result and support each at the appropriate location.

## Undefined evaluative adjectives

Flag:

- efficient — efficient in what resource?
- robust — robust to what perturbation?
- accurate — by what error metric?
- stable — under what variation?
- flexible — in what dimension?
- general — across what tasks/populations?

## `not only ... but also ...`

Often used by language models to inflate two ordinary facts. Use only when the paired emphasis is genuinely useful.

## `This work paves the way ...`

Replace with a concrete next implication or omit.

## Abstract filler

Avoid spending abstract space on:

- generic growth of a field;
- textbook definitions;
- long lists of challenges;
- `extensive experiments demonstrate...` without the actual result.

## Result narration that duplicates tables

Do not read every table cell into prose. State the comparison or pattern that matters, then give the key values needed to support it.
