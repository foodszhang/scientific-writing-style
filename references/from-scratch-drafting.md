# From-Scratch Scientific Drafting

Use this workflow when the user asks to write a manuscript, section, or paragraph from the beginning rather than iteratively patching an existing draft.

The central principle is:

> **Plan once from verified knowledge, then draft consistently from a frozen blueprint.**

Do not regenerate the paper's conceptual framing independently on every turn.

## 1. Required inputs

Before drafting a substantial section, assemble:

- target venue and manuscript type;
- project profile;
- section role and target size;
- contribution hierarchy;
- canonical terminology;
- relevant domain pack;
- relevant paper cards;
- verified results/data;
- citation set available for the section.

If an essential input is missing, identify the gap instead of inventing it.

## 2. Project profile

The project profile is the manuscript's source of truth.

It should freeze:

- one-sentence problem;
- technical difficulty;
- exact gap;
- study aim;
- contribution hierarchy;
- method/module names;
- canonical terminology;
- data/evaluation scope;
- strongest supported results;
- evidence boundaries;
- title/abstract terminology decisions;
- terms explicitly rejected by the authors.

Use `knowledge/templates/project-profile.md`.

Once accepted, do not silently change these decisions in later drafts.

## 3. Section blueprint

Before prose, create a section blueprint.

For each paragraph define:

- paragraph job;
- evidence/source;
- target length;
- key terms;
- expected transition;
- whether it is factual, interpretive, or evaluative.

Example:

| Paragraph | Job | Evidence/source | Target |
| --- | --- | --- | --- |
| Intro P1 | FMT significance + NIR-II context + core difficulty | reviews + modality papers | 120–150 words |
| Intro P2 | conventional reconstruction approaches | refs 9–15 | 120–160 words |
| Intro P3 | learned reconstruction approaches | refs 16–21 | 120–160 words |
| Intro P4 | structured/model-guided approaches | refs 22–24 | 100–140 words |
| Intro P5 | unresolved measurement-usage gap | physics + prior-method synthesis | 100–140 words |
| Intro P6 | aim + method response + contributions | project profile | 120–160 words |

Use `knowledge/templates/section-blueprint.md`.

## 4. Drafting contract

When a blueprint is accepted:

- keep paragraph roles stable;
- keep canonical terms stable;
- keep contribution hierarchy stable;
- do not reframe the scientific gap without explicit reason;
- do not add new claims or citations silently;
- do not change strong/weak evidence verbs across turns unless evidence changes.

If a later revision requires structural change, explain which frozen decision changes and why.

## 5. Use literature actively

While drafting:

- borrow field-standard terminology and conceptual organization;
- use paper cards to decide what each citation actually supports;
- use equation registry entries for mathematical consistency;
- use domain patterns to choose section order and detail level;
- paraphrase published-paper rhetoric instead of copying sentences.

## 6. Draft in two passes

### Pass A — scientific skeleton

Write plain, compact prose that makes the logic explicit.

Prioritize:
- factual accuracy;
- source/evidence traceability;
- paragraph role;
- terminology consistency.

### Pass B — publication prose

Then apply:
- sentence flow;
- field-standard collocations;
- claim-strength calibration;
- venue overlay;
- compression.

Do not reverse this order.

## 7. Consistency lock

Before delivering a section, check:

- Does terminology match the project profile?
- Does the gap match the Introduction plan?
- Do method names match the Methods plan?
- Are all cited claims supported by paper cards?
- Are equations consistent with the registry?
- Do Results use the same metric definitions?
- Does Discussion use the same evidence boundaries?
- Does Conclusion preserve the same contribution hierarchy?

## 8. Version stability

For long manuscript projects, maintain a small decision ledger.

For each major change record:

- previous wording/decision;
- new wording/decision;
- reason;
- affected sections.

This avoids oscillation such as:
- `response` one day, `measurement` the next;
- `yield` one section, `source distribution` another;
- contribution order changing between Abstract and Conclusion.

## 9. When to rewrite from scratch

Prefer from-scratch drafting when:

- the original section has the wrong rhetorical structure;
- reviewer comments show the section performs the wrong job;
- many local edits would preserve a flawed organization;
- terminology or contribution hierarchy has changed substantially;
- the manuscript has been patched across many revisions and has become internally inconsistent.

Prefer local revision when the scientific structure is already sound.
