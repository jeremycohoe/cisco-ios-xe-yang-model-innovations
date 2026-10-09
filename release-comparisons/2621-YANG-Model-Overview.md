# IOS XE YANG Model Overview: 26.1.1 → 26.2.1

**Comparison scope:** `2611/` (26.1.1) against `2621/` (26.2.1)

**Updated:** 2026-10-09

**Model flavors:** Oper, RPC, Native, Config, OpenConfig, IETF, Other

> **Source files:** The YANG folders used for this comparison are input artifacts and are not published in this repository. Module filenames below are plain text; the report links to its own details and supporting CSVs.

## Quick navigation

- [Executive summary](#executive-summary)
- [At-a-glance change summary](#at-a-glance-change-summary)
- [Release inventory by model flavor](#release-inventory-by-model-flavor)
- [Platform applicability](#platform-applicability)
- [Newly listed modules by platform profile](#newly-listed-modules-by-platform-profile)
- [Advertised feature and deviation changes](#advertised-feature-and-deviation-changes)
- [Structural change signals](#structural-change-signals)
- [Expanded augment audit](#expanded-augment-audit)
- [What stands out](#what-stands-out)
- [Added models](#added-models)
- [Removed model](#removed-model)
- [Existing models with tracked schema changes](#existing-models-with-tracked-schema-changes)
  - [Oper](#tracked-oper)
  - [RPC](#tracked-rpc)
  - [Native](#tracked-native)
  - [Config](#tracked-config)
  - [Other](#tracked-other)
- [Expanded grouping-content audit](#expanded-grouping-content-audit)
- [Deviation and import changes](#deviation-and-import-changes)
- [Revision and source-identity callouts](#revision-and-source-identity-callouts)
- [Models without tracked schema signature changes](#existing-models-with-no-tracked-schema-signature-change)
- [Method and interpretation](#method-and-interpretation)


## Executive summary

The 26.2.1 source snapshot contains **842 YANG modules and 68 submodules**, compared with **819 modules and 68 submodules** in 26.1.1. Filename inventory shows **24 modules added**, **1 removed**, **336 existing source files changed**, and **550 unchanged**. Of the changed files, the source-level comparison detected tracked declaration changes in **189**; **147** had no detected change in the tracked categories. That does not prove there is no effective-schema impact: imports, revisions, and other untracked statements still need resolution and review.

The **189** count is a count of source files with a change in one or more tracked declarations, including top-level augment targets and their `uses` references. A change can be limited to a reusable grouping, typedef, or other definition; it does not mean 189 modules gained or lost effective schema nodes.

New coverage is concentrated in Cisco operational and configuration models, with a coordinated Next-Generation Firewall (NGFW) set, new wireless and Industrial IoT operational models, configuration-management RPCs, and OpenConfig telemetry. The monolithic Native model also has direct node changes. The detailed tables below distinguish source declarations from the resolved YANG schema they may contribute to.

> **Counting note:** “schema signature” and “declared node” counts below come from statements present in each `.yang` source file. They are not counts of nodes in a fully resolved schema tree. This source comparison does not expand imported `uses` groupings, apply the full augment/deviation set, or resolve platform-specific schemas. The separate [Platform applicability](#platform-applicability) section compares the saved module-set inventories.

### At-a-glance change summary

| Model flavor | New modules | Removed modules | Existing source files changed | With tracked schema signal | Without tracked schema signal |
|---|---:|---:|---:|---:|---:|
| Oper | 7 | 1 | 178 | 60 | 118 |
| RPC | 4 | 0 | 13 | 8 | 5 |
| Native | 0 | 0 | 6 | 6 | 0 |
| Config | 6 | 0 | 103 | 89 | 14 |
| OpenConfig | 4 | 0 | 1 | 0 | 1 |
| IETF | 0 | 0 | 0 | 0 | 0 |
| Other | 3 | 0 | 35 | 26 | 9 |
| **Total** | **24** | **1** | **336** | **189** | **147** |

Added and removed counts are standalone module files. Existing changed-file counts include modules and submodules. “Tracked schema signal” means the source parser detected a difference in a tracked YANG declaration; it is a review signal, not proof of semantic impact. For example, two grouping bodies differ only by statement order. The additional 24 Config entries are augment changes previously omitted from this signal. “Without tracked signal” means the file changed but no tracked declaration difference was detected. Neither count is a resolved per-device schema count.

**RPC count:** the four new RPC modules declare **12 top-level RPC operations**. The eight RPC entries in the tracked-change column are eight existing RPC modules with changed declarations; they are a separate count.

## Release inventory by model flavor

| Model flavor | Modules (26.1.1 → 26.2.1) | Submodules (26.1.1 → 26.2.1) | Added files* | Removed files* | Changed files (schema / other) | Unchanged files |
|---|---:|---:|---:|---:|---:|---:|
| **Oper** — Operational data and state models | 219 → 225 | 0 → 0 | 7 | 1 | 178 (60 / 118) | 40 |
| **RPC** — RPC and action models | 63 → 67 | 10 → 10 | 4 | 0 | 13 (8 / 5) | 60 |
| **Native** — Cisco IOS XE monolithic native configuration model | 1 → 1 | 11 → 11 | 0 | 0 | 6 (6 / 0) | 6 |
| **Config** — Cisco IOS XE configuration models outside the Native model | 199 → 205 | 8 → 8 | 6 | 0 | 103 (89 / 14) | 104 |
| **OpenConfig** — OpenConfig models, including Cisco OpenConfig extensions and deviations | 137 → 141 | 37 → 37 | 4 | 0 | 1 (0 / 1) | 173 |
| **IETF** — IETF and IANA standard models | 36 → 36 | 0 → 0 | 0 | 0 | 0 (0 / 0) | 36 |
| **Other** — Shared types, events, deviations, framework and remaining models | 164 → 167 | 2 → 2 | 3 | 0 | 35 (26 / 9) | 131 |
| **Total** | 819 → 842 | 68 → 68 | 24 | 1 | 336 (189 / 147) | 550 |

* Added/removed files are all standalone module files in this pair. Modified/unchanged counts include submodules, assigned to their parent module flavor.

Flavor is assigned once per source module for this inventory. Submodules inherit the flavor of their `belongs-to` module. Classification uses module name/namespace and declared YANG constructs: `Cisco-IOS-XE-native` is Native; OpenConfig and IETF/IANA namespaces are standards flavors; `*-oper` and RPC/action modules are Oper and RPC; Cisco configuration models are Config; remaining support/event/deviation models are Other. These are source-based labels for organizing the audit.

## Platform applicability

The release folders contain YANG Library module-set snapshots (`yang-set-<profile>.xml`) for ten platform profiles. The [platform applicability CSV](2621-YANG-Platform-Applicability.csv) compares source modules with each profile in both releases. It includes source file status, profile presence, advertised revision and conformance type, and deviations associated with each module. Advertised feature changes are in the separate [feature-delta CSV](2621-YANG-Platform-Feature-Deltas.csv). Filter `profile` to narrow the CSV, then `model_flavor` or `module` to find relevant model changes.

| Profile | Modules from these source folders listed (26.1.1 → 26.2.1) | Newly listed | No longer listed | Existing module revisions changed | Deviation associations changed |
|---|---:|---:|---:|---:|---:|
| [`cat9k`](#newly-listed-cat9k) | 606 → 620 | 15 (14 + 1) | 1 | 251 | 4 |
| [`cat9200`](#newly-listed-cat9200) | 321 → 326 | 5 (4 + 1) | 0 | 62 | 3 |
| [`wireless`](#newly-listed-wireless) | 530 → 540 | 11 (11 + 0) | 1 | 203 | 2 |
| [`asr1k`](#newly-listed-asr1k) | 501 → 525 | 24 (14 + 10) | 0 | 171 | 4 |
| [`c8500`](#newly-listed-c8500) | 501 → 525 | 24 (14 + 10) | 0 | 171 | 4 |
| [`isr1k`](#newly-listed-isr1k) | 539 → 558 | 19 (15 + 4) | 0 | 194 | 3 |
| [`c8000v`](#newly-listed-c8000v) | 505 → 526 | 21 (14 + 7) | 0 | 175 | 6 |
| [`ir1101`](#newly-listed-ir1101) | 564 → 577 | 14 (14 + 0) | 1 | 224 | 3 |
| [`ie3x00`](#newly-listed-ie3x00) | 447 → 459 | 12 (8 + 4) | 0 | 154 | 2 |
| [`ess3x00`](#newly-listed-ess3x00) | 447 → 459 | 12 (8 + 4) | 0 | 154 | 2 |

**Newly listed breakdown:** The total is followed by **new 26.2.1 source modules + modules already present in the 26.1.1 source folder**. Click a profile for exact names. Counts cover modules present in the supplied source folders; they are not total modules in each device's full YANG Library. “Newly listed” and “no longer listed” mean profile membership changed between the two saved snapshots. Revision and deviation counts are separate because a module may remain listed while its advertised revision or effective schema changes. See exact rows and revision/deviation values in the CSV.

**Choosing a profile:** use `cat9k` as a family-level starting point for a Catalyst 9300; use `wireless` for the wireless profile; and select the relevant router family (`asr1k`, `c8500`, `isr1k`, `c8000v`, or another listed profile) for routing platforms. “Routing” is not a single profile in these files. The profile names do not identify an exact PID, line card, software image, enabled feature, or license. Confirm a candidate on the target device by querying its YANG Library and then validate the operation itself.

**Evidence level:** these are saved per-profile release snapshots, not a live query to a device. The `module-set-id` identifies a snapshot but does not identify the exact PID or IOS XE image that produced it. The `cat9k` → Catalyst 9300 association is a family-level starting assumption, not a per-SKU guarantee. Profile presence means the module/revision appears in that saved set. The CSV records deviation associations but does not compile and resolve each complete schema set into its effective YANG schema tree.

### Newly listed modules by platform profile

The **Newly listed** total above compares saved 26.1.1 and 26.2.1 YANG Library profile snapshots. It combines modules newly present in the 26.2.1 source folder with modules already in the 26.1.1 source folder that this profile did not list before. For example, `c8500` has **24 newly listed: 14 from new YANG files and 10 from previously existing YANG files**. These are profile-listing changes, not proof of support on every device in the family.

For `c8500`, the snapshot labels **22 of the 24 as `implement` and 2 as `import`**. The import-only entries are `Cisco-IOS-XE-ngfw-common-oper` and `Cisco-IOS-XE-livetools-common-types`. An `import` listing makes a module's definitions available to other modules; it does not claim that module's data tree is implemented. Import-only names are marked in every profile list below.

Of the 24 modules new to the source folder, **22 appear in at least one supplied 26.2.1 profile**. `Cisco-IOS-XE-webauth-banner-internal` and `cisco-yang-mgmt-internal` appear in none of the ten saved profiles.

Open a profile below for exact names, grouped by model flavor. New-source names link to their [Added models](#added-models) descriptions; older modules link to existing report details where available. The focused [newly listed modules CSV](2621-YANG-Platform-Newly-Listed.csv) has one row per profile/module listing, including revision, conformance, and source-file status.

<a id="newly-listed-cat9k"></a>
<details>
<summary><code>cat9k</code> — 15 newly listed (14 new files, 1 existing file)</summary>

**New in the 26.2.1 source folder (14):**

- **Oper (4):** [`Cisco-IOS-XE-isis-operv2-oper.yang`](#module-cisco-ios-xe-isis-operv2-oper), [`Cisco-IOS-XE-live-protect-oper.yang`](#module-cisco-ios-xe-live-protect-oper), [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only), [`Cisco-IOS-XE-wireless-wat-oper.yang`](#module-cisco-ios-xe-wireless-wat-oper).
- **RPC (3):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc), [`Cisco-IOS-XE-wireless-raf-cfg-rpc.yang`](#module-cisco-ios-xe-wireless-raf-cfg-rpc).
- **Config (3):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg), [`Cisco-IOS-XE-live-protect-cfg.yang`](#module-cisco-ios-xe-live-protect-cfg), [`Cisco-IOS-XE-wireless-ld-cfg.yang`](#module-cisco-ios-xe-wireless-ld-cfg).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).

**Already in the 26.1.1 source folder, newly listed by this profile (1):**

- **Other (1):** `Cisco-IOS-XE-vlan-ewlc-deviation.yang`.

</details>

<a id="newly-listed-cat9200"></a>
<details>
<summary><code>cat9200</code> — 5 newly listed (4 new files, 1 existing file)</summary>

**New in the 26.2.1 source folder (4):**

- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).

**Already in the 26.1.1 source folder, newly listed by this profile (1):**

- **Other (1):** `Cisco-IOS-XE-vlan-ewlc-deviation.yang`.

</details>

<a id="newly-listed-wireless"></a>
<details>
<summary><code>wireless</code> — 11 newly listed (11 new files, 0 existing files)</summary>

**New in the 26.2.1 source folder (11):**

- **Oper (2):** [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only), [`Cisco-IOS-XE-wireless-wat-oper.yang`](#module-cisco-ios-xe-wireless-wat-oper).
- **RPC (3):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc), [`Cisco-IOS-XE-wireless-raf-cfg-rpc.yang`](#module-cisco-ios-xe-wireless-raf-cfg-rpc).
- **Config (2):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg), [`Cisco-IOS-XE-wireless-ld-cfg.yang`](#module-cisco-ios-xe-wireless-ld-cfg).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).

**Already in the 26.1.1 source folder, newly listed by this profile (0):**

None.

</details>

<a id="newly-listed-asr1k"></a>
<details>
<summary><code>asr1k</code> — 24 newly listed (14 new files, 10 existing files)</summary>

**New in the 26.2.1 source folder (14):**

- **Oper (3):** [`Cisco-IOS-XE-dp-tcam-usage-oper.yang`](#module-cisco-ios-xe-dp-tcam-usage-oper), [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only), [`Cisco-IOS-XE-ngfw-oper.yang`](#module-cisco-ios-xe-ngfw-oper).
- **RPC (2):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc).
- **Config (3):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg), [`Cisco-IOS-XE-ngfw.yang`](#module-cisco-ios-xe-ngfw), [`Cisco-IOS-XE-sla-policy.yang`](#module-cisco-ios-xe-sla-policy).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).
- **Other (2):** [`Cisco-IOS-XE-ethernet-port-settings-autoneg-deviation.yang`](#module-cisco-ios-xe-ethernet-port-settings-autoneg-deviation), [`Cisco-IOS-XE-sdwan-stats-events.yang`](#module-cisco-ios-xe-sdwan-stats-events).

**Already in the 26.1.1 source folder, newly listed by this profile (10):**

- **Oper (4):** [`Cisco-IOS-XE-livetools-oper.yang`](#module-cisco-ios-xe-livetools-oper), [`Cisco-IOS-XE-meraki-connect-oper.yang`](#module-cisco-ios-xe-meraki-connect-oper), `Cisco-IOS-XE-sse-oper.yang`, [`Cisco-IOS-XE-uplink-autoconfig-oper.yang`](#module-cisco-ios-xe-uplink-autoconfig-oper).
- **RPC (2):** `Cisco-IOS-XE-livetools-actions-rpc.yang`, [`Cisco-IOS-XE-sse-actions-rpc.yang`](#module-cisco-ios-xe-sse-actions-rpc).
- **Config (1):** `Cisco-IOS-XE-uplink-autoconfig.yang`.
- **Other (3):** `Cisco-IOS-XE-autovpn-events.yang`, `Cisco-IOS-XE-livetools-common-types.yang` (import only), `Cisco-IOS-XE-sse-events.yang`.

</details>

<a id="newly-listed-c8500"></a>
<details>
<summary><code>c8500</code> — 24 newly listed (14 new files, 10 existing files)</summary>

**New in the 26.2.1 source folder (14):**

- **Oper (3):** [`Cisco-IOS-XE-dp-tcam-usage-oper.yang`](#module-cisco-ios-xe-dp-tcam-usage-oper), [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only), [`Cisco-IOS-XE-ngfw-oper.yang`](#module-cisco-ios-xe-ngfw-oper).
- **RPC (2):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc).
- **Config (3):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg), [`Cisco-IOS-XE-ngfw.yang`](#module-cisco-ios-xe-ngfw), [`Cisco-IOS-XE-sla-policy.yang`](#module-cisco-ios-xe-sla-policy).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).
- **Other (2):** [`Cisco-IOS-XE-ethernet-port-settings-autoneg-deviation.yang`](#module-cisco-ios-xe-ethernet-port-settings-autoneg-deviation), [`Cisco-IOS-XE-sdwan-stats-events.yang`](#module-cisco-ios-xe-sdwan-stats-events).

**Already in the 26.1.1 source folder, newly listed by this profile (10):**

- **Oper (4):** [`Cisco-IOS-XE-livetools-oper.yang`](#module-cisco-ios-xe-livetools-oper), [`Cisco-IOS-XE-meraki-connect-oper.yang`](#module-cisco-ios-xe-meraki-connect-oper), `Cisco-IOS-XE-sse-oper.yang`, [`Cisco-IOS-XE-uplink-autoconfig-oper.yang`](#module-cisco-ios-xe-uplink-autoconfig-oper).
- **RPC (2):** `Cisco-IOS-XE-livetools-actions-rpc.yang`, [`Cisco-IOS-XE-sse-actions-rpc.yang`](#module-cisco-ios-xe-sse-actions-rpc).
- **Config (1):** `Cisco-IOS-XE-uplink-autoconfig.yang`.
- **Other (3):** `Cisco-IOS-XE-autovpn-events.yang`, `Cisco-IOS-XE-livetools-common-types.yang` (import only), `Cisco-IOS-XE-sse-events.yang`.

</details>

<a id="newly-listed-isr1k"></a>
<details>
<summary><code>isr1k</code> — 19 newly listed (15 new files, 4 existing files)</summary>

**New in the 26.2.1 source folder (15):**

- **Oper (3):** [`Cisco-IOS-XE-iiot-pwr-mgmt-oper.yang`](#module-cisco-ios-xe-iiot-pwr-mgmt-oper), [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only), [`Cisco-IOS-XE-ngfw-oper.yang`](#module-cisco-ios-xe-ngfw-oper).
- **RPC (3):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc), [`Cisco-IOS-XE-ngfw-ctrl-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-ctrl-actions-rpc).
- **Config (3):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg), [`Cisco-IOS-XE-ngfw.yang`](#module-cisco-ios-xe-ngfw), [`Cisco-IOS-XE-sla-policy.yang`](#module-cisco-ios-xe-sla-policy).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).
- **Other (2):** [`Cisco-IOS-XE-ethernet-port-settings-autoneg-deviation.yang`](#module-cisco-ios-xe-ethernet-port-settings-autoneg-deviation), [`Cisco-IOS-XE-sdwan-stats-events.yang`](#module-cisco-ios-xe-sdwan-stats-events).

**Already in the 26.1.1 source folder, newly listed by this profile (4):**

- **Oper (2):** `Cisco-IOS-XE-sse-oper.yang`, `Cisco-IOS-XE-vlan-oper.yang`.
- **RPC (1):** [`Cisco-IOS-XE-sse-actions-rpc.yang`](#module-cisco-ios-xe-sse-actions-rpc).
- **Other (1):** `Cisco-IOS-XE-sse-events.yang`.

</details>

<a id="newly-listed-c8000v"></a>
<details>
<summary><code>c8000v</code> — 21 newly listed (14 new files, 7 existing files)</summary>

**New in the 26.2.1 source folder (14):**

- **Oper (3):** [`Cisco-IOS-XE-isis-operv2-oper.yang`](#module-cisco-ios-xe-isis-operv2-oper), [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only), [`Cisco-IOS-XE-ngfw-oper.yang`](#module-cisco-ios-xe-ngfw-oper).
- **RPC (3):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc), [`Cisco-IOS-XE-ngfw-ctrl-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-ctrl-actions-rpc).
- **Config (3):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg), [`Cisco-IOS-XE-ngfw.yang`](#module-cisco-ios-xe-ngfw), [`Cisco-IOS-XE-sla-policy.yang`](#module-cisco-ios-xe-sla-policy).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).
- **Other (1):** [`Cisco-IOS-XE-sdwan-stats-events.yang`](#module-cisco-ios-xe-sdwan-stats-events).

**Already in the 26.1.1 source folder, newly listed by this profile (7):**

- **Oper (2):** `Cisco-IOS-XE-sse-oper.yang`, `Cisco-IOS-XE-vlan-oper.yang`.
- **RPC (1):** [`Cisco-IOS-XE-sse-actions-rpc.yang`](#module-cisco-ios-xe-sse-actions-rpc).
- **Config (1):** [`Cisco-IOS-XE-gnmi-cfg.yang`](#module-cisco-ios-xe-gnmi-cfg).
- **OpenConfig (2):** `cisco-xe-openconfig-system-grpc-deviation.yang`, `openconfig-system-grpc.yang`.
- **Other (1):** `Cisco-IOS-XE-sse-events.yang`.

</details>

<a id="newly-listed-ir1101"></a>
<details>
<summary><code>ir1101</code> — 14 newly listed (14 new files, 0 existing files)</summary>

**New in the 26.2.1 source folder (14):**

- **Oper (2):** [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only), [`Cisco-IOS-XE-wireless-wat-oper.yang`](#module-cisco-ios-xe-wireless-wat-oper).
- **RPC (3):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc), [`Cisco-IOS-XE-wireless-raf-cfg-rpc.yang`](#module-cisco-ios-xe-wireless-raf-cfg-rpc).
- **Config (4):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg), [`Cisco-IOS-XE-ngfw.yang`](#module-cisco-ios-xe-ngfw), [`Cisco-IOS-XE-sla-policy.yang`](#module-cisco-ios-xe-sla-policy), [`Cisco-IOS-XE-wireless-ld-cfg.yang`](#module-cisco-ios-xe-wireless-ld-cfg).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).
- **Other (1):** [`Cisco-IOS-XE-ethernet-port-settings-autoneg-deviation.yang`](#module-cisco-ios-xe-ethernet-port-settings-autoneg-deviation).

**Already in the 26.1.1 source folder, newly listed by this profile (0):**

None.

</details>

<a id="newly-listed-ie3x00"></a>
<details>
<summary><code>ie3x00</code> — 12 newly listed (8 new files, 4 existing files)</summary>

**New in the 26.2.1 source folder (8):**

- **Oper (1):** [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only).
- **RPC (2):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc).
- **Config (1):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).

**Already in the 26.1.1 source folder, newly listed by this profile (4):**

- **Oper (4):** `Cisco-IOS-XE-dhcp-security-track-server-oper.yang`, `Cisco-IOS-XE-lacp-oper.yang`, `Cisco-IOS-XE-matm-oper.yang`, `Cisco-IOS-XE-udld-oper.yang`.

</details>

<a id="newly-listed-ess3x00"></a>
<details>
<summary><code>ess3x00</code> — 12 newly listed (8 new files, 4 existing files)</summary>

**New in the 26.2.1 source folder (8):**

- **Oper (1):** [`Cisco-IOS-XE-ngfw-common-oper.yang`](#module-cisco-ios-xe-ngfw-common-oper) (import only).
- **RPC (2):** [`Cisco-IOS-XE-config-mgmt-rpc.yang`](#module-cisco-ios-xe-config-mgmt-rpc), [`Cisco-IOS-XE-ngfw-actions-rpc.yang`](#module-cisco-ios-xe-ngfw-actions-rpc).
- **Config (1):** [`Cisco-IOS-XE-audit-cfg.yang`](#module-cisco-ios-xe-audit-cfg).
- **OpenConfig (4):** [`cisco-xe-openconfig-telemetry-deviation.yang`](#module-cisco-xe-openconfig-telemetry-deviation), [`cisco-xe-openconfig-telemetry-ext.yang`](#module-cisco-xe-openconfig-telemetry-ext), [`openconfig-telemetry.yang`](#module-openconfig-telemetry), [`openconfig-telemetry-types.yang`](#module-openconfig-telemetry-types).

**Already in the 26.1.1 source folder, newly listed by this profile (4):**

- **Oper (4):** `Cisco-IOS-XE-dhcp-security-track-server-oper.yang`, `Cisco-IOS-XE-lacp-oper.yang`, `Cisco-IOS-XE-matm-oper.yang`, `Cisco-IOS-XE-udld-oper.yang`.

</details>

### Advertised feature and deviation changes

The saved YANG Library snapshots list supported `feature` names. Six profiles add one advertised feature in `Cisco-IOS-XE-features`; no existing module/profile pair removes a feature. The [feature-delta CSV](2621-YANG-Platform-Feature-Deltas.csv) records before/after revisions and feature counts. A reported feature can enable nodes guarded by `if-feature`, but it does not establish every downstream node or device behavior.

| Profile | Newly advertised feature | New deviation targets in associated modules | Of those, `not-supported` | Existing targets changed |
|---|---|---:|---:|---:|
| `cat9k` | `ip-forward` | 49 | 43 | 2 |
| `cat9200` | — | 47 | 43 | 2 |
| `wireless` | — | 47 | 43 | 0 |
| `asr1k` | `port-settings` | 58 | 49 | 0 |
| `c8500` | `port-settings` | 58 | 49 | 0 |
| `isr1k` | `port-settings` | 54 | 49 | 0 |
| `c8000v` | `port-settings` | 60 | 51 | 0 |
| `ir1101` | `port-settings` | 54 | 49 | 0 |
| `ie3x00` | — | 47 | 43 | 0 |
| `ess3x00` | — | 47 | 43 | 0 |

The deviation columns join the 63 new and 2 modified source-level targets to deviation modules referenced by each saved 26.2.1 profile. Filter the [profile deviation-target CSV](2621-YANG-Platform-Deviation-Targets.csv) by profile, action, or deviation file for the exact targets. These are **candidate schema effects**, not compiled effective-node counts: target availability, feature conditions, and the complete deviation graph still need resolution. The inventory table's count of changed *deviation associations* does not include new target statements inside an already associated deviation module.

For `cat9k`, `ip-forward` is newly advertised. The saved module set references `Cisco-IOS-XE-interfaces-deviation`, which adds 43 `not-supported` targets for interface `ip-forward` branches. It also references four newly declared OSPF `delete` deviations and two device-tracking `add` deviations. This is family-level evidence; confirm the exact device's YANG Library before treating it as C9300 schema support.

## Structural change signals

| Declaration type | Added | Removed | Existing definitions changed |
|---|---:|---:|---:|
| Direct data-node declarations | 54 | 0 | 40 |
| Grouping bodies changed in source | 65 | 0 | 276 |
| Typedefs | 36 | 0 | 21 |
| Deviation statements | 63 | 0 | 2 |
| Features | 2 | 0 | 0 |
| Top-level augment declarations and tracked body changes | 139 | 0 | 15 |
| `uses` references inside top-level augments | 175 | 0 | 0 |
| Added `refine` constraints | 2 | 0 | 0 |

The two added `feature` declarations are source-level definitions; the six rows in the [profile feature-delta CSV](2621-YANG-Platform-Feature-Deltas.csv) show where the saved module sets newly advertise them.

Among the 40 changed direct data-node declarations, the changed properties were status (30), type (5), default (3), when (1), must (1). These are statement-level occurrences; a changed grouping may affect multiple schema locations where it is used. Of the 15 existing augment targets with tracked body changes, 14 gain a `uses` reference and one changes its count of directly declared data nodes. The 63 added deviations are especially relevant to the effective schema because they can remove or alter nodes in a profile’s schema set. Choice/case statements are traversed to find data nodes but are not themselves data nodes in the resulting schema tree.

### Expanded augment audit

An `augment` attaches statements to a target elsewhere in the schema. A new augment containing `uses` can attach an existing grouping at a new location even when the grouping definition and its direct nodes do not change. This audit compares top-level augment declarations, their nested `uses` sites, and direct data-node counts at existing targets. The [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) has one row per added declaration or `uses` reference and one row for the changed direct-node count; it preserves any `when` condition on the declaration.

| Source-level measure | Count |
|---|---:|
| Existing Config files with added augment/`uses` statements | 47 |
| New augment declarations | 139 |
| Distinct new augment target paths | 135 |
| Added `uses` references inside augments | 175 |
| Existing augment targets gaining `uses` references | 14 |
| Existing augment targets with a direct data-node count change | 1 |
| Files moved from “no tracked signal” to tracked changes | 24 |
| Distinct new augment target paths in those 24 files | 59 |

Of the 135 distinct new target paths, 63 mention `TwoHundredGigE`, 63 mention `FourHundredGigE`, and 6 mention `FiftyGigabitEthernet`; 3 target other paths. The 139 declarations include four conditional `when` variants in IS-IS at two target paths. These are source statements, not resulting data-node counts or proof that every target is available on every platform. For example, VTP adds `TwoHundredGigE` and `FourHundredGigE` targets that each use `interface-vtp-grouping`.

One existing augment in `Cisco-IOS-XE-rawsocket.yang` changes from 2 to 6 directly declared data nodes under the Async interface target. Its module entry lists the four new paths and changes to the existing `media-type` and `duplex-mode` leaves. The direct-node count excludes `choice` and `case` statements.

The revised **189 tracked / 147 untracked** file split includes these augment declarations. An unchanged module revision, grouping body, or direct-node list can coexist with a new augmentation. Final per-profile effect requires resolving target schemas, grouping contents, feature expressions, and deviations.

### Expanded grouping-content audit

**How to read grouping changes:** a `grouping` is a named, reusable set of YANG schema statements—similar to a template. A `uses` statement inserts that template at a particular location in the schema. The grouping name itself does not create a data node. A new grouping has no effect on the schema tree unless a module uses it; an updated grouping may affect every use site, while an unused grouping may have no effect. Counts below describe grouping definitions and references, not the number of resulting nodes. This audit compares their source bodies but does not expand all local/imported `uses` references, so the final affected schema locations still need resolution.

The grouping-body comparison flagged **276 existing definitions** as different between the source releases. The detailed CSV contains schema-relevant rows for **274** of those definitions: 273 with node, property, or `uses` deltas, plus `config-ospf-passive-interface-grouping`, where two `must` refinements were added for `TwoHundredGigE/name` and `FourHundredGigE/name`. The other two changed bodies (`config-ntp-grouping` and `ip-wccp-group-address-grouping`) only move existing statements within the same grouping-relative paths; no schema path or value change was detected for those moves, so they are not listed as schema deltas.

A path-relative comparison of grouping contents found:

- **65 new grouping definitions** contain 295 directly declared data nodes and 311 `uses` references. These are template contents and references, not 295 guaranteed additions to a module’s schema tree.
- **274 existing grouping definitions with schema-relevant deltas** have 305 directly declared data nodes added, no direct data nodes removed, 960 existing data nodes with 964 tracked property changes, 44 `uses` references added, 10 `uses` references removed, and the two OSPF `must` refinements noted above. A data node can have multiple changed properties, which is why the property-change total is larger than the node count.


| Flavor | New grouping definitions | Existing groupings with schema-relevant delta rows | Existing bodies changed only by statement order |
|---|---:|---:|---:|
| Oper | 19 | 129 | 0 |
| RPC | 6 | 6 | 0 |
| Native | 2 | 9 | 0 |
| Config | 29 | 111 | 2 |
| Other | 9 | 19 | 0 |
| OpenConfig / IETF | 0 | 0 | 0 |
| **Total** | **65** | **274** | **2** |

- **Units and lifecycle metadata dominate:** 735 nodes gained a `units` statement (537 `octets`, 48 `seconds`, 39 `bytes`, 26 `milliseconds`); status was added as `deprecated` on 99 nodes and `obsolete` on 16, with 6 nodes moving from `deprecated` to `obsolete`. Units clarify value meaning; status marks lifecycle. Neither alone removes a node. There were also 45 type changes and 42 existing `must` constraint changes in the row-level property comparison, plus the two newly added OSPF refinements. These can change accepted values or validity rules and deserve closer compatibility review.

The removed `uses` references are a follow-up priority: BGP removes IPv4/IPv6/VPN unicast groupings from `address-family-no-vrf-obsolete-grouping`; crypto removes shared authentication groupings from several IKEv2 profile branches; IP removes route-replication and VRF-maximum groupings from its VRF branch. Those changes can remove inherited schema nodes after `uses` resolution even though no local data node was deleted from the grouping bodies. Confirm whether those parent groupings are still used and resolve the resulting schema before concluding that nodes were added or removed.

The row-level before/after data is in [2621-YANG-Model-Grouping-Deltas.csv](2621-YANG-Model-Grouping-Deltas.csv). `path_relative_to_grouping` is local to the named grouping, not a complete top-level schema path. `choice_case_context` preserves the YANG branch for similarly named alternatives. The CSV compares direct statements and `uses` references without recursively expanding imported or local groupings.

### Deviation and import changes

The 26.2.1 source adds **63 deviation targets**: 51 use `not-supported`, 6 use `replace`, 4 use `delete`, and 2 use `add`. `not-supported` removes the targeted node from an effective schema when that deviation applies; the other actions alter the target’s properties. Two existing targets in `Cisco-IOS-XE-switch-deviation.yang` also have updated `must` expressions for classifier condition and device-type limits. The expression context changed from absolute to relative paths, so those constraints deserve a semantic check before the report treats them as equivalent. See the complete target and before/after statement data in [2621-YANG-Model-Deviation-Deltas.csv](2621-YANG-Model-Deviation-Deltas.csv).

The comparison also finds **9 added imports**, with no removed or modified import statements:

- `Cisco-IOS-XE-ngfw-events.yang` imports `Cisco-IOS-XE-common-types`, `Cisco-IOS-XE-ngfw-common-oper`, `ietf-inet-types`, and `ietf-yang-types`.
- `Cisco-IOS-XE-spanning-tree.yang` imports `Cisco-IOS-XE-types`.
- `Cisco-IOS-XE-sse-actions-rpc.yang` imports `ietf-yang-types`.
- `Cisco-IOS-XE-utd-events.yang` imports `Cisco-IOS-XE-common-types`.
- `Cisco-IOS-XE-wireless-urwb-cfg.yang` and `Cisco-IOS-XE-wireless-urwb-common-types.yang` each import `ietf-inet-types`.

Import additions can change how a module resolves even when its own node list appears unchanged. The source audit records the dependency delta but does not resolve the imported schema graph.

### Revision and source-identity callouts

Five changed source files retain the same latest YANG revision across the two folders. Their differences deserve explicit review because a revision alone does not uniquely identify the supplied file contents:

| Source file | Unchanged latest revision | Difference to review |
|---|---|---|
| `Cisco-IOS-XE-ethernet-radium-deviation.yang` | `2024-07-01` | Adds a `max-bundle` range deviation. |
| `Cisco-IOS-XE-switch-deviation.yang` | `2026-02-01` | Changes existing `must` expressions; Cisco module version `1.8.0 → 1.9.0`. |
| `Cisco-IOS-XE-vlan-ewlc-deviation.yang` | `2024-11-01` | Changes its local prefix spelling. |
| `Cisco-IOS-XE-vtp.yang` | `2026-02-01` | Adds two interface augments while Cisco module version remains `2.0.0`. |
| `cisco-xe-openconfig-access-points-deviation.yang` | `2020-03-01` | Cisco module version moves `1.1.0 → 1.0.0`; verify source packaging. |

The source archive URL, retrieval date, and file checksums were not captured for this comparison. Record them before making a release-support claim; a checksum manifest can be shared without publishing the YANG sources.

#### Recommended next source-audit steps

1. Resolve the module sets, submodules, imported groupings, augments, features, and deviations for each profile before concluding which nodes appear in its effective schema tree.
2. Trace the removed BGP, crypto, and IP `uses` references to their consumers. The containing groupings may themselves be obsolete; check the schema after expansion before reporting a node removal.
3. Review the 45 grouping-level type changes and the 42 `must` constraint changes for schema-consumer compatibility. Prioritize changes to unions, ranges, enums, list keys, and mandatory/conditional rules over added units and description edits.
4. Separate lifecycle changes (`deprecated`/`obsolete`) from node removals. Status changes are useful migration signals but do not automatically remove a node from the schema.

## What stands out

- **NGFW coverage arrives as a family:** configuration (`Cisco-IOS-XE-ngfw` and `-live-protect-cfg`), operational state (`-ngfw-oper`, `-ngfw-common-oper`, `-live-protect-oper`), and two action/RPC modules (`-ngfw-actions-rpc`, `-ngfw-ctrl-actions-rpc`).
- **OpenConfig telemetry is added:** `openconfig-telemetry` and `openconfig-telemetry-types` arrive with Cisco extension and deviation modules. The deviation module matters when assessing the effective IOS XE schema; it can change which standard nodes are exposed.
- **Operational coverage broadens** with datapath TCAM usage, IIoT power management, IS-IS operational v2, Live Protect, NGFW, and wireless WAT models.
- **Configuration and management coverage expands** with audit monitor configuration, SLA policy, wireless Live-Detect configuration, and device configuration-management RPCs.
- **Interface augmentation broadens:** 47 existing Config files add or change augment `uses` sites, especially at 200G and 400G interface paths. The [augment audit](#expanded-augment-audit) distinguishes declarations from effective schema results.
- **Auto-negotiation modeling changes:** the new Ethernet port-settings deviation says the fixed YANG default is removed for platforms where the default is platform- or media-dependent. Treat this as a meaningful default/behavior change when evaluating effective schemas.
- **The sole removed file** is `Cisco-IOS-XE-wireless-rrm-emul-oper.yang`; removal from this source snapshot does not by itself prove removal from every IOS XE platform image.

## Added models

The 24 numbers below are **new source modules**, not 24 new data trees. Ten declare data trees, four declare RPCs, three augment existing Native paths, two declare deviations, three provide reusable types or identities, one declares a notification, and one contains only module metadata. Each entry selects the most useful paths, operations, or fields; it is not an exhaustive schema listing. For advertised module membership by saved platform profile, use the [platform applicability CSV](2621-YANG-Platform-Applicability.csv); a profile listing alone is not a device-support guarantee.

[Oper (1–7)](#added-oper) · [RPC (8–11)](#added-rpc) · [Config (12–17)](#added-config) · [OpenConfig (18–21)](#added-openconfig) · [Other (22–24)](#added-other)

<details>
<summary>Jump to a specific new module</summary>

- **Oper:** [1 TCAM usage](#module-cisco-ios-xe-dp-tcam-usage-oper) · [2 IIoT power](#module-cisco-ios-xe-iiot-pwr-mgmt-oper) · [3 IS-IS v2](#module-cisco-ios-xe-isis-operv2-oper) · [4 Live Protect state](#module-cisco-ios-xe-live-protect-oper) · [5 NGFW shared types](#module-cisco-ios-xe-ngfw-common-oper) · [6 NGFW state](#module-cisco-ios-xe-ngfw-oper) · [7 wireless WAT](#module-cisco-ios-xe-wireless-wat-oper)
- **RPC:** [8 configuration management](#module-cisco-ios-xe-config-mgmt-rpc) · [9 NGFW actions](#module-cisco-ios-xe-ngfw-actions-rpc) · [10 NGFW controller update](#module-cisco-ios-xe-ngfw-ctrl-actions-rpc) · [11 wireless RAF](#module-cisco-ios-xe-wireless-raf-cfg-rpc)
- **Config:** [12 audit monitor](#module-cisco-ios-xe-audit-cfg) · [13 Live Protect configuration](#module-cisco-ios-xe-live-protect-cfg) · [14 NGFW configuration](#module-cisco-ios-xe-ngfw) · [15 SLA policy](#module-cisco-ios-xe-sla-policy) · [16 web authentication banner](#module-cisco-ios-xe-webauth-banner-internal) · [17 wireless Live-Detect](#module-cisco-ios-xe-wireless-ld-cfg)
- **OpenConfig:** [18 telemetry deviations](#module-cisco-xe-openconfig-telemetry-deviation) · [19 Cisco telemetry identities](#module-cisco-xe-openconfig-telemetry-ext) · [20 telemetry base identities](#module-openconfig-telemetry-types) · [21 telemetry data tree](#module-openconfig-telemetry)
- **Other:** [22 auto-negotiation default deviation](#module-cisco-ios-xe-ethernet-port-settings-autoneg-deviation) · [23 SD-WAN drop event](#module-cisco-ios-xe-sdwan-stats-events) · [24 internal metadata](#module-cisco-yang-mgmt-internal)

</details>

<a id="added-oper"></a>

### Oper — operational data and shared definitions

1. <a id="module-cisco-ios-xe-dp-tcam-usage-oper"></a> **`Cisco-IOS-XE-dp-tcam-usage-oper.yang` — datapath TCAM use.** Adds `/dp-tcam-usage-oper-data/location`, keyed by hardware location. Each location has a `tcam-usage` list keyed by `feature-id`, with client name, 160/320-bit VMR entry counts, total TCAM cells, and use percentage.

2. <a id="module-cisco-ios-xe-iiot-pwr-mgmt-oper"></a> **`Cisco-IOS-XE-iiot-pwr-mgmt-oper.yang` — IIoT power state and history.** Adds `/iiot-pwr-mgmt-oper-data` with `pwr-mgmt-history` (hourly averages and a last-31-day list) and `pwr-mgmt-reg` (input voltage, hardware/software power state, power mode, sensing thresholds, and sleep or shutdown timing). The source describes this as Industrial IoT power management; the saved profile evidence is separate.

3. <a id="module-cisco-ios-xe-isis-operv2-oper"></a> **`Cisco-IOS-XE-isis-operv2-oper.yang` — IS-IS instance state.** Adds `/isis-operv2-oper-data/isis-inst-rec`, keyed by instance `tag`. Each instance organizes levels and LSP database records, interface state, and neighbors; neighbor records include system ID, level, interface, addresses, and adjacency state.

4. <a id="module-cisco-ios-xe-live-protect-oper"></a> **`Cisco-IOS-XE-live-protect-oper.yang` — Live Protect shield state.** Adds `/live-protect-oper-data` with shield entries keyed by `id` and hardware-location entries containing member shields. Shield records expose mode and total, enforcement, and monitoring hit counters.

5. <a id="module-cisco-ios-xe-ngfw-common-oper"></a> **`Cisco-IOS-XE-ngfw-common-oper.yang` — NGFW update types.** Defines two reusable enumerations: update type (LSP or VDB, plus unknown) and update result (success, failure, no update, or unknown). It declares **no top-level operational data path**; the NGFW action module imports these types.

6. <a id="module-cisco-ios-xe-ngfw-oper"></a> **`Cisco-IOS-XE-ngfw-oper.yang` — NGFW status.** Adds `/ngfw-oper-data` with five branches: version/support information, LSP update status, VDB update status, engine status, and custom-signature status. Engine data includes version, profile, memory condition, and per-instance state; signature data is organized globally and by profile.

7. <a id="module-cisco-ios-xe-wireless-wat-oper"></a> **`Cisco-IOS-XE-wireless-wat-oper.yang` — Wireless Active Testing state.** Adds `/wat-oper-data` with AP entries keyed by `wtp-mac`, a wired-test request container, and wired-client entries keyed by `wtp-mac`. The AP records carry test/profile status and test-engine state; request and client records carry MAC addresses, timing, WLAN/VLAN context, and installation state.

<a id="added-rpc"></a>

### RPC — operations and their declared inputs

8. <a id="module-cisco-ios-xe-config-mgmt-rpc"></a> **`Cisco-IOS-XE-config-mgmt-rpc.yang` — configuration erase.** Declares one operation, `erase-config`. The RPC has **no explicit `input` or `output` statements** in this module. This is an operation declaration, not a new data tree or a claim about device execution.

9. <a id="module-cisco-ios-xe-ngfw-actions-rpc"></a> **`Cisco-IOS-XE-ngfw-actions-rpc.yang` — six NGFW file and signature operations.** `ngfw-upd-file` takes update type and filename. Profile-scoped signature apply/load take profile name and filename; validation and global apply/load take a filename. The module defines three reusable input groupings and no explicit RPC output statements.

10. <a id="module-cisco-ios-xe-ngfw-ctrl-actions-rpc"></a> **`Cisco-IOS-XE-ngfw-ctrl-actions-rpc.yang` — controller-initiated NGFW update.** Declares `ngfw-upd` with `json` and `dwnld-timeout` input leaves and a `resp-msg` output leaf. Its two groupings define the request and response shapes.

11. <a id="module-cisco-ios-xe-wireless-raf-cfg-rpc"></a> **`Cisco-IOS-XE-wireless-raf-cfg-rpc.yang` — Regulatory Activation File operations.** Declares four RPCs: `set-raf-name` takes a filename; `apply-raf-config` has no explicit input; `clear-country-map-all-ap` has no explicit input; and `clear-country-ap-map` takes an AP MAC address. No explicit output statements are declared.

<a id="added-config"></a>

### Config — configuration data and Native augments

12. <a id="module-cisco-ios-xe-audit-cfg"></a> **`Cisco-IOS-XE-audit-cfg.yang` — Audit Monitor switches.** Adds the presence container `/audit-cfg-data/audit-cfg` and an `audit-rls-list` beneath it. Six boolean leaves, all defaulting to false, control monitoring for DNS client files, kernel modules, system software, user/group files, user privileges, and Guest Shell.

13. <a id="module-cisco-ios-xe-live-protect-cfg"></a> **`Cisco-IOS-XE-live-protect-cfg.yang` — shield configuration.** Adds `/live-protect-cfg-data/lp-shield-configs/lp-shield-cfg`, a list keyed by `shield-id`. Its `is-enf` boolean defaults to false: the model distinguishes monitoring from enforcement for each configured shield.

14. <a id="module-cisco-ios-xe-ngfw"></a> **`Cisco-IOS-XE-ngfw.yang` — Native NGFW configuration.** Uses three augments rather than a standalone root: one under `/ios:native`, and two under the Native `inspect` and `inspect-global` parameter-map branches. The Native branch provides NGFW global logging/update settings, encrypted-visibility exemptions, threat-inspection profiles, and policies; the parameter-map branches attach a policy by `policy-name` leafref.

15. <a id="module-cisco-ios-xe-sla-policy"></a> **`Cisco-IOS-XE-sla-policy.yang` — SLA global preference.** Augments `/ios:native/ios:sla-policy` with a `global-preference` presence container. It defines `failover` (graceful or immediate; default graceful) and `load-balance` (enable or disable; default enable). It does not create a separate top-level tree.

16. <a id="module-cisco-ios-xe-webauth-banner-internal"></a> **`Cisco-IOS-XE-webauth-banner-internal.yang` — internal web-authentication banners.** Two augments attach the same grouping to global and per-parameter-map web authentication banner locations. Each location gains `webauth-internal-banner-text` and `webauth-internal-banner-title` leaves. This source file is not listed in the supplied 26.2.1 profile snapshots.

17. <a id="module-cisco-ios-xe-wireless-ld-cfg"></a> **`Cisco-IOS-XE-wireless-ld-cfg.yang` — global Live-Detect settings.** Adds `/ld-cfg-data/ld-config` as a presence container. It contains `sensor-ip` for communication with the Ultra-Sensor and `dnld-url` for the DDN agent container download endpoint, with defaults and URL validation declared in the source.

<a id="added-openconfig"></a>

### OpenConfig — telemetry tree, identities, and deviations

18. <a id="module-cisco-xe-openconfig-telemetry-deviation"></a> **`cisco-xe-openconfig-telemetry-deviation.yang` — telemetry restrictions.** Declares 13 `not-supported` deviations under OpenConfig `telemetry-system` subscriptions. They target selected dynamic/persistent subscription fields, including heartbeat and redundant-update controls, QoS marking, source address, protocol/encoding, and an exclude filter. This module adds **no data nodes**; its effect depends on deviation association.

19. <a id="module-cisco-xe-openconfig-telemetry-ext"></a> **`cisco-xe-openconfig-telemetry-ext.yang` — Cisco telemetry identity values.** Adds four identities: gNMI and gRPC-TLS stream protocols, an unspecified stream value, and KVGPB encoding. Despite the “ext” name, this file contains **no `augment` statement or top-level data tree**.

20. <a id="module-openconfig-telemetry-types"></a> **`openconfig-telemetry-types.yang` — base telemetry identities.** Defines ten identities: bases for data encoding and stream protocol, with encoding values such as XML, JSON-IETF, and Proto3, and stream values such as SSH, gRPC, JSON-RPC, Thrift, and WebSocket. It is a type/identity module with **no data tree**.

21. <a id="module-openconfig-telemetry"></a> **`openconfig-telemetry.yang` — telemetry system data tree.** A top-level `uses telemetry-top` creates `/telemetry-system`. Its main branches are sensor groups and paths, destination groups and destinations, and persistent or dynamic subscriptions. The 18 groupings define reusable settings such as sample interval, heartbeat, redundant-update suppression, destination address/port, and stream protocol/encoding; the deviation module above may remove selected fields.

<a id="added-other"></a>

### Other — deviations, notification, and internal metadata

22. <a id="module-cisco-ios-xe-ethernet-port-settings-autoneg-deviation"></a> **`Cisco-IOS-XE-ethernet-port-settings-autoneg-deviation.yang` — auto-negotiation default.** Declares 20 deviations across interface types, each deleting the YANG `default "enable"` statement from `port-settings/auto-negotiation`. This **does not remove the leaf**; it avoids imposing that fixed model default where the deviation applies.

23. <a id="module-cisco-ios-xe-sdwan-stats-events"></a> **`Cisco-IOS-XE-sdwan-stats-events.yang` — dropped-statistics notification.** Declares `stats-dropped`, not a persistent data root. Its payload includes severity, host/system IP, and a list of dropped-statistics records with table ID/name, time interval, drop reason, and count.

24. <a id="module-cisco-yang-mgmt-internal"></a> **`cisco-yang-mgmt-internal.yang` — internal module metadata.** Contains a module declaration, description, and revision but **no data nodes, groupings, RPCs, notifications, augments, or deviations**. Its presence increases the file/module inventory; the source alone adds no callable operation or data path. It is not listed in the supplied profile snapshots.


## Removed model

<a id="module-cisco-ios-xe-wireless-rrm-emul-oper"></a>
<details>
<summary><code>Cisco-IOS-XE-wireless-rrm-emul-oper.yang</code> — removed from the 26.2.1 source folder</summary>

**Last module revision in 26.1.1:** `2023-03-01`.

**Profile snapshot change:** listed with `implement` conformance in the 26.1.1 `cat9k`, `ir1101`, and `wireless` profiles; not listed in those 26.2.1 snapshots. It was not listed in the other seven supplied profiles in either release.

This is a source-folder and saved-profile change. It does not by itself establish runtime behavior on every device in those families. See the [platform applicability CSV](2621-YANG-Platform-Applicability.csv) for the complete profile rows.

</details>

## Existing models with tracked schema changes

Counts below are source entries, grouped by model flavor. Open a flavor to see its changed modules; expand each module row to see its detailed revision note, changed paths, and schema signals. Source YANG files are not published with this report.

| Flavor | Existing source files with tracked changes | Browse |
|---|---:|---|
| Oper | 60 | [Open Oper changes](#tracked-oper) |
| RPC | 8 | [Open RPC changes](#tracked-rpc) |
| Native | 6 (1 module, 5 submodules) | [Open Native changes](#tracked-native) |
| Config | 89 | [Open Config changes](#tracked-config) |
| Other | 26 | [Open Other changes](#tracked-other) |

Each flavor and each module can be expanded independently. The counts here cover existing module and submodule files whose tracked declarations changed; newly added modules are listed separately above.

<a id="tracked-oper"></a>

### Oper (60 source entries)

<details>
<summary>Show 60 Oper entries</summary>

**Module index:**

- [Cisco-IOS-XE-app-hosting-oper.yang](#module-cisco-ios-xe-app-hosting-oper) · [Cisco-IOS-XE-bgp-oper.yang](#module-cisco-ios-xe-bgp-oper) · [Cisco-IOS-XE-bgp-rib-oper.yang](#module-cisco-ios-xe-bgp-rib-oper)
- [Cisco-IOS-XE-bgp-route-oper.yang](#module-cisco-ios-xe-bgp-route-oper) · [Cisco-IOS-XE-bridge-oper.yang](#module-cisco-ios-xe-bridge-oper) · [Cisco-IOS-XE-cdp-oper.yang](#module-cisco-ios-xe-cdp-oper)
- [Cisco-IOS-XE-cellwan-oper.yang](#module-cisco-ios-xe-cellwan-oper) · [Cisco-IOS-XE-crypto-oper.yang](#module-cisco-ios-xe-crypto-oper) · [Cisco-IOS-XE-device-hardware-oper.yang](#module-cisco-ios-xe-device-hardware-oper)
- [Cisco-IOS-XE-dhcp-oper.yang](#module-cisco-ios-xe-dhcp-oper) · [Cisco-IOS-XE-eigrp-oper.yang](#module-cisco-ios-xe-eigrp-oper) · [Cisco-IOS-XE-environment-oper.yang](#module-cisco-ios-xe-environment-oper)
- [Cisco-IOS-XE-evpn-oper.yang](#module-cisco-ios-xe-evpn-oper) · [Cisco-IOS-XE-fib-oper.yang](#module-cisco-ios-xe-fib-oper) · [Cisco-IOS-XE-flow-monitor-oper.yang](#module-cisco-ios-xe-flow-monitor-oper)
- [Cisco-IOS-XE-fw-oper.yang](#module-cisco-ios-xe-fw-oper) · [Cisco-IOS-XE-fwd-oper.yang](#module-cisco-ios-xe-fwd-oper) · [Cisco-IOS-XE-gnss-oper.yang](#module-cisco-ios-xe-gnss-oper)
- [Cisco-IOS-XE-install-oper.yang](#module-cisco-ios-xe-install-oper) · [Cisco-IOS-XE-interfaces-oper.yang](#module-cisco-ios-xe-interfaces-oper) · [Cisco-IOS-XE-ios-events-oper.yang](#module-cisco-ios-xe-ios-events-oper)
- [Cisco-IOS-XE-ip-sla-oper.yang](#module-cisco-ios-xe-ip-sla-oper) · [Cisco-IOS-XE-isis-intf-oper.yang](#module-cisco-ios-xe-isis-intf-oper) · [Cisco-IOS-XE-livetools-oper.yang](#module-cisco-ios-xe-livetools-oper)
- [Cisco-IOS-XE-meraki-connect-oper.yang](#module-cisco-ios-xe-meraki-connect-oper) · [Cisco-IOS-XE-mpls-ldp-oper.yang](#module-cisco-ios-xe-mpls-ldp-oper) · [Cisco-IOS-XE-mpls-te-oper.yang](#module-cisco-ios-xe-mpls-te-oper)
- [Cisco-IOS-XE-mroute-oper.yang](#module-cisco-ios-xe-mroute-oper) · [Cisco-IOS-XE-mrp-oper.yang](#module-cisco-ios-xe-mrp-oper) · [Cisco-IOS-XE-ntp-oper.yang](#module-cisco-ios-xe-ntp-oper)
- [Cisco-IOS-XE-nwpi-oper.yang](#module-cisco-ios-xe-nwpi-oper) · [Cisco-IOS-XE-ospf-oper.yang](#module-cisco-ios-xe-ospf-oper) · [Cisco-IOS-XE-perf-measure-oper.yang](#module-cisco-ios-xe-perf-measure-oper)
- [Cisco-IOS-XE-platform-software-oper.yang](#module-cisco-ios-xe-platform-software-oper) · [Cisco-IOS-XE-poe-health-oper.yang](#module-cisco-ios-xe-poe-health-oper) · [Cisco-IOS-XE-poe-oper.yang](#module-cisco-ios-xe-poe-oper)
- [Cisco-IOS-XE-process-memory-oper.yang](#module-cisco-ios-xe-process-memory-oper) · [Cisco-IOS-XE-qfp-appqoe-dp-oper.yang](#module-cisco-ios-xe-qfp-appqoe-dp-oper) · [Cisco-IOS-XE-qfp-dp-cmn-stats-oper.yang](#module-cisco-ios-xe-qfp-dp-cmn-stats-oper)
- [Cisco-IOS-XE-qfp-stats-oper.yang](#module-cisco-ios-xe-qfp-stats-oper) · [Cisco-IOS-XE-rawsocket-oper.yang](#module-cisco-ios-xe-rawsocket-oper) · [Cisco-IOS-XE-sd-vxlan-oper.yang](#module-cisco-ios-xe-sd-vxlan-oper)
- [Cisco-IOS-XE-stack-info-oper.yang](#module-cisco-ios-xe-stack-info-oper) · [Cisco-IOS-XE-stack-oper.yang](#module-cisco-ios-xe-stack-oper) · [Cisco-IOS-XE-switch-ptp-oper.yang](#module-cisco-ios-xe-switch-ptp-oper)
- [Cisco-IOS-XE-system-security-oper.yang](#module-cisco-ios-xe-system-security-oper) · [Cisco-IOS-XE-tunnel-oper.yang](#module-cisco-ios-xe-tunnel-oper) · [Cisco-IOS-XE-uplink-autoconfig-oper.yang](#module-cisco-ios-xe-uplink-autoconfig-oper)
- [Cisco-IOS-XE-utd-oper.yang](#module-cisco-ios-xe-utd-oper) · [Cisco-IOS-XE-wireless-access-point-oper.yang](#module-cisco-ios-xe-wireless-access-point-oper) · [Cisco-IOS-XE-wireless-ble-ltx-oper.yang](#module-cisco-ios-xe-wireless-ble-ltx-oper)
- [Cisco-IOS-XE-wireless-cisco-spaces-oper.yang](#module-cisco-ios-xe-wireless-cisco-spaces-oper) · [Cisco-IOS-XE-wireless-client-global-oper.yang](#module-cisco-ios-xe-wireless-client-global-oper) · [Cisco-IOS-XE-wireless-mesh-global-oper.yang](#module-cisco-ios-xe-wireless-mesh-global-oper)
- [Cisco-IOS-XE-wireless-mesh-oper.yang](#module-cisco-ios-xe-wireless-mesh-oper) · [Cisco-IOS-XE-wireless-rogue-oper.yang](#module-cisco-ios-xe-wireless-rogue-oper) · [Cisco-IOS-XE-wireless-rrm-oper.yang](#module-cisco-ios-xe-wireless-rrm-oper)
- [Cisco-IOS-XE-wireless-urwb-oper.yang](#module-cisco-ios-xe-wireless-urwb-oper) · [Cisco-IOS-XE-wireless-urwbnet-oper.yang](#module-cisco-ios-xe-wireless-urwbnet-oper) · [Cisco-IOS-XE-yang-interfaces-oper.yang](#module-cisco-ios-xe-yang-interfaces-oper)


<a id="module-cisco-ios-xe-ip-sla-oper"></a>
<details>
<summary>Cisco-IOS-XE-ip-sla-oper.yang — adds/updates 19 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated string-typed frame loss ratio leaves (average-frame-loss-ratio, cum-frame-loss-ratio) and added new decimal64-typed leaves with units percent for proper numeric representation. - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 19 reusable grouping(s).

**Updated groupings:** `http-rtt-stats`, `icmp-packet-loss`, `jitter`, `latest-rtt-type`, `sla-dist-stats`, `sla-err-stats-key`, `sla-frame-loss-ratio`, `sla-mcast-dist-stats`, `sla-mcast-stats`, `sla-packet-loss-info` (+9 more).

</details>

<a id="module-cisco-ios-xe-wireless-urwbnet-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-urwbnet-oper.yang — adds 1 declared schema path(s); adds/updates 10 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added band, slot-id, and radio-profile-name leaves to node interface data. - Added Ethernet MAC address leaf to node data. - Updated descriptions of several model elements to clarify their meaning and purpose. - Added uplink and downlink byte-rate leaves and uplink/downlink MCS-rate leaves to wireless link statistics. - Added URWB network name table oper-data mapping. - Added nw-info container mappings for URWB links/routes/nodes. - Added subnet network-name and network-id operational leaves. - Added connected-device last-update timestamp leaf to URWB network operational data.

**Change at a glance:** adds 1 declared schema path(s); adds/updates 10 reusable grouping(s); adds/updates 1 reusable type(s).

**Newly declared schema paths:**
- `/urwbnet-oper-data/urwbnet-name-entry` (list, key=nw-name)

**New groupings:** `st-urwbnet-nw-name`.

**Updated groupings:** `st-urwbnet-conn-dev`, `st-urwbnet-coord-rt`, `st-urwbnet-fix-lnk`, `st-urwbnet-mob-link`, `st-urwbnet-node`, `st-urwbnet-node-intf`, `st-urwbnet-subnet`, `st-urwbnet-wfm`, `st-urwbnet-wlink-stats`.

**New typedefs:** `urwb-net-band-id`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-gnss-oper"></a>
<details>
<summary>Cisco-IOS-XE-gnss-oper.yang — adds/updates 4 reusable grouping(s); adds/updates 6 reusable type(s)</summary>

**26.2.1 revision note:** Added optional GNSS device information grouping with version details and constellation type - Added Dilution of Precision metrics, major and minor alarm status leaves - Added satellite health, quality leaves - Updated descriptions for several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 4 reusable grouping(s); adds/updates 6 reusable type(s).

**New groupings:** `gnss-device`.

**Updated groupings:** `gnss-data`, `gnss-location`, `gnss-satellite-info`.

**New typedefs:** `gnss-constellation-type`, `gnss-fix-type`, `gnss-sv-health`, `maj-alrm`, `min-alrm`.

**Updated typedefs:** `gnss-module-sv-tracking-status`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-device-hardware-oper"></a>
<details>
<summary>Cisco-IOS-XE-device-hardware-oper.yang — adds 1 declared schema path(s); adds/updates 3 reusable grouping(s); adds/updates 5 reusable type(s)</summary>

**26.2.1 revision note:** Added XFSU operational data and state change history into the device hardware operational model - Updated description of hardware related elements to clarify their meaning and purpose

**Change at a glance:** adds 1 declared schema path(s); adds/updates 3 reusable grouping(s); adds/updates 5 reusable type(s).

**Newly declared schema paths:**
- `/device-hardware-data/xfsu-oper` (container, presence=xfsu-oper)

**New groupings:** `xfsu-history-entry`, `xfsu-info`, `xlt`.

**New typedefs:** `xcs`, `xfsu-client-name`, `xfsu-infra-status`, `xfsu-platform-status`, `xfsu-proto-inelig`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-fwd-oper"></a>
<details>
<summary>Cisco-IOS-XE-fwd-oper.yang — adds 1 declared schema path(s); adds/updates 6 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added support for AFT Ethernet table. - Updated descriptions of several model elements to clarify their meaning and purpose.

**Change at a glance:** adds 1 declared schema path(s); adds/updates 6 reusable grouping(s); adds/updates 1 reusable type(s).

**Newly declared schema paths:**
- `/fwd-oper-data/aft-eth-ni` (list, key=ni-name)

**New groupings:** `aft-eth-entry`, `aft-eth-ni-entry`, `nh-port-list`.

**Updated groupings:** `fib-ipv4-entry`, `fib-ipv6-entry`, `nh-entry`.

**New typedefs:** `e-nh-port-type`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-wireless-access-point-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-access-point-oper.yang — adds/updates 4 reusable grouping(s); adds/updates 3 reusable type(s)</summary>

**26.2.1 revision note:** Added support for proximity method - Added support for the Local-MAC capability flag on AP stacks - Added support for auto-MACsec - Added support for SIA serial number - Added AP capability flag ap-idr-capable - Added WAT Wired Testing capability flag - Added AP auto-MACsec capability flag

**Change at a glance:** adds/updates 4 reusable grouping(s); adds/updates 3 reusable type(s).

**Updated groupings:** `capwap-wtp-data`, `cdp-cache-data-op`, `ewlc-radio-operation-config`, `lldp-neigh-data-op`.

**New typedefs:** `cdp-device-security`, `proximity-resolution-method`.

**Updated typedefs:** `flag-ap-capability-ext`.

</details>

<a id="module-cisco-ios-xe-wireless-cisco-spaces-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-cisco-spaces-oper.yang — adds 1 declared schema path(s); adds/updates 2 reusable grouping(s); adds/updates 3 reusable type(s)</summary>

**26.2.1 revision note:** Added IoT Orchestrator operational data - Added IoT Orchestrator auto-configuration reason codes - Deprecated specific failure states of IoT Orchestrator auto-configuration

**Change at a glance:** adds 1 declared schema path(s); adds/updates 2 reusable grouping(s); adds/updates 3 reusable type(s).

**Newly declared schema paths:**
- `/cisco-spaces-oper-data/ewlc-caf-app` (list, key=app-name)

**New groupings:** `st-ewlc-caf-app`.

**Updated groupings:** `st-iot-auto-cfg-params`.

**New typedefs:** `enm-app-state`, `enm-iot-auto-cfg-reason-code`.

**Updated typedefs:** `enm-iot-auto-cfg-state`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-bgp-oper"></a>
<details>
<summary>Cisco-IOS-XE-bgp-oper.yang — adds/updates 5 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 5 reusable grouping(s).

**Updated groupings:** `address-family-summary`, `bgp-transport`, `configured-peer-policy`, `entry-stats`, `negotiated-keepalive-timers`.

</details>

<a id="module-cisco-ios-xe-evpn-oper"></a>
<details>
<summary>Cisco-IOS-XE-evpn-oper.yang — adds 1 declared schema path(s); adds/updates 4 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for several leaves to better explain their meaning and purpose - Added EVPN statistics list with per-VNI route counters for telemetry support

**Change at a glance:** adds 1 declared schema path(s); adds/updates 4 reusable grouping(s).

**Newly declared schema paths:**
- `/evpn-oper-data/evpn-stats` (list, key=evpn-stats-id)

**New groupings:** `evpn-rt-cnt`, `evpn-stats`, `evpn-vni-rt-cnt`, `evpn-vni-rt-cnt-table-key`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-ospf-oper"></a>
<details>
<summary>Cisco-IOS-XE-ospf-oper.yang — adds/updates 5 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 5 reusable grouping(s).

**Updated groupings:** `lsa-header`, `ospf-interface`, `ospfv2-header`, `ospfv2-interface`, `ospfv2-link-tlv`.

</details>

<a id="module-cisco-ios-xe-dhcp-oper"></a>
<details>
<summary>Cisco-IOS-XE-dhcp-oper.yang — adds/updates 4 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated description of several DHCP model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 4 reusable grouping(s).

**Updated groupings:** `dhcpv6-binding-vrf-oper`, `dhcpv6-intf-at-client-oper`, `dhcpv6-intf-at-srv-oper`, `dhcpv6-relay-binding-oper`.

</details>

<a id="module-cisco-ios-xe-nwpi-oper"></a>
<details>
<summary>Cisco-IOS-XE-nwpi-oper.yang — adds/updates 4 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 4 reusable grouping(s).

**Updated groupings:** `nwpi-domain-res`, `nwpi-flow-adv-stats`, `nwpi-flow-base-stats`, `nwpi-qos-mon`.

</details>

<a id="module-cisco-ios-xe-poe-oper"></a>
<details>
<summary>Cisco-IOS-XE-poe-oper.yang — updates 1 status value(s); adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated PoE operational model descriptions for clarity and accuracy. - Marked the legacy poe-port list obsolete in favor of poe-port-detail.

**Change at a glance:** updates 1 status value(s); adds/updates 3 reusable grouping(s).

**Existing paths with contract changes:**
- `/poe-oper-data/poe-port` — status: not specified → obsolete

**Updated groupings:** `lldp-pwr-via-mdi-tlv`, `poe-data-ethernet`, `poe-ethernet`.

**Why this matters:** Review the new lifecycle status; a status change alone does not remove the path.

</details>

<a id="module-cisco-ios-xe-stack-info-oper"></a>
<details>
<summary>Cisco-IOS-XE-stack-info-oper.yang — adds/updates 2 reusable grouping(s); adds/updates 2 reusable type(s)</summary>

**26.2.1 revision note:** Added stack adapter presence, authentication status, and serial number to stack node info - Updated descriptions of several model elements to improve description quality

**Change at a glance:** adds/updates 2 reusable grouping(s); adds/updates 2 reusable type(s).

**New groupings:** `bss-stack-adapter-info`.

**Updated groupings:** `bss-stack-node-info`.

**New typedefs:** `bss-stack-adapter-auth-status`, `bss-stack-adapter-presence`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-wireless-client-global-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-client-global-oper.yang — adds/updates 4 reusable grouping(s)</summary>

**26.2.1 revision note:** Added additional client stats for STA/PMK and anchor request from AP - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 4 reusable grouping(s).

**Updated groupings:** `ap-emltd-by-list`, `client-statistics`, `rssi-sample`, `wlan-emltd-by-list`.

</details>

<a id="module-cisco-ios-xe-wireless-mesh-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-mesh-oper.yang — adds/updates 4 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 4 reusable grouping(s).

**Updated groupings:** `mesh-link-test-config`, `mesh-link-test-rssi-profile`, `st-dca-result`, `st-mesh-wmm-data`.

</details>

<a id="module-cisco-ios-xe-wireless-rrm-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-rrm-oper.yang — adds 2 declared schema path(s); adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added AP Regulatory Activation File (RAF) information

**Change at a glance:** adds 2 declared schema path(s); adds/updates 2 reusable grouping(s).

**Newly declared schema paths:**
- `/rrm-oper-data/reg-blob-ap-data` (list, key=ap-mac)
- `/rrm-oper-data/reg-blob-meta` (container, presence=reg-blob-meta)

**New groupings:** `st-reg-blob-ap-data`, `st-reg-blob-meta`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-crypto-oper"></a>
<details>
<summary>Cisco-IOS-XE-crypto-oper.yang — adds/updates 2 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added PQC key exchange group type leaf to IKE and IPsec SAs

**Change at a glance:** adds/updates 2 reusable grouping(s); adds/updates 1 reusable type(s).

**Updated groupings:** `crypto-ike-sa-data`, `crypto-ipsec-ident-data`.

**New typedefs:** `crypto-pqc-group-type`.

</details>

<a id="module-cisco-ios-xe-fw-oper"></a>
<details>
<summary>Cisco-IOS-XE-fw-oper.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for ZBFW operational leaves to include component context and improve specificity

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `fw-drop-stats`, `fw-l7-traffic-class-list-entry`, `fw-traffic-class-list-entry`.

</details>

<a id="module-cisco-ios-xe-install-oper"></a>
<details>
<summary>Cisco-IOS-XE-install-oper.yang — adds/updates 2 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable grouping(s); adds/updates 1 reusable type(s).

**Updated groupings:** `install-common-smu-pkg-info`, `install-package-data`.

**Updated typedefs:** `install-package-type`.

</details>

<a id="module-cisco-ios-xe-mpls-te-oper"></a>
<details>
<summary>Cisco-IOS-XE-mpls-te-oper.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Refined existing leaf descriptions for clarity and consistency

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `te-he-tunnel`, `te-lm-bw-pool-value`, `te-lm-link`.

</details>

<a id="module-cisco-ios-xe-poe-health-oper"></a>
<details>
<summary>Cisco-IOS-XE-poe-health-oper.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose - Marked poe-meta-data container as obsolete

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `pair-info`, `poe-meta`, `port-health`.

</details>

<a id="module-cisco-ios-xe-switch-ptp-oper"></a>
<details>
<summary>Cisco-IOS-XE-switch-ptp-oper.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of PTP operational model elements to improve clarity and context.

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `ptp-clock-current-data`, `ptp-clock-default-data`, `ptp-oper-time-interval`.

</details>

<a id="module-cisco-ios-xe-uplink-autoconfig-oper"></a>
<details>
<summary>Cisco-IOS-XE-uplink-autoconfig-oper.yang — adds/updates 2 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added a new uplink score enum value and point to point (P2P) indicator leaves for uplink interfaces - Enhanced the descriptions of uplink interface leaves and containers to provide more detailed usage information

**Change at a glance:** adds/updates 2 reusable grouping(s); adds/updates 1 reusable type(s).

**Updated groupings:** `uplink-ipv4-if`, `uplink-ipv6-if`.

**Updated typedefs:** `uplink-score`.

</details>

<a id="module-cisco-ios-xe-wireless-urwb-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-urwb-oper.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Added URWB Ethernet operational data leaves - Added configured URWB network name to operational data - Added learned URWB network name to operational data - Added URWB NAT operational data - Updated descriptions of urwb-oper-data list and urwb-support leaf for clarity, grammar, and consistency

**Change at a glance:** adds/updates 3 reusable grouping(s).

**New groupings:** `st-urwb-nat-rule-oper`, `st-urwb-radius-server`.

**Updated groupings:** `st-urwb-oper-data`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-app-hosting-oper"></a>
<details>
<summary>Cisco-IOS-XE-app-hosting-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements across the model from terse labels to complete English sentences, improving documentation clarity for model consumers. - Added application memory utilization support in the memory utilization container.

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `memory-util`, `vs-process`.

</details>

<a id="module-cisco-ios-xe-bgp-rib-oper"></a>
<details>
<summary>Cisco-IOS-XE-bgp-rib-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `bgp-path-unknown-attr`, `bgp-path-unknown-attr-key`.

</details>

<a id="module-cisco-ios-xe-bridge-oper"></a>
<details>
<summary>Cisco-IOS-XE-bridge-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `bridge-entry`, `bridge-intf-entry`.

</details>

<a id="module-cisco-ios-xe-cdp-oper"></a>
<details>
<summary>Cisco-IOS-XE-cdp-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Changed description of several leaves in CDP neighbor details - Added units for CDP hello payload length and power available leaves

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `cdp-power-avail`, `cdp-protocol-hello`.

</details>

<a id="module-cisco-ios-xe-cellwan-oper"></a>
<details>
<summary>Cisco-IOS-XE-cellwan-oper.yang — adds 1 declared schema path(s); adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added cellwan-dg list for dying-gasp functionality; when enabled, sends SMS to specified phone number on platform or module power down - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds 1 declared schema path(s); adds/updates 1 reusable grouping(s).

**Newly declared schema paths:**
- `/cellwan-oper-data/cellwan-dg` (list, key=cell-if-name)

**New groupings:** `cellwan-dg-entry`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-interfaces-oper"></a>
<details>
<summary>Cisco-IOS-XE-interfaces-oper.yang — adds/updates 1 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added port SNR link quality status, fast-retrain event counter, and third-party SFP indicator for Ethernet interfaces - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s); adds/updates 1 reusable type(s).

**Updated groupings:** `ethernet-state`.

**New typedefs:** `intf-snr-value`.

</details>

<a id="module-cisco-ios-xe-ios-events-oper"></a>
<details>
<summary>Cisco-IOS-XE-ios-events-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added host-name and system-ip to bridge state notifications

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `bridge-intf-state`, `bridge-state`.

</details>

<a id="module-cisco-ios-xe-livetools-oper"></a>
<details>
<summary>Cisco-IOS-XE-livetools-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose.

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `dns-query-response`, `mtr-host`.

</details>

<a id="module-cisco-ios-xe-mpls-ldp-oper"></a>
<details>
<summary>Cisco-IOS-XE-mpls-ldp-oper.yang — adds/updates 1 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Refined existing leaf descriptions for clarity and consistency - Deprecated existing password-pending leaf containing pending password state in favor of a new bits type leaf

**Change at a glance:** adds/updates 1 reusable grouping(s); adds/updates 1 reusable type(s).

**Updated groupings:** `hello-adjacency`.

**New typedefs:** `password-pending-flag`.

</details>

<a id="module-cisco-ios-xe-mroute-oper"></a>
<details>
<summary>Cisco-IOS-XE-mroute-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `mcast-outgoing-interface`, `mroute-state`.

</details>

<a id="module-cisco-ios-xe-qfp-appqoe-dp-oper"></a>
<details>
<summary>Cisco-IOS-XE-qfp-appqoe-dp-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `appnav-snstats`, `sdvt-pkt-stats-entry`.

</details>

<a id="module-cisco-ios-xe-wireless-ble-ltx-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-ble-ltx-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose - Added scan config related data

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `ble-ltx-scan-config`, `ble-ltx-scan-config-feedback`.

</details>

<a id="module-cisco-ios-xe-wireless-rogue-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-rogue-oper.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `st-rldp-stats`, `st-rogue-data-per-band`.

</details>

<a id="module-cisco-ios-xe-bgp-route-oper"></a>
<details>
<summary>Cisco-IOS-XE-bgp-route-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `peer-group`.

</details>

<a id="module-cisco-ios-xe-eigrp-oper"></a>
<details>
<summary>Cisco-IOS-XE-eigrp-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to help clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `eigrp-ios-oper-metric`.

</details>

<a id="module-cisco-ios-xe-environment-oper"></a>
<details>
<summary>Cisco-IOS-XE-environment-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added a signed reading leaf for current sensor reading to replace deprecated unsigned current-reading leaf -Updated description of environment related elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `sensor-params`.

</details>

<a id="module-cisco-ios-xe-fib-oper"></a>
<details>
<summary>Cisco-IOS-XE-fib-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Modified descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `cef-interface`.

</details>

<a id="module-cisco-ios-xe-flow-monitor-oper"></a>
<details>
<summary>Cisco-IOS-XE-flow-monitor-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Refined existing leaf descriptions for clarity and consistency

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `flow-export-protocol-stats`.

</details>

<a id="module-cisco-ios-xe-isis-intf-oper"></a>
<details>
<summary>Cisco-IOS-XE-isis-intf-oper.yang — updates 1 status value(s)</summary>

**26.2.1 revision note:** This model has been deprecated and replaced by version 2 yang model - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** updates 1 status value(s).

**Existing paths with contract changes:**
- `/isis-intf-oper-data` — status: not specified → deprecated

**Why this matters:** Review the new lifecycle status; a status change alone does not remove the path.

</details>

<a id="module-cisco-ios-xe-meraki-connect-oper"></a>
<details>
<summary>Cisco-IOS-XE-meraki-connect-oper.yang — adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added new product identifiers for Meraki monitoring support - Added new switching platform identifiers for Cloud monitoring support. - Added product identifiers of industrial switches for Meraki Cloud support. - Updated the virtual switch product identifier description for clarity. - Updated descriptions for clarity and consistency.

**Change at a glance:** adds/updates 1 reusable type(s).

**Updated typedefs:** `meraki-device-pid`.

</details>

<a id="module-cisco-ios-xe-mrp-oper"></a>
<details>
<summary>Cisco-IOS-XE-mrp-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for several model elements to clarify their meaning and purpose - Added a units annotation to beacon-interval leaf in mrp-ring-hw-stats grouping

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `mrp-ring-hw-stats`.

</details>

<a id="module-cisco-ios-xe-ntp-oper"></a>
<details>
<summary>Cisco-IOS-XE-ntp-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to help clarify their meaning and purpose.

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `ntp-container-data`.

</details>

<a id="module-cisco-ios-xe-perf-measure-oper"></a>
<details>
<summary>Cisco-IOS-XE-perf-measure-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Improved YANG description quality for better clarity and completeness

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `metric`.

</details>

<a id="module-cisco-ios-xe-platform-software-oper"></a>
<details>
<summary>Cisco-IOS-XE-platform-software-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for load average, memory, CPU, and process statistics leafs to provide more detailed and precise explanations

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `core`.

</details>

<a id="module-cisco-ios-xe-process-memory-oper"></a>
<details>
<summary>Cisco-IOS-XE-process-memory-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Changed description of get-buffers and ret-buffers leaves - Added units for get-buffers and ret-buffers leaves

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `process-memory-usage`.

</details>

<a id="module-cisco-ios-xe-qfp-dp-cmn-stats-oper"></a>
<details>
<summary>Cisco-IOS-XE-qfp-dp-cmn-stats-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added DHCPv6 Relay Punt Statistics

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `gw-dp-global-punt-stats`.

</details>

<a id="module-cisco-ios-xe-qfp-stats-oper"></a>
<details>
<summary>Cisco-IOS-XE-qfp-stats-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Update the counter descriptions.

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `datapath-qfp-stats`.

</details>

<a id="module-cisco-ios-xe-rawsocket-oper"></a>
<details>
<summary>Cisco-IOS-XE-rawsocket-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `connection-stats`.

</details>

<a id="module-cisco-ios-xe-sd-vxlan-oper"></a>
<details>
<summary>Cisco-IOS-XE-sd-vxlan-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for several leaves to better explain their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `per-vni-vrf-policer`.

</details>

<a id="module-cisco-ios-xe-stack-oper"></a>
<details>
<summary>Cisco-IOS-XE-stack-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `stack-info`.

</details>

<a id="module-cisco-ios-xe-system-security-oper"></a>
<details>
<summary>Cisco-IOS-XE-system-security-oper.yang — adds 1 declared schema path(s)</summary>

**26.2.1 revision note:** Enhanced index field description for improved clarity - Added operational data support for insecure dynamic warnings.

**Change at a glance:** adds 1 declared schema path(s).

**Newly declared schema paths:**
- `/system-security-oper-data/sys-insec-warn` (list, key=index)

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-tunnel-oper"></a>
<details>
<summary>Cisco-IOS-XE-tunnel-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `tunnel-common-interface`.

</details>

<a id="module-cisco-ios-xe-utd-oper"></a>
<details>
<summary>Cisco-IOS-XE-utd-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for UTD operational leafs to include component context and improve specificity

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `utd-file-analysis-status`.

</details>

<a id="module-cisco-ios-xe-wireless-mesh-global-oper"></a>
<details>
<summary>Cisco-IOS-XE-wireless-mesh-global-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `st-emltd-mesh-path-info`.

</details>

<a id="module-cisco-ios-xe-yang-interfaces-oper"></a>
<details>
<summary>Cisco-IOS-XE-yang-interfaces-oper.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Refined existing leaf descriptions for clarity and consistency - Added aes128-gcm@openssh.com to Device Management Interface SSH cipher algorithms operational data

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `dmi-ssh-cipher-algorithms-oper`.

</details>

</details>

<a id="tracked-rpc"></a>

### RPC (8 existing modules with tracked changes)

<details>
<summary>Show 8 RPC entries</summary>

**Module index:**

- [Cisco-IOS-XE-crypto-rpc.yang](#module-cisco-ios-xe-crypto-rpc) · [Cisco-IOS-XE-cts-rpc.yang](#module-cisco-ios-xe-cts-rpc) · [Cisco-IOS-XE-meraki-leds-actions-rpc.yang](#module-cisco-ios-xe-meraki-leds-actions-rpc)
- [Cisco-IOS-XE-port-bounce-rpc.yang](#module-cisco-ios-xe-port-bounce-rpc) · [Cisco-IOS-XE-sse-actions-rpc.yang](#module-cisco-ios-xe-sse-actions-rpc) · [Cisco-IOS-XE-utd-rpc.yang](#module-cisco-ios-xe-utd-rpc)
- [Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang](#module-cisco-ios-xe-wireless-access-point-cfg-rpc) · [Cisco-IOS-XE-xcopy-rpc.yang](#module-cisco-ios-xe-xcopy-rpc)


<a id="module-cisco-ios-xe-cts-rpc"></a>
<details>
<summary>Cisco-IOS-XE-cts-rpc.yang — adds 8 declared schema path(s); updates 2 type constraint(s)</summary>

**26.2.1 revision note:** Added cts refresh environment-data, policy, policy sgt and pac RPCs

**Change at a glance:** adds 8 declared schema path(s); updates 2 type constraint(s).

**Newly declared schema paths:**
- `/rpc:cts/input/refresh` (container)
- `/rpc:cts/input/refresh/environment-data` (leaf, type=empty)
- `/rpc:cts/input/refresh/pac` (leaf, type=empty)
- `/rpc:cts/input/refresh/policy` (container, presence=Refresh all peer and Role-Based Access Control List policies)
- `/rpc:cts/input/refresh/policy/sgt` (container, presence=Refresh all SGT policies)
- `/rpc:cts/input/refresh/policy/sgt/default` (leaf, type=empty)
- `/rpc:cts/input/refresh/policy/sgt/sgt-drop-node-name` (leaf, type=uint16 (range 2..65521))
- `/rpc:cts/input/refresh/policy/sgt/unknown` (leaf, type=empty)

**Existing paths with contract changes:**
- `/rpc:cts/input/credentials/id` — type: string (length 1..24) → string (length 1..32)
- `/rpc:cts/input/credentials/password` — type: string → string (length 1..24)

**Why this matters:** Check the listed type and range changes against client validation and accepted input values.

</details>

<a id="module-cisco-ios-xe-wireless-access-point-cfg-rpc"></a>
<details>
<summary>Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang — adds operation(s) <code>/rpc:clear-ap-country</code>, <code>/rpc:clear-ap-floor</code>, <code>/rpc:set-sniffing-request</code>; adds 3 declared schema path(s); adds/updates 5 reusable grouping(s)</summary>

**26.2.1 revision note:** Removed the invalid when constraint for band leaf - Added support to configure URWB network name on Coordinator AP - Added RPC for clearing AP country code - Added support for set-sniffing-request RPC to start and stop the sniffer with required parameters, and deprecated chan and ip-addr leaves in dual-band-role RPC - Added RPC for clearing AP floor ID setting

**Change at a glance:** adds operation(s) `/rpc:clear-ap-country`, `/rpc:clear-ap-floor`, `/rpc:set-sniffing-request`; adds 3 declared schema path(s); adds/updates 5 reusable grouping(s).

**RPC/actions in this module:** 54 → 57.

**New operation entry points:** `/rpc:clear-ap-country`, `/rpc:clear-ap-floor`, `/rpc:set-sniffing-request`.

**New groupings:** `clear-ap-country`, `clear-ap-floor`, `set-sniffing-request`.

**Updated groupings:** `dual-band-role`, `set-ap-urwb-crd-mode`.

**Why this matters:** 3 new RPC/action entry point(s) are declared in this module.

</details>

<a id="module-cisco-ios-xe-sse-actions-rpc"></a>
<details>
<summary>Cisco-IOS-XE-sse-actions-rpc.yang — adds operation(s) <code>/rpc:set-sse-root-ca-bdl-upd</code>; adds 1 declared schema path(s); adds/updates 2 reusable grouping(s); adds/updates 2 reusable type(s)</summary>

**26.2.1 revision note:** Added an RPC to update the Secure Service Edge (SSE) Root Certificate Authority (CA) bundle path and SHA-256 digest

**Change at a glance:** adds operation(s) `/rpc:set-sse-root-ca-bdl-upd`; adds 1 declared schema path(s); adds/updates 2 reusable grouping(s); adds/updates 2 reusable type(s).

**RPC/actions in this module:** 2 → 3.

**New operation entry points:** `/rpc:set-sse-root-ca-bdl-upd`.

**New groupings:** `sse-root-ca-bdl-upd`, `sse-root-ca-bdl-upd-rsp`.

**New typedefs:** `sse-root-ca-bdl-fail-reason`, `sse-root-ca-bdl-status`.

**Why this matters:** 1 new RPC/action entry point(s) are declared in this module.

</details>

<a id="module-cisco-ios-xe-crypto-rpc"></a>
<details>
<summary>Cisco-IOS-XE-crypto-rpc.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added ML-DSA key generate command.

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `crypto-input-grouping`.

</details>

<a id="module-cisco-ios-xe-meraki-leds-actions-rpc"></a>
<details>
<summary>Cisco-IOS-XE-meraki-leds-actions-rpc.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added slot-num input to blink LEDs RPC

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `blink-leds-params`.

</details>

<a id="module-cisco-ios-xe-port-bounce-rpc"></a>
<details>
<summary>Cisco-IOS-XE-port-bounce-rpc.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added length constraint and extended if-name leaf pattern to include 50 Gigabit Ethernet and 400 Gigabit Ethernet interface name formats

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `port-bounce`.

</details>

<a id="module-cisco-ios-xe-utd-rpc"></a>
<details>
<summary>Cisco-IOS-XE-utd-rpc.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Add refresh-token authentication

**Change at a glance:** adds/updates 1 reusable grouping(s).

**New groupings:** `utd-refresh-token-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-xcopy-rpc"></a>
<details>
<summary>Cisco-IOS-XE-xcopy-rpc.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added deprecation warnings to the path leaf for insecure FTP, HTTP, and TFTP protocols. - Added support for the '~' character in URL source and destination path input parameters of express copy RPC

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `xcopy`.

</details>

</details>

<a id="tracked-native"></a>

### Native (6 source entries)

<details>
<summary>Show 6 Native entries</summary>

**Module index:**

- [Cisco-IOS-XE-interfaces.yang](#module-cisco-ios-xe-interfaces) · [Cisco-IOS-XE-ip.yang](#module-cisco-ios-xe-ip) · [Cisco-IOS-XE-ipv6.yang](#module-cisco-ios-xe-ipv6)
- [Cisco-IOS-XE-license.yang](#module-cisco-ios-xe-license) · [Cisco-IOS-XE-line.yang](#module-cisco-ios-xe-line) · [Cisco-IOS-XE-native.yang](#module-cisco-ios-xe-native)


<a id="module-cisco-ios-xe-native"></a>
<details>
<summary>Cisco-IOS-XE-native.yang — adds 15 declared schema path(s); updates 25 status value(s), 3 type constraint(s), 3 default value(s)</summary>

**26.2.1 revision note:** Added stack-power stack mode container with power-shared and redundant options - Added stack-power switch list for per-switch power stack assignment; stack and standalone leaves are independently configurable; must constraint requires the power stack to exist before switch assignment - Deprecated ip vrf - Added a leaf for ip-forward feature support - Deprecated the nsap leaf - Marked insecure TFTP configuration nodes as deprecated - Deprecated insecure transport options for archive path - Added sla-policy container for SLA Policy configuration - Added default value for mac address-table aging time value, threshold - Added security container inside system for avoiding mode collision - Obsoleted unsupported ciphersuites - Moved deprecated service dhcp leaf to obsolete, use dhcp-config instead - Add vlan container under ethernet module for vlan unlimited command - Added support for subslot 0 to 5 in subslot-number leaf - Added auto secure macsec leaf - Marked archive log config hidekeys as obsolete - Added type 6 support for redundancy authentication text config

**Change at a glance:** adds 15 declared schema path(s); updates 25 status value(s), 3 type constraint(s), 3 default value(s).

**Newly declared schema paths:**
- `/native/auto` (container)
- `/native/auto/secure` (container, if-feature=ios-features:switching-platform)
- `/native/auto/secure/macsec` (leaf, default=false, type=boolean)
- `/native/hw-module/subslot/ethernet/vlan` (container)
- `/native/hw-module/subslot/ethernet/vlan/unlimited` (leaf, type=empty)
- `/native/sla-policy` (container)
- `/native/stack-power/stack/mode` (container)
- `/native/stack-power/stack/mode/power-shared` (container)
- `/native/stack-power/stack/mode/power-shared/strict` (leaf, type=empty)
- `/native/stack-power/stack/mode/redundant` (container, presence=true)
- `/native/stack-power/stack/mode/redundant/strict` (leaf, type=empty)
- `/native/stack-power/switch` (list, key=switch-id)
- Plus 3 additional paths; see the linked module for full definitions.

**Existing paths with contract changes:**
- `/native/archive/log/config/hidekeys` — status: deprecated → obsolete
- `/native/archive/path` — the union still permits `bootflash:`, `flash:`, `ftp:`, `harddisk:`, `http:`, `https:`, `pram:`, `rcp:`, `scp:`, `tftp:`, or a string; 26.2.1 marks the `ftp:`, `http:`, `rcp:`, and `tftp:` enum values deprecated as insecure transports.
- `/native/eap/profile/ciphersuite/dhe-rsa-aes256-sha` — status: deprecated → obsolete
- `/native/eap/profile/ciphersuite/ecdhe-ecdsa-aes-sha` — status: deprecated → obsolete
- `/native/eap/profile/ciphersuite/ecdhe-rsa-aes-sha` — status: deprecated → obsolete
- `/native/hw-module/subslot/subslot-number` — type: string (length 1..3; pattern [0-2/0-2]*) → string (length 1..3; pattern [0-2]/[0-5])
- `/native/mac/address-table/aging-time/val` — default: not specified → 300
- `/native/mac/address-table/notification/threshold/interval` — default: not specified → 120
- `/native/mac/address-table/notification/threshold/limit/percentage` — default: not specified → 50
- `/native/redundancy/application/redundancy/protocol/authentication/text/encrypt` — type: enumeration (enum 7) → enumeration (enum 7; enum 6)
- `/native/service/dhcp` — status: deprecated → obsolete
- `/native/tftp-server-config` — status: not specified → deprecated
- Plus 19 additional changed paths.

**Why this matters:** Check the listed type and range changes against client validation and accepted input values. The value applied when a client omits the leaf may change. Review the new lifecycle status; a status change alone does not remove the path.

</details>

<a id="module-cisco-ios-xe-ip"></a>
<details>
<summary>Cisco-IOS-XE-ip.yang — adds/updates 7 reusable grouping(s)</summary>

**26.2.1 revision note:** Obsolete ip prefix-lists sequence-number leaf - Deprecated ip vrf - Obsolete use-bgp leaf - Added strict hostkey support for ssh - Added support for server ssh public key chain - Added DHCP track - Added back Must condition for vlan interface existence in ip route which was removed earlier in version 17.15.1 - Deprecated the nsap leaf - Fixed backslash escape issue in type6 encrypted passwords for ftp, scp, and sftp - Added tag support for ip route dhcp

**Change at a glance:** adds/updates 7 reusable grouping(s).

**New groupings:** `route-replicate-grouping-deprecated`, `vrf-maximum-grouping-deprecated`.

**Updated groupings:** `config-ip-grouping`, `config-mvpn-mdt-grouping`, `ip-route-dhcp-only-options-grouping`, `ip-route-fwd-list-key-grouping`, `ip-route-grouping-min-elements`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-interfaces"></a>
<details>
<summary>Cisco-IOS-XE-interfaces.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added uplink extension - Added a leaf for ip-forward feature support - Changed default value of ip proxy-arp to false - Added cloud tracker and uplink priority model support - Updated IPv4/IPv6 tcp adjust-mss ranges - Added ordering for 5Gig main interface and sub interface - Removed cloud tracker support - Added unique constraint of uplink color model.

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `interface-common-grouping`.

</details>

<a id="module-cisco-ios-xe-ipv6"></a>
<details>
<summary>Cisco-IOS-XE-ipv6.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Obsolete ipv6 source-guard policy validate address

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-ipv6-grouping`.

</details>

<a id="module-cisco-ios-xe-license"></a>
<details>
<summary>Cisco-IOS-XE-license.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added reservation keyword and default for transport. -Added mode container with universal leaf to configure device boot with universal license mode. -Updated license boot essentials and license boot advantage behavior, so remove operations are handled correctly. -Ensured universal mode is set before license boot level essentials during configuration replay. -Ensured universal mode is set before license boot level advantage during configuration replay.

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-license-grouping`.

</details>

<a id="module-cisco-ios-xe-line"></a>
<details>
<summary>Cisco-IOS-XE-line.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated no-activation-character leaf for line console

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `line-grouping-con-and-aux`.

</details>

</details>

<a id="tracked-config"></a>

### Config (89 source entries)

<details>
<summary>Show 89 Config entries</summary>

**Module index:**

- [Cisco-IOS-XE-aaa.yang](#module-cisco-ios-xe-aaa) · [Cisco-IOS-XE-acl.yang](#module-cisco-ios-xe-acl) · [Cisco-IOS-XE-bfd.yang](#module-cisco-ios-xe-bfd)
- [Cisco-IOS-XE-bgp.yang](#module-cisco-ios-xe-bgp) · [Cisco-IOS-XE-cdp.yang](#module-cisco-ios-xe-cdp) · [Cisco-IOS-XE-cip.yang](#module-cisco-ios-xe-cip)
- [Cisco-IOS-XE-controller.yang](#module-cisco-ios-xe-controller) · [Cisco-IOS-XE-crypto.yang](#module-cisco-ios-xe-crypto) · [Cisco-IOS-XE-ctrl-mng-cfg.yang](#module-cisco-ios-xe-ctrl-mng-cfg)
- [Cisco-IOS-XE-cts.yang](#module-cisco-ios-xe-cts) · [Cisco-IOS-XE-device-sensor.yang](#module-cisco-ios-xe-device-sensor) · [Cisco-IOS-XE-dhcp.yang](#module-cisco-ios-xe-dhcp)
- [Cisco-IOS-XE-dot1x.yang](#module-cisco-ios-xe-dot1x) · [Cisco-IOS-XE-eigrp.yang](#module-cisco-ios-xe-eigrp) · [Cisco-IOS-XE-eta.yang](#module-cisco-ios-xe-eta)
- [Cisco-IOS-XE-ethernet.yang](#module-cisco-ios-xe-ethernet) · [Cisco-IOS-XE-flow.yang](#module-cisco-ios-xe-flow) · [Cisco-IOS-XE-gnmi-cfg.yang](#module-cisco-ios-xe-gnmi-cfg)
- [Cisco-IOS-XE-gnss.yang](#module-cisco-ios-xe-gnss) · [Cisco-IOS-XE-group-policy.yang](#module-cisco-ios-xe-group-policy) · [Cisco-IOS-XE-grpc-tunnel-cfg.yang](#module-cisco-ios-xe-grpc-tunnel-cfg)
- [Cisco-IOS-XE-http.yang](#module-cisco-ios-xe-http) · [Cisco-IOS-XE-icmp.yang](#module-cisco-ios-xe-icmp) · [Cisco-IOS-XE-igmp.yang](#module-cisco-ios-xe-igmp)
- [Cisco-IOS-XE-isg.yang](#module-cisco-ios-xe-isg) · [Cisco-IOS-XE-isis.yang](#module-cisco-ios-xe-isis) · [Cisco-IOS-XE-l2vpn.yang](#module-cisco-ios-xe-l2vpn)
- [Cisco-IOS-XE-lisp.yang](#module-cisco-ios-xe-lisp) · [Cisco-IOS-XE-lldp.yang](#module-cisco-ios-xe-lldp) · [Cisco-IOS-XE-loop-detect.yang](#module-cisco-ios-xe-loop-detect)
- [Cisco-IOS-XE-lte450.yang](#module-cisco-ios-xe-lte450) · [Cisco-IOS-XE-mdns-gateway.yang](#module-cisco-ios-xe-mdns-gateway) · [Cisco-IOS-XE-mdt-cfg.yang](#module-cisco-ios-xe-mdt-cfg)
- [Cisco-IOS-XE-mdt-oper-v2.yang](#module-cisco-ios-xe-mdt-oper-v2) · [Cisco-IOS-XE-mka.yang](#module-cisco-ios-xe-mka) · [Cisco-IOS-XE-mld.yang](#module-cisco-ios-xe-mld)
- [Cisco-IOS-XE-mobileip.yang](#module-cisco-ios-xe-mobileip) · [Cisco-IOS-XE-mpls.yang](#module-cisco-ios-xe-mpls) · [Cisco-IOS-XE-mrp.yang](#module-cisco-ios-xe-mrp)
- [Cisco-IOS-XE-multicast.yang](#module-cisco-ios-xe-multicast) · [Cisco-IOS-XE-mvrp.yang](#module-cisco-ios-xe-mvrp) · [Cisco-IOS-XE-nat.yang](#module-cisco-ios-xe-nat)
- [Cisco-IOS-XE-nbar.yang](#module-cisco-ios-xe-nbar) · [Cisco-IOS-XE-ncch-cfg.yang](#module-cisco-ios-xe-ncch-cfg) · [Cisco-IOS-XE-nd.yang](#module-cisco-ios-xe-nd)
- [Cisco-IOS-XE-ntp.yang](#module-cisco-ios-xe-ntp) · [Cisco-IOS-XE-ospf.yang](#module-cisco-ios-xe-ospf) · [Cisco-IOS-XE-ospfv3.yang](#module-cisco-ios-xe-ospfv3)
- [Cisco-IOS-XE-platform.yang](#module-cisco-ios-xe-platform) · [Cisco-IOS-XE-pnp.yang](#module-cisco-ios-xe-pnp) · [Cisco-IOS-XE-policy.yang](#module-cisco-ios-xe-policy)
- [Cisco-IOS-XE-power.yang](#module-cisco-ios-xe-power) · [Cisco-IOS-XE-prp.yang](#module-cisco-ios-xe-prp) · [Cisco-IOS-XE-ptp.yang](#module-cisco-ios-xe-ptp)
- [Cisco-IOS-XE-rawsocket.yang](#module-cisco-ios-xe-rawsocket) · [Cisco-IOS-XE-rip.yang](#module-cisco-ios-xe-rip) · [Cisco-IOS-XE-rsvp.yang](#module-cisco-ios-xe-rsvp)
- [Cisco-IOS-XE-sanet.yang](#module-cisco-ios-xe-sanet) · [Cisco-IOS-XE-site-manager.yang](#module-cisco-ios-xe-site-manager) · [Cisco-IOS-XE-snmp.yang](#module-cisco-ios-xe-snmp)
- [Cisco-IOS-XE-spanning-tree.yang](#module-cisco-ios-xe-spanning-tree) · [Cisco-IOS-XE-switch.yang](#module-cisco-ios-xe-switch) · [Cisco-IOS-XE-synce.yang](#module-cisco-ios-xe-synce)
- [Cisco-IOS-XE-template.yang](#module-cisco-ios-xe-template) · [Cisco-IOS-XE-track.yang](#module-cisco-ios-xe-track) · [Cisco-IOS-XE-udld.yang](#module-cisco-ios-xe-udld)
- [Cisco-IOS-XE-umbrella.yang](#module-cisco-ios-xe-umbrella) · [Cisco-IOS-XE-utd.yang](#module-cisco-ios-xe-utd) · [Cisco-IOS-XE-vlan.yang](#module-cisco-ios-xe-vlan)
- [Cisco-IOS-XE-voice.yang](#module-cisco-ios-xe-voice) · [Cisco-IOS-XE-vrrp.yang](#module-cisco-ios-xe-vrrp) · [Cisco-IOS-XE-vtp.yang](#module-cisco-ios-xe-vtp)
- [Cisco-IOS-XE-wccp.yang](#module-cisco-ios-xe-wccp) · [Cisco-IOS-XE-wireless-ap-cfg.yang](#module-cisco-ios-xe-wireless-ap-cfg) · [Cisco-IOS-XE-wireless-cts-sxp-cfg.yang](#module-cisco-ios-xe-wireless-cts-sxp-cfg)
- [Cisco-IOS-XE-wireless-dot11-cfg.yang](#module-cisco-ios-xe-wireless-dot11-cfg) · [Cisco-IOS-XE-wireless-general-cfg.yang](#module-cisco-ios-xe-wireless-general-cfg) · [Cisco-IOS-XE-wireless-mesh-cfg.yang](#module-cisco-ios-xe-wireless-mesh-cfg)
- [Cisco-IOS-XE-wireless-mstream-cfg.yang](#module-cisco-ios-xe-wireless-mstream-cfg) · [Cisco-IOS-XE-wireless-rf-cfg.yang](#module-cisco-ios-xe-wireless-rf-cfg) · [Cisco-IOS-XE-wireless-rlan-cfg.yang](#module-cisco-ios-xe-wireless-rlan-cfg)
- [Cisco-IOS-XE-wireless-rogue-cfg.yang](#module-cisco-ios-xe-wireless-rogue-cfg) · [Cisco-IOS-XE-wireless-rrm-cfg.yang](#module-cisco-ios-xe-wireless-rrm-cfg) · [Cisco-IOS-XE-wireless-site-cfg.yang](#module-cisco-ios-xe-wireless-site-cfg)
- [Cisco-IOS-XE-wireless-urwb-cfg.yang](#module-cisco-ios-xe-wireless-urwb-cfg) · [Cisco-IOS-XE-wireless-wat-cfg.yang](#module-cisco-ios-xe-wireless-wat-cfg) · [Cisco-IOS-XE-wireless-wlan-cfg.yang](#module-cisco-ios-xe-wireless-wlan-cfg)
- [Cisco-IOS-XE-wsma.yang](#module-cisco-ios-xe-wsma) · [Cisco-IOS-XE-yang-interfaces-cfg.yang](#module-cisco-ios-xe-yang-interfaces-cfg)


<a id="module-cisco-ios-xe-bgp"></a>
<details>
<summary>Cisco-IOS-XE-bgp.yang — adds/updates 18 reusable grouping(s)</summary>

**26.2.1 revision note:** Obsoleted child nodes for Container Scope which is already obsoleted - Add encap SRv6 under l2vpn evpn address-family - Import crypto, neighbor-ao-grouping to delete before key chain - Set maximum length of password to support type 6 encryption - Removed must constraint on redistribute isis under BGP address-family to avoid dmi process crash during BGP sync - Add default value to address-family / neighbor allowas-in as-number - Fixed standard large-community-list action edits to preserve sibling actions

**Change at a glance:** adds/updates 18 reusable grouping(s).

**New groupings:** `ipv4-unicast-neighbor-obsolete`, `ipv4-unicast-obsolete-grouping`, `ipv6-unicast-neighbor-obsolete`, `ipv6-unicast-obsolete-grouping`, `neighbor-send-community-obsolete-grouping-v1`, `vpnv4-unicast-neighbor-obsolete`, `vpnv4-unicast-obsolete-grouping`, `vpnv6-unicast-neighbor-obsolete`, `vpnv6-unicast-obsolete-grouping`.

**Updated groupings:** `address-family-no-vrf-obsolete-grouping`, `address-family-redistribute-grouping`, `address-family-redistribute-grouping-obsolete`, `address-family-v6-redistribute-grouping-obsolete`, `neighbor-allowas-in-grouping`, `neighbor-encap-grouping`, `neighbor-password-grouping`, `redist-isis-grouping`, `redistribute-isis-v6-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-mdt-cfg"></a>
<details>
<summary>Cisco-IOS-XE-mdt-cfg.yang — adds 2 declared schema path(s); adds/updates 6 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose - Added configuration to support a subscription subscribing to a sensor group. - Added support for gRPC keepalive configuration.

**Change at a glance:** adds 2 declared schema path(s); adds/updates 6 reusable grouping(s).

**Newly declared schema paths:**
- `/mdt-config-data/mdt-sensor-groups` (container)
- `/mdt-config-data/mdt-sensor-groups/mdt-sensor-group` (list, key=id)

**New groupings:** `mdt-cnfg-sensor-group`, `mdt-cnfg-sensor-path`.

**Updated groupings:** `mdt-named-protocol-rcvr`, `mdt-protocol-grpc-profile`, `mdt-xfrm-input`, `mdt-xfrm-op-filter`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-switch"></a>
<details>
<summary>Cisco-IOS-XE-switch.yang — adds/updates 8 reusable grouping(s)</summary>

**26.2.1 revision note:** Update device classifier cli to suite mac regex for or operation - Update condition as check in device classifier - Added model support for voice vlan - Obsoleted config-network-policy-grouping - Added the model support for voice-signaling vlan - Adding new cli for auto macsec - Moved the must from container mac-move to the redundancy-protocol leaf - Update range for system mtu

**Change at a glance:** adds/updates 8 reusable grouping(s).

**New groupings:** `condition-list-grouping`, `config-network-policy-grouping-v2`.

**Updated groupings:** `config-device-grouping`, `config-interface-switch-grouping`, `config-interface-switchport-grouping`, `config-network-policy-grouping`, `config-system-grouping`, `mac-regex-condition-grouping-v2`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

**Augment delta:** 0 new target(s), 1 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-crypto"></a>
<details>
<summary>Cisco-IOS-XE-crypto.yang — adds/updates 6 reusable grouping(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support - Added missed cli parameter descriptions for command crypto skip-client server - Added support for certificate hide hex - Added tailf to re-order to detach the keyring from ikev2 profile before deletion - Added tailf:cli-preformatted to handle escape sequence in leaf nodes for key - Added MACsec key chain key-id and key-string validation constraints to align YANG behavior with CLI validation - Added mldsakeypair container under crypto pki trustpoint for ML-DSA key support - Added mldsa-sig leaf under ikev2 profile authentication local and remote

**Change at a glance:** adds/updates 6 reusable grouping(s).

**New groupings:** `crypto-ikev2-profile-authentication-grouping-deprecated`, `crypto-ikev2-profile-authentication-key-grouping-deprecated`.

**Updated groupings:** `config-crypto-grouping`, `config-key-grouping`, `crypto-ikev2-profile-grouping`, `crypto-pki-trustpoint-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

**Augment delta:** 4 new target(s), 4 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-mdt-oper-v2"></a>
<details>
<summary>Cisco-IOS-XE-mdt-oper-v2.yang — adds 1 declared schema path(s); adds/updates 4 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added support to allow subscriptions to subscribe to a sensor group - Added backoff receiver state enum and retry tracking leaves - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds 1 declared schema path(s); adds/updates 4 reusable grouping(s); adds/updates 1 reusable type(s).

**Newly declared schema paths:**
- `/mdt-oper-v2-data/mdt-sensor-group` (list, key=id)

**New groupings:** `mdt-sensor-group`, `mdt-sensor-path`.

**Updated groupings:** `mdt-receiver-name`, `pull-con-params`.

**Updated typedefs:** `mdt-receiver-state`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-rawsocket"></a>
<details>
<summary>Cisco-IOS-XE-rawsocket.yang — adds 4 declared schema path(s); updates 1 <code>when</code> condition(s), 1 status value(s)</summary>

**26.2.1 revision note:** Added support DCE/DTE for RS232 media type

**Change at a glance:** adds 4 declared schema path(s); updates 1 `when` condition(s), 1 status value(s).

**Newly declared schema paths:**
- `/augment[/ios:native/ios:interface/ios:Async]/media-type-new` (container)
- `/augment[/ios:native/ios:interface/ios:Async]/media-type-new/rs232` (container, presence=true)
- `/augment[/ios:native/ios:interface/ios:Async]/media-type-new/rs232/rs232-mode` (leaf, default=dce, type=enumeration (enum dce; enum dte), if-feature=ios-features:rs232-feature)
- `/augment[/ios:native/ios:interface/ios:Async]/media-type-new/rs485` (leaf, type=empty)

**Existing paths with contract changes:**
- `/augment[/ios:native/ios:interface/ios:Async]/duplex-mode` — when: ../media-type = 'rs485' → ../media-type-new/rs485
- `/augment[/ios:native/ios:interface/ios:Async]/media-type` — status: not specified → deprecated

**Why this matters:** Review the new lifecycle status; a status change alone does not remove the path. The conditions for accepting or exposing these nodes changed.

</details>

<a id="module-cisco-ios-xe-aaa"></a>
<details>
<summary>Cisco-IOS-XE-aaa.yang — adds/updates 5 reusable grouping(s)</summary>

**26.2.1 revision note:** removed hidden and cli-ignore-modified from accounting group - removed cli-sequence-commands from accounting network - Added model support for tls version and tls cipher under radius server - Modified the position of MA knobs in radius server-private to be in line with IOS

**Change at a glance:** adds/updates 5 reusable grouping(s).

**Updated groupings:** `config-aaa-grouping`, `config-radius-server-grouping`, `config-radius-server-tls-dtls-common`, `config-tacacs-server-grouping`, `tacacsplus-server-private-grouping`.

</details>

<a id="module-cisco-ios-xe-flow"></a>
<details>
<summary>Cisco-IOS-XE-flow.yang — adds/updates 5 reusable grouping(s)</summary>

**26.2.1 revision note:** Add interface role support for flow monitor interface bind and flow record - Add flow support for Virtual-Template - Added TwoHundredGigE and FourHundredGigE interface support - Add EVE (Encrypted Visibility Engine) fields for unified logging

**Change at a glance:** adds/updates 5 reusable grouping(s).

**Updated groupings:** `flow-default-exporter-grouping`, `flow-exporter-grouping`, `flow-exporter-option-timeout-grouping`, `flow-record-collect-grouping`, `interface-ip-monitor-grouping`.

**Augment delta:** 6 new target(s), 6 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-isis"></a>
<details>
<summary>Cisco-IOS-XE-isis.yang — adds 4 declared schema path(s); adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Obsolete nodes deprecated on or before 17.11 - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds 4 declared schema path(s); adds/updates 1 reusable grouping(s).

**Newly declared schema paths:**
- `/augment[/ios:native/ios:interface/ios:FourHundredGigE/ios:isis]/isis-lan` (container)
- `/augment[/ios:native/ios:interface/ios:FourHundredGigE/ios:isis]/isis-serial` (container)
- `/augment[/ios:native/ios:interface/ios:TwoHundredGigE/ios:isis]/isis-lan` (container)
- `/augment[/ios:native/ios:interface/ios:TwoHundredGigE/ios:isis]/isis-serial` (container)

**Updated groupings:** `isis-flex-grouping`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

**Augment delta:** 8 new target(s), 14 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-multicast"></a>
<details>
<summary>Cisco-IOS-XE-multicast.yang — adds/updates 5 reusable grouping(s)</summary>

**26.2.1 revision note:** Update augmentations to support 200 Gigabit Ethernet and 400 Gigabit Ethernet interfaces - Added new list for IPv4-to-IPv6 service reflect configuration - Added new list for IPv6-to-IPv6 and IPv6-to-IPv4 service reflect configurations - Moved cli-incomplete-command from fec-id leaf to fec list in MLDP configuration - Added a tailf dependency with interface container for register-source config

**Change at a glance:** adds/updates 5 reusable grouping(s).

**New groupings:** `config-ipv4-to-v6-service-reflect-grouping`, `config-ipv6-service-reflect-grouping`, `config-ipv6-service-reflect-list-grouping`, `config-ipv6-to-v4-service-reflect-grouping`.

**Updated groupings:** `config-service-reflect-list-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

**Augment delta:** 6 new target(s), 7 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-wireless-wlan-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-wlan-cfg.yang — adds/updates 5 reusable grouping(s)</summary>

**26.2.1 revision note:** Added GCMP256 cipher support for ft-dot1x, dot1x-sha256 AKMs - Added must constraint to disallow FT Adaptive with FT-dot1X/FT-psk AKMs - Added URWB access capability if radio in URWB mode - Added DHCPv6 configuration support for WLAN policies, including new grouping, container, and validation for DHCPv6 parameters - Obsolete OSEN, CCKM and load balance features - Obsolete ATF feature and related parameters - Added must constraint to restrict 5GHz minimum data rate to 80211a only rates - Removed a `must` constraint from gtk-randomize leaf to allow GTK randomization with WPA3

**Change at a glance:** adds/updates 5 reusable grouping(s).

**New groupings:** `st-dhcpv6-params`, `urwb-access-cfg`.

**Updated groupings:** `st-wlan-policies`, `wlan-data-config-file`, `wlan-profile`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-device-sensor"></a>
<details>
<summary>Cisco-IOS-XE-device-sensor.yang — adds/updates 4 reusable grouping(s)</summary>

**26.2.1 revision note:** Adding must condition for cdp, lldp, dhcp and dhcpv6 filter list - Deprecated insecure tftp-server option for dhcp filter - Adding support for TwoHundredGigE and FourHundredGigE interfaces

**Change at a glance:** adds/updates 4 reusable grouping(s).

**Updated groupings:** `cdp-filter-list-grouping`, `dhcp-filter-list-grouping`, `dhcpv6-filter-list-grouping`, `lldp-filter-list-grouping`.

**Augment delta:** 3 new target(s), 3 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-wireless-rf-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-rf-cfg.yang — updates 2 status value(s); adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Obsoleted ATF feature and related leafs - Added support for DBS minimum and maximum channel widths for RF profile - Deprecated rf-dca-chan-width leaf and disallowed its modification - Enhanced descriptions for RF profile leaves including DCA channels, RSSI thresholds, band-select, trap thresholds, HSR, MCS, and Multi-BSSID profile parameters for improved clarity and consistency - Modified the default values of channel-width-min and channel-width-max - Updated channel-width-max validation to allow band-default minimum channel width with 80 MHz maximum channel width

**Change at a glance:** updates 2 status value(s); adds/updates 2 reusable grouping(s).

**Existing paths with contract changes:**
- `/rf-cfg-data/atf-policies` — status: deprecated → obsolete
- `/rf-cfg-data/atf-policies/atf-policy` — status: deprecated → not specified

**Updated groupings:** `rfprofile`, `rfprofile-default`.

**Why this matters:** Review the new lifecycle status; a status change alone does not remove the path.

</details>

<a id="module-cisco-ios-xe-wireless-wat-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-wat-cfg.yang — adds 2 declared schema path(s); adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for wat-cfg-data container and te-conn-str leaf - Added new WAT profile configuration - Added a 'must' constraint for wat-profile enable leaf to disallow test-wired and test-wireless from being enabled simultaneously

**Change at a glance:** adds 2 declared schema path(s); adds/updates 2 reusable grouping(s).

**Newly declared schema paths:**
- `/wat-cfg-data/wat-profiles` (container)
- `/wat-cfg-data/wat-profiles/wat-profile` (list, key=profile-name)

**New groupings:** `wat-profile`.

**Updated groupings:** `wat-config`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-dhcp"></a>
<details>
<summary>Cisco-IOS-XE-dhcp.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Added snooping leaf under dhcp-snoop-conf container to solve the xpath issue - Added support for Address and VRF option after dhcp-server - Added support for match server mac access-list - Added TwoHundredGigE and FourHundredGigE interface support - Added warnings to url leaf for insecure protocols FTP, HTTP, TFTP, RCP

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `ip-dhcp-grouping`, `ip-dhcp-server-grouping`, `ipv6-dhcp-grouping`.

**Augment delta:** 6 new target(s), 6 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-l2vpn"></a>
<details>
<summary>Cisco-IOS-XE-l2vpn.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Add VPWS SRv6 configure CLI - Separated port channel EVPN segment into platform specific models - Add EVPN subnet slicing - Add telemetry statistics for l2vpn evpn - Fix for context replace issue - Fix l2vpn evpn instance not deleting - Fix l2vpn evpn cedge mode issues - Obsolete ack and keepalive leaves as IOS does not support them - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `config-l2vpn-evpn-instance-sub-cmd`, `config-l2vpn-evpn-main`, `config-l2vpn-grouping`.

**Augment delta:** 4 new target(s), 6 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-policy"></a>
<details>
<summary>Cisco-IOS-XE-policy.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Added FQDN list to log-export destination options - Deprecated table, added a new table with type as string under exceed action set-dscp-transmit - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 3 reusable grouping(s).

**New groupings:** `police-action-table-v2-grouping`.

**Updated groupings:** `config-parameter-map-type-inspect-global-grouping`, `police-exceed-action-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

**Augment delta:** 2 new target(s), 4 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-wireless-rlan-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-rlan-cfg.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated flow monitor ingress and egress for IPv4 and IPv6

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `st-flow-monitor`, `st-rlan-policy-profile-config`, `st-split-tunnel`.

</details>

<a id="module-cisco-ios-xe-acl"></a>
<details>
<summary>Cisco-IOS-XE-acl.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated src-eq, dst-eq for role based acl and added src-eq-list, dst-eq-list, and also for not equal case

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `ipv4-acl-dst-addr-port-grouping`, `ipv4-acl-src-addr-port-grouping`.

</details>

<a id="module-cisco-ios-xe-cdp"></a>
<details>
<summary>Cisco-IOS-XE-cdp.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added all missing TLV options for cdp tlv-list configuration - Added global cdp log mismatch duplex - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 2 reusable grouping(s).

**New groupings:** `config-cdp-log-mismatch-duplex-grouping`.

**Updated groupings:** `config-cdp-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-mobileip"></a>
<details>
<summary>Cisco-IOS-XE-mobileip.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecating container key under auth-option grouping

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `auth-key-options-grouping`, `auth-option-grouping`.

</details>

<a id="module-cisco-ios-xe-ncch-cfg"></a>
<details>
<summary>Cisco-IOS-XE-ncch-cfg.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated description of NETCONF Call Home local VRF leaf to clarify its meaning. - Made several changes to the remote peer address type choice model element by removing defaults and making leaves mandatory.

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `ncch-client-endpoint-cnfg`, `ncch-ssh`.

</details>

<a id="module-cisco-ios-xe-ospf"></a>
<details>
<summary>Cisco-IOS-XE-ospf.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated Must constraint for ip ospf interface config to validate ip VRF - Added support for TwoHundredGigE and FourHundredGigE interface

**Change at a glance:** adds/updates 2 reusable grouping(s); adds 2 `must` refinements for newer interface types.

**Updated groupings:** `config-ospf-interface-process-id-igrouping`, `config-ospf-passive-interface-grouping`.

**Refine constraints:** added the existing passive-interface `must` rule for `TwoHundredGigE/name` and `FourHundredGigE/name`; see the two dedicated rows in the grouping-delta CSV.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-spanning-tree"></a>
<details>
<summary>Cisco-IOS-XE-spanning-tree.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added global bridge mac leaf under spanning-tree bridge container - Added new mst instance list with tailf:cli-delete-when-empty to support deletion of individual cost or port-priority parameters - Changed instance type from string to unsigned integer with range 1..4094 for proper validation - Added must statement for port-priority to enforce increments of 16 - Deprecated old mst instance list to maintain backward compatibility - Added support for spanning-tree mst simulate pvst [disable] - Added support for spanning-tree sso block-tcn - Added support for spanning-tree queue maxsize

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `config-interface-spanning-tree`, `config-spanning-tree-grouping`.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-track"></a>
<details>
<summary>Cisco-IOS-XE-track.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** added interface virtual router redundancy protocol - added interface cloud-tracker support - added a constraint to ensure object is configurable only when track type is list

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `config-track-grouping`, `track-grouping`.

</details>

<a id="module-cisco-ios-xe-utd"></a>
<details>
<summary>Cisco-IOS-XE-utd.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated host length - Add refresh-token authentication - Add tailf:cli-preformatted annotation to password, refresh-token, and api-key to fix Type6 password backslash handling - Added support for TwoHundredGigE and FourHundredGigE interfaces

**Change at a glance:** adds/updates 2 reusable grouping(s).

**New groupings:** `refresh-token-grouping`.

**Updated groupings:** `utd-engine-standard-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-voice"></a>
<details>
<summary>Cisco-IOS-XE-voice.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added deprecated status and warning to wsapi container in UC configuration - Added warning for insecure protocols in play message leaf under call treatment - Added deprecated status and warning to ftp container in gw-accounting - Added warning for insecure protocols in voice class e164-pattern-map URL

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `config-uc-grouping`, `gw-accounting-primary-secondary-grouping`.

</details>

<a id="module-cisco-ios-xe-wireless-ap-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-ap-cfg.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added WAT Profile name to static AP and AP filter configuration

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `ap-tag`, `st-ap-filter-config`.

</details>

<a id="module-cisco-ios-xe-wireless-dot11-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-dot11-cfg.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `dot11-80211-qos-pm-config`, `spectrum-cfg`.

</details>

<a id="module-cisco-ios-xe-wireless-site-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-site-cfg.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added IDR Tetragon configuration - Added WAT Profile name to Site Tag configuration

**Change at a glance:** adds/updates 2 reusable grouping(s).

**Updated groupings:** `ap-cfg-profile`, `site-tag-config`.

</details>

<a id="module-cisco-ios-xe-wireless-urwb-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-urwb-cfg.yang — adds/updates 2 reusable grouping(s)</summary>

**26.2.1 revision note:** Added URWB Ethernet configuration leaves - Added RADIUS server group configuration for URWB profile - Added URWB NAT configuration support - Updated descriptions for URWB profile configuration leaves and containers - Updated URWB passphrase constraint to allow special characters only for AES encrypted network keys - Updated RADIUS server group must constraint to allow unconfigured state - Added maximum elements constraint for URWB NAT rule list

**Change at a glance:** adds/updates 2 reusable grouping(s).

**New groupings:** `st-urwb-nat-rule-list`.

**Updated groupings:** `urwb-profile`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-yang-interfaces-cfg"></a>
<details>
<summary>Cisco-IOS-XE-yang-interfaces-cfg.yang — updates 1 <code>must</code> constraint(s); adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Refined existing leaf descriptions for clarity and consistency - Added aes128-gcm@openssh.com to Device Management Interface SSH cipher algorithms - Disabled diffie-hellman-group14-sha1 key exchange algorithm in FIPS mode

**Change at a glance:** updates 1 `must` constraint(s); adds/updates 1 reusable grouping(s).

**Existing paths with contract changes:**
- `/yang-interfaces-cfg-data/ssh-server` — must: not((../ssh-server/kex-alg/dh-group14-sha1 = 'false') and (../ssh-server/kex-alg/dh-group14-sha256 = 'false') and (../ssh-server/kex-alg/ecdh-sha2-nistp256 = 'false') and (../ssh-server/kex-alg/ecdh-sha2-nistp384 = 'false') and (../ssh-server/kex-alg/ecdh-sha2-nistp521 = 'false') and (../ssh-server/kex-alg/dh-group16-sha512 = 'false')), not((../ssh-server/macs/hmac-sha2-256 = 'false') and (../ssh-server/macs/hmac-sha2-512 = 'false') and (../ssh-server/macs/hmac-sha1 = 'false')), not((../ssh-server/ciphers/aes128-ctr = 'false') and (../ssh-server/ciphers/aes192-ctr = 'false') and (../ssh-server/ciphers/aes256-ctr = 'false') and (../ssh-server/ciphers/aes128-cbc = 'false') and (../ssh-server/ciphers/aes256-cbc = 'false')), not((../ssh-server/hostkey-alg/rsa-sha2-256 = 'false') and (../ssh-server/hostkey-alg/rsa-sha2-512 = 'false')) → not((../ssh-server/kex-alg/dh-group14-sha256 = 'false') and (../ssh-server/kex-alg/ecdh-sha2-nistp256 = 'false') and (../ssh-server/kex-alg/ecdh-sha2-nistp384 = 'false') and (../ssh-server/kex-alg/ecdh-sha2-nistp521 = 'false') and (../ssh-server/kex-alg/dh-group16-sha512 = 'false')), not((../ssh-server/macs/hmac-sha2-256 = 'false') and (../ssh-server/macs/hmac-sha2-512 = 'false') and (../ssh-server/macs/hmac-sha1 = 'false')), not((../ssh-server/ciphers/aes128-ctr = 'false') and (../ssh-server/ciphers/aes192-ctr = 'false') and (../ssh-server/ciphers/aes256-ctr = 'false') and (../ssh-server/ciphers/aes128-cbc = 'false') and (../ssh-server/ciphers/aes256-cbc = 'false') and (../ssh-server/ciphers/aes128-gcm = 'false')), not((../ssh-server/hostkey-alg/rsa-sha2-256 = 'false') and (../ssh-server/hostkey-alg/rsa-sha2-512 = 'false'))

**Updated groupings:** `dmi-ssh-cipher-algorithms`.

**Why this matters:** The conditions for accepting or exposing these nodes changed.

</details>

<a id="module-cisco-ios-xe-cip"></a>
<details>
<summary>Cisco-IOS-XE-cip.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added encryption (type 8) support for password - Marked insecure password leaf as deprecated

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-global-cip-grouping`.

</details>

<a id="module-cisco-ios-xe-controller"></a>
<details>
<summary>Cisco-IOS-XE-controller.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated container 'udp' and added new list 'udp-stream' to support multiple NMEA streams - Added require-instance false to data-profile and attach-profile leafrefs to prevent an illegal access error when the profile instance does not exist

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-controller-grouping`.

</details>

<a id="module-cisco-ios-xe-ctrl-mng-cfg"></a>
<details>
<summary>Cisco-IOS-XE-ctrl-mng-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Improved descriptions for control management configuration leaves

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `ctrl-mng-config`.

</details>

<a id="module-cisco-ios-xe-cts"></a>
<details>
<summary>Cisco-IOS-XE-cts.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added model support sxp delete-hold-down

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-cts-grouping`.

</details>

<a id="module-cisco-ios-xe-ethernet"></a>
<details>
<summary>Cisco-IOS-XE-ethernet.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Consolidate modeling for interface pagp - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 1 reusable grouping(s).

**New groupings:** `config-interface-ethernet-member-link-pagp-grouping`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

**Augment delta:** 2 new target(s), 26 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-gnmi-cfg"></a>
<details>
<summary>Cisco-IOS-XE-gnmi-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Improve description of top level configuration and server containers - Deprecated insecure gNxI server enable leaf and port leaf

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `gnmi-config`.

</details>

<a id="module-cisco-ios-xe-gnss"></a>
<details>
<summary>Cisco-IOS-XE-gnss.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added shutdown leaf to enable or disable GNSS module

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-gnss-grouping`.

</details>

<a id="module-cisco-ios-xe-grpc-tunnel-cfg"></a>
<details>
<summary>Cisco-IOS-XE-grpc-tunnel-cfg.yang — adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Improve the description of address host type unspecified leaf - Deprecated insecure gNxI gRPC tunnel target type

**Change at a glance:** adds/updates 1 reusable type(s).

**Updated typedefs:** `grpctunnel-target-type`.

</details>

<a id="module-cisco-ios-xe-http"></a>
<details>
<summary>Cisco-IOS-XE-http.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added support for 'ip http secure-ecdhe-curve' - Updated Max range for 'ip http session-idle-timeout' - Added yang model for 'ip http secure-pqc-type' CLI - Updated ip http server to be set as disabled by default - Updated default value for 'ip http secure-server'

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-ip-http-grouping`.

</details>

<a id="module-cisco-ios-xe-lisp"></a>
<details>
<summary>Cisco-IOS-XE-lisp.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added support for silent-host pre-auth VLAN CLIs under interface <SVI> - Added support for FiftyGigabitEthernet,TwoHundredGigE and FourHundredGigE interfaces

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-interface-lisp-grouping`.

**Augment delta:** 6 new target(s), 6 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-lte450"></a>
<details>
<summary>Cisco-IOS-XE-lte450.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Adding password

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-interface-lte450-grouping`.

</details>

<a id="module-cisco-ios-xe-mrp"></a>
<details>
<summary>Cisco-IOS-XE-mrp.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated 'enable' leaf and added new container 'profinet-enable' with leaf 'profinet' of type boolean - Added tailf cli extensions for profinet container - Changed mrp leaf default to false

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-profinet-grouping`.

</details>

<a id="module-cisco-ios-xe-mvrp"></a>
<details>
<summary>Cisco-IOS-XE-mvrp.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated timer containers (join, leave, leave-all) with presence statements - Added new timer leaf nodes without presence (join-timer, leave-timer, leave-all-timer)

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-interface-mvrp-grouping`.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-nat"></a>
<details>
<summary>Cisco-IOS-XE-nat.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added tailf:cli-preformatted annotation to password, username, key, and URL leafs under NAT64 address-resolution-server, api-key, and rule-server containers to fix Type6 password backslash handling - Added TwoHundredGigE and FourHundredGigE interface support - Added VRF create/delete ordering for ip nat inside source list/route-map interface VRF mappings

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-nat64-grouping`.

**Augment delta:** 4 new target(s), 6 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-nbar"></a>
<details>
<summary>Cisco-IOS-XE-nbar.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Add delete ordering dependency between custom protocol and class-map match protocol - Add authentication-token (max 4096 chars) to sd-service controller - Add enforce-tls-hostname to sd-service controller - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-avc-grouping`.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-ntp"></a>
<details>
<summary>Cisco-IOS-XE-ntp.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Modified ntp allow mode control to be disabled by default - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-ntp-grouping`.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-ospfv3"></a>
<details>
<summary>Cisco-IOS-XE-ospfv3.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Made the must constraint in config-interface-ospfv3-grouping stricter to verify address-family with VRF is configured. - Added support for TwoHundredGigE and FourHundredGigE interfaces

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-interface-ospfv3-grouping`.

**Augment delta:** 4 new target(s), 4 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-platform"></a>
<details>
<summary>Cisco-IOS-XE-platform.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Add platform ip reassembly warning - Add platform ip reassembly threshold - Add platform security audit monitor rule sets

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-platform-grouping`.

</details>

<a id="module-cisco-ios-xe-power"></a>
<details>
<summary>Cisco-IOS-XE-power.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added model support for 2-event - Removed presence for power inline - Added FiftyGigabitEthernet, TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-power-grouping`.

**Augment delta:** 3 new target(s), 3 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-prp"></a>
<details>
<summary>Cisco-IOS-XE-prp.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added logging-interval CLI

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-prp-grouping`.

</details>

<a id="module-cisco-ios-xe-site-manager"></a>
<details>
<summary>Cisco-IOS-XE-site-manager.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Add tailf:cli-preformatted annotation to site-manager password

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-password`.

</details>

<a id="module-cisco-ios-xe-snmp"></a>
<details>
<summary>Cisco-IOS-XE-snmp.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added model for vrf under snmp-server - Added warning message for insecure protocols under file-transfer - Added tailf:cli-ignore-modified for sdwan traps obsolete nodes - Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-snmp-server-grouping`.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-synce"></a>
<details>
<summary>Cisco-IOS-XE-synce.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added model support for 1hz signal type

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-synce-grouping`.

</details>

<a id="module-cisco-ios-xe-template"></a>
<details>
<summary>Cisco-IOS-XE-template.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated bpduguard container and added bpduguard-v2 for spanning-tree container

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `template-grouping`.

</details>

<a id="module-cisco-ios-xe-vlan"></a>
<details>
<summary>Cisco-IOS-XE-vlan.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added EVPN subnet slicing and host routing features

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-interface-vlan-grouping`.

</details>

<a id="module-cisco-ios-xe-wccp"></a>
<details>
<summary>Cisco-IOS-XE-wccp.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `ip-wccp-group-address-grouping`.

**Augment delta:** 2 new target(s), 2 added uses reference(s). Full target paths and grouping names are in the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv).

</details>

<a id="module-cisco-ios-xe-wireless-cts-sxp-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-cts-sxp-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `cts-sxp-config-profile`.

</details>

<a id="module-cisco-ios-xe-wireless-general-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-general-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated the default value of derive-geolocation leaf from 'false' to 'true' - Updated descriptions for several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `st-ap-loc-ranging-cfg`.

</details>

<a id="module-cisco-ios-xe-wireless-mesh-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-mesh-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `st-mesh-profile`.

</details>

<a id="module-cisco-ios-xe-wireless-mstream-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-mstream-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Modified end IP address constraint

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `mstreamgrp`.

</details>

<a id="module-cisco-ios-xe-wireless-rogue-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-rogue-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `rogue-global`.

</details>

<a id="module-cisco-ios-xe-wireless-rrm-cfg"></a>
<details>
<summary>Cisco-IOS-XE-wireless-rrm-cfg.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated chan-width-cap leaf and disallowed its modification

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `rrm-rrm-config`.

</details>

<a id="module-cisco-ios-xe-wsma"></a>
<details>
<summary>Cisco-IOS-XE-wsma.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Deprecated insecure transport options for WSMA listener

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `config-wsma-grouping`.

</details>

<a id="module-cisco-ios-xe-bfd"></a>
<details>
<summary>Cisco-IOS-XE-bfd.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:bfd</code>, <code>ios:TwoHundredGigE/ios:bfd</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-dot1x"></a>
<details>
<summary>Cisco-IOS-XE-dot1x.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-eigrp"></a>
<details>
<summary>Cisco-IOS-XE-eigrp.yang — adds 6 augment target(s) and 6 reused grouping reference(s)</summary>

**Change at a glance:** 6 new top-level augment target(s) and 6 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ip</code>, <code>ios:ip/ios:summary-address</code>, <code>ios:FourHundredGigE/ios:ipv6</code> (+3 more).

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-eta"></a>
<details>
<summary>Cisco-IOS-XE-eta.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-group-policy"></a>
<details>
<summary>Cisco-IOS-XE-group-policy.yang — adds 3 augment target(s) and 3 reused grouping reference(s)</summary>

**Change at a glance:** 3 new top-level augment target(s) and 3 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FiftyGigabitEthernet</code>, <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-icmp"></a>
<details>
<summary>Cisco-IOS-XE-icmp.yang — adds 4 augment target(s) and 4 reused grouping reference(s)</summary>

**Change at a glance:** 4 new top-level augment target(s) and 4 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ip</code>, <code>ios:FourHundredGigE/ios:ipv6</code>, <code>ios:TwoHundredGigE/ios:ip</code> (+1 more).

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-igmp"></a>
<details>
<summary>Cisco-IOS-XE-igmp.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ip</code>, <code>ios:TwoHundredGigE/ios:ip</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-isg"></a>
<details>
<summary>Cisco-IOS-XE-isg.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ip</code>, <code>ios:TwoHundredGigE/ios:ip</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-lldp"></a>
<details>
<summary>Cisco-IOS-XE-lldp.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-loop-detect"></a>
<details>
<summary>Cisco-IOS-XE-loop-detect.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-mdns-gateway"></a>
<details>
<summary>Cisco-IOS-XE-mdns-gateway.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-mka"></a>
<details>
<summary>Cisco-IOS-XE-mka.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-mld"></a>
<details>
<summary>Cisco-IOS-XE-mld.yang — adds 3 augment target(s) and 3 reused grouping reference(s)</summary>

**Change at a glance:** 3 new top-level augment target(s) and 3 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ipv6</code>, <code>ios:TwoHundredGigE/ios:ipv6</code>, <code>ios:Vif/ios:ipv6</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-mpls"></a>
<details>
<summary>Cisco-IOS-XE-mpls.yang — adds 3 augment target(s) and 3 reused grouping reference(s)</summary>

**Change at a glance:** 3 new top-level augment target(s) and 3 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FiftyGigabitEthernet/ios:mpls</code>, <code>ios:FourHundredGigE/ios:mpls</code>, <code>ios:TwoHundredGigE/ios:mpls</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-nd"></a>
<details>
<summary>Cisco-IOS-XE-nd.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ipv6/ios:nd</code>, <code>ios:TwoHundredGigE/ios:ipv6/ios:nd</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-pnp"></a>
<details>
<summary>Cisco-IOS-XE-pnp.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-ptp"></a>
<details>
<summary>Cisco-IOS-XE-ptp.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-rip"></a>
<details>
<summary>Cisco-IOS-XE-rip.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ipv6</code>, <code>ios:TwoHundredGigE/ios:ipv6</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-rsvp"></a>
<details>
<summary>Cisco-IOS-XE-rsvp.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:FourHundredGigE/ios:ip</code>, <code>ios:TwoHundredGigE/ios:ip</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-sanet"></a>
<details>
<summary>Cisco-IOS-XE-sanet.yang — adds 4 augment target(s) and 6 reused grouping reference(s)</summary>

**Change at a glance:** 4 new top-level augment target(s) and 6 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:FourHundredGigE/ios:access-session</code>, <code>ios:interface/ios:TwoHundredGigE</code> (+1 more).

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-udld"></a>
<details>
<summary>Cisco-IOS-XE-udld.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-umbrella"></a>
<details>
<summary>Cisco-IOS-XE-umbrella.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-vrrp"></a>
<details>
<summary>Cisco-IOS-XE-vrrp.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

<a id="module-cisco-ios-xe-vtp"></a>
<details>
<summary>Cisco-IOS-XE-vtp.yang — adds 2 augment target(s) and 2 reused grouping reference(s)</summary>

**Change at a glance:** 2 new top-level augment target(s) and 2 added uses reference(s) attach existing definitions at new schema locations. The resulting nodes have not been expanded here.

**Target examples:** <code>ios:interface/ios:FourHundredGigE</code>, <code>ios:interface/ios:TwoHundredGigE</code>.

**Detail:** filter the [augment-delta CSV](2621-YANG-Model-Augment-Deltas.csv) by this filename for full target paths and grouping names. Platform features and deviations may further affect the schema.

</details>

</details>

<a id="tracked-other"></a>

### Other (26 source entries)

<details>
<summary>Show 26 Other entries</summary>

**Module index:**

- [Cisco-IOS-XE-cdp-deviation.yang](#module-cisco-ios-xe-cdp-deviation) · [Cisco-IOS-XE-controller-shdsl-common.yang](#module-cisco-ios-xe-controller-shdsl-common) · [Cisco-IOS-XE-device-tracking-cat9k-deviation.yang](#module-cisco-ios-xe-device-tracking-cat9k-deviation)
- [Cisco-IOS-XE-dhcp-deviation.yang](#module-cisco-ios-xe-dhcp-deviation) · [Cisco-IOS-XE-ethernet-radium-deviation.yang](#module-cisco-ios-xe-ethernet-radium-deviation) · [Cisco-IOS-XE-features.yang](#module-cisco-ios-xe-features)
- [Cisco-IOS-XE-install-event-types.yang](#module-cisco-ios-xe-install-event-types) · [Cisco-IOS-XE-interface-common.yang](#module-cisco-ios-xe-interface-common) · [Cisco-IOS-XE-interfaces-deviation.yang](#module-cisco-ios-xe-interfaces-deviation)
- [Cisco-IOS-XE-mdt-common-defs.yang](#module-cisco-ios-xe-mdt-common-defs) · [Cisco-IOS-XE-ngfw-events.yang](#module-cisco-ios-xe-ngfw-events) · [Cisco-IOS-XE-nwpi-types.yang](#module-cisco-ios-xe-nwpi-types)
- [Cisco-IOS-XE-ospf-deviation.yang](#module-cisco-ios-xe-ospf-deviation) · [Cisco-IOS-XE-port-channel-deviation.yang](#module-cisco-ios-xe-port-channel-deviation) · [Cisco-IOS-XE-port-channel-unsupported-deviation.yang](#module-cisco-ios-xe-port-channel-unsupported-deviation)
- [Cisco-IOS-XE-switch-deviation.yang](#module-cisco-ios-xe-switch-deviation) · [Cisco-IOS-XE-system-security-types.yang](#module-cisco-ios-xe-system-security-types) · [Cisco-IOS-XE-utd-events.yang](#module-cisco-ios-xe-utd-events)
- [Cisco-IOS-XE-wireless-afc-types.yang](#module-cisco-ios-xe-wireless-afc-types) · [Cisco-IOS-XE-wireless-ap-types.yang](#module-cisco-ios-xe-wireless-ap-types) · [Cisco-IOS-XE-wireless-client-types.yang](#module-cisco-ios-xe-wireless-client-types)
- [Cisco-IOS-XE-wireless-enum-types.yang](#module-cisco-ios-xe-wireless-enum-types) · [Cisco-IOS-XE-wireless-mobility-types.yang](#module-cisco-ios-xe-wireless-mobility-types) · [Cisco-IOS-XE-wireless-types.yang](#module-cisco-ios-xe-wireless-types)
- [Cisco-IOS-XE-wireless-urwb-common-types.yang](#module-cisco-ios-xe-wireless-urwb-common-types) · [Cisco-IOS-XE-xcopy-events.yang](#module-cisco-ios-xe-xcopy-events)


<a id="module-cisco-ios-xe-interfaces-deviation"></a>
<details>
<summary>Cisco-IOS-XE-interfaces-deviation.yang — adds 43 platform deviation(s)</summary>

**26.2.1 revision note:** Added interface deviations for ip-forward feature

**Change at a glance:** adds 43 platform deviation(s).

**New deviations:** `/ios:native/ios:interface/ios:ATM-subinterface/ios:ATM/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:ATM/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:AppGigabitEthernet/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:AppNav-Compress/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:AppNav-UnCompress/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:Async/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:BD-VIF/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:BDI/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:Bundle/ios:ip/ios:address-choice/ios:forward/ios:forward`, `/ios:native/ios:interface/ios:Cellular/ios:ip/ios:address-choice/ios:forward/ios:forward` (+33 more).

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-ngfw-events"></a>
<details>
<summary>Cisco-IOS-XE-ngfw-events.yang — adds 4 declared schema path(s); adds/updates 4 reusable grouping(s); adds/updates 5 reusable type(s)</summary>

**26.2.1 revision note:** Added NGFW IPS alert notifications. - Added NGFW version notification. - Added NGFW update notification - Added NGFW FQDN destination status change alarm notification.

**Change at a glance:** adds 4 declared schema path(s); adds/updates 4 reusable grouping(s); adds/updates 5 reusable type(s).

**Notifications in this module:** 1 → 5.

**New groupings:** `hsl-fqdn-dst-status-change`, `ngfw-ips-alert`, `ngfw-update`, `ngfw-ver-notif`.

**New typedefs:** `fqdn-destination-error-reason`, `fqdn-destination-state`, `ngfw-ips-alert-action-val`, `ngfw-ips-alert-classification-val`, `ngfw-ips-alert-priority-val`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-port-channel-unsupported-deviation"></a>
<details>
<summary>Cisco-IOS-XE-port-channel-unsupported-deviation.yang — adds 6 platform deviation(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds 6 platform deviation(s).

**New deviations:** `/ios:native/ios:interface/ios:FourHundredGigE/ios-eth:channel-group/ios-eth:auto`, `/ios:native/ios:interface/ios:FourHundredGigE/ios-eth:channel-group/ios-eth:non-silent`, `/ios:native/ios:interface/ios:HundredGigE/ios-eth:channel-group/ios-eth:auto`, `/ios:native/ios:interface/ios:HundredGigE/ios-eth:channel-group/ios-eth:non-silent`, `/ios:native/ios:interface/ios:TwoHundredGigE/ios-eth:channel-group/ios-eth:auto`, `/ios:native/ios:interface/ios:TwoHundredGigE/ios-eth:channel-group/ios-eth:non-silent`.

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-wireless-ap-types"></a>
<details>
<summary>Cisco-IOS-XE-wireless-ap-types.yang — adds/updates 5 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added support for AP auto-MACsec configuration - Added IDR Tetragon configuration - Added NTP trust-key length validation constraints - Added new AP Filter Type for Wireless Active Testing (WAT) - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 5 reusable grouping(s); adds/updates 1 reusable type(s).

**New groupings:** `st-tetragon-config`.

**Updated groupings:** `st-ap-macsec`, `st-dot1x-eap-auth-info`, `st-hyperlocation`, `st-ntp-server-info-cfg`.

**Updated typedefs:** `enm-ap-filter-type`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-wireless-enum-types"></a>
<details>
<summary>Cisco-IOS-XE-wireless-enum-types.yang — adds/updates 6 reusable type(s)</summary>

**26.2.1 revision note:** Added URWB egress point enumerated type - Added enumeration for Wireless Active Testing (WAT) VLAN source - Added enumeration for URWB NAT protocol types (TCP/UDP)

**Change at a glance:** adds/updates 6 reusable type(s).

**New typedefs:** `ble-ltx-scan-disc-mode`, `ble-ltx-scan-mode`, `ble-ltx-scan-phy`, `urwb-egress-point`, `urwb-nat-protocol`, `wat-vlan-src`.

</details>

<a id="module-cisco-ios-xe-wireless-urwb-common-types"></a>
<details>
<summary>Cisco-IOS-XE-wireless-urwb-common-types.yang — adds/updates 6 reusable grouping(s)</summary>

**26.2.1 revision note:** Added URWB LAN ID Ethernet configuration leaf - Added URWB LAN PoE Ethernet configuration leaf - Added URWB traffic egress point leaf - Moved URWB NAT configuration grouping from cfg module to common types - Added URWB NAT rule key grouping - Updated descriptions for URWB mobility and MPLS leaves - Updated descriptions for chan and c-width leaves in st-urwb-chan-list-entry grouping - Updated descriptions of several model elements for clarity, grammar, and consistency

**Change at a glance:** adds/updates 6 reusable grouping(s).

**New groupings:** `st-urwb-eth`, `st-urwb-nat`, `st-urwb-nat-rule-key`.

**Updated groupings:** `st-urwb-chan-list-entry`, `st-urwb-mob`, `st-urwb-mpls`.

**Why this matters:** New reusable groupings can change the schema of modules that use them; inspect their consumers to see the resulting paths.

</details>

<a id="module-cisco-ios-xe-system-security-types"></a>
<details>
<summary>Cisco-IOS-XE-system-security-types.yang — adds/updates 5 reusable type(s)</summary>

**26.2.1 revision note:** Added an enumeration value for TFTP server configuration command - Added enum for Tool Command Line module. - Added reason, remedy and description enums for Tool Command Language and Logging. - Added description enums for Parser module. - Added reason, remedy and description enums for SNMP File transfer. - Added enum value for Device Sensor module. - Added submode enum value for Device Sensor DHCP filter list configuration. - Added an enumeration for SSH EC weak host key - Added reason, remedy, description, and submode enums for AAA weak password/key - Added description enum for boot system insecure file transfer protocol - Added module enum for IFS module - Added module enum for Crypto PKI Trustpoint module - Added description enum for Crypto PKI insecure file transfer protocol - Added submode enum for crypto-ca-trustpoint - Added dedicated remedy enum for generic secure protocol usage - Added module enum for DHCP snooping module - Added enum for DHCP module - Added remedy and description enums for DHCP - Added module enums for voice configuration contexts - Added remedy enum for insecure real-time streaming transport usage - Added description enums for insecure voice URL and transport configurations - Added submode enums for voice configuration contexts - Added reason, remediation and description enums for service password-encryption. - Added module enum for macro command and description enum for macro auto execute CLI. - Added reason, remedy, and description enums for RADIUS Message Authenticator warnings - Added description enums for RADIUS, TACACS, and LDAP without TLS warnings - Added description enum for Tool Command Language encoding directory - Added reason for SNMP group and remediation for SNMP group and cipher AES - Added module enums for IVR, gateway accounting, call leg, application monitor, and web service - Added description enums for IVR voice prompts, gateway accounting, call leg, event log, and web service configurations - Added submode enums for gateway accounting and application monitor configurations - Added reason, remedy and description enums for NTP allow mode control - Added description enum for NTP without authentication - Added module, description, and submode enums for IP SLA insecure protocol - Added submode enums for IP SLA LSR path echo and jitter configuration - Added module, reason, remediation and description enums for the insecure gNxI server - Updated SNMP no ACL reason and remedy descriptions - Added module and description enums for Crimson Function Tracking (CRFT) collect-on-reload insecure protocol

**Change at a glance:** adds/updates 5 reusable type(s).

**Updated typedefs:** `insec-conf-desc`, `insec-conf-module`, `insec-conf-reason`, `insec-conf-remedy`, `insec-conf-submode`.

</details>

<a id="module-cisco-ios-xe-ospf-deviation"></a>
<details>
<summary>Cisco-IOS-XE-ospf-deviation.yang — adds 4 platform deviation(s)</summary>

**26.2.1 revision note:** Adding deviation for the TwoHundredGigE and FourHundredGigE interfaces

**Change at a glance:** adds 4 platform deviation(s).

**New deviations:** `/ios:native/ios:router/ios-ospf:router-ospf/ios-ospf:ospf/ios-ospf:process-id/ios-ospf:passive-interface-config/ios-ospf:disable-interface/ios-ospf:FourHundredGigE/ios-ospf:name`, `/ios:native/ios:router/ios-ospf:router-ospf/ios-ospf:ospf/ios-ospf:process-id/ios-ospf:passive-interface-config/ios-ospf:disable-interface/ios-ospf:TwoHundredGigE/ios-ospf:name`, `/ios:native/ios:router/ios-ospf:router-ospf/ios-ospf:ospf/ios-ospf:process-id/ios-ospf:passive-interface-config/ios-ospf:enable-interface/ios-ospf:FourHundredGigE/ios-ospf:name`, `/ios:native/ios:router/ios-ospf:router-ospf/ios-ospf:ospf/ios-ospf:process-id/ios-ospf:passive-interface-config/ios-ospf:enable-interface/ios-ospf:TwoHundredGigE/ios-ospf:name`.

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-utd-events"></a>
<details>
<summary>Cisco-IOS-XE-utd-events.yang — adds 1 declared schema path(s); adds/updates 1 reusable grouping(s); adds/updates 2 reusable type(s)</summary>

**26.2.1 revision note:** Added UTD FQDN destination status change alarm notification.

**Change at a glance:** adds 1 declared schema path(s); adds/updates 1 reusable grouping(s); adds/updates 2 reusable type(s).

**Notifications in this module:** 1 → 2.

**New groupings:** `utd-log-fqdn-dst-status-change`.

**New typedefs:** `fqdn-destination-error-reason`, `fqdn-destination-state`.

**Why this matters:** The module now declares additional data paths; check device and platform support before relying on them.

</details>

<a id="module-cisco-ios-xe-wireless-afc-types"></a>
<details>
<summary>Cisco-IOS-XE-wireless-afc-types.yang — adds/updates 4 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions for clarity and accuracy

**Change at a glance:** adds/updates 4 reusable grouping(s).

**Updated groupings:** `afc-chan-resp`, `afc-ellipse`, `afc-point`, `afc-request-data`.

</details>

<a id="module-cisco-ios-xe-interface-common"></a>
<details>
<summary>Cisco-IOS-XE-interface-common.yang — adds/updates 3 reusable grouping(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds/updates 3 reusable grouping(s).

**Updated groupings:** `interface-deprecated-grouping`, `interface-grouping`, `interface-grouping-list`.

</details>

<a id="module-cisco-ios-xe-port-channel-deviation"></a>
<details>
<summary>Cisco-IOS-XE-port-channel-deviation.yang — adds 3 platform deviation(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds 3 platform deviation(s).

**New deviations:** `/ios:native/ios:interface/ios:FourHundredGigE/ios-eth:channel-group/ios-eth:number`, `/ios:native/ios:interface/ios:HundredGigE/ios-eth:channel-group/ios-eth:number`, `/ios:native/ios:interface/ios:TwoHundredGigE/ios-eth:channel-group/ios-eth:number`.

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-wireless-types"></a>
<details>
<summary>Cisco-IOS-XE-wireless-types.yang — adds/updates 1 reusable grouping(s); adds/updates 2 reusable type(s)</summary>

**26.2.1 revision note:** Added new AP reboot reason enumerations - Added default value for AP proxy configuration password type leaf - Added new band-default enumeration value to dca-ewlc-chan-width-cap typedef - Added the validation for hostname and no-proxy-list - Modified hostname regex pattern to support HTTP and HTTPS - Modified description for the dca-ewlc-chan-width-cap-band-default enum

**Change at a glance:** adds/updates 1 reusable grouping(s); adds/updates 2 reusable type(s).

**Updated groupings:** `st-ap-proxy-cfg`.

**Updated typedefs:** `dca-ewlc-chan-width-cap`, `spam-ap-reboot-reason`.

</details>

<a id="module-cisco-ios-xe-cdp-deviation"></a>
<details>
<summary>Cisco-IOS-XE-cdp-deviation.yang — adds 2 platform deviation(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds 2 platform deviation(s).

**New deviations:** `/ios:native/ios:interface/ios:FourHundredGigE/ios-cdp:cdp/ios-cdp:enable`, `/ios:native/ios:interface/ios:TwoHundredGigE/ios-cdp:cdp/ios-cdp:enable`.

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-device-tracking-cat9k-deviation"></a>
<details>
<summary>Cisco-IOS-XE-device-tracking-cat9k-deviation.yang — adds 2 platform deviation(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds 2 platform deviation(s).

**New deviations:** `/ios:native/ios:interface/ios:FourHundredGigE/ios-sw:device-tracking`, `/ios:native/ios:interface/ios:TwoHundredGigE/ios-sw:device-tracking`.

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-dhcp-deviation"></a>
<details>
<summary>Cisco-IOS-XE-dhcp-deviation.yang — adds 2 platform deviation(s)</summary>

**26.2.1 revision note:** Added TwoHundredGigE and FourHundredGigE interface support

**Change at a glance:** adds 2 platform deviation(s).

**New deviations:** `/ios:native/ios:interface/ios:FourHundredGigE/ios:ip/ios:dhcp/ios-dhcp:snooping`, `/ios:native/ios:interface/ios:TwoHundredGigE/ios:ip/ios:dhcp/ios-dhcp:snooping`.

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-features"></a>
<details>
<summary>Cisco-IOS-XE-features.yang — YANG schema declarations changed</summary>

**26.2.1 revision note:** Added feature ip-forward

**Change at a glance:** YANG schema declarations changed..

**New features:** `ip-forward`, `rs232-feature`.

</details>

<a id="module-cisco-ios-xe-mdt-common-defs"></a>
<details>
<summary>Cisco-IOS-XE-mdt-common-defs.yang — adds/updates 1 reusable grouping(s); adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added support for sensor group type filter - Removed defaults for no-synch-on-start-v2 and dampening-period - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s); adds/updates 1 reusable type(s).

**Updated groupings:** `mdt-subscription-base`.

**Updated typedefs:** `mdt-sub-filter-type`.

</details>

<a id="module-cisco-ios-xe-switch-deviation"></a>
<details>
<summary>Cisco-IOS-XE-switch-deviation.yang — YANG schema declarations changed</summary>

**26.2.1 revision note:** Update version for igmp to <1-3>

**Change at a glance:** YANG schema declarations changed..

**Updated deviations:** `/ios:native/ios-sw:device/ios-sw:classifier-with-condition/ios-sw:classifier/ios-sw:condition`, `/ios:native/ios-sw:device/ios-sw:classifier-with-condition/ios-sw:classifier/ios-sw:device-type`.

</details>

<a id="module-cisco-ios-xe-wireless-client-types"></a>
<details>
<summary>Cisco-IOS-XE-wireless-client-types.yang — adds/updates 2 reusable type(s)</summary>

**26.2.1 revision note:** Added new enum value Zebra to sta-type - Added new wired client connected through URWB backhaul - Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 2 reusable type(s).

**Updated typedefs:** `ms-client-type`, `sta-type`.

</details>

<a id="module-cisco-ios-xe-controller-shdsl-common"></a>
<details>
<summary>Cisco-IOS-XE-controller-shdsl-common.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `dsl-stats`.

</details>

<a id="module-cisco-ios-xe-ethernet-radium-deviation"></a>
<details>
<summary>Cisco-IOS-XE-ethernet-radium-deviation.yang — adds 1 platform deviation(s)</summary>

**26.2.1 revision note:** Add deviation file to restrict LACP min-bundle and max-bundle range for radium platforms (4-port limit)

**Change at a glance:** adds 1 platform deviation(s).

**New deviations:** `/ios:native/ios:interface/ios:Port-channel/ios-eth:lacp/ios-eth:max-bundle`.

**Why this matters:** New deviation statements can alter the effective schema on the target platform; inspect each deviation target.

</details>

<a id="module-cisco-ios-xe-install-event-types"></a>
<details>
<summary>Cisco-IOS-XE-install-event-types.yang — adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added install-sub-state enum value for xFSU pre-check failure when an external packet buffer is enabled on the node - Added install status for Live Patching Service (LPS) conflict with existing LPS on device - Added install sub status for one-shot install rejection during APSP SMU installation

**Change at a glance:** adds/updates 1 reusable type(s).

**Updated typedefs:** `install-sub-state`.

</details>

<a id="module-cisco-ios-xe-nwpi-types"></a>
<details>
<summary>Cisco-IOS-XE-nwpi-types.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Updated descriptions of several model elements to clarify their meaning and purpose

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `nwpi-pcap-replay`.

</details>

<a id="module-cisco-ios-xe-wireless-mobility-types"></a>
<details>
<summary>Cisco-IOS-XE-wireless-mobility-types.yang — adds/updates 1 reusable type(s)</summary>

**26.2.1 revision note:** Added URWB telemetry message

**Change at a glance:** adds/updates 1 reusable type(s).

**Updated typedefs:** `mm-mobility-msg-type`.

</details>

<a id="module-cisco-ios-xe-xcopy-events"></a>
<details>
<summary>Cisco-IOS-XE-xcopy-events.yang — adds/updates 1 reusable grouping(s)</summary>

**26.2.1 revision note:** Added file-size leaf (bytes) to express-copy-event-fields grouping and deprecated file size leaf (megabytes) in the same grouping

**Change at a glance:** adds/updates 1 reusable grouping(s).

**Updated groupings:** `xcopy-event-fields`.

</details>

</details>

## Existing models with no tracked schema signature change

These files differ byte-for-byte between releases, but the comparison found no change to the tracked data-node, grouping, augment-target/uses, typedef, deviation, feature, identity, RPC/action, or notification signatures. Differences in imports, revision statements, and other untracked statements are not resolved here and may affect effective schemas. This section means “no tracked declaration change detected,” not “no model change.”

<details>
<summary>Show all 147 changed source entries with no tracked signature change</summary>


### Oper (118 changed source entries)

- Cisco-IOS-XE-aaa-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-acl-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-app-cflowd-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-arp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-aws-common-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-aws-cw-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-aws-s3-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-bbu-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-bfd-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-bgp-nbr-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-boot-integrity-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-cable-diag-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-cfm-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-checkpoint-archive-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-cloud-services-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-controller-shdsl-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-controller-t1e1-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-controller-vdsl-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-crypto-pki-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-dhcp-security-track-server-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-digital-io-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-dlr-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-dns-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-eem-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-embedded-ap-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-endpoint-tracker-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-gir-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-gnss-dr-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-group-policy-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ha-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-hsr-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-hsrp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-iad-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-identity-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ignition-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ip-arp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ipv6-nd-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ipv6-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-isdn-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-l2nat-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-l2tp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-l2vpn-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-lacp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-line-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-lisp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-lldp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-lorawan-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-lte450-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-macsec-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-matm-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-mdt-capabilities-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-mdt-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-mdt-stats-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-mka-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-mlppp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-mpls-forwarding-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-msdp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-nat-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ncch-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-netconf-diag-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-nve-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-omp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-pim-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-platform-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-policymap-target-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ppp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-process-cpu-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-prp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-psecure-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-qfp-classification-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-qfp-crypto-dp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-qfp-resource-utilization-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-rg-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-rib-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-scada-gw-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-sdwan-ipsec-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-service-chain-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-spanning-tree-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-sr-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-sse-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-stack-member-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-stacking-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-steering-policy-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-switch-dp-mac-learning-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-switch-dp-resources-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-switchport-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-system-integrity-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-tcam-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-transceiver-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-trustsec-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ucse-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-udld-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-umbrella-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-vdsp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-vlan-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-voice-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-vrrp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-afc-cloud-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-afc-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-awips-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-ble-mgmt-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-cts-sxp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-general-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-geolocation-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-hyperlocation-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-lisp-agent-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-location-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-mcast-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-mdns-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-nmsp-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-rfid-global-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-rfid-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-rrm-global-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-rule-mdns-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-sdavc-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-sisf-global-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-tunnel-oper.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wpan-oper.yang — no tracked declaration change detected.

### RPC (5 changed source entries)

- Cisco-IOS-XE-cloud-services-rpc.yang — no tracked declaration change detected.
- Cisco-IOS-XE-install-rpc.yang — no tracked declaration change detected.
- Cisco-IOS-XE-nwpi-rpc.yang — no tracked declaration change detected.
- Cisco-IOS-XE-rpc.yang — no tracked declaration change detected.
- Cisco-IOS-XE-verify-rpc.yang — no tracked declaration change detected.

### Config (14 changed source entries)

- Cisco-IOS-XE-app-hosting-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-aws-common-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-aws-cw-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-aws-s3-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-cloud-services-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-ppp.yang — no tracked declaration change detected.
- Cisco-IOS-XE-scada-gw.yang — no tracked declaration change detected.
- Cisco-IOS-XE-uplink-autoconfig.yang — no tracked declaration change detected.
- Cisco-IOS-XE-voice-class.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-dot15-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-fabric-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-location-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-rfid-cfg.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-rule-cfg.yang — no tracked declaration change detected.

### OpenConfig (1 changed source entries)

- cisco-xe-openconfig-access-points-deviation.yang — no tracked declaration change detected.

### Other (9 changed source entries)

- Cisco-IOS-XE-common-types.yang — no tracked declaration change detected.
- Cisco-IOS-XE-event-history-types.yang — no tracked declaration change detected.
- Cisco-IOS-XE-tunnel-types.yang — no tracked declaration change detected.
- Cisco-IOS-XE-types.yang — no tracked declaration change detected.
- Cisco-IOS-XE-vlan-ewlc-deviation.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-geolocation-types.yang — no tracked declaration change detected.
- Cisco-IOS-XE-wireless-rogue-types.yang — no tracked declaration change detected.
- tailf-cli-extensions.yang — no tracked declaration change detected.
- tailf-common.yang — no tracked declaration change detected.

</details>

## Method and interpretation

1. **Inventory:** matched files by filename across `2611/` and `2621/`; recorded additions, removals, byte-identical files, and changed files. Separately parsed the ten supplied `yang-set-<profile>.xml` snapshots and matched modules by name.
2. **Module classification:** assigned one requested model flavor using module name, namespace, and top-level YANG constructs.
3. **Structural comparison:** parsed YANG statement blocks and compared top-level augment targets, their nested `uses` sites, and direct data-node counts, declared data nodes by schema path and kind, selected schema-relevant properties (`type`, `config`, `default`, `mandatory`, `must`, `when`, cardinality, key, status, and related statements), plus named groupings, typedefs, deviations, features, identities, RPC/actions, and notifications. Description/reference prose is excluded from structural signatures.
4. **No inferred resolved-node totals:** this report does not label source-level node counts as counts from a fully expanded YANG schema tree.
5. **Static-analysis boundary:** this pass compares parsed source statements; it is not a YANG compiler or full semantic validation. It does not compose submodules, recursively expand `uses`, resolve the full import/augment graph, or apply the complete deviation set. Grouping and deviation CSVs expose the underlying declaration changes so those effects can be reviewed and resolved in a later schema-resolution pass.

### Limits to keep in mind

- YANG `uses` expansion, imported groupings, submodule composition, cross-module augments, complete deviation application, and feature selection are not fully resolved in this source-level pass. The augment CSV records target and `uses` declarations without expanding groupings. The platform CSV compares module-set membership, revisions, conformance types, and listed deviation associations; the feature-delta CSV records advertised feature changes. Neither applies deviations or compiles each profile’s effective schema tree.
- Input provenance is based on the supplied folder names and files; the source URL/archive, retrieval date, and checksums are not recorded. For a release-support claim, record those along with the exact hardware PID and software build, and confirm the saved platform profile against the device.
- A file-level deletion or module presence does not establish runtime feature availability. The platform table describes the supplied profile inventories, not a guarantee that a feature is enabled or supported by every product in a family.
- The release inventory reports modules and submodules separately. Change and unchanged counts are source files; submodule changes are assigned to the parent module flavor. These counts are not resolved schema-node totals or unique feature-family totals.
- Source YANG files are input artifacts and are not published with this report. Module names expand to show report details; supporting CSVs provide row-level changes and profile evidence.

## Reproducibility

- Older source folder used for this comparison: `2611/` (input files are not published here).
- Newer source folder used for this comparison: `2621/` (input files are not published here).
- Comparison filename follows the release-comparison convention: `2621-YANG-Model-Overview.md`.
- Grouping statement deltas: [2621-YANG-Model-Grouping-Deltas.csv](2621-YANG-Model-Grouping-Deltas.csv).
- Deviation targets and statement deltas: [2621-YANG-Model-Deviation-Deltas.csv](2621-YANG-Model-Deviation-Deltas.csv).
- Augment targets and nested `uses` deltas: [2621-YANG-Model-Augment-Deltas.csv](2621-YANG-Model-Augment-Deltas.csv).
- Platform module-set applicability by profile and release: [2621-YANG-Platform-Applicability.csv](2621-YANG-Platform-Applicability.csv).
- Modules newly listed by each saved profile, split by source age: [2621-YANG-Platform-Newly-Listed.csv](2621-YANG-Platform-Newly-Listed.csv).
- Advertised profile feature deltas: [2621-YANG-Platform-Feature-Deltas.csv](2621-YANG-Platform-Feature-Deltas.csv).
- Deviation targets referenced by each saved profile: [2621-YANG-Platform-Deviation-Targets.csv](2621-YANG-Platform-Deviation-Targets.csv).
