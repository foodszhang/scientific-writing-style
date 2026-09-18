# W-010 — Use protocol-inheritance verbs that match the actual relationship

**Status:** ADOPTED  
**Category:** Citation / Experimental Setup / Method

## Original comment

Experimental protocols derived from prior work were sometimes described vaguely, making it unclear whether the protocol was copied exactly, modified, or only conceptually similar.

## Trigger example

> The imaging protocol was based on [X].

when the actual relationship is exact reproduction or a material adaptation.

## Underlying concern

Protocol wording should communicate provenance and deviations. Ambiguous verbs can hide changes that matter for reproducibility and citation accuracy.

## External verification

### Official guidance

No universal verb mapping is imposed by IEEE/TMI; the wording should reflect the factual relationship.

### Recent-paper evidence

No further sampling is required for the provenance principle, though domain-specific reporting guidelines may impose additional requirements.

## Assessment

**Judgment:** Strongly supported

## Current rule

Choose the inheritance verb according to the actual relationship:

- **reproduced** — implemented essentially as reported, with no material procedural change;
- **followed** — adhered to the cited protocol, possibly with explicitly stated local details;
- **adapted** — intentionally modified one or more material elements;
- **based on** — inherited the general protocol/design but not necessarily the full procedure;
- **similar to** — only broad similarity is claimed.

When changes matter for interpretation or reproducibility, state them explicitly rather than relying on the verb alone.

## Examples

### Avoid

> The protocol was based on [X].

when excitation, timing, dose, or preprocessing were changed materially.

### Prefer

> The acquisition protocol was adapted from [X], with the excitation wavelength and exposure time modified as described below.

## Scope

Methods / Experimental Setup / acquisition protocols / preprocessing protocols

## Confidence

High

## Last verified

2026-09-18

## Decision history

| Date | Status | Change | Evidence / reason |
| --- | --- | --- | --- |
| 2026-09-18 | ADOPTED | Initial rule | Reproducibility and citation-provenance principle |
