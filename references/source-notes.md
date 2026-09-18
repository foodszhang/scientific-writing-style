# Source Notes and Provenance

This skill is an original synthesis of public scientific/technical writing principles, manuscript-review practice, and anonymized structural failure patterns observed during real manuscript revision. It does **not** reproduce a proprietary phrase bank, journal manual, reviewer report, or published-paper prose as a template library.

## Primary inspirations

### Academic Phrasebank, University of Manchester

The Phrasebank organizes academic language by communicative/rhetorical function and draws on genre-analysis traditions associated with rhetorical moves. This skill adopts the general idea of **function-first writing** but does not copy its phrase inventory.

- https://www.phrasebank.manchester.ac.uk/
- https://www.phrasebank.manchester.ac.uk/about-academic-phrasebank/

### Microsoft Writing Style Guide

Useful general principles include choosing simple precise words, removing words that add no substance, and using one term consistently for one concept.

- https://learn.microsoft.com/en-us/style-guide/word-choice/use-simple-words-concise-sentences
- https://learn.microsoft.com/en-us/style-guide/checklists/word-choice-checklist

### Google Developer Documentation Style Guide / Technical Writing

Useful transferable principles include clear actor/action relations, purposeful use of active/passive voice, single-idea paragraphs, early placement of important information, concise sentences, consistent terminology, and explicit information structure.

- https://developers.google.com/style
- https://developers.google.com/style/voice
- https://developers.google.com/style/paragraph-structure
- https://developers.google.com/style/word-list
- https://developers.google.com/tech-writing/one/short-sentences

These sources target technical documentation, not scientific manuscripts, so this skill adapts only principles that transfer well to scientific prose. Scientific field conventions take precedence.

### IEEE Editorial Style Manual for Authors

The IEEE manual supplies the optional IEEE overlay, including house-style concerns such as American spelling, acronym treatment, headings, figures/tables, and article structure. The skill does not redistribute the manual.

- https://journals.ieeeauthorcenter.ieee.org/wp-content/uploads/sites/7/IEEE-Editorial-Style-Manual-for-Authors.pdf

### Real manuscript-review failure patterns

Version 0.2 adds regression cases derived from recurring problems observed during manuscript revision, including:

- Methods beginning with notation before task/input/output/data flow is clear;
- experimental protocols that read smoothly but are not reproducible;
- comparison methods cited or adapted ambiguously;
- prose numbers that cannot be traced to tables/figures;
- subgroup results whose relation to overall results is unclear;
- Discussion sections that repeat Results instead of interpreting them;
- small in vivo cohorts used to support inferential or generalization claims;
- contributions that do not have corresponding direct experiments.

These patterns are abstracted into general rules and synthetic eval prompts. No reviewer report or manuscript text is bundled verbatim as training/template content.

## Domain-paper patterning

The skill may use relevant published papers to infer:

- rhetorical section structure;
- ordering of scientific information;
- field-standard terminology;
- typical evidence presentation;
- Discussion organization.

It must not copy or store published-paper prose as a phrase bank. The goal is to learn **functions and conventions**, not sentences.

## Design decisions

1. **Structure before style for full manuscripts.** A polished sentence cannot repair a missing evidence chain.
2. **No phrase-template corpus.** The skill teaches selection principles rather than canned academic phrases.
3. **Meaning before elegance.** Technical semantics outrank stylistic variety.
4. **Minimal revision in wording mode.** An acceptable sentence is not rewritten merely to create a different sentence.
5. **Structural repair in manuscript mode.** Minimal-diff editing does not override section-function or evidence problems.
6. **Terminology stability.** Scientific prose often benefits from deliberate repetition.
7. **Claim-strength preservation.** Editing must not upgrade evidence.
8. **Evidence traceability.** Important claims and numbers should map to explicit analyses, figures, or tables.
9. **Reproducibility before compression.** Do not shorten away experimental details needed to understand or repeat the work.
10. **Venue overlays are optional.** General scientific manuscript rules remain separate from IEEE house style.

## Licensing note

The text of this repository is released under MIT. External sources listed above remain subject to their own terms and licenses. URLs are provided for attribution and verification; their content is not bundled.
