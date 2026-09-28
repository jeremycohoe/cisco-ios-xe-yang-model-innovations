# IOS XE YANG release comparison: project plan

## Purpose

Produce a clear, evidence-based comparison of YANG model changes between two IOS XE releases. The report is for engineers reviewing model coverage and schema changes. Keep device-call examples and protocol-specific workflows separate from this project.

This plan is reusable for the next release pair. Do not assume its release number, source layout, platform profiles, or counts in advance.

## Current baseline and handoff

The completed baseline compares `2611/` (26.1.1) with `2621/` (26.2.1):

- Overview: [2621-YANG-Model-Overview.md](2621-YANG-Model-Overview.md)
- Grouping deltas: [2621-YANG-Model-Grouping-Deltas.csv](2621-YANG-Model-Grouping-Deltas.csv)
- Deviation deltas: [2621-YANG-Model-Deviation-Deltas.csv](2621-YANG-Model-Deviation-Deltas.csv)
- Platform applicability: [2621-YANG-Platform-Applicability.csv](2621-YANG-Platform-Applicability.csv)

These filenames and counts are examples for the completed comparison. Recompute all values for the next release pair.

## Scope

Compare the supplied YANG module sources and saved platform module-set inventories. Cover:

- Added, removed, unchanged, and modified modules and submodules.
- Model flavors: Oper, RPC, Native, Config, OpenConfig, IETF, and Other.
- Data nodes and schema-relevant properties such as type, default, units, status, constraints, keys, cardinality, and feature conditions.
- Reusable groupings, `uses` references, typedefs, identities, features, imports, augments, deviations, RPCs/actions, and notifications.
- Per-profile module presence, advertised revision, conformance type, and listed deviation associations where matching profile snapshots are supplied.

Do not infer runtime feature behavior from a YANG source file or a profile name. This project describes the supplied model evidence and labels unresolved questions.

## Inputs to collect

For each release, obtain the complete YANG source set and available platform module-set snapshots. Record:

- Exact release label and source folder.
- Source origin (repository, archive, or other source), retrieval date, and checksums where available.
- Platform-profile filenames and any release/profile identifiers present in the files.
- Missing profiles, incomplete folders, or differences in source formats.

Treat folder names and profile names as labels until checked against their contents. A family profile is not automatically an exact hardware SKU.

## Audit workflow

### 1. Inventory and classify

Build a release inventory of module and submodule names, revisions, namespaces, `belongs-to` relationships, and source file status. Classify each module once using explicit rules for the requested model flavors. Explain ambiguous classifications and keep source-based classification distinct from any externally supplied taxonomy.

### 2. Compare source declarations

Compare the YANG statement trees and report declaration-level changes. Separate direct data-node declarations from reusable definitions. Track changes to types, defaults, units, status, conditions and constraints, keys, cardinality, features, operation definitions, notifications, imports, augments, and deviations. Preserve before/after values for detailed CSV rows.

Do not label declaration counts as counts of a fully resolved schema tree. Description-only and metadata changes should be distinguished from changes that can alter schema shape or validation rules.

### 3. Explain grouping changes

A `grouping` is a reusable schema definition. A `uses` statement applies it at a particular location. The grouping itself is not a data node; a changed grouping can affect one or many use sites, and an unused grouping may not affect the effective schema.

Report separately:

- New, removed, and modified grouping definitions.
- Direct data-node declarations and tracked property changes inside them.
- Added and removed `uses` references.
- Likely consumers/use sites when they can be traced.
- Metadata/lifecycle changes versus type, constraint, default, key, or cardinality changes.

If the full use graph is not resolved, say so and do not convert grouping counts into effective-node totals. Investigate removed `uses` references before describing them as node removals.

### 4. Compare platform profiles

Parse each supplied `yang-set-<profile>.xml` inventory. For each source module/profile pair, record release presence, revision, conformance type, and deviation associations. Summarize newly listed modules, no-longer-listed modules, revision changes, and deviation-association changes by profile and flavor.

Make the comparison denominator explicit: if the table covers only source modules supplied in the two folders, say that it is not the complete module inventory of the profile. Treat a profile-to-product mapping as family-level unless exact model evidence is available.

### 5. Resolve effective schemas where possible

When a YANG compiler/resolver is available and the complete dependencies are supplied, compose submodules, resolve imports and `uses`, apply augments, features, and profile deviations, then compare the resulting schema trees per profile. Record tool/version and inputs. If resolution is unavailable or incomplete, retain the source-level audit and state exactly what remains unresolved; do not invent effective node totals.

### 6. Write the report for readers

Use this order:

1. Scope, releases, evidence basis, and a short executive summary.
2. Navigation and release inventory by model flavor.
3. Platform applicability summary with a searchable CSV.
4. Key changes and high-priority YANG semantics.
5. Added/removed modules.
6. Existing changed modules grouped by flavor, with a compact index, direct source links, collapsible flavor sections, and collapsible per-module details.
7. Grouping explanation before grouping statistics; distinguish definitions, use sites, and resolved schema nodes.
8. Deviation/import findings, method, limitations, and reproducibility links.

Prefer concise before/after statements and plain-language impact. Avoid dense inline path lists that wrap across a page. Keep CSVs row-oriented, with stable column names and a brief explanation in the report.

## Deliverables

Create release-named artifacts in `release-comparisons/`:

- A Markdown overview with flavor navigation, platform summary, findings, method, and limitations.
- A grouping-delta CSV with grouping, local path/context, change kind, and before/after values.
- A deviation-delta CSV with target, action, and before/after details.
- A platform-applicability CSV with one row per source module/profile and release values.
- An optional share bundle containing the overview, linked CSVs, source YANG folders, profile snapshots, this plan, and scoped agent instructions.

Keep relative links valid in both the directory layout and any generated ZIP. Include only the comparison materials needed to support the YANG report.

## Review and completion criteria

- Release labels, file counts, and per-flavor counts reconcile with the supplied inputs.
- The report explains what is a direct declaration, grouping definition, `uses` reference, profile listing, and resolved schema result.
- Grouping and deviation changes are not overclaimed as effective schema changes unless resolved.
- Hardware/profile labels are evidence-based and do not imply exact SKU support without evidence.
- Reader navigation, collapsible sections, source links, and CSV links work in the delivered layout.
- Limitations, provenance gaps, and classification assumptions are easy to find.
- The report contains only YANG comparison material; other workflows live separately.

## Known baseline limitations

The 26.1.1 → 26.2.1 comparison was generated by a static source parser and did not compile the complete dependency graph or produce resolved per-profile schema trees. Grouping and deviation CSVs expose declaration changes for follow-up. The supplied platform snapshots do not identify an exact PID/software build, and input source provenance was not recorded. Do not carry these baseline limitations forward as assumptions for a later comparison; re-check the next release inputs and document what can be verified.
