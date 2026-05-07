# All YANG Model Changes: v17.14.1 → v17.15.1
**Summary: 30 New Models & 136 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (30 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 8 | 327 XPaths |
| **[NEW RPC Models](#new-rpc-models)** | 4 | 142 XPaths |
| **[NEW Events Models](#new-events-models)** | 3 | 19 XPaths |
| **[NEW Types Models](#new-types-models)** | 2 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 6 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 7 | 175 XPaths |
| **TOTAL NEW MODELS** | **30** | **663 total XPaths** |

---

## UPDATED Models Summary (136 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 13 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 14 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 8 | XPath changes vary |
| **[UPDATED Events Models](#updated-events-models)** | 1 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 9 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 8 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 78 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 1 | XPath changes vary |
| **[UPDATED IETF Models](#updated-ietf-models)** | 1 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 2 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 1 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **136** | **See individual models** |

---

## Key Highlights - NEW Models


**30 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-livetools-oper.yang`: 132 XPaths (Operational)

  - `Cisco-IOS-XE-livetools-actions-rpc.yang`: 98 XPaths (RPC)

  - `Cisco-IOS-XE-irig.yang`: 68 XPaths (Native)


- **Breakdown by category:**

  - Operational: 8 models

  - Native: 7 models

  - Deviation: 6 models

  - RPC: 4 models

  - Events: 3 models

  - Types: 2 models


---


## Key Highlights - UPDATED Models


**136 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-isis.yang`: +1,583 XPaths (now 7,478 total)

  - `Cisco-IOS-XE-native.yang`: +1,269 XPaths (now 113,553 total)

  - `Cisco-IOS-XE-switch.yang`: +394 XPaths (now 7,374 total)


- **Significant removals:**

  - `Cisco-IOS-XE-udld.yang`: -41 XPaths (now 64 total)

  - `Cisco-IOS-XE-bgp.yang`: -8 XPaths (now 26,159 total)

  - `Cisco-IOS-XE-cloud-services-cfg.yang`: -3 XPaths (now 2 total)


- **Updates by category:**

  - Native: 78 models

  - Operational: 14 models

  - Configuration: 13 models

  - Types: 9 models

  - RPC: 8 models

  - Deviation: 8 models

  - Vendor: 2 models

  - Events: 1 model

  - Other: 1 model

  - IETF: 1 model

  - OpenConfig: 1 model


---


## Summary Statistics

### Release v17.15.1 Totals:
- **Total YANG Files:** ~566 files
- **New Files:** 30 models
- **Modified Files:** 136 models
- **Deleted Files:** 2 models
- **New Model XPaths:** 663 XPaths across 30 new models

---

# NEW YANG Models in v17.15.1

**30 Brand New Models**

---

## NEW Operational Models (8 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-cloud-services-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cloud-services-oper.yang) | Cloud Services Oper | Operational | 13 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-l2nat-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-l2nat-oper.yang) | L2Nat Oper | Operational | 27 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-livetools-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-livetools-oper.yang) | Livetools Oper | Operational | 132 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-nve-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nve-oper.yang) | Nve Oper | Operational | 65 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-omp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-omp-oper.yang) | Omp Oper | Operational | 40 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-rg-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-rg-oper.yang) | Rg Oper | Operational | 9 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-uplink-autoconfig-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-uplink-autoconfig-oper.yang) | Uplink Autoconfig Oper | Operational | 27 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-wireless-cisco-spaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-cisco-spaces-oper.yang) | Wireless Cisco Spaces Oper | Operational | 14 | Wireless Controllers | New model introduced in this release |

---

## NEW RPC Models (4 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-livetools-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-livetools-actions-rpc.yang) | Livetools Actions Rpc | RPC | 98 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-omp-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-omp-rpc.yang) | Omp Rpc | RPC | 25 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-port-bounce-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-port-bounce-rpc.yang) | Port Bounce Rpc | RPC | 7 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-wireless-tech-support-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-tech-support-rpc.yang) | Wireless Tech Support Rpc | RPC | 12 | Wireless Controllers | New model introduced in this release |

---

## NEW Events Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-mcast-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-mcast-events.yang) | Mcast Events | Events | 9 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-port-bounce-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-port-bounce-events.yang) | Port Bounce Events | Events | 4 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-red-app-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-red-app-events.yang) | Red App Events | Events | 6 | All Platforms | New model introduced in this release |

---

## NEW Types Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-livetools-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-livetools-common-types.yang) | Livetools Common Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-red-app-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-red-app-common-types.yang) | Red App Common Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Deviation Models (6 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-interfaces-deviation.yang) | Interfaces Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-logging-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-logging-deviation.yang) | Logging Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-perf-measure-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-perf-measure-deviation.yang) | Perf Measure Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-port-channel-crankshaft-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-port-channel-crankshaft-deviation.yang) | Port Channel Crankshaft Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-port-channel-unsupported-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-port-channel-unsupported-deviation.yang) | Port Channel Unsupported Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-ppp-mcp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ppp-mcp-deviation.yang) | Ppp Mcp Deviation | Deviation | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (7 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-buffers.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-buffers.yang) | Buffers | Native | 32 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-clns.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-clns.yang) | Clns | Native | 13 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-cwmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cwmp.yang) | Cwmp | Native | 27 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-gnss.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-gnss.yang) | Gnss | Native | 16 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-ipc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ipc.yang) | Ipc | Native | 11 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-irig.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-irig.yang) | Irig | Native | 68 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-uplink-autoconfig.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-uplink-autoconfig.yang) | Uplink Autoconfig | Native | 8 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v17.14.1 → v17.15.1

**136 Models Modified**

---

## UPDATED Configuration Models (13 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cloud-services-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cloud-services-cfg.yang) | Cloud Services Cfg | Configuration | -3 / 2 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [Cisco-IOS-XE-gnmi-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-gnmi-cfg.yang) | Gnmi Cfg | Configuration | +2 / 13 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 3 | [Cisco-IOS-XE-wireless-ap-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-ap-cfg.yang) | Wireless Ap Cfg | Configuration | 45 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 4 | [Cisco-IOS-XE-wireless-dot11-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-dot11-cfg.yang) | Wireless Dot11 Cfg | Configuration | +7 / 175 | Wireless Controllers | [Auto-generated summary] | Added 7 new data nodes; new enum values added |
| 5 | [Cisco-IOS-XE-wireless-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-general-cfg.yang) | Wireless General Cfg | Configuration | 125 | Wireless Controllers | [Auto-generated summary] | Added is, is |
| 6 | [Cisco-IOS-XE-wireless-mesh-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-mesh-cfg.yang) | Wireless Mesh Cfg | Configuration | 81 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-wireless-mstream-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-mstream-cfg.yang) | Wireless Mstream Cfg | Configuration | 20 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 8 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless Rf Cfg | Configuration | +12 / 211 | Wireless Controllers | [Auto-generated summary] | Added 12 new data nodes |
| 9 | [Cisco-IOS-XE-wireless-rogue-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-rogue-cfg.yang) | Wireless Rogue Cfg | Configuration | +1 / 88 | Wireless Controllers | [Auto-generated summary] | Added mld-link-records |
| 10 | [Cisco-IOS-XE-wireless-rrm-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-rrm-cfg.yang) | Wireless Rrm Cfg | Configuration | 70 | Wireless Controllers | [Auto-generated summary] | Added channel, DCA; enhanced validation constraints |
| 11 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless Site Cfg | Configuration | +6 / 382 | Wireless Controllers | [Auto-generated summary] | Added height, height-uncertainty, height-type; new enum values added; enhanced validation constraints |
| 12 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | +15 / 381 | Wireless Controllers | [Auto-generated summary] | Added 15 new data nodes; enhanced validation constraints |
| 13 | [Cisco-IOS-XE-yang-interfaces-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-yang-interfaces-cfg.yang) | Yang Interfaces Cfg | Configuration | +5 / 51 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |

---

## UPDATED Operational Models (14 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-aaa-oper.yang) | Aaa Oper | Operational | +68 / 204 | All Platforms | [Auto-generated summary] | Added 68 new data nodes |
| 2 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces Oper | Operational | +6 / 503 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added |
| 3 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +12 / 494 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 4 | [Cisco-IOS-XE-lldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-lldp-oper.yang) | Lldp Oper | Operational | +5 / 101 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added |
| 5 | [Cisco-IOS-XE-meraki-connect-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-meraki-connect-oper.yang) | Meraki Connect Oper | Operational | +8 / 95 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; new enum values added |
| 6 | [Cisco-IOS-XE-nwpi-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nwpi-oper.yang) | Nwpi Oper | Operational | +60 / 1152 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; new enum values added |
| 7 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | +4 / 216 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 8 | [Cisco-IOS-XE-spanning-tree-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-spanning-tree-oper.yang) | Spanning Tree Oper | Operational | +5 / 54 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 9 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | +124 / 1482 | Wireless Controllers | [Auto-generated summary] | Added 66 new data nodes; new enum values added |
| 10 | [Cisco-IOS-XE-wireless-client-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-client-global-oper.yang) | Wireless Client Global Oper | Operational | +2 / 564 | Wireless Controllers | [Auto-generated summary] | Added ext-key-accepted |
| 11 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | +51 / 363 | Wireless Controllers | [Auto-generated summary] | Added 25 new data nodes; new enum values added |
| 12 | [Cisco-IOS-XE-wireless-rfid-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-rfid-global-oper.yang) | Wireless Rfid Global Oper | Operational | 47 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 13 | [Cisco-IOS-XE-wireless-rfid-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-rfid-oper.yang) | Wireless Rfid Oper | Operational | 60 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 14 | [Cisco-IOS-XE-wireless-rogue-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-rogue-oper.yang) | Wireless Rogue Oper | Operational | +28 / 383 | Wireless Controllers | [Auto-generated summary] | Added 24 new data nodes; imported Cisco-IOS-XE-wireless-types; new enum values added |

---

## UPDATED RPC Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cli-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cli-rpc.yang) | Cli Rpc | RPC | +8 / 27 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added |
| 2 | [Cisco-IOS-XE-cloud-services-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cloud-services-rpc.yang) | Cloud Services Rpc | RPC | +6 / 9 | All Platforms | [Auto-generated summary] | Added service; imported {, OTP |
| 3 | [Cisco-IOS-XE-meraki-leds-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-meraki-leds-actions-rpc.yang) | Meraki Leds Actions Rpc | RPC | 9 | All Platforms | [Auto-generated summary] | Added chassis-number, chassis-number; deprecated 2 nodes |
| 4 | [Cisco-IOS-XE-nwpi-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nwpi-rpc.yang) | Nwpi Rpc | RPC | +11 / 82 | All Platforms | [Auto-generated summary] | Added net-id, enable-cmd-header, trnspt-if-name |
| 5 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +54 / 1763 | All Platforms | [Auto-generated summary] | Added 37 new data nodes; imported Cisco-IOS-XE-types |
| 6 | [Cisco-IOS-XE-switch-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-switch-rpc.yang) | Switch Rpc | RPC | +12 / 45 | Cat9K, IE3x00 | [Auto-generated summary] | Added 10 new data nodes |
| 7 | [Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang) | Wireless Access Point Cfg Rpc | RPC | +8 / 377 | Wireless Controllers | [Auto-generated summary] | Added 6 new data nodes; new enum values added; enhanced validation constraints |
| 8 | [Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang) | Wireless Access Point Cmd Rpc | RPC | +1 / 351 | Wireless Controllers | [Auto-generated summary] | Added for, reset-ap |

---

## UPDATED Events Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-endpoint-tracker-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-endpoint-tracker-events.yang) | Endpoint Tracker Events | Events | +10 / 19 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; new enum values added |

---

## UPDATED Types Models (9 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-nwpi-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nwpi-types.yang) | Nwpi Types | Types | 0 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; imported Cisco-IOS-XE-common-types |
| 2 | [Cisco-IOS-XE-wireless-afc-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-afc-types.yang) | Wireless Afc Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added band320, band320 |
| 3 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added uwb-enabled, uwb-init-burst-size, uwb-init-burst-duration; enhanced validation constraints |
| 4 | [Cisco-IOS-XE-wireless-client-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-client-types.yang) | Wireless Client Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added exceeded-max-mlo-links; new enum values added |
| 5 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless Enum Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 6 | [Cisco-IOS-XE-wireless-geolocation-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-geolocation-types.yang) | Wireless Geolocation Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-wireless-mobility-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-mobility-types.yang) | Wireless Mobility Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 8 | [Cisco-IOS-XE-wireless-rogue-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-rogue-types.yang) | Wireless Rogue Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added; enhanced validation constraints |
| 9 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |

---

## UPDATED Deviation Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cts-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cts-routing-deviation.yang) | Cts Routing Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 2 | [Cisco-IOS-XE-cts-switching-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cts-switching-deviation.yang) | Cts Switching Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |
| 3 | [Cisco-IOS-XE-line-nonquake-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-line-nonquake-deviation.yang) | Line Nonquake Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-ospf-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ospf-deviation.yang) | Ospf Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 5 | [Cisco-IOS-XE-port-channel-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-port-channel-deviation.yang) | Port Channel Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [Cisco-IOS-XE-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-switch-deviation.yang) | Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-switchport-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-switchport-deviation.yang) | Switchport Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |
| 8 | [cisco-xe-openconfig-evpn-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/cisco-xe-openconfig-evpn-deviation.yang) | Cisco Xe Openconfig Evpn Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Native Models (78 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +164 / 3299 | All Platforms | [Auto-generated summary] | Added 85 new data nodes; imported Cisco-IOS-XE-features; new enum values added |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-acl.yang) | Acl | Native | 1737 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 3 | [Cisco-IOS-XE-alarm-profile.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-alarm-profile.yang) | Alarm Profile | Native | +6 / 676 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 4 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-bfd.yang) | Bfd | Native | 406 | All Platforms | [Auto-generated summary] | Added for |
| 5 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-bgp.yang) | Bgp | Native | -8 / 26159 | All Platforms | [Auto-generated summary] | Added 39 new data nodes; new enum values added; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-bridge-domain.yang) | Bridge Domain | Native | 329 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-call-home.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-call-home.yang) | Call Home | Native | +8 / 241 | All Platforms | [Auto-generated summary] | Added 8 new data nodes |
| 8 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cdp.yang) | Cdp | Native | 281 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 9 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-controller.yang) | Controller | Native | +1 / 614 | All Platforms | [Auto-generated summary] | Added constellation; new enum values added |
| 10 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-crypto.yang) | Crypto | Native | +200 / 6541 | All Platforms | [Auto-generated summary] | Added 96 new data nodes; new enum values added; enhanced validation constraints |
| 11 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-cts.yang) | Cts | Native | +2 / 617 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; new enum values added; enhanced validation constraints |
| 12 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | +1 / 207 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added; enhanced validation constraints |
| 13 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +17 / 7585 | All Platforms | [Auto-generated summary] | Added 21 new data nodes; new enum values added; enhanced validation constraints |
| 14 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | 268 | All Platforms | [Auto-generated summary] | Added pae; new enum values added; deprecated 1 node |
| 15 | [Cisco-IOS-XE-dying-gasp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-dying-gasp.yang) | Dying Gasp | Native | 3 | All Platforms | [Auto-generated summary] | new enum values added; enhanced validation constraints |
| 16 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-eem.yang) | Eem | Native | +156 / 457 | All Platforms | [Auto-generated summary] | Added 125 new data nodes; new enum values added; enhanced validation constraints |
| 17 | [Cisco-IOS-XE-ethernet-oam.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ethernet-oam.yang) | Ethernet Oam | Native | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 18 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | +170 / 12795 | All Platforms | [Auto-generated summary] | Added 16 new data nodes; new enum values added; enhanced validation constraints |
| 19 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | +12 / 306 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added; deprecated 6 nodes |
| 20 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 21 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-flow.yang) | Flow | Native | +133 / 3052 | All Platforms | [Auto-generated summary] | Added vrf, source |
| 22 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-http.yang) | Http | Native | +13 / 89 | All Platforms | [Auto-generated summary] | Added 13 new data nodes |
| 23 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-igmp.yang) | Igmp | Native | 5210 | All Platforms | [Auto-generated summary] | Added expiry; deprecated 1 node |
| 24 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 25 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 25 new data nodes; new enum values added; enhanced validation constraints |
| 26 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 77 new data nodes; added 6 new imports; new enum values added |
| 27 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added 7 new data nodes |
| 28 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-isis.yang) | Isis | Native | +1583 / 7478 | All Platforms | [Auto-generated summary] | Added 110 new data nodes; new enum values added; enhanced validation constraints |
| 29 | [Cisco-IOS-XE-l2nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-l2nat.yang) | L2Nat | Native | +1 / 57 | All Platforms | [Auto-generated summary] | Added for, gateway, name; imported cisco-semver; deprecated 1 node |
| 30 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +8 / 2341 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added; deprecated 1 node |
| 31 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added for, logout-warning, logout-warning |
| 32 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +58 / 28912 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; deprecated 1 node |
| 33 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | Added 37 new data nodes; new enum values added; enhanced validation constraints |
| 34 | [Cisco-IOS-XE-mdns-gateway.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-mdns-gateway.yang) | Mdns Gateway | Native | +1 / 787 | All Platforms | [Auto-generated summary] | Added threshold |
| 35 | [Cisco-IOS-XE-mld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-mld.yang) | Mld | Native | +36 / 546 | All Platforms | [Auto-generated summary] | Added to, explicit-tracking, acl |
| 36 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-mpls.yang) | Mpls | Native | +16 / 1732 | ASR, ISR, NCS | [Auto-generated summary] | Added 14 new data nodes; new enum values added; deprecated 2 nodes |
| 37 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +17 / 4332 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; imported Cisco-IOS-XE-snmp; enhanced validation constraints |
| 38 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nat.yang) | Nat | Native | +9 / 4295 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; deprecated 1 node |
| 39 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-native.yang) | Native | Native | +1269 / 113553 | All Platforms | [Auto-generated summary] | Added 105 new data nodes; new enum values added; enhanced validation constraints |
| 40 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +68 / 648 | All Platforms | [Auto-generated summary] | Added 17 new data nodes |
| 41 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nd.yang) | Nd | Native | +113 / 2484 | All Platforms | [Auto-generated summary] | Added 23 new data nodes; enhanced validation constraints |
| 42 | [Cisco-IOS-XE-nhrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-nhrp.yang) | Nhrp | Native | +26 / 9605 | All Platforms | [Auto-generated summary] | Added 11 new data nodes |
| 43 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-object-group.yang) | Object Group | Native | +3 / 431 | All Platforms | [Auto-generated summary] | Added knob, knob_option, enable; new enum values added |
| 44 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +10 / 6285 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; deprecated 1 node |
| 45 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | 21408 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 46 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | [Auto-generated summary] | Added configuration; new enum values added |
| 47 | [Cisco-IOS-XE-perf-measure.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-perf-measure.yang) | Perf Measure | Native | +4 / 282 | All Platforms | [Auto-generated summary] | Added measurement-mode-v2, measurement-mode-v2, measurement-mode-v2; new enum values added |
| 48 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-platform.yang) | Platform | Native | +6 / 171 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added |
| 49 | [Cisco-IOS-XE-pnp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-pnp.yang) | Pnp | Native | 55 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 50 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-policy.yang) | Policy | Native | +1 / 6742 | All Platforms | [Auto-generated summary] | Added nodes, cos-inner |
| 51 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-ppp.yang) | Ppp | Native | +1 / 442 | All Platforms | [Auto-generated summary] | Added hold-queue |
| 52 | [Cisco-IOS-XE-qfp-stats.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-qfp-stats.yang) | Qfp Stats | Native | +2 / 1059 | All Platforms | [Auto-generated summary] | Added pa-pkt-not-supported-pkts, pa-pkt-not-supported-octets |
| 53 | [Cisco-IOS-XE-qos.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-qos.yang) | Qos | Native | 43 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 54 | [Cisco-IOS-XE-rawsocket.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-rawsocket.yang) | Rawsocket | Native | 65 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 55 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +2 / 1196 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; deprecated 16 nodes |
| 56 | [Cisco-IOS-XE-rsvp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-rsvp.yang) | Rsvp | Native | 690 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 57 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-sanet.yang) | Sanet | Native | +1 / 1384 | All Platforms | [Auto-generated summary] | Added and, session-terminate |
| 58 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | +7 / 410 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; new enum values added; enhanced validation constraints |
| 59 | [Cisco-IOS-XE-sip-ua.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-sip-ua.yang) | Sip Ua | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | updated descriptions and documentation |
| 60 | [Cisco-IOS-XE-sisf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-sisf.yang) | Sisf | Native | 0 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 61 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +80 / 1767 | All Platforms | [Auto-generated summary] | Added 73 new data nodes; new enum values added; deprecated 6 nodes |
| 62 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | +201 / 616 | All Platforms | [Auto-generated summary] | Added 20 new data nodes; deprecated 2 nodes |
| 63 | [Cisco-IOS-XE-stackwise-virtual.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-stackwise-virtual.yang) | Stackwise Virtual | Native | 8 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 64 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-switch.yang) | Switch | Native | +394 / 7374 | Cat9K, IE3x00 | [Auto-generated summary] | Added 25 new data nodes; imported Cisco-IOS-XE-flow; new enum values added |
| 65 | [Cisco-IOS-XE-synce.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-synce.yang) | Synce | Native | +2 / 678 | All Platforms | [Auto-generated summary] | Added timing-source, bits |
| 66 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-template.yang) | Template | Native | 2844 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 67 | [Cisco-IOS-XE-track.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-track.yang) | Track | Native | +4 / 216 | All Platforms | [Auto-generated summary] | Added ha-wan-tracker, ha-dia-tracker |
| 68 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | 1642 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 69 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-udld.yang) | Udld | Native | -41 / 64 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; new enum values added |
| 70 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-umbrella.yang) | Umbrella | Native | +1 / 205 | All Platforms | [Auto-generated summary] | Added use-v2-api |
| 71 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-vlan.yang) | Vlan | Native | 154 | Cat9K, IE3x00 | [Auto-generated summary] | Added id; enhanced validation constraints |
| 72 | [Cisco-IOS-XE-voice-class.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-voice-class.yang) | Voice Class | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 4 new data nodes |
| 73 | [Cisco-IOS-XE-voice-port.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-voice-port.yang) | Voice Port | Native | +3 / 172 | ISR, Voice Gateways | [Auto-generated summary] | Added timeouts, interdigit, mwi |
| 74 | [Cisco-IOS-XE-voice-register.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-voice-register.yang) | Voice Register | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 6 new data nodes; deprecated 6 nodes |
| 75 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-voice.yang) | Voice | Native | +18 / 3112 | ISR, Voice Gateways | [Auto-generated summary] | Added 15 new data nodes; new enum values added |
| 76 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-vrrp.yang) | Vrrp | Native | 1664 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 77 | [Cisco-IOS-XE-vtp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-vtp.yang) | Vtp | Native | +2 / 30 | All Platforms | [Auto-generated summary] | Added server, primary |
| 78 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/Cisco-IOS-XE-zone.yang) | Zone | Native | +8 / 70 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED OpenConfig Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [openconfig-network-instance.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/openconfig-network-instance.yang) | Openconfig Network Instance | OpenConfig | 5456 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED IETF Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-ietf-yang-push-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/cisco-xe-ietf-yang-push-ext.yang) | Cisco Xe Ietf Yang Push Ext | IETF | +28 / 42 | All Platforms | [Auto-generated summary] | Added nested-uri-filter, transform-name-filter |

---

## UPDATED Vendor Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | 756 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/tailf-common.yang) | Tailf Common | Vendor | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Other Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-ia.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17151/cisco-ia.yang) | Cisco Ia | Other | +5 / 77 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
