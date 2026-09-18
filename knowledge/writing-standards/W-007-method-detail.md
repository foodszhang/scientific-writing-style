# W-007 — Method writing should prioritize role, operation, interface, and necessary rationale over layer-by-layer detail

**Status:** CONDITIONAL  
**Category:** Method / Section Structure

## Original comment

Method sections became crowded when they described every layer, parameter, and implementation choice despite strict page limits.

## Trigger example

A subsection spends most of its space enumerating channel counts, kernel sizes, and minor settings before explaining what the module does.

## Underlying concern

Implementation detail can displace the conceptual contribution and make the pipeline harder to understand. At the same time, excessive compression can harm reproducibility.

## External verification

### Official guidance

No universal journal rule fixes the amount of architectural detail required in the main text.

### Recent-paper evidence

Formal paper sampling remains pending. The correct level depends on venue space, novelty location, reproducibility needs, and whether details can be placed in supplementary material.

## Assessment

**Judgment:** Context-dependent

## Current rule

In the main Methods narrative, explain each principal component in this order when practical:

`role → input/state → operation → output → interface/constraint → necessary rationale`.

Keep implementation details that are essential to reproduce or understand the contribution. Compress or move low-value layer-by-layer details when they do not explain the mechanism and page limits are tight.

Conceptual contribution is not equivalent to architecture description.

## Examples

### Avoid when this rule applies

> The module uses three 3×3 convolutions with 64 channels, followed by ...

before the reader knows why the module exists.

### Prefer

> The refinement block predicts only the residual component not represented by the coarse approximation; its implementation details are summarized afterward.

## Scope

Methods / architecture descriptions / space-limited manuscripts

## Confidence

High

## Last verified

2026-09-18

## Decision history

| Date | Status | Change | Evidence / reason |
| --- | --- | --- | --- |
| 2026-09-18 | CONDITIONAL | Initial rule | Recurrent page-limit feedback + method-writing framework |
