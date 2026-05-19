# Wireless YANG Schema Delta: Direct Upgrade Cisco IOS XE 17.15.1 -> 17.18.1

**Scope:** every `Cisco-IOS-XE-wireless-*.yang` module, treating 17.18.1 as the upgrade target from a 17.15.1 baseline. All schema additions, removals, obsoleted XPaths, and constraint tightenings introduced in 17.16.1 and 17.17.1 are folded into the 17.18.1 view -- this document is written for operators who skip the intermediate releases.

Derived directly from the YANG sources and "Backward Incompatible Change" (BIC) deltas shipped in this repository.

### TL;DR -- what's new and changed between 17.15.1 and 17.18.1

- **5 NEW modules**: `wireless-rogue-authz-rpc`, `wireless-urwb-cfg`, `wireless-urwb-common-types`, `wireless-urwbnet-oper`, `wireless-wat-cfg`.
- **32 CHANGED modules** out of 83 (46 unchanged). **0 modules removed.**
- **+309 schema symbols added, 0 removed** across modified modules. Top adders: `access-point-oper` (+70), `types` (+65), `client-global-oper` (+38), `rogue-cfg` (+25), `rogue-oper` (+22).
- **8 dominant feature programs**: Wi-Fi 7 / 802.11be MLO, URWB backhaul, Cisco Smart Licensing observability, LSC renewal, 802.11k/v request stats, Rogue Authorization, AP next-gen tunnel, UWB DL-TDOA + WAT/ThousandEyes.
- **Backward-incompatible footprint is small**: 1 XPath obsoleted (`access-point-oper-data/stgrd-upg-report/stgrd-upgd-ap`), 0 deprecated, ~60 tightened `must`/`length`/`pattern` constraints across 19 modules.

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Module Inventory Matrix](#2-module-inventory-matrix)
3. [Consolidated Symbol Delta (Modified Existing Modules)](#3-consolidated-symbol-delta-modified-existing-modules)
4. [New Modules Deep Dive](#4-new-modules-deep-dive)
   - [wireless-rogue-authz-rpc](#41-cisco-ios-xe-wireless-rogue-authz-rpc)
   - [wireless-urwb-cfg](#42-cisco-ios-xe-wireless-urwb-cfg)
   - [wireless-urwb-common-types](#43-cisco-ios-xe-wireless-urwb-common-types)
   - [wireless-urwbnet-oper](#44-cisco-ios-xe-wireless-urwbnet-oper)
   - [wireless-wat-cfg](#45-cisco-ios-xe-wireless-wat-cfg)
5. [Consolidated Constraint Changes (BIC, 17.15.1 -> 17.18.1)](#5-consolidated-constraint-changes-bic-17151---17181)
6. _[reserved]_
7. [XPath Appendix (Hotspot Modules + New Modules)](#7-xpath-appendix-hotspot-modules--new-modules)
8. [Telemetry Subscription Cross-Reference](#8-telemetry-subscription-cross-reference)
9. [Methodology and Sources](#9-methodology-and-sources)

## 1) Executive Summary

### At a glance

| Metric | 17.15.1 | 17.18.1 | Delta |
|---|---:|---:|---:|
| Wireless YANG modules | 78 | 83 | **+5 / -0** |
| Modules CHANGED across span | -- | -- | **32** |
| Modules UNCHANGED across span | -- | -- | **46** |
| New top-level leaves/containers/lists/groupings/typedefs/RPCs (existing modules) | -- | -- | **+309** symbols added, **0** removed |
| Modules with constraint tightenings (BIC) across span | -- | -- | **19** (26 BIC files merged) |
| XPaths obsoleted in span | -- | -- | **1** (`access-point-oper-data/stgrd-upg-report/stgrd-upgd-ap`, 17.18.1) |
| XPaths deprecated in span | -- | -- | **0** |
| XPaths with tightened `must`/`length`/`pattern` constraints | -- | -- | ~60 across 26 modules |

**Five net-new modules** land between 17.15.1 and 17.18.1: `wireless-rogue-authz-rpc` (Rogue Authorization import/export RPCs), `wireless-urwb-cfg`, `wireless-urwb-common-types`, `wireless-urwbnet-oper`, and `wireless-wat-cfg`.

### What's new (functional themes)

The 17.15.1 -> 17.18.1 span is dominated by **eight feature programs** that together account for the bulk of the added schema:

1. **Wi-Fi 7 / 802.11be Multi-Link Operation (MLO).** New per-band MLO containers (`mlo-24ghz`, `mlo-5ghz`, `mlo-5ghz-sec`, `mlo-6ghz`) appear on both WLAN config and the shared `wireless-types` groupings. Client-side multi-link visibility added via `multi-link-capable` and `multi-link-client` leaves on client-oper / client-global-oper. New unsupported-security guard: `unsupported-wifi7-security` (client-types).
2. **Ultra Reliable Wireless Backhaul (URWB).** Net-new in 17.18.1 as a first-class feature set across **four new modules** (`urwb-cfg`, `urwb-common-types`, `urwbnet-oper`, plus `wat-cfg` for the active-testing companion) and deep extensions into existing modules: radio-mode containers (`radio-urwb-mode`, `radio-urwb-mode-80211-6ghz`, `radio-urwb-mode-80211a`), 20+ new URWB enums (mobility/MPO/MPLS/crypto/role/DFS), URWB channel lists on radio-cfg, and per-AP `urwb-cfg-status`.
3. **Cisco Wireless (Smart) Licensing observability.** New `ap-license` container with `cw-lic-state`, `cw-lic-required`, `cw-lic-ooc-reason`, `feature-type`, `expiry-time`, plus the `cw-license-info` grouping and `enm-cw-compliance-state` / `enm-cw-non-compliance-reason` typedefs on access-point-oper.
4. **LSC (Locally Significant Certificate) renewal workflow.** New `lsc-renew` container in security-cfg, new RPCs `all-ap-lsc-renew` and `per-ap-lsc-renew` in access-point-cmd-rpc, `ap-lsc` list on access-point-oper with renewal failure typedefs (`ap-lsc-renew-failure-rc`, `ap-lsc-prov-workflow`, `ap-lsc-usage`), and the `st-lsc-renew` grouping in wireless-types (with constraint tightening on `one-shot` / `staggered`).
5. **802.11k / 802.11v request statistics.** Per-client (`dot11k-req-stats`, `dot11v-req-stats` on client-oper) and per-radio (`dot11k-req-stats-radio`, `dot11v-req-stats-radio` on access-point-oper) counters, plus `invalid-11k-req` / `invalid-11v-req` containers and individual `dot11k-req-*` / `dot11v-req-*` reason leaves on wireless-types.
6. **Rogue Authorization framework.** Net-new RPC module `wireless-rogue-authz-rpc` plus large additions to `wireless-rogue-cfg` (+25): `ap-cfg`, `client-cfg`, `authz-mode`, paired `authz-*` / `unauthz-*` alarms for AP, Client, SSID, AKM, Cipher, Mesh, Hotspot, MAC-Spoof. New rogue-oper containers (`rogue-akm`, `rogue-cipher`), `rogue-unconnected-*` lists, and unconnected-client telemetry (`unconnected-client-count/report/drop`, `iapp-unconnected-client`).
7. **AP next-gen tunnel telemetry.** New `ap-nextunnel*` lists and `st-ap-next-tunnel-cfg` / `st-ap-nextunnel-if-data` / `st-ap-nextunnel-state-data` groupings on access-point-oper, with `enm-tunnel-cfg-fetch-state` and `enm-tunnel-state` typedefs.
8. **UWB DL-TDOA fine-time positioning + WAT (Wireless Active Testing / ThousandEyes).** New `set-ap-uwb-dltdoa` RPC in access-point-cfg-rpc, `cluster-grp-json-params` leaf, and `st-uwb-dltdoa-anchor/cluster/cluster-grp/init/resp` groupings on wireless-types. WAT receives its own `wat-cfg` module plus `wat-cfg` container on radio-cfg and `st-radio-wat-cfg` / `wat-radio-admin-state` symbols on wireless-types; the WAT manager integrates with ThousandEyes via `te-conn-str` and `te-download-url`.

Additional cross-cutting additions:

- **Consolidated client telemetry.** New `client-cnsld-data` list/grouping on client-global-oper exposes 24+ fields (auth-key-mgmt, cipher-suite, AP MAC, BSSID, radio type, RSSI/SNR, association/auth/L3-auth/MAB success/failure counters, run-state counters, IPv4/IPv6 addresses, VLAN, policy/wlan profile). This is a major aggregation point for client KPIs.
- **AP onboarding / management ACL / static MTU / Spaces connector.** New site-cfg containers `ap-mgmt-acl`, `onboard-cfg`, `rlan-cfg`, `spaces-conn-cfg`, `static-mtu` plus matching ap-types groupings (`st-ap-mgmt-acl`, `st-ap-onboard-cfg`, `st-ap-pmtu`, `st-spaces-conn-cfg`).
- **AP port authentication telemetry.** `ap-port-auth-info` list on access-point-oper with `eap-status-code`, port/MAC/auth-status leaves and matching `enm-ap-port-auth-*` enums.
- **AP environmental mode + beam state.** `ap-env-mode` + `ap-beam-state` leaves with companion typedefs.

### Hotspot modules (top adders)

| Module | Symbols Added |
|---|---:|
| `Cisco-IOS-XE-wireless-access-point-oper` | +70 |
| `Cisco-IOS-XE-wireless-types` | +65 |
| `Cisco-IOS-XE-wireless-client-global-oper` | +38 |
| `Cisco-IOS-XE-wireless-rogue-cfg` | +25 |
| `Cisco-IOS-XE-wireless-rogue-oper` | +22 |
| `Cisco-IOS-XE-wireless-enum-types` | +21 |
| `Cisco-IOS-XE-wireless-ap-types` | +19 |

These seven modules account for **~85%** of all schema-level additions in this span.

### Compatibility and upgrade considerations

- **No module removals. No XPath deprecations.** A consumer that ignores unknown leaves can roll forward without breakage.
- **One XPath obsoleted** in 17.18.1: `access-point-oper-data/stgrd-upg-report/stgrd-upgd-ap`. Consumers should stop subscribing to this leaf prior to 17.18.1 upgrade.
- **Constraint tightening** is the dominant BIC pattern. Common cases: `must` expressions made more restrictive, new `length` ranges on string leaves, new `pattern` regexes (notably WLAN PSK / preauth ACL name fields). Configurations that were valid in 17.15.1 may be rejected by 17.18.1 if they exceed the new bounds. See Section 5 for the verbatim BIC notes per release.
- **Cisco semver bumps** track real schema deltas. Notable major-version jumps in this span: `wireless-types` 6.6.0 -> 7.0.0, `wireless-wlan-cfg` 17.0.0 -> 20.0.0, `wireless-site-cfg` 14.0.0 -> 16.0.0, `wireless-rrm-cfg` 10.0.0 -> 11.0.0, `wireless-tunnel-cfg` 3.1.0 -> 4.0.0, `wireless-tunnel-types` 2.1.0 -> 3.0.0.
- **Telemetry subscriptions** that reference any of the seven hotspot modules above will see new leaves on the wire after upgrade -- review parser/schema-validation strictness and downstream metric cardinality before rolling forward.
- **Catalyst 9300 relevance:** these are WLC-side wireless models. They apply to Catalyst 9800 controllers and AP-integrated wireless on supported platforms, not directly to the Catalyst 9300 switch focus of the rest of this repository.

### Data caveats

- **Capability XML for 17.18.1 is empty in the upstream `YangModels/yang` repository** (verified zero-byte at `vendor/cisco/xe/17181/capability-wireless.xml`). All 17.18.1 capability conclusions in this document are derived from the YANG file inventory itself rather than the capability advertisement. For comparison, [reference/xe/17151/capability-wireless.xml](reference/xe/17151/capability-wireless.xml) carries 366 `<capability>` entries.
- **OpenConfig wireless modules** (`openconfig-wifi-*`, `openconfig-ap-manager`, `openconfig-access-points`) and the Cisco OpenConfig wireless deviations (`cisco-xe-wireless-openconfig-*-deviation.yang`) did **not** change materially in this span and are excluded from the symbol delta. See Section 6 for sourcing.

### How to use this document

| You want to... | Go to |
|---|---|
| See which modules moved revision between 17.15.1 and 17.18.1 | Section 2 (inventory matrix) |
| Find every leaf/container/grouping added to an existing module | Section 3 (consolidated symbol delta) |
| Understand a brand-new module's full schema (RPCs, leaves with type/units/description) | Section 4 (new modules deep dive) |
| Review every `must` / `length` / `pattern` constraint that tightened between 17.15.1 and 17.18.1 | Section 5 (consolidated BIC) |
| Find a RESTCONF/gNMI XPath for a newly-added leaf or list | Section 7 (XPath appendix) |
| Plan telemetry subscriptions to cover the new schema | Section 8 (subscription cross-reference) |
| Verify source files and parsing rules | Section 6 (methodology) |

## 2) Module Inventory Matrix

Cells show `revision-date / cisco-semver` for the two endpoints of the upgrade. Status: `NEW` = module did not exist in 17.15.1 but ships in 17.18.1; `CHANGED` = revision or semver moved between 17.15.1 and 17.18.1; `UNCHANGED` = identical schema in 17.15.1 and 17.18.1.

**Modules with schema changes (37 of 83):**

| Module | 17.15.1 | 17.18.1 | Status |
|---|---|---|---|
| `Cisco-IOS-XE-wireless-rogue-authz-rpc` | - | 2025-07-01 / 1.1.0 | NEW |
| `Cisco-IOS-XE-wireless-urwb-cfg` | - | 2025-07-01 / 1.0.0 | NEW |
| `Cisco-IOS-XE-wireless-urwb-common-types` | - | 2025-07-01 / 1.0.0 | NEW |
| `Cisco-IOS-XE-wireless-urwbnet-oper` | - | 2025-07-01 / 1.0.0 | NEW |
| `Cisco-IOS-XE-wireless-wat-cfg` | - | 2025-07-01 / 1.0.0 | NEW |
| `Cisco-IOS-XE-wireless-access-point-cfg-rpc` | 2024-07-01 / 6.1.0 | 2025-03-01 / 6.2.0 | CHANGED |
| `Cisco-IOS-XE-wireless-access-point-cmd-rpc` | 2024-07-01 / 2.11.0 | 2025-03-01 / 2.12.0 | CHANGED |
| `Cisco-IOS-XE-wireless-access-point-oper` | 2024-07-01 / 8.1.0 | 2025-07-01 / 9.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-ap-cfg` | 2024-07-01 / 7.0.0 | 2025-03-01 / 8.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-ap-global-oper` | 2023-11-01 / 1.4.0 | 2025-07-01 / 1.6.0 | CHANGED |
| `Cisco-IOS-XE-wireless-ap-types` | 2024-07-01 / 11.0.0 | 2025-07-01 / 13.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-apf-cfg` | 2023-11-01 / 10.1.0 | 2025-07-01 / 12.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-awips-oper` | 2023-11-01 / 1.3.0 | 2025-07-01 / 1.4.0 | CHANGED |
| `Cisco-IOS-XE-wireless-client-global-oper` | 2024-07-01 / 1.7.0 | 2025-07-01 / 1.9.0 | CHANGED |
| `Cisco-IOS-XE-wireless-client-oper` | 2024-07-01 / 7.14.0 | 2025-07-01 / 7.17.0 | CHANGED |
| `Cisco-IOS-XE-wireless-client-types` | 2024-07-01 / 4.12.0 | 2025-03-01 / 4.14.0 | CHANGED |
| `Cisco-IOS-XE-wireless-cts-sxp-cfg` | 2022-11-01 / 2.1.0 | 2025-03-01 / 3.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-dot11-cfg` | 2024-07-01 / 11.0.0 | 2025-07-01 / 12.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-enum-types` | 2024-07-01 / 4.4.0 | 2025-07-01 / 4.6.0 | CHANGED |
| `Cisco-IOS-XE-wireless-events-oper` | 2022-11-01 / 2.3.0 | 2025-07-01 / 2.4.0 | CHANGED |
| `Cisco-IOS-XE-wireless-flex-cfg` | 2023-11-01 / 9.3.0 | 2025-07-01 / 10.1.0 | CHANGED |
| `Cisco-IOS-XE-wireless-general-cfg` | 2024-07-01 / 9.0.0 | 2025-03-01 / 9.1.0 | CHANGED |
| `Cisco-IOS-XE-wireless-mobility-cfg` | 2024-03-01 / 7.0.0 | 2025-03-01 / 8.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-mobility-types` | 2024-07-01 / 2.7.0 | 2025-07-01 / 2.8.0 | CHANGED |
| `Cisco-IOS-XE-wireless-mstream-cfg` | 2024-07-01 / 5.0.0 | 2024-11-01 / 6.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-radio-cfg` | 2022-11-01 / 3.4.0 | 2025-07-01 / 4.1.0 | CHANGED |
| `Cisco-IOS-XE-wireless-rf-cfg` | 2024-07-01 / 9.6.0 | 2025-07-01 / 11.1.0 | CHANGED |
| `Cisco-IOS-XE-wireless-rlan-cfg` | 2023-07-01 / 4.0.0 | 2025-03-01 / 5.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-rogue-cfg` | 2024-07-01 / 6.6.0 | 2025-07-01 / 6.8.0 | CHANGED |
| `Cisco-IOS-XE-wireless-rogue-oper` | 2024-07-01 / 5.12.0 | 2025-07-01 / 5.14.0 | CHANGED |
| `Cisco-IOS-XE-wireless-rrm-cfg` | 2024-07-01 / 10.0.0 | 2025-03-01 / 11.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-security-cfg` | 2022-11-01 / 2.1.0 | 2025-03-01 / 2.2.0 | CHANGED |
| `Cisco-IOS-XE-wireless-site-cfg` | 2024-07-01 / 14.0.0 | 2025-07-01 / 16.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-tunnel-cfg` | 2022-11-01 / 3.1.0 | 2024-11-01 / 4.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-tunnel-types` | 2022-11-01 / 2.1.0 | 2024-11-01 / 3.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-types` | 2024-07-01 / 6.6.0 | 2025-07-01 / 7.0.0 | CHANGED |
| `Cisco-IOS-XE-wireless-wlan-cfg` | 2024-07-01 / 17.0.0 | 2025-07-01 / 20.0.0 | CHANGED |

<details><summary>Show 46 UNCHANGED modules</summary>

| Module | 17.15.1 | 17.18.1 | Status |
|---|---|---|---|
| `Cisco-IOS-XE-wireless-actions-rpc` | 2022-11-01 / 1.1.0 | 2022-11-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-afc-cloud-oper` | 2023-11-01 / 1.0.0 | 2023-11-01 / 1.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-afc-oper` | 2024-03-01 / 1.1.0 | 2024-03-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-afc-types` | 2024-07-01 / 1.1.0 | 2024-07-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-ble-ltx-oper` | 2023-03-01 / 2.0.0 | 2023-03-01 / 2.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-ble-mgmt-cmd-rpc` | 2022-11-01 / 2.1.0 | 2022-11-01 / 2.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-ble-mgmt-oper` | 2022-11-01 / 1.2.0 | 2022-11-01 / 1.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-cisco-spaces-oper` | 2024-07-01 / 1.0.0 | 2024-07-01 / 1.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-client-rpc` | 2024-03-01 / 1.3.0 | 2024-03-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-cts-sxp-oper` | 2022-11-01 / 1.3.0 | 2022-11-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-dot15-cfg` | 2022-11-01 / 1.1.0 | 2022-11-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-fabric-cfg` | 2024-03-01 / 6.0.0 | 2024-03-01 / 6.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-fqdn-cfg` | 2022-11-01 / 3.1.0 | 2022-11-01 / 3.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-general-oper` | 2022-11-01 / 1.2.0 | 2022-11-01 / 1.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-geolocation-oper` | 2022-11-01 / 1.0.0 | 2022-11-01 / 1.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-geolocation-types` | 2024-07-01 / 1.2.0 | 2024-07-01 / 1.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-hotspot-cfg` | 2022-11-01 / 2.3.0 | 2022-11-01 / 2.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-hyperlocation-oper` | 2022-11-01 / 1.3.0 | 2022-11-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-lisp-agent-oper` | 2022-11-01 / 4.2.0 | 2022-11-01 / 4.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-location-cfg` | 2022-11-01 / 3.3.0 | 2022-11-01 / 3.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-location-oper` | 2022-11-01 / 1.3.0 | 2022-11-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-mcast-oper` | 2022-11-01 / 3.2.0 | 2022-11-01 / 3.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-mdns-oper` | 2022-11-01 / 1.3.0 | 2022-11-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-mesh-cfg` | 2024-07-01 / 7.0.0 | 2024-07-01 / 7.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-mesh-global-oper` | 2022-11-01 / 1.1.0 | 2022-11-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-mesh-oper` | 2024-03-01 / 5.4.0 | 2024-03-01 / 5.4.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-mesh-rpc` | 2023-07-01 / 2.2.1 | 2023-07-01 / 2.2.1 | UNCHANGED |
| `Cisco-IOS-XE-wireless-mobility-oper` | 2023-03-01 / 6.4.0 | 2023-03-01 / 6.4.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-nmsp-oper` | 2022-11-01 / 4.2.0 | 2022-11-01 / 4.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-power-cfg` | 2023-07-01 / 1.2.0 | 2023-07-01 / 1.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rfid-cfg` | 2022-11-01 / 4.3.0 | 2022-11-01 / 4.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rfid-global-oper` | 2024-07-01 / 1.3.0 | 2024-07-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rfid-oper` | 2024-07-01 / 3.5.0 | 2024-07-01 / 3.5.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rogue-types` | 2024-07-01 / 5.5.0 | 2024-07-01 / 5.5.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rrm-emul-oper` | 2023-03-01 / 1.2.0 | 2023-03-01 / 1.2.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rrm-global-oper` | 2023-07-01 / 1.3.0 | 2023-07-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rrm-oper` | 2023-11-01 / 5.11.0 | 2023-11-01 / 5.11.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rrm-rpc` | 2023-03-01 / 1.3.0 | 2023-03-01 / 1.3.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rrm-types` | 2022-11-01 / 4.4.0 | 2022-11-01 / 4.4.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rule-cfg` | 2023-07-01 / 2.0.0 | 2023-07-01 / 2.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-rule-mdns-oper` | 2022-11-01 / 1.1.0 | 2022-11-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-sdavc-oper` | 2022-11-01 / 1.1.0 | 2022-11-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-sisf-global-oper` | 2022-11-01 / 1.1.0 | 2022-11-01 / 1.1.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-tech-support-rpc` | 2024-07-01 / 1.0.0 | 2024-07-01 / 1.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-tunnel-oper` | 2023-11-01 / 1.0.0 | 2023-11-01 / 1.0.0 | UNCHANGED |
| `Cisco-IOS-XE-wireless-wlan-global-oper` | 2023-03-01 / 1.1.0 | 2023-03-01 / 1.1.0 | UNCHANGED |

</details>


## 3) Consolidated Symbol Delta (Modified Existing Modules)

Schema-level adds/removes for modules that existed in 17.15.1 and changed by 17.18.1.
**Brand-new modules are detailed in Section 4** and excluded here to avoid duplication.

### `Cisco-IOS-XE-wireless-access-point-cfg-rpc`  (+3 / -0)

**Added:**

- *grouping*: `set-ap-uwb-dltdoa`
- *rpc*: `set-ap-uwb-dltdoa`
- *leaf*: `cluster-grp-json-params`

### `Cisco-IOS-XE-wireless-access-point-cmd-rpc`  (+6 / -0)

**Added:**

- *grouping*: `all-ap-lsc-renew`, `per-ap-lsc-renew`
- *rpc*: `all-ap-lsc-renew`, `ap-tag-reval`, `per-ap-lsc-renew`
- *leaf*: `due-days`

### `Cisco-IOS-XE-wireless-access-point-oper`  (+70 / -0)

**Added:**

- *container*: `ap-license`, `dot11k-req-stats-radio`, `dot11v-req-stats-radio`
- *list*: `ap-lsc`, `ap-nextunnel`, `ap-nextunnel-if-info`, `ap-nextunnel-state-info`, `ap-port-auth-info`, `comp-ap`, `radio-oper-ext-data`, `stgrd-upg-failed-ap`
- *grouping*: `cw-license-info`, `ewlc-radio-operation-ext-config`, `mac-iter-key`, `st-ap-lsc`, `st-ap-lsc-key`, `st-ap-next-tunnel-cfg`, `st-ap-nextunnel-if-data`, `st-ap-nextunnel-state-data`, `stgrd-upg-failed-ap`
- *typedef*: `ap-lsc-prov-workflow`, `ap-lsc-renew-failure-rc`, `ap-lsc-usage`, `enm-ap-env-mode`, `enm-cw-compliance-state`, `enm-cw-non-compliance-reason`, `enm-tunnel-cfg-fetch-state`, `enm-tunnel-state`
- *leaf*: `airtime-used-cum`, `ap-beam-state`, `ap-env-mode`, `ap-nextunnel-state`, `bp-enabled`, `client-ipv6-addr`, `client-last-restart`, `config-server-url`, `cumulative-rx-bytes`, `cumulative-tx-bytes`, `cw-lic-ooc-reason`, `cw-lic-required`, `cw-lic-state`, `data-rate`, `disc-meraki-l2-pkts`, `disc-meraki-pkts`, `expiry-time`, `failed-ap-count`, `feature-type`, `fetch-fail-reason`, `fetch-state`, `last-fetch`, `last-renew-attempt`, `last-renew-failure-rc`, `lsc-prov-workflow`, `lsc-usage`, `next-fetch`, `primary-last-change`, `primary-state`, `primary-url`, `radio-uptime-cum`, `secondary-last-change`, `secondary-state`, `secondary-url`, `serial-iter-num`, `server-ipv6-addr`, `sp-static-chan`, `sp-static-chan-width`, `sp-static-txpwr`, `storage-usage`, `tmp-usage`, `urwb-cfg-status`

### `Cisco-IOS-XE-wireless-ap-global-oper`  (+4 / -0)

**Added:**

- *container*: `radio-urwb-mode`, `radio-urwb-mode-80211-6ghz`, `radio-urwb-mode-80211a`, `total-xor-24-6ghz-rad`

### `Cisco-IOS-XE-wireless-ap-types`  (+19 / -0)

**Added:**

- *grouping*: `st-ap-mgmt-acl`, `st-ap-onboard-cfg`, `st-ap-pmtu`, `st-ap-port-auth-info`, `st-ap-prof-rlan-cfg`, `st-spaces-conn-cfg`
- *typedef*: `enm-ap-onboard-cfg`
- *leaf*: `acl-name-v4`, `acl-name-v6`, `config`, `eap-status-code`, `fast-switching`, `kcd-dlimit`, `pmf-offchannel`, `port`, `port-mac`, `size`, `token`, `token-type`

### `Cisco-IOS-XE-wireless-awips-oper`  (+6 / -0)

**Added:**

- *leaf*: `band-id`, `channel`, `radio-id`, `rssi`, `snr`, `src-mac`

### `Cisco-IOS-XE-wireless-client-global-oper`  (+38 / -0)

**Added:**

- *list*: `client-cnsld-data`
- *grouping*: `client-cnsld-data`
- *typedef*: `dot11i-auth-key-mgmt-type`
- *leaf*: `ap-mac-addr`, `assoc-requests-received`, `auth-key-mgmt`, `cipher-suite`, `client-l2auth-failures`, `client-l2auth-success`, `client-l3auth-attempts`, `client-l3auth-failures`, `client-mab-attempts`, `client-mab-failures`, `client-state-associated`, `client-state-deleted`, `client-state-run`, `client-state-start`, `client-type`, `co-state`, `cur-chan`, `data-retries`, `ft-localauth-attempts`, `ip-addr`, `mm-client-role`, `ms-bssid`, `ms-radio-type`, `multi-link-client`, `pkts-tx`, `policy-profile`, `res-vlan-name`, `rssi`, `slot-id`, `snr`, `speed`, `user-name`, `wlan-profile`, `wpa-version`
- *leaf-list*: `ipv6-addr`

### `Cisco-IOS-XE-wireless-client-oper`  (+4 / -0)

**Added:**

- *container*: `dot11k-req-stats`, `dot11v-req-stats`
- *leaf*: `band-id`, `multi-link-capable`

### `Cisco-IOS-XE-wireless-client-types`  (+1 / -0)

**Added:**

- *leaf*: `unsupported-wifi7-security`

### `Cisco-IOS-XE-wireless-enum-types`  (+21 / -0)

**Added:**

- *typedef*: `enm-ap-beam-state`, `enm-ap-port-auth-eap-status-code`, `enm-ap-port-auth-status`, `enm-dot11-protocol`, `enm-hybrid-ap-ant-mode`, `enm-radio-urwb-crypto`, `enm-radio-urwb-role`, `enm-rogue-akm`, `enm-rogue-cipher`, `enm-rogue-hotspot`, `enm-rogue-mesh`, `urwb-cfg-status`, `urwb-crd-mode`, `urwb-efm`, `urwb-mcast`, `urwb-mob-bcc`, `urwb-mob-bce`, `urwb-mob-hl`, `urwb-mob-mode`, `urwb-mpo-st`, `urwb-rad-dfs`

### `Cisco-IOS-XE-wireless-events-oper`  (+1 / -0)

**Added:**

- *leaf*: `serial-iter-num`

### `Cisco-IOS-XE-wireless-radio-cfg`  (+6 / -0)

**Added:**

- *container*: `urwb`, `urwb-chan-lists`, `wat-cfg`
- *list*: `urwb-chan-list`
- *grouping*: `st-urwb-chan-list`
- *leaf*: `prio`

### `Cisco-IOS-XE-wireless-rf-cfg`  (+3 / -0)

**Added:**

- *container*: `urwb`
- *leaf*: `ap-beam-state`, `unii3-lp-channels`

### `Cisco-IOS-XE-wireless-rogue-cfg`  (+25 / -0)

**Added:**

- *container*: `ap-cfg`, `client-cfg`
- *grouping*: `rogue-authz-ap-alarms`, `rogue-authz-cl-alarms`
- *leaf*: `actv-probe`, `actv-wlan-scan`, `ap-imprsn`, `authz-akm`, `authz-ap`, `authz-cipher`, `authz-clnt`, `authz-mode`, `authz-ssid`, `hidden-ssid`, `hotspot-ics`, `mac-spoof`, `mesh-detect`, `unauthz-akm`, `unauthz-ap`, `unauthz-cipher`, `unauthz-clnt`, `unauthz-ssid`, `uncon-clnt`, `unenc-traffic`, `weak-proto`

### `Cisco-IOS-XE-wireless-rogue-oper`  (+22 / -0)

**Added:**

- *container*: `rogue-akm`, `rogue-cipher`
- *list*: `rogue-unconnected-data`, `rogue-unconnected-lrad`
- *grouping*: `st-rogue-akm`, `st-rogue-cipher`, `st-rogue-unconnected-data`, `st-rogue-unconnected-lrad`
- *typedef*: `ucon-clnt-sec-vio`
- *leaf*: `ap-drop-urwb-link`, `beacon-interval`, `client-mac`, `clnt-syslog`, `first-timestamp`, `hotspot-type`, `iapp-unconnected-client`, `last-timestamp`, `unconnected-client-count`, `unconnected-client-report`, `unconnected-reports-drop`
- *leaf-list*: `wpa-cipher`, `wpa-support`

### `Cisco-IOS-XE-wireless-security-cfg`  (+2 / -0)

**Added:**

- *container*: `lsc-renew`
- *leaf*: `lsc-renew-syslog`

### `Cisco-IOS-XE-wireless-site-cfg`  (+5 / -0)

**Added:**

- *container*: `ap-mgmt-acl`, `onboard-cfg`, `rlan-cfg`, `spaces-conn-cfg`, `static-mtu`

### `Cisco-IOS-XE-wireless-types`  (+65 / -0)

**Added:**

- *container*: `init-cfg`, `invalid-11k-req`, `invalid-11v-req`, `resp-cfg`
- *list*: `cluster`, `resp-anchor`
- *grouping*: `st-11k-invalid-req`, `st-11v-invalid-req`, `st-dot11k-req-stats`, `st-dot11v-req-stats`, `st-lsc-renew`, `st-mlo-group-24ghz`, `st-mlo-group-5ghz`, `st-mlo-group-5ghz-sec`, `st-mlo-group-6ghz`, `st-radio-wat-cfg`, `st-urwb-cfg`, `st-uwb-dltdoa-anchor`, `st-uwb-dltdoa-cluster`, `st-uwb-dltdoa-cluster-grp`, `st-uwb-dltdoa-init`, `st-uwb-dltdoa-resp`
- *typedef*: `enm-wat-radio-admin-state`, `enum-ap-upgrade-feature-type`, `enum-mlo-group-24ghz`, `enum-mlo-group-5ghz`, `enum-mlo-group-5ghz-sec`, `enum-mlo-group-6ghz`, `uwb-dltdoa-anchor-role`
- *leaf*: `dot11k-req-assisted-roam`, `dot11k-req-diff-ap`, `dot11k-req-neigh-list`, `dot11k-req-parse-fail`, `dot11k-req-wl-sfc-info`, `dot11v-req-diff-ap`, `dot11v-req-dms-disabled`, `due-days`, `enable`, `id`, `init-anchor-addr`, `mac-addr`, `max-rounds`, `mlo-24ghz`, `mlo-5ghz`, `mlo-5ghz-sec`, `mlo-6ghz`, `one-shot`, `other-invalid-11k-req`, `other-invalid-11v-req`, `parent-anchor`, `resp-slot-index`, `round-index`, `schedular-cal-name`, `slot-index`, `staggered`, `staggered-iter-expiry`, `stratum`, `tot-dot11k-req`, `tot-dot11v-req`, `tot-invalid-11k-req`, `tot-invalid-11v-req`, `urwb-profile-name`, `valid-11k-req`, `valid-11v-req`, `wat-radio-admin-state`

### `Cisco-IOS-XE-wireless-wlan-cfg`  (+5 / -0)

**Added:**

- *container*: `mlo-24ghz`, `mlo-5ghz`, `mlo-5ghz-sec`, `mlo-6ghz`
- *leaf*: `multicast-foreign-fw`

## 4) New Modules Deep Dive

### 4.1) `Cisco-IOS-XE-wireless-rogue-authz-rpc`

- **First appears in:** 17.17.1
- **Namespace:** `http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-rogue-authz-rpc`
- **Prefix:** `wireless-rogue-authz-rpc`
- **Revisions:** 2025-03-01
- **Cisco semver:** 1.0.0
- **Source:** [reference/xe/17171/Cisco-IOS-XE-wireless-rogue-authz-rpc.yang](reference/xe/17171/Cisco-IOS-XE-wireless-rogue-authz-rpc.yang)

**Top-level schema counts:** grouping=2, rpc=4

**RPCs:** `clear-client-allow-list`, `clear-ap-allow-list`, `client-allow-list-export`, `ap-allow-list-export`

**Groupings:** `client-allow-list-export`, `ap-allow-list-export`

**Leaves (2 total):**

| Kind | Name | Type | Default | Units | Description |
|---|---|---|---|---|---|
| leaf | `filename` | `string` | - | - | Client Allow list export filename with csv extension |
| leaf | `filename` | `string` | - | - | Access Point Allow list export filename with csv extension |

### 4.2) `Cisco-IOS-XE-wireless-urwb-cfg`

- **First appears in:** 17.18.1
- **Namespace:** `http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-urwb-cfg`
- **Prefix:** `wireless-urwb-cfg`
- **Revisions:** 2025-07-01
- **Cisco semver:** 1.0.0
- **Source:** [reference/xe/17181/Cisco-IOS-XE-wireless-urwb-cfg.yang](reference/xe/17181/Cisco-IOS-XE-wireless-urwb-cfg.yang)

**Top-level schema counts:** grouping=2, container=6, list=2

**Top-level data containers/lists:** `mob`, `mpls`, `mpo`, `ethertype-lists`, `urwb-cfg-data`, `urwb-profiles`, `ethertype-list`, `urwb-profile`

**Groupings:** `st-ethertype-list`, `urwb-profile`

**Leaves (7 total):**

| Kind | Name | Type | Default | Units | Description |
|---|---|---|---|---|---|
| leaf | `ethertype` | `uint16` | - | - | This value indicates the ether type used |
| leaf | `profile-name` | `string` | - | - | URWB profile name |
| leaf | `descp` | `string` | - | - | Description for URWB profile |
| leaf | `enabled` | `boolean` | false | - | This value indicates whether URWB feature is enabled |
| leaf | `passphr` | `string` | - | - | This value indicates the URWB network-key |
| leaf | `mcast` | `wireless-enum-types:urwb-mcast` | urwb-mcast-dis | - | URWB multicast configuration |
| leaf | `strong-netkey` | `boolean` | false | - | Indicates whether strong network key is enabled |

### 4.3) `Cisco-IOS-XE-wireless-urwb-common-types`

- **First appears in:** 17.18.1
- **Namespace:** `http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-urwb-common-types`
- **Prefix:** `wireless-urwb-common-types`
- **Revisions:** 2025-07-01
- **Cisco semver:** 1.0.0
- **Source:** [reference/xe/17181/Cisco-IOS-XE-wireless-urwb-common-types.yang](reference/xe/17181/Cisco-IOS-XE-wireless-urwb-common-types.yang)

**Top-level schema counts:** grouping=5

**Groupings:** `st-urwb-mob`, `st-urwb-mpls`, `st-urwb-mpo`, `st-urwb-radio`, `st-urwb-chan-list-entry`

**Leaves (35 total):**

| Kind | Name | Type | Default | Units | Description |
|---|---|---|---|---|---|
| leaf | `role` | `wireless-enum-types:urwb-mob-mode` | urwb-mob-base | - | This value indicates role of backhaul device |
| leaf | `scan-idle` | `uint32` | 0 | seconds | This value indicated the time of the periodic background channel scanning |
| leaf | `scan-after` | `uint32` | 0 | milliseconds | This value indicates the timeout for running an active scanning when the device is isolated from the infrastructure |
| leaf | `scan-rssi-th` | `uint32` | 0 | dBm | This value depicts RSSI threshold for active scanning |
| leaf | `warmup` | `uint32` | 30000 | milliseconds | This value depicts warm up time before accepting/initiating handoff |
| leaf | `timeout` | `uint16` | 800 | milliseconds | This value depicts timeout for candidate infrastructure units |
| leaf | `rssi-dhi` | `uint16` | 6 | dBm | This value indicates mobility handoff hysteresis high threshold value |
| leaf | `rssi-dlo` | `uint16` | 3 | - | This value indicates mobility handoff hysteresis low threshold value |
| leaf | `rssi-dth` | `uint16` | 35 | dBm | This value indicates low or high threshold value |
| leaf | `ra-red` | `uint8` | 1 | - | This value indicates level of redundancy for route advertisement signalling |
| leaf | `bc-eth` | `wireless-enum-types:urwb-mob-bce` | urwb-mbce-dis | - | Configure handoff when all ethernet ports are disconnected |
| leaf | `bc-crd` | `wireless-enum-types:urwb-mob-bcc` | urwb-mbcc-dis | - | Configure handoff when coordinator is unreachable |
| leaf | `ha-en` | `boolean` | false | - | This value indicates whether high availability is enabled on the backhaul radio |
| leaf | `ha-timeout` | `uint16` | 100 | - | This value indicates MPLS high availability timeout |
| leaf | `uni-fl` | `boolean` | false | - | This value indicates MPLS unicast flood is enabled |
| leaf | `uni-fl-l` | `boolean` | false | - | This value indicates MPLS unicast flood limits |
| leaf | `eth-1` | `boolean` | false | - | This value indicates ethernet I frames forwarding |
| leaf | `eth-fm` | `wireless-enum-types:urwb-efm` | urwb-efm-none | - | This value indicates the method of configuration for the ethernet filter |
| leaf | `status` | `wireless-enum-types:urwb-mpo-st` | urwb-mpo-dis | - | This value indicates whether MPO is enabled on the backhaul radio |
| leaf | `max-links` | `uint8` | 2 | - | This value indicated the maximum number of MPO links on the backhaul radio |
| leaf | `min-rssi` | `int8` | 20 | dBm | This value indicates minimum RSSI to establish MPO redundant links |
| leaf | `class-cs` | `uint8` | 6 | - | This value indicates class-of-service of traffic to protect with MPO redundancy |
| leaf | `tlmtry` | `boolean` | false | - | This value indicates MPO telemetry is enabled |
| leaf | `role` | `wireless-enum-types:enm-radio-urwb-role` | urwb-rad-role-none | - | This value indicates URWB radio role |
| leaf | `band` | `wireless-types:enm-ewlc-dot11-radio-band` | dot11-invalid-band | - | This value indicates URWB radio band |
| leaf | `chan` | `uint16` | 1 | - | This value indicates URWB channel |
| leaf | `c-width` | `wireless-enum-types:rrm-chan-width` | rrm-channel-width-20-mhz | MHz | This value indicates URWB channel width |
| leaf | `crypto` | `wireless-enum-types:enm-radio-urwb-crypto` | urwb-rad-crypt-fxkey | - | This value indicates AES key type |
| leaf | `kc-rt` | `uint16` | 15 | seconds | This value indicates key control rotation timeout |
| leaf | `rssi-th` | `uint8` | 0 | dBm | This value indicates RSSI threshold  for PTMP scanning |
| leaf | `autoscan` | `boolean` | false | - | This value indicates whether autoscan is enabled for PTMP |
| leaf | `cl-id` | `string` | CiscoURWB | - | This value indicates cluster id for PTMP |
| leaf | `tw-id` | `string` | - | - | This value indicates tower id for PTMP |
| leaf | `chan` | `uint16` | - | - | This value indicates URWB channel number |
| leaf | `c-width` | `uint16` | - | MHz | This value indicates URWB channel width |

### 4.4) `Cisco-IOS-XE-wireless-urwbnet-oper`

- **First appears in:** 17.18.1
- **Namespace:** `http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-urwbnet-oper`
- **Prefix:** `wireless-oper-urwbnet`
- **Revisions:** 2025-07-01
- **Cisco semver:** 1.0.0
- **Source:** [reference/xe/17181/Cisco-IOS-XE-wireless-urwbnet-oper.yang](reference/xe/17181/Cisco-IOS-XE-wireless-urwbnet-oper.yang)

**Top-level schema counts:** typedef=6, grouping=16, container=15, list=12

**Top-level data containers/lists:** `intf-id`, `id`, `prim-id`, `tx-wfm`, `rx-wfm`, `link-id`, `rx-stats`, `tx-stats`, `id`, `id`, `lnk-id`, `id`, `coord-id`, `gw`, `urwbnet-oper-data`, `sec-mesh-id`, `peer`, `node-if`, `urwbnet-conn-dev`, `urwbnet-lnk-id`, `urwbnet-node`, `urwbnet-coord-routes`, `urwbnet-fixed-links`, `urwbnet-mobility-links`, `urwbnet-wlink-stats`, `urwbnet-stats`, `urwbnet-node-g`

**Typedefs:** `uar`, `urr`, `urwbnet-bw`, `urwb-network-mcstype`, `urwb-network-gi`, `urwb-network-conn-type`

**Groupings:** `st-urwbnet-inaddr`, `st-urwbnet-mesh-id`, `st-urwbnet-link-id`, `st-urwbnet-conn-dev`, `st-urwbnet-node-intf`, `st-urwbnet-mob-link`, `st-urwbnet-wfm`, `st-urwbnet-wl-tx`, `st-urwbnet-wl-rx`, `st-urwbnet-wlink-stats`, `st-urwbnet-fix-lnk`, `st-urwbnet-coord-rt`, `st-urwbnet-node`, `st-urwb-node-link-id`, `st-urwbnet-node-g`, `st-urwbnet-subnet`

**Leaves (46 total):**

| Kind | Name | Type | Default | Units | Description |
|---|---|---|---|---|---|
| leaf | `addr` | `inet:ip-address` | - | - | URWB network interface address |
| leaf | `addr` | `inet:ip-address` | - | - | URWB network mesh identifier address |
| leaf | `src` | `inet:ip-address` | - | - | Source identifier |
| leaf | `dest` | `inet:ip-address` | - | - | Destination identifier |
| leaf | `ip` | `inet:ip-address` | - | - | IP Address of device |
| leaf | `vlan-id` | `uint32` | - | - | Vlan ID of device |
| leaf | `intf-enabled` | `boolean` | - | - | URWB network node interface enable status |
| leaf | `role` | `wireless-oper-urwbnet:urr` | - | - | URWB network node interface radio role |
| leaf | `freq` | `int32` | - | MHz | URWB network node interface radio frequency |
| leaf | `bw` | `wireless-oper-urwbnet:urwbnet-bw` | - | - | URWB network node interface bandwidth |
| leaf | `tx-power` | `int32` | - | dBm | URWB network node interface tx power |
| leaf | `is-tdma` | `boolean` | - | - | URWB network node interface is time division multiple access |
| leaf | `freq-scan` | `boolean` | - | - | URWB network node interface frequency scan status |
| leaf | `client-id` | `int32` | - | - | Client ID |
| leaf | `ho-seq-nu` | `uint32` | - | - | Handoff sequence number |
| leaf | `bw` | `wireless-oper-urwbnet:urwbnet-bw` | - | MHz | Wireless link waveform bandwidth |
| leaf | `mcs` | `wireless-oper-urwbnet:urwb-network-mcstype` | - | - | MCS Type |
| leaf | `mcs-index` | `uint32` | - | - | MCS Index |
| leaf | `gi` | `wireless-oper-urwbnet:urwb-network-gi` | - | nanoseconds/microseconds | Guard Interval |
| leaf | `tstamp` | `yang:date-and-time` | - | - | Time of transmit statistics collection |
| leaf | `sent` | `uint64` | - | packets | Tx packets sent |
| leaf | `failed` | `uint64` | - | - | Tx fail count |
| leaf | `retries` | `uint64` | - | - | Tx retries |
| leaf | `bytes` | `uint64` | - | bytes | Tx bytes |
| leaf | `tstamp` | `yang:date-and-time` | - | - | Time of receive statistics collection |
| leaf | `rssi` | `int32` | - | dBm | Received Signal Strength |
| leaf | `recv` | `uint64` | - | - | Received packet count |
| leaf | `bytes` | `uint64` | - | bytes | Rx bytes |
| leaf | `type` | `wireless-oper-urwbnet:urwb-network-conn-type` | - | - | Type of the link |
| leaf | `index` | `uint32` | - | - | Coordinator route index |
| leaf | `name` | `string` | - | - | URWB network node name |
| leaf | `device-model` | `string` | - | - | URWB network node device model |
| leaf | `role` | `wireless-oper-urwbnet:uar` | - | - | URWB network node role |
| leaf | `ip-addr` | `inet:ip-address` | - | - | URWB network node IP address |
| leaf | `net-mask` | `inet:ip-address` | - | - | URWB network node netmask |
| leaf | `conn-dev-count` | `uint8` | - | - | URWB network connected device count |
| leaf | `rad-role` | `wireless-oper-urwbnet:urr` | - | - | Radio role |
| leaf | `coord-mac` | `yang:mac-address` | - | - | Coordinator mac address of the network node |
| leaf | `dev-count` | `uint32` | - | - | Connected device count |
| leaf | `mac` | `yang:mac-address` | - | - | Coordinator MAC address |
| leaf | `nodes-cnt` | `uint32` | - | - | URWB network node count |
| leaf | `coord-rt-cnt` | `uint32` | - | - | URWB network coordinator route count |
| leaf | `fix-lnk-cnt` | `uint32` | - | - | URWB network fixed link count |
| leaf | `mob-lnk-cnt` | `uint32` | - | - | URWB network mobility link count |
| leaf | `wlinks-cnt` | `uint32` | - | - | URWB wireless link count |
| leaf | `coord-name` | `string` | - | - | URWB coordinator AP name |

### 4.5) `Cisco-IOS-XE-wireless-wat-cfg`

- **First appears in:** 17.18.1
- **Namespace:** `http://cisco.com/ns/yang/Cisco-IOS-XE-wireless-wat-cfg`
- **Prefix:** `ios-xe-wat-cfg`
- **Revisions:** 2025-07-01
- **Cisco semver:** 1.0.0
- **Source:** [reference/xe/17181/Cisco-IOS-XE-wireless-wat-cfg.yang](reference/xe/17181/Cisco-IOS-XE-wireless-wat-cfg.yang)

**Top-level schema counts:** grouping=1, container=2

**Top-level data containers/lists:** `wat-cfg-data`, `wat-config`

**Groupings:** `wat-config`

**Leaves (3 total):**

| Kind | Name | Type | Default | Units | Description |
|---|---|---|---|---|---|
| leaf | `wat-enable` | `boolean` | true | - | Enable WAT at global level |
| leaf | `te-conn-str` | `string` | - | - | Represents the connection string used by the ThousandEyes agent for
         for communication with the ThousandEyes cloud |
| leaf | `te-download-url` | `string` | https://downloads.thousandeyes.com/endpointagent/iox/arm64/latest.tar | - | ThousandEyes endpoint URL from which the WAT manager download the
         ThousandEyes agent IOx container |

## 5) Consolidated Constraint Changes (BIC, 17.15.1 -> 17.18.1)

Backward Incompatible Changes (BIC) -- predominantly `must` / `length` / `pattern` constraint tightenings and the one obsoleted XPath -- are listed here grouped by module, with all intermediate-release deltas folded together. **19 modules** are affected.

For each module, every release in which a BIC was published contributes a sub-block; if you are coming directly from 17.15.1 you will need to satisfy the union of all sub-blocks for that module.

### `Cisco-IOS-XE-wireless-access-point-oper`

_Constraint changes introduced in: **17.18.1**_

<details><summary>17.18.1 BIC (<a href="reference/xe/17181/BIC/Cisco-IOS-XE-wireless-access-point-oper.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-access-point-oper.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

- access-point-oper-data/stgrd-upg-report/stgrd-upgd-ap

*Description*

Status changed from current to obsolete.

**XPaths Modified**

*Description*

</details>

### `Cisco-IOS-XE-wireless-ap-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-ap-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-ap-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-ap-rule-priority-config(grouping)/priority

*Description*

The range '[(0, 1023)]' is added

</details>

### `Cisco-IOS-XE-wireless-ap-types`

_Constraint changes introduced in: **17.17.1 -> 17.18.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-ap-types.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-ap-types.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-rogue-params(grouping)/profile-name
- st-traffic-limit-cfg(grouping)/max1x-session-limit-per-ap
- st-user-mgmt-cfg(grouping)/password

*Description*

- A new length expression '0..32' added
- The range '[(0, 255)]' is added
- A new must expression added

</details>

<details><summary>17.18.1 BIC (<a href="reference/xe/17181/BIC/Cisco-IOS-XE-wireless-ap-types.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-ap-types.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-ap-prof-country-cfg(grouping)/country-code
- st-login-credentials-cfg(grouping)/dot1x-password
- st-rogue-params(grouping)/pmf-deauth

*Description*

The must expression is more constrained than before.

</details>

### `Cisco-IOS-XE-wireless-apf-cfg`

_Constraint changes introduced in: **17.17.1 -> 17.18.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-apf-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-apf-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- apf-cfg-data/apf/https-custom-port

*Description*

A new must expression added.

</details>

<details><summary>17.18.1 BIC (<a href="reference/xe/17181/BIC/Cisco-IOS-XE-wireless-apf-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-apf-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-apf(grouping)/network-name

*Description*

New length expression added.

</details>

### `Cisco-IOS-XE-wireless-cts-sxp-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-cts-sxp-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-cts-sxp-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- cts-sxp-cfg-data/cts-sxp-configuration/cts-sxp-config/listener-maximum-holdtime

*Description*

A new must expression added

</details>

### `Cisco-IOS-XE-wireless-dot11-cfg`

_Constraint changes introduced in: **17.17.1 -> 17.18.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-dot11-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-dot11-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- dot11-cfg-data/dot11-entries/dot11-entry/cac-voice-max-bandwidth
- dot11-cfg-data/dot11-entries/dot11-entry/dot11ac-cfg/vht-enable
- dot11-cfg-data/dot11-entries/dot11-entry/dot11ac-cfg/vht-enable
- dot11-cfg-data/dot11-entries/dot11-entry/dot11ax-cfg/he-enable
- dot11-cfg-data/dot11-entries/dot11-entry/dot11ax-cfg/he-enable
- dot11-cfg-data/dot11-entries/dot11-entry/dot11ax-cfg/he-enable
- dot11-cfg-data/dot11-entries/dot11-entry/dot11ax-cfg/he-enable
- dot11-cfg-data/dot11-entries/dot11-entry/ht-cfg/dot11n-enabled
- dot11-cfg-data/dot11-entries/dot11-entry/ht-cfg/dot11n-enabled
- dot11-cfg-data/dot11-entries/dot11-entry/ht-cfg/dot11n-enabled
- dot11-cfg-data/dot11-entries/dot11-entry/ht-cfg/dot11n-enabled

*Description*

A new must expression added.

</details>

<details><summary>17.18.1 BIC (<a href="reference/xe/17181/BIC/Cisco-IOS-XE-wireless-dot11-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-dot11-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- dot11-cfg-data/configured-countries/configured-country/country-code

*Description*

Must expression more constrained than before.

</details>

### `Cisco-IOS-XE-wireless-flex-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-flex-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-flex-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- flex-cfg-data/flex-policy-entries/flex-policy-entry/if-name-vlan-ids/if-name-vlan-id/acl-name-in
- flex-cfg-data/flex-policy-entries/flex-policy-entry/if-name-vlan-ids/if-name-vlan-id/acl-name-out

*Description*

The must expression may be more constrained than before

</details>

### `Cisco-IOS-XE-wireless-gw-system-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-gw-system-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-gw-system-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- gw-system-cfg-data/gw-dstore-info/gw-dstore

*Description*

The max-elements '1' is added

</details>

### `Cisco-IOS-XE-wireless-mobility-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-mobility-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-mobility-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- mobility-cfg-data/mobility-groups/mobility-group/multicast-addressv6

*Description*

Must expression more constrained than before.

</details>

### `Cisco-IOS-XE-wireless-mstream-cfg`

_Constraint changes introduced in: **17.16.1**_

<details><summary>17.16.1 BIC (<a href="reference/xe/17161/BIC/Cisco-IOS-XE-wireless-mstream-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-mstream-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- mstreamglob(grouping)/note
- mstreamglob(grouping)/url

*Description*

A new length expression '0..128' is added.

- mstreamglob(grouping)/phone

*Description*

A new length expression '0..30' added

- mstreamglob(grouping)/email

*Description*

A new length expression '0..64' added

- mstream-cfg-data/mstream-groups/mstream-group/end-ip-addr
- mstream-cfg-data/mstream-groups/mstream-group/start-ip-addr
- mstreamgrp(grouping)/end-ip-addr
- mstreamgrp(grouping)/start-ip-addr

*Description*

Must expression is more constrained than before.

</details>

### `Cisco-IOS-XE-wireless-radio-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-radio-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-radio-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-radio-profile(grouping)/dtim-period

*Description*

The range '[(1, 255)]' is added

</details>

### `Cisco-IOS-XE-wireless-rf-cfg`

_Constraint changes introduced in: **17.16.1 -> 17.17.1**_

<details><summary>17.16.1 BIC (<a href="reference/xe/17161/BIC/Cisco-IOS-XE-wireless-rf-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-rf-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- rfprofile(grouping)/description

*Description*

A new length expression '0..64' added

- rfprofile(grouping)/name

*Description*

A new length expression '1..32' added

- st-atf-policy(grouping)/atfpolicy-name

*Description*

Length expression may be more constrained than before. Old length '0..32' new length '0..31'

</details>

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-rf-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-rf-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- rf-cfg-data/rf-profile-default-entries/rf-profile-default-entry/band-select-client-mid-rssi
- rf-cfg-data/rf-profiles/rf-profile/band-select-client-mid-rssi
- rf-cfg-data/rf-profiles/rf-profile/channel-width-min
- rf-cfg-data/rf-profiles/rf-profile/status
- rf-cfg-data/rf-profiles/rf-profile/status

*Description*

A new must expression added.

</details>

### `Cisco-IOS-XE-wireless-rlan-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-rlan-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-rlan-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- rlan-cfg-data/rlan-configs/rlan-config/profile-name

*Description*

A new must expression added

</details>

### `Cisco-IOS-XE-wireless-rrm-cfg`

_Constraint changes introduced in: **17.17.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-rrm-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-rrm-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- rrm-defaultlradcfg-config(grouping)/automatic-cfg

*Description*

- The range '[(1, 2)]' is  added

</details>

### `Cisco-IOS-XE-wireless-site-cfg`

_Constraint changes introduced in: **17.17.1 -> 17.18.1**_

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-site-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-site-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- ap-cfg-profile(grouping)/user-mgmt/password
- ap-priming-profile(grouping)/primary-wlc-ip
- ap-priming-profile(grouping)/secondary-wlc-ip
- ap-priming-profile(grouping)/tertiary-wlc-ip
- site-cfg-data/ap-cfg-profiles/ap-cfg-profile/user-mgmt/password
- site-cfg-data/ap-priming-profiles/ap-priming-profile/primary-wlc-ip
- site-cfg-data/ap-priming-profiles/ap-priming-profile/secondary-wlc-ip
- site-cfg-data/ap-priming-profiles/ap-priming-profile/tertiary-wlc-ip

*Description*

A new must expression added.

- ap-cfg-profile(grouping)/ap-packet-capture-profile
- st-rogue-params(grouping)/profile-name

*Description*

A new length expression '0..32' added

- st-traffic-limit-cfg(grouping)/max1x-session-limit-per-ap

*Description*

The range '[(0, 255)]' is  added

</details>

<details><summary>17.18.1 BIC (<a href="reference/xe/17181/BIC/Cisco-IOS-XE-wireless-site-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-site-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- site-cfg-data/ap-cfg-profiles/ap-cfg-profile/ap-country/country-code
- site-cfg-data/ap-cfg-profiles/ap-cfg-profile/login-credentials/dot1x-password
- site-cfg-data/ap-cfg-profiles/ap-cfg-profile/rogue-detection/pmf-deauth

*Description*

Must expression more constrained than before.

</details>

### `Cisco-IOS-XE-wireless-tunnel-cfg`

_Constraint changes introduced in: **17.16.1**_

<details><summary>17.16.1 BIC (<a href="reference/xe/17161/BIC/Cisco-IOS-XE-wireless-tunnel-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-tunnel-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- wireless-tunnel-cfg/tunnel-domain-cfgs/tunnel-domain-cfg/primary-tunnel-name
- wireless-tunnel-cfg/tunnel-domain-cfgs/tunnel-domain-cfg/secondary-tunnel-name
- wireless-tunnel-cfg/tunnel-profiles/tunnel-profile/cfg/aaa-accounting-proxy

*Description*

A new must expression added.

</details>

### `Cisco-IOS-XE-wireless-tunnel-types`

_Constraint changes introduced in: **17.16.1**_

<details><summary>17.16.1 BIC (<a href="reference/xe/17161/BIC/Cisco-IOS-XE-wireless-tunnel-types.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-tunnel-types.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-tunnel-profile-base(grouping)/aaa-accounting-proxy

*Description*

A new must expression added.

</details>

### `Cisco-IOS-XE-wireless-types`

_Constraint changes introduced in: **17.18.1**_

<details><summary>17.18.1 BIC (<a href="reference/xe/17181/BIC/Cisco-IOS-XE-wireless-types.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-types.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-lsc-renew(grouping)/one-shot
- st-lsc-renew(grouping)/staggered

*Description*

Must expression more constrained then before.

</details>

### `Cisco-IOS-XE-wireless-wlan-cfg`

_Constraint changes introduced in: **17.16.1 -> 17.17.1 -> 17.18.1**_

<details><summary>17.16.1 BIC (<a href="reference/xe/17161/BIC/Cisco-IOS-XE-wireless-wlan-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-wlan-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- st-mdns-sd-service-policy(grouping)/policy-name

*Description*

This length expression may be more constrained than before. Old length '1..64' new length '1..164'

- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/akm-owe
- wlan-profile(grouping)/akm-owe

*Description*

This must expression may be more constrained than before

</details>

<details><summary>17.17.1 BIC (<a href="reference/xe/17171/BIC/Cisco-IOS-XE-wireless-wlan-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-wlan-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- wlan-cfg-data/wlan-cfg-entries(container)/wlan-cfg-entry/psk-key-type
- wlan-profile(grouping)/psk-key-type

*Description*

The must expression more constraint than before

</details>

<details><summary>17.18.1 BIC (<a href="reference/xe/17181/BIC/Cisco-IOS-XE-wireless-wlan-cfg.md">source</a>)</summary>

**Cisco-IOS-XE-wireless-wlan-cfg.yang**

- [XPaths Obsoleted](#xpaths-obsoleted)
- [XPaths Deprecated](#xpaths-deprecated)
- [XPaths Modified](#xpaths-modified)
- [XPaths Added](#xpaths-added)

**XPaths Deprecated**

*Description*

- wlan-profile(grouping)/webauth-ipv4-preauth-acl
- wlan-profile(grouping)/webauth-ipv6-preauth-acl

*Description*

New length expression 0...32 is added.

*Description*

New must expression cannot be added.

- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-psk
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/easy-psk
- wlan-cfg-data/wlan-policies/wlan-policy/dhcp-params/ap-ethmac
- wlan-cfg-data/wlan-policies/wlan-policy/dhcp-params/ap-location
- wlan-cfg-data/wlan-policies/wlan-policy/dhcp-params/apmac
- wlan-cfg-data/wlan-policies/wlan-policy/dhcp-params/apname
- wlan-cfg-data/wlan-policies/wlan-policy/dhcp-params/policy-tag
- wlan-cfg-data/wlan-policies/wlan-policy/dhcp-params/ssid
- wlan-cfg-data/wlan-policies/wlan-policy/dhcp-params/vlan-id
- wlan-profile(grouping)/auth-key-mgmt-psk
- wlan-profile(grouping)/easy-psk

*Description*

A new pattern expression '([!-~]([ -~]*[!-~])?)?' cannot be added

- wlan-profile(grouping)/webauth-ipv4-preauth-acl
- wlan-profile(grouping)/webauth-ipv6-preauth-acl

*Description*

length expression may be more constrained than before

- st-dot11be-profile(grouping)/profile-name

*Description*

The must expression is more constrained than before.

- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/akm-ft-sae-ext-key
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/akm-owe
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/akm-sae-ext-key
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/apf-vap-id-data/wlan-status
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/apf-vap-id-data/wlan-status
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/apf-vap-id-data/wlan-status
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/apf-vap-id-data/wlan-status
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-ft-sae
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/auth-key-mgmt-sae
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/beacon-protection-enabled
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/osen
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/psk-key-type
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/transition-mode-wlan-id
- wlan-cfg-data/wlan-cfg-entries/wlan-cfg-entry/wpa3-enabled

</details>


## 7) XPath Appendix (Hotspot Modules + New Modules)

Best-effort RESTCONF / gNMI subscription XPaths for every leaf, leaf-list, container, and list **added in 17.18.1** within the seven hotspot modules and the five new modules. Generated by [tools/wireless_yang_delta.py](tools/wireless_yang_delta.py) using an indent-aware YANG scanner -- see [Section 9](#9-methodology-and-sources) for parsing rules.

**How to read the XPath column:**

- Entries beginning with `/<module-prefix>:` are absolute paths under the module's root data container -- these are **directly subscribable** in a `telemetry ietf subscription` config.
- Entries beginning with `[grouping] (<grouping-name>)/...` are defined inside a `grouping` block. To get a subscribable path, find every `uses <grouping-name>` site in the parent module (typically inside a `container` or `list` block) and prepend that container's path. The grouping name is shown so you can grep for it in the source YANG.
- Some leaves appear in multiple groupings; up to five sites are listed per row.

### `Cisco-IOS-XE-wireless-access-point-oper`

| Kind | Name | XPath(s) |
|---|---|---|
| container | `ap-license` | `[grouping] (capwap-wtp-data)/ap-license` |
| container | `dot11k-req-stats-radio` | `[grouping] (radio-statistics)/dot11k-req-stats-radio` |
| container | `dot11v-req-stats-radio` | `[grouping] (radio-statistics)/dot11v-req-stats-radio` |
| leaf | `airtime-used-cum` | `[grouping] (radio-statistics)/airtime-used-cum` |
| leaf | `ap-beam-state` | `[grouping] (wtp-rf-tag-info)/ap-beam-state` |
| leaf | `ap-env-mode` | `[grouping] (capwap-wtp-data)/ap-env-mode` |
| leaf | `ap-nextunnel-state` | `[grouping] (capwap-wtp-data)/ap-nextunnel-state` |
| leaf | `bp-enabled` | `[grouping] (ewlc-vap-operational-config)/bp-enabled` |
| leaf | `client-ipv6-addr` | `[grouping] (st-ap-next-tunnel-cfg)/client-ipv6-addr` |
| leaf | `client-last-restart` | `[grouping] (st-ap-nextunnel-state-data)/client-last-restart` |
| leaf | `config-server-url` | `[grouping] (st-ap-next-tunnel-cfg)/config-server-url` |
| leaf | `cumulative-rx-bytes` | `[grouping] (radio-statistics)/cumulative-rx-bytes` |
| leaf | `cumulative-tx-bytes` | `[grouping] (radio-statistics)/cumulative-tx-bytes` |
| leaf | `cw-lic-ooc-reason` | `[grouping] (cw-license-info)/cw-lic-ooc-reason` |
| leaf | `cw-lic-required` | `[grouping] (cw-license-info)/cw-lic-required` |
| leaf | `cw-lic-state` | `[grouping] (cw-license-info)/cw-lic-state` |
| leaf | `data-rate` | `[grouping] (radio-statistics)/data-rate` |
| leaf | `disc-meraki-l2-pkts` | `[grouping] (st-capwap-discovery-pkt-info)/disc-meraki-l2-pkts` |
| leaf | `disc-meraki-pkts` | `[grouping] (st-capwap-discovery-pkt-info)/disc-meraki-pkts` |
| leaf | `expiry-time` | `[grouping] (st-ap-lsc-key)/expiry-time` |
| leaf | `failed-ap-count` | `[grouping] (stgrd-upg-report)/failed-ap-count` |
| leaf | `feature-type` | `[grouping] (stgrd-upg-report)/feature-type` |
| leaf | `fetch-fail-reason` | `[grouping] (st-ap-next-tunnel-cfg)/fetch-fail-reason` |
| leaf | `fetch-state` | `[grouping] (st-ap-next-tunnel-cfg)/fetch-state` |
| leaf | `last-fetch` | `[grouping] (st-ap-next-tunnel-cfg)/last-fetch` |
| leaf | `last-renew-attempt` | `[grouping] (st-ap-lsc)/last-renew-attempt` |
| leaf | `last-renew-failure-rc` | `[grouping] (st-ap-lsc)/last-renew-failure-rc` |
| leaf | `lsc-prov-workflow` | `[grouping] (st-ap-lsc)/lsc-prov-workflow` |
| leaf | `lsc-usage` | `[grouping] (st-ap-lsc)/lsc-usage` |
| leaf | `next-fetch` | `[grouping] (st-ap-next-tunnel-cfg)/next-fetch` |
| leaf | `primary-last-change` | `[grouping] (st-ap-nextunnel-state-data)/primary-last-change` |
| leaf | `primary-state` | `[grouping] (st-ap-nextunnel-state-data)/primary-state` |
| leaf | `primary-url` | `[grouping] (st-ap-next-tunnel-cfg)/primary-url` |
| leaf | `radio-uptime-cum` | `[grouping] (radio-statistics)/radio-uptime-cum` |
| leaf | `secondary-last-change` | `[grouping] (st-ap-nextunnel-state-data)/secondary-last-change` |
| leaf | `secondary-state` | `[grouping] (st-ap-nextunnel-state-data)/secondary-state` |
| leaf | `secondary-url` | `[grouping] (st-ap-next-tunnel-cfg)/secondary-url` |
| leaf | `serial-iter-num` | `[grouping] (stgrd-upg-upgd-ap)/serial-iter-num` |
| leaf | `server-ipv6-addr` | `[grouping] (st-ap-next-tunnel-cfg)/server-ipv6-addr` |
| leaf | `sp-static-chan` | `[grouping] (ewlc-radio-operation-ext-config)/sp-static-chan` |
| leaf | `sp-static-chan-width` | `[grouping] (ewlc-radio-operation-ext-config)/sp-static-chan-width` |
| leaf | `sp-static-txpwr` | `[grouping] (ewlc-radio-operation-ext-config)/sp-static-txpwr` |
| leaf | `storage-usage` | `[grouping] (ap-sys-stats-data)/storage-usage` |
| leaf | `tmp-usage` | `[grouping] (ap-sys-stats-data)/tmp-usage` |
| leaf | `urwb-cfg-status` | `[grouping] (capwap-wtp-data)/urwb-cfg-status` |
| list | `ap-lsc` | `/wireless-access-point-oper:access-point-oper-data/ap-lsc` |
| list | `ap-nextunnel` | `/wireless-access-point-oper:access-point-oper-data/ap-nextunnel` |
| list | `ap-nextunnel-if-info` | `/wireless-access-point-oper:access-point-oper-data/ap-nextunnel-if-info` |
| list | `ap-nextunnel-state-info` | `/wireless-access-point-oper:access-point-oper-data/ap-nextunnel-state-info` |
| list | `ap-port-auth-info` | `[grouping] (capwap-wtp-data)/ap-port-auth-info` |
| list | `comp-ap` | `[grouping] (stgrd-upg-report)/comp-ap` |
| list | `radio-oper-ext-data` | `/wireless-access-point-oper:access-point-oper-data/radio-oper-ext-data` |
| list | `stgrd-upg-failed-ap` | `[grouping] (stgrd-upg-report)/stgrd-upg-failed-ap` |

### `Cisco-IOS-XE-wireless-ap-types`

| Kind | Name | XPath(s) |
|---|---|---|
| leaf | `acl-name-v4` | `[grouping] (st-ap-mgmt-acl)/acl-name-v4` |
| leaf | `acl-name-v6` | `[grouping] (st-ap-mgmt-acl)/acl-name-v6` |
| leaf | `config` | `[grouping] (st-ap-onboard-cfg)/config` |
| leaf | `eap-status-code` | `[grouping] (st-ap-port-auth-info)/eap-status-code` |
| leaf | `fast-switching` | `[grouping] (st-ap-prof-rlan-cfg)/fast-switching` |
| leaf | `kcd-dlimit` | `[grouping] (st-kernel-coredump-cfg)/kcd-dlimit` |
| leaf | `pmf-offchannel` | `[grouping] (st-rogue-params)/pmf-offchannel` |
| leaf | `port` | `[grouping] (st-ap-port-auth-info)/port` |
| leaf | `port-mac` | `[grouping] (st-ap-port-auth-info)/port-mac` |
| leaf | `size` | `[grouping] (st-ap-pmtu)/size` |
| leaf | `token` | `[grouping] (st-spaces-conn-cfg)/token` |
| leaf | `token-type` | `[grouping] (st-spaces-conn-cfg)/token-type` |

### `Cisco-IOS-XE-wireless-client-global-oper`

| Kind | Name | XPath(s) |
|---|---|---|
| leaf | `ap-mac-addr` | `[grouping] (client-cnsld-data)/ap-mac-addr` |
| leaf | `assoc-requests-received` | `[grouping] (client-statistics)/assoc-requests-received` |
| leaf | `auth-key-mgmt` | `[grouping] (client-cnsld-data)/auth-key-mgmt` |
| leaf | `cipher-suite` | `[grouping] (client-cnsld-data)/cipher-suite` |
| leaf | `client-l2auth-failures` | `[grouping] (client-statistics)/client-l2auth-failures` |
| leaf | `client-l2auth-success` | `[grouping] (client-statistics)/client-l2auth-success` |
| leaf | `client-l3auth-attempts` | `[grouping] (client-statistics)/client-l3auth-attempts` |
| leaf | `client-l3auth-failures` | `[grouping] (client-statistics)/client-l3auth-failures` |
| leaf | `client-mab-attempts` | `[grouping] (client-statistics)/client-mab-attempts` |
| leaf | `client-mab-failures` | `[grouping] (client-statistics)/client-mab-failures` |
| leaf | `client-state-associated` | `[grouping] (client-statistics)/client-state-associated` |
| leaf | `client-state-deleted` | `[grouping] (client-statistics)/client-state-deleted` |
| leaf | `client-state-run` | `[grouping] (client-statistics)/client-state-run` |
| leaf | `client-state-start` | `[grouping] (client-statistics)/client-state-start` |
| leaf | `client-type` | `[grouping] (client-cnsld-data)/client-type` |
| leaf | `co-state` | `[grouping] (client-cnsld-data)/co-state` |
| leaf | `cur-chan` | `[grouping] (client-cnsld-data)/cur-chan` |
| leaf | `data-retries` | `[grouping] (client-cnsld-data)/data-retries` |
| leaf | `ft-localauth-attempts` | `[grouping] (client-statistics)/ft-localauth-attempts` |
| leaf | `ip-addr` | `[grouping] (client-cnsld-data)/ip-addr` |
| leaf | `mm-client-role` | `[grouping] (client-cnsld-data)/mm-client-role` |
| leaf | `ms-bssid` | `[grouping] (client-cnsld-data)/ms-bssid` |
| leaf | `ms-radio-type` | `[grouping] (client-cnsld-data)/ms-radio-type` |
| leaf | `multi-link-client` | `[grouping] (client-cnsld-data)/multi-link-client` |
| leaf | `pkts-tx` | `[grouping] (client-cnsld-data)/pkts-tx` |
| leaf | `policy-profile` | `[grouping] (client-cnsld-data)/policy-profile` |
| leaf | `res-vlan-name` | `[grouping] (client-cnsld-data)/res-vlan-name` |
| leaf | `rssi` | `[grouping] (client-cnsld-data)/rssi` |
| leaf | `slot-id` | `[grouping] (client-cnsld-data)/slot-id` |
| leaf | `snr` | `[grouping] (client-cnsld-data)/snr` |
| leaf | `speed` | `[grouping] (client-cnsld-data)/speed` |
| leaf | `user-name` | `[grouping] (client-cnsld-data)/user-name` |
| leaf | `wlan-profile` | `[grouping] (client-cnsld-data)/wlan-profile` |
| leaf | `wpa-version` | `[grouping] (client-cnsld-data)/wpa-version` |
| leaf-list | `ipv6-addr` | `[grouping] (client-cnsld-data)/ipv6-addr` |
| list | `client-cnsld-data` | `/wireless-client-global-oper:client-global-oper-data/client-cnsld-data` |

### `Cisco-IOS-XE-wireless-rogue-cfg`

| Kind | Name | XPath(s) |
|---|---|---|
| container | `ap-cfg` | `[grouping] (rogue-global)/ap-cfg` |
| container | `client-cfg` | `[grouping] (rogue-global)/client-cfg` |
| leaf | `actv-probe` | `[grouping] (rogue-authz-cl-alarms)/actv-probe` |
| leaf | `actv-wlan-scan` | `[grouping] (rogue-authz-cl-alarms)/actv-wlan-scan` |
| leaf | `ap-imprsn` | `[grouping] (rogue-authz-ap-alarms)/ap-imprsn` |
| leaf | `authz-akm` | `[grouping] (rogue-authz-ap-alarms)/authz-akm`<br>`[grouping] (rogue-authz-cl-alarms)/authz-akm` |
| leaf | `authz-ap` | `[grouping] (rogue-authz-ap-alarms)/authz-ap` |
| leaf | `authz-cipher` | `[grouping] (rogue-authz-ap-alarms)/authz-cipher`<br>`[grouping] (rogue-authz-cl-alarms)/authz-cipher` |
| leaf | `authz-clnt` | `[grouping] (rogue-authz-cl-alarms)/authz-clnt` |
| leaf | `authz-mode` | `[grouping] (rogue-global)/authz-mode` |
| leaf | `authz-ssid` | `[grouping] (rogue-authz-ap-alarms)/authz-ssid`<br>`[grouping] (rogue-authz-cl-alarms)/authz-ssid` |
| leaf | `hidden-ssid` | `[grouping] (rogue-authz-ap-alarms)/hidden-ssid` |
| leaf | `hotspot-ics` | `[grouping] (rogue-authz-ap-alarms)/hotspot-ics` |
| leaf | `mac-spoof` | `[grouping] (rogue-authz-cl-alarms)/mac-spoof` |
| leaf | `mesh-detect` | `[grouping] (rogue-authz-ap-alarms)/mesh-detect` |
| leaf | `unauthz-akm` | `[grouping] (rogue-authz-ap-alarms)/unauthz-akm`<br>`[grouping] (rogue-authz-cl-alarms)/unauthz-akm` |
| leaf | `unauthz-ap` | `[grouping] (rogue-authz-ap-alarms)/unauthz-ap` |
| leaf | `unauthz-cipher` | `[grouping] (rogue-authz-ap-alarms)/unauthz-cipher`<br>`[grouping] (rogue-authz-cl-alarms)/unauthz-cipher` |
| leaf | `unauthz-clnt` | `[grouping] (rogue-authz-cl-alarms)/unauthz-clnt` |
| leaf | `unauthz-ssid` | `[grouping] (rogue-authz-ap-alarms)/unauthz-ssid`<br>`[grouping] (rogue-authz-cl-alarms)/unauthz-ssid` |
| leaf | `uncon-clnt` | `[grouping] (rogue-authz-cl-alarms)/uncon-clnt` |
| leaf | `unenc-traffic` | `[grouping] (rogue-authz-cl-alarms)/unenc-traffic` |
| leaf | `weak-proto` | `[grouping] (rogue-authz-ap-alarms)/weak-proto`<br>`[grouping] (rogue-authz-cl-alarms)/weak-proto` |

### `Cisco-IOS-XE-wireless-rogue-oper`

| Kind | Name | XPath(s) |
|---|---|---|
| container | `rogue-akm` | `[grouping] (st-rogue-lrad)/rogue-akm` |
| container | `rogue-cipher` | `[grouping] (st-rogue-lrad)/rogue-cipher` |
| leaf | `ap-drop-urwb-link` | `[grouping] (st-rogue-stats)/ap-drop-urwb-link` |
| leaf | `beacon-interval` | `[grouping] (st-rogue-lrad)/beacon-interval` |
| leaf | `client-mac` | `[grouping] (st-rogue-unconnected-data)/client-mac` |
| leaf | `clnt-syslog` | `[grouping] (st-rogue-unconnected-lrad)/clnt-syslog` |
| leaf | `first-timestamp` | `[grouping] (st-rogue-unconnected-data)/first-timestamp` |
| leaf | `hotspot-type` | `[grouping] (st-rogue-lrad)/hotspot-type` |
| leaf | `iapp-unconnected-client` | `[grouping] (st-rogue-stats)/iapp-unconnected-client` |
| leaf | `last-timestamp` | `[grouping] (st-rogue-unconnected-data)/last-timestamp` |
| leaf | `unconnected-client-count` | `[grouping] (st-rogue-stats)/unconnected-client-count` |
| leaf | `unconnected-client-report` | `[grouping] (st-rogue-stats)/unconnected-client-report` |
| leaf | `unconnected-reports-drop` | `[grouping] (st-rogue-stats)/unconnected-reports-drop` |
| leaf-list | `wpa-cipher` | `[grouping] (st-rogue-cipher)/wpa-cipher` |
| leaf-list | `wpa-support` | `[grouping] (st-rogue-akm)/wpa-support` |
| list | `rogue-unconnected-data` | `/wireless-rogue-oper:rogue-oper-data/rogue-unconnected-data` |
| list | `rogue-unconnected-lrad` | `[grouping] (st-rogue-unconnected-data)/rogue-unconnected-lrad` |

### `Cisco-IOS-XE-wireless-types`

| Kind | Name | XPath(s) |
|---|---|---|
| container | `init-cfg` | `[grouping] (st-uwb-dltdoa-cluster)/init-cfg` |
| container | `invalid-11k-req` | `[grouping] (st-dot11k-req-stats)/invalid-11k-req` |
| container | `invalid-11v-req` | `[grouping] (st-dot11v-req-stats)/invalid-11v-req` |
| container | `resp-cfg` | `[grouping] (st-uwb-dltdoa-cluster)/resp-cfg` |
| leaf | `dot11k-req-assisted-roam` | `[grouping] (st-11k-invalid-req)/dot11k-req-assisted-roam` |
| leaf | `dot11k-req-diff-ap` | `[grouping] (st-11k-invalid-req)/dot11k-req-diff-ap` |
| leaf | `dot11k-req-neigh-list` | `[grouping] (st-11k-invalid-req)/dot11k-req-neigh-list` |
| leaf | `dot11k-req-parse-fail` | `[grouping] (st-11k-invalid-req)/dot11k-req-parse-fail` |
| leaf | `dot11k-req-wl-sfc-info` | `[grouping] (st-11k-invalid-req)/dot11k-req-wl-sfc-info` |
| leaf | `dot11v-req-diff-ap` | `[grouping] (st-11v-invalid-req)/dot11v-req-diff-ap` |
| leaf | `dot11v-req-dms-disabled` | `[grouping] (st-11v-invalid-req)/dot11v-req-dms-disabled` |
| leaf | `due-days` | `[grouping] (st-lsc-renew)/due-days` |
| leaf | `enable` | `[grouping] (st-uwb-dltdoa-cluster-grp)/enable` |
| leaf | `id` | `[grouping] (st-uwb-dltdoa-cluster-grp)/id` |
| leaf | `init-anchor-addr` | `[grouping] (st-uwb-dltdoa-resp)/init-anchor-addr` |
| leaf | `mac-addr` | `[grouping] (st-uwb-dltdoa-anchor)/mac-addr` |
| leaf | `max-rounds` | `[grouping] (st-uwb-dltdoa-cluster-grp)/max-rounds` |
| leaf | `mlo-24ghz` | `[grouping] (st-mlo-group-24ghz)/mlo-24ghz` |
| leaf | `mlo-5ghz` | `[grouping] (st-mlo-group-5ghz)/mlo-5ghz` |
| leaf | `mlo-5ghz-sec` | `[grouping] (st-mlo-group-5ghz-sec)/mlo-5ghz-sec` |
| leaf | `mlo-6ghz` | `[grouping] (st-mlo-group-6ghz)/mlo-6ghz` |
| leaf | `one-shot` | `[grouping] (st-lsc-renew)/one-shot` |
| leaf | `other-invalid-11k-req` | `[grouping] (st-11k-invalid-req)/other-invalid-11k-req` |
| leaf | `other-invalid-11v-req` | `[grouping] (st-11v-invalid-req)/other-invalid-11v-req` |
| leaf | `parent-anchor` | `[grouping] (st-uwb-dltdoa-init)/parent-anchor` |
| leaf | `resp-slot-index` | `[grouping] (st-uwb-dltdoa-resp)/resp-slot-index` |
| leaf | `round-index` | `[grouping] (st-uwb-dltdoa-cluster)/round-index` |
| leaf | `schedular-cal-name` | `[grouping] (st-lsc-renew)/schedular-cal-name` |
| leaf | `slot-index` | `[grouping] (st-uwb-dltdoa-anchor)/slot-index` |
| leaf | `staggered` | `[grouping] (st-lsc-renew)/staggered` |
| leaf | `staggered-iter-expiry` | `[grouping] (st-lsc-renew)/staggered-iter-expiry` |
| leaf | `stratum` | `[grouping] (st-uwb-dltdoa-init)/stratum` |
| leaf | `tot-dot11k-req` | `[grouping] (st-dot11k-req-stats)/tot-dot11k-req` |
| leaf | `tot-dot11v-req` | `[grouping] (st-dot11v-req-stats)/tot-dot11v-req` |
| leaf | `tot-invalid-11k-req` | `[grouping] (st-dot11k-req-stats)/tot-invalid-11k-req` |
| leaf | `tot-invalid-11v-req` | `[grouping] (st-dot11v-req-stats)/tot-invalid-11v-req` |
| leaf | `urwb-profile-name` | `[grouping] (st-urwb-cfg)/urwb-profile-name` |
| leaf | `valid-11k-req` | `[grouping] (st-dot11k-req-stats)/valid-11k-req` |
| leaf | `valid-11v-req` | `[grouping] (st-dot11v-req-stats)/valid-11v-req` |
| leaf | `wat-radio-admin-state` | `[grouping] (st-radio-wat-cfg)/wat-radio-admin-state` |
| list | `cluster` | `[grouping] (st-uwb-dltdoa-cluster-grp)/cluster` |
| list | `resp-anchor` | `[grouping] (st-uwb-dltdoa-init)/resp-anchor` |

### `Cisco-IOS-XE-wireless-urwb-cfg`

| Kind | Name | XPath(s) |
|---|---|---|
| container | `ethertype-lists` | `[grouping] (urwb-profile)/ethertype-lists` |
| container | `mob` | `[grouping] (urwb-profile)/mob` |
| container | `mpls` | `[grouping] (urwb-profile)/mpls` |
| container | `mpo` | `[grouping] (urwb-profile)/mpo` |
| container | `urwb-cfg-data` | `/wireless-urwb-cfg:urwb-cfg-data` |
| container | `urwb-profiles` | `/wireless-urwb-cfg:urwb-cfg-data/urwb-profiles` |
| leaf | `descp` | `[grouping] (urwb-profile)/descp` |
| leaf | `enabled` | `[grouping] (urwb-profile)/enabled` |
| leaf | `ethertype` | `[grouping] (st-ethertype-list)/ethertype` |
| leaf | `mcast` | `[grouping] (urwb-profile)/mcast` |
| leaf | `passphr` | `[grouping] (urwb-profile)/passphr` |
| leaf | `profile-name` | `[grouping] (urwb-profile)/profile-name` |
| leaf | `strong-netkey` | `[grouping] (urwb-profile)/strong-netkey` |
| list | `ethertype-list` | `[grouping] (urwb-profile)/ethertype-lists/ethertype-list` |
| list | `urwb-profile` | `/wireless-urwb-cfg:urwb-cfg-data/urwb-profiles/urwb-profile` |

### `Cisco-IOS-XE-wireless-urwbnet-oper`

| Kind | Name | XPath(s) |
|---|---|---|
| container | `coord-id` | `[grouping] (st-urwbnet-node-g)/coord-id` |
| container | `gw` | `[grouping] (st-urwbnet-subnet)/gw` |
| container | `id` | `[grouping] (st-urwbnet-mob-link)/id`<br>`[grouping] (st-urwbnet-fix-lnk)/id`<br>`[grouping] (st-urwbnet-node)/id`<br>`[grouping] (st-urwbnet-node-g)/id` |
| container | `intf-id` | `[grouping] (st-urwbnet-node-intf)/intf-id` |
| container | `link-id` | `[grouping] (st-urwbnet-wlink-stats)/link-id` |
| container | `lnk-id` | `[grouping] (st-urwb-node-link-id)/lnk-id` |
| container | `prim-id` | `[grouping] (st-urwbnet-mob-link)/prim-id` |
| container | `rx-stats` | `[grouping] (st-urwbnet-wlink-stats)/rx-stats` |
| container | `rx-wfm` | `[grouping] (st-urwbnet-wl-rx)/rx-wfm` |
| container | `tx-stats` | `[grouping] (st-urwbnet-wlink-stats)/tx-stats` |
| container | `tx-wfm` | `[grouping] (st-urwbnet-wl-tx)/tx-wfm` |
| container | `urwbnet-oper-data` | `/wireless-oper-urwbnet:urwbnet-oper-data` |
| leaf | `addr` | `[grouping] (st-urwbnet-inaddr)/addr`<br>`[grouping] (st-urwbnet-mesh-id)/addr` |
| leaf | `bw` | `[grouping] (st-urwbnet-node-intf)/bw`<br>`[grouping] (st-urwbnet-wfm)/bw` |
| leaf | `bytes` | `[grouping] (st-urwbnet-wl-tx)/bytes`<br>`[grouping] (st-urwbnet-wl-rx)/bytes` |
| leaf | `client-id` | `[grouping] (st-urwbnet-mob-link)/client-id` |
| leaf | `conn-dev-count` | `[grouping] (st-urwbnet-node)/conn-dev-count` |
| leaf | `coord-mac` | `[grouping] (st-urwbnet-node-g)/coord-mac` |
| leaf | `coord-name` | `[grouping] (st-urwbnet-subnet)/coord-name` |
| leaf | `coord-rt-cnt` | `[grouping] (st-urwbnet-subnet)/coord-rt-cnt` |
| leaf | `dest` | `[grouping] (st-urwbnet-link-id)/dest` |
| leaf | `dev-count` | `[grouping] (st-urwbnet-node-g)/dev-count` |
| leaf | `device-model` | `[grouping] (st-urwbnet-node)/device-model` |
| leaf | `failed` | `[grouping] (st-urwbnet-wl-tx)/failed` |
| leaf | `fix-lnk-cnt` | `[grouping] (st-urwbnet-subnet)/fix-lnk-cnt` |
| leaf | `freq` | `[grouping] (st-urwbnet-node-intf)/freq` |
| leaf | `freq-scan` | `[grouping] (st-urwbnet-node-intf)/freq-scan` |
| leaf | `gi` | `[grouping] (st-urwbnet-wfm)/gi` |
| leaf | `ho-seq-nu` | `[grouping] (st-urwbnet-mob-link)/ho-seq-nu` |
| leaf | `index` | `[grouping] (st-urwbnet-coord-rt)/index` |
| leaf | `intf-enabled` | `[grouping] (st-urwbnet-node-intf)/intf-enabled` |
| leaf | `ip` | `[grouping] (st-urwbnet-conn-dev)/ip` |
| leaf | `ip-addr` | `[grouping] (st-urwbnet-node)/ip-addr` |
| leaf | `is-tdma` | `[grouping] (st-urwbnet-node-intf)/is-tdma` |
| leaf | `mac` | `[grouping] (st-urwbnet-subnet)/mac` |
| leaf | `mcs` | `[grouping] (st-urwbnet-wfm)/mcs` |
| leaf | `mcs-index` | `[grouping] (st-urwbnet-wfm)/mcs-index` |
| leaf | `mob-lnk-cnt` | `[grouping] (st-urwbnet-subnet)/mob-lnk-cnt` |
| leaf | `name` | `[grouping] (st-urwbnet-node)/name` |
| leaf | `net-mask` | `[grouping] (st-urwbnet-node)/net-mask` |
| leaf | `nodes-cnt` | `[grouping] (st-urwbnet-subnet)/nodes-cnt` |
| leaf | `rad-role` | `[grouping] (st-urwb-node-link-id)/rad-role` |
| leaf | `recv` | `[grouping] (st-urwbnet-wl-rx)/recv` |
| leaf | `retries` | `[grouping] (st-urwbnet-wl-tx)/retries` |
| leaf | `role` | `[grouping] (st-urwbnet-node-intf)/role`<br>`[grouping] (st-urwbnet-node)/role` |
| leaf | `rssi` | `[grouping] (st-urwbnet-wl-rx)/rssi` |
| leaf | `sent` | `[grouping] (st-urwbnet-wl-tx)/sent` |
| leaf | `src` | `[grouping] (st-urwbnet-link-id)/src` |
| leaf | `tstamp` | `[grouping] (st-urwbnet-wl-tx)/tstamp`<br>`[grouping] (st-urwbnet-wl-rx)/tstamp` |
| leaf | `tx-power` | `[grouping] (st-urwbnet-node-intf)/tx-power` |
| leaf | `type` | `[grouping] (st-urwbnet-fix-lnk)/type` |
| leaf | `vlan-id` | `[grouping] (st-urwbnet-conn-dev)/vlan-id` |
| leaf | `wlinks-cnt` | `[grouping] (st-urwbnet-subnet)/wlinks-cnt` |
| list | `node-if` | `[grouping] (st-urwbnet-node)/node-if` |
| list | `peer` | `[grouping] (st-urwbnet-coord-rt)/peer` |
| list | `sec-mesh-id` | `[grouping] (st-urwbnet-mob-link)/sec-mesh-id` |
| list | `urwbnet-conn-dev` | `[grouping] (st-urwbnet-node-g)/urwbnet-conn-dev` |
| list | `urwbnet-coord-routes` | `[grouping] (st-urwbnet-subnet)/urwbnet-coord-routes` |
| list | `urwbnet-fixed-links` | `[grouping] (st-urwbnet-subnet)/urwbnet-fixed-links` |
| list | `urwbnet-lnk-id` | `[grouping] (st-urwbnet-node-g)/urwbnet-lnk-id` |
| list | `urwbnet-mobility-links` | `[grouping] (st-urwbnet-subnet)/urwbnet-mobility-links` |
| list | `urwbnet-node` | `[grouping] (st-urwbnet-subnet)/urwbnet-node` |
| list | `urwbnet-node-g` | `/wireless-oper-urwbnet:urwbnet-oper-data/urwbnet-node-g` |
| list | `urwbnet-stats` | `/wireless-oper-urwbnet:urwbnet-oper-data/urwbnet-stats` |
| list | `urwbnet-wlink-stats` | `[grouping] (st-urwbnet-subnet)/urwbnet-wlink-stats` |

### `Cisco-IOS-XE-wireless-wat-cfg`

| Kind | Name | XPath(s) |
|---|---|---|
| container | `wat-cfg-data` | `/ios-xe-wat-cfg:wat-cfg-data` |
| container | `wat-config` | `/ios-xe-wat-cfg:wat-cfg-data/wat-config` |
| leaf | `te-conn-str` | `[grouping] (wat-config)/te-conn-str` |
| leaf | `te-download-url` | `[grouping] (wat-config)/te-download-url` |
| leaf | `wat-enable` | `[grouping] (wat-config)/wat-enable` |

## 8) Telemetry Subscription Cross-Reference

This repository's primary subject is **Catalyst 9300 switch telemetry** ([validation/subscriptions.yaml](validation/subscriptions.yaml), 66 subscriptions covering CPU, memory, interfaces, environment, routing, security, etc.). The wireless YANG models documented here apply to **Catalyst 9800 WLCs** and AP-integrated wireless on supported platforms, not directly to the C9300.

**Current subscription overlap with wireless models: zero.** A search of `validation/subscriptions.yaml` returns no matches for `Cisco-IOS-XE-wireless-*`. If you intend to add the C9800 to the same telemetry pipeline, consider these starting subscriptions (suggested IDs use the next free range in the 30xxx/60xxx/50xxx scheme):

| Suggested ID | Tier | Name | YANG module | XPath | Why |
|---|---|---|---|---|---|
| 30050 | HOT (30s) | Client global consolidated | `Cisco-IOS-XE-wireless-client-global-oper` | `/wireless-client-global-oper:client-global-oper-data/client-cnsld-data` | Major new aggregation list (24+ fields per client) added in 17.18.1 |
| 60050 | WARM (60s) | AP licensing state | `Cisco-IOS-XE-wireless-access-point-oper` | `/wireless-access-point-oper:access-point-oper-data/ap-license` (via `cw-license-info` grouping) | Cisco Wireless Licensing observability -- new in 17.18.1 |
| 60051 | WARM (60s) | AP LSC renewal | `Cisco-IOS-XE-wireless-access-point-oper` | `/wireless-access-point-oper:access-point-oper-data/ap-lsc` | New LSC renewal workflow |
| 60052 | WARM (60s) | Radio operational ext | `Cisco-IOS-XE-wireless-access-point-oper` | `/wireless-access-point-oper:access-point-oper-data/radio-oper-ext-data` | Includes URWB radio state, MLO group membership, beam state |
| 60053 | WARM (60s) | URWB network nodes | `Cisco-IOS-XE-wireless-urwbnet-oper` | `/wireless-oper-urwbnet:urwbnet-oper-data/urwbnet-node-g` | URWB topology -- new in 17.18.1 |
| 60054 | WARM (60s) | URWB network stats | `Cisco-IOS-XE-wireless-urwbnet-oper` | `/wireless-oper-urwbnet:urwbnet-oper-data/urwbnet-stats` | URWB link/throughput counters |
| 50050 | COOL (300s) | Rogue unconnected clients | `Cisco-IOS-XE-wireless-rogue-oper` | `/wireless-rogue-oper:rogue-oper-data/rogue-unconnected-data` | New unconnected-client visibility |
| 50051 | COOL (300s) | URWB profile config | `Cisco-IOS-XE-wireless-urwb-cfg` | `/wireless-urwb-cfg:urwb-cfg-data/urwb-profiles/urwb-profile` | URWB configuration inventory |

**Subscription tiers** follow the convention in [AGENTS.md](AGENTS.md): `30xxx`=HOT (30s) for high-frequency counters, `60xxx`=WARM (60s) for state/config, `50xxx`=COOL (300s) for slowly-changing data. Adjust intervals to your collector capacity.

Generation:

```bash
# Regenerate this document's JSON companion (consumable by dashboards/Splunk lookups):
python3 tools/wireless_yang_delta.py json \
    --base 17151 --target 17181 \
    --intermediate 17161 17171 \
    --out wireless-yang-17151-to-17181.json

# Regenerate the XPath appendix (Section 7) for any subset of modules:
python3 tools/wireless_yang_delta.py xpaths \
    --base 17151 --target 17181 \
    --modules Cisco-IOS-XE-wireless-access-point-oper \
    --out /tmp/appendix.md
```

## 9) Methodology and Sources

**Data sources** (all local to this repository):

- YANG modules: [reference/xe/17151](reference/xe/17151), [reference/xe/17161](reference/xe/17161), [reference/xe/17171](reference/xe/17171), [reference/xe/17181](reference/xe/17181) (filtered to `Cisco-IOS-XE-wireless-*.yang`)
- BIC files: `reference/xe/{17161,17171,17181}/BIC/Cisco-IOS-XE-wireless-*.md` (constraint changes: must/length/pattern/range, obsoleted/deprecated XPaths)
- Capability XML: [reference/xe/17151/capability-wireless.xml](reference/xe/17151/capability-wireless.xml) (17.18.1 file is empty in this snapshot)
- Cross-reference: [reference/17181/yang-innovation-analysis.md](reference/17181/yang-innovation-analysis.md) for release-over-release totals.

**Derivation rules:**

- Module inventory = file-system presence of `reference/xe/<rel>/Cisco-IOS-XE-wireless-*.yang`.
- Symbol delta = parsing `leaf`, `leaf-list`, `container`, `list`, `grouping`, `typedef`, `rpc`, `action`, `notification`, `identity` declarations and set-differencing the names.
- Constraint changes = verbatim BIC content from each release's `BIC/Cisco-IOS-XE-wireless-*.md` file, with empty `XPaths Obsoleted/Deprecated/Modified/Added` headers stripped, grouped by module across the three intermediate releases.
- Leaf catalog = first `type`, `default`, `units`, and `description` string extracted from each `leaf {}` block.

**Out of scope** (note for completeness):

- OpenConfig wireless modules (`openconfig-wifi-*`, `openconfig-ap-manager`, `openconfig-access-points`): per `yang-innovation-analysis.md`, these did not materially change across 17.15.1..17.18.1.
- Cisco OpenConfig wireless deviations (`cisco-xe-wireless-openconfig-*-deviation.yang`): unchanged in the inventory matrix above.

**Generator and machine-readable companion:**

- This document is reproducible via [tools/wireless_yang_delta.py](tools/wireless_yang_delta.py). Re-run with `--base`/`--target` for any future release pair (e.g. `17181`/`17191`).
- JSON companion: [wireless-yang-17151-to-17181.json](wireless-yang-17151-to-17181.json) carries the structured `{module, status, added, removed, bic}` data for programmatic consumers (dashboards, Splunk lookups, validation harnesses).
- **Known parser limitation:** Section 7 XPaths derived for symbols defined inside `grouping` blocks are reported relative to the grouping. Resolving them to a subscribable absolute path requires following the `uses <grouping>` references back to a parent data container -- the grouping name is included so this lookup is straightforward in the source YANG.
