# Instructions for this release-comparisons folder

This folder contains Cisco IOS XE YANG release comparisons. Read `NEXT-RELEASE-HANDOFF.md` before starting a new release audit. The repository’s existing `PROJECT_PLAN.md` is retained as historical project context; use the handoff for the current comparison method and verified limitations.

## User preferences

- Keep comparison documents focused on YANG modules, schema declarations, revisions, dependencies, deviations, and saved platform module-set profiles. Keep device-call workflows separate and do not link them from a YANG comparison.
- Explain YANG terms in plain language when first used. A `grouping` is a reusable definition and contributes schema nodes only where it is referenced with `uses`; grouping-change counts are not effective-schema-node counts.
- Organize changed modules by model flavor. Use a short index, collapsible flavor sections, collapsible per-module details, and module names should link only to verifiable public sources; otherwise keep them as plain text and link to report details.
- Label model flavors and platform profiles with their evidence and limits. Do not imply an exact hardware SKU from a family profile without evidence.
- Prefer clear before/after descriptions and searchable CSVs over dense source-signature strings.
- Include an at-a-glance summary by model flavor. Reconcile module, changed-source, tracked-schema, grouping, and RPC-entry counts; distinguish new modules from changed existing modules.

## Current comparison

- Baseline folders, when supplied locally: `../2611/` (26.1.1) and `../2621/` (26.2.1); these source folders are not committed to this repository.
- Overview: `2621-YANG-Model-Overview.md`.
- Supporting files: `2621-YANG-Model-Grouping-Deltas.csv`, `2621-YANG-Model-Deviation-Deltas.csv`, `2621-YANG-Model-Augment-Deltas.csv`, `2621-YANG-Platform-Applicability.csv`, `2621-YANG-Platform-Feature-Deltas.csv`, and `2621-YANG-Platform-Deviation-Targets.csv`.

The files in `scripts/` are legacy generators for earlier comparison formats. They are not a reproducible generator for the current 26.1.1 → 26.2.1 report. Use the handoff and source/profile evidence to design the next release audit; do not treat the old script output as a validated schema comparison.

Do not publish or bundle the source YANG files. The current report is a static source/profile audit, not a compiled schema comparison. Its limitations and input-provenance gaps are documented in the report and must remain visible unless resolved with evidence.
