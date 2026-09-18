# W-002 — Make the paragraph route clear early; do not force a formulaic topic sentence

**Status:** CONDITIONAL  
**Category:** Paragraph Architecture

## Original comment

A recurring teacher/reviewer preference was that each paragraph should have a clear main point.

## Trigger example

A paragraph begins with implementation detail and only reveals its purpose several sentences later.

## Underlying concern

The reader cannot identify the paragraph's communicative job early enough. The underlying issue is orientation and information flow, not compliance with a rigid school-style "topic sentence first" template.

## External verification

### Official guidance

No explicit TMI rule identified requiring every paragraph to begin with a topic sentence.

### Recent-paper evidence

Formal paper sampling is pending. Published scientific prose often orients the reader early, but the first sentence may be a finding, comparison, technical issue, or transition rather than a generic topic sentence.

## Assessment

**Judgment:** Context-dependent

**Reason:** Strong paragraphs usually reveal their route early, but forcing an explicit summary sentence at the start of every paragraph can make prose formulaic.

## Current rule

Make the paragraph's dominant communicative function clear early. The first sentence should usually orient the reader, but it does not need to be a formulaic topic sentence. Do not add an opening sentence that merely repeats what the paragraph already makes clear.

## Examples

### Avoid when this rule applies

> The kernel size is 3. The feature dimension is 64. Three blocks are stacked. These choices are used to refine the estimate.

### Prefer

> The refinement block maps the coarse estimate into a voxel-space residual; its implementation uses three convolutional blocks with 64 channels.

### Also acceptable when appropriate

A Results paragraph may open directly with the tested comparison or the main finding.

## Scope

Entire manuscript

## Confidence

High

## Last verified

2026-09-18

## Decision history

| Date | Status | Change | Evidence / reason |
| --- | --- | --- | --- |
| 2026-09-18 | CONDITIONAL | Initial rule | Recurrent manuscript feedback + current paragraph-design guidance |
