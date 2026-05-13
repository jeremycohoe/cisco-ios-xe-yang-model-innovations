# All YANG Model Changes: v17.8.1 → v17.9.1
**Summary: 26 New Models & 112 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (26 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 10 | 627 XPaths |
| **[NEW RPC Models](#new-rpc-models)** | 4 | 33 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 2 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 6 | 109 XPaths |
| **[NEW OpenConfig Models](#new-openconfig-models)** | 3 | 43 XPaths |
| **[NEW Other Models](#new-other-models)** | 1 | 0 XPaths |
| **TOTAL NEW MODELS** | **26** | **812 total XPaths** |

---

## UPDATED Models Summary (112 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 13 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 19 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 9 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 8 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 10 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 48 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 1 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 4 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **112** | **See individual models** |

---

## Key Highlights - NEW Models


**26 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-qfp-appqoe-dp-oper.yang`: 214 XPaths (Operational)

  - `Cisco-IOS-XE-appqoe-http-oper.yang`: 115 XPaths (Operational)

  - `Cisco-IOS-XE-prp-oper.yang`: 102 XPaths (Operational)


- **Breakdown by category:**

  - Operational: 10 models

  - Native: 6 models

  - RPC: 4 models

  - OpenConfig: 3 models

  - Deviation: 2 models

  - Other: 1 model


---


## Key Highlights - UPDATED Models


**112 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-bgp.yang`: +5,874 XPaths (now 25,462 total)

  - `Cisco-IOS-XE-appqoe-serv-oper.yang`: +1,137 XPaths (now 1,198 total)

  - `Cisco-IOS-XE-crypto.yang`: +458 XPaths (now 5,556 total)


- **Significant removals:**

  - `Cisco-IOS-XE-nbar.yang`: -1 XPaths (now 591 total)


- **Updates by category:**

  - Native: 48 models

  - Operational: 19 models

  - Configuration: 13 models

  - Deviation: 10 models

  - RPC: 9 models

  - Types: 8 models

  - Vendor: 4 models

  - OpenConfig: 1 model


---


## Summary Statistics

### Release v17.9.1 Totals:
- **Total YANG Files:** ~538 files
- **New Files:** 26 models
- **Modified Files:** 112 models
- **Deleted Files:** 3 models
- **New Model XPaths:** 812 XPaths across 26 new models

---

# NEW YANG Models in v17.9.1

**26 Brand New Models**

---

## NEW Operational Models (10 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-appqoe-http-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-appqoe-http-oper.yang) | Appqoe Http Oper | Operational | 115 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-poe-health-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-poe-health-oper.yang) | Poe Health Oper | Operational | 74 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-prp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-prp-oper.yang) | Prp Oper | Operational | 102 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-qfp-appqoe-dp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-qfp-appqoe-dp-oper.yang) | Qfp Appqoe Dp Oper | Operational | 214 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-system-integrity-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-system-integrity-oper.yang) | System Integrity Oper | Operational | 45 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-uidp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-uidp-oper.yang) | Uidp Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-wireless-rfid-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rfid-global-oper.yang) | Wireless Rfid Global Oper | Operational | 12 | Wireless Controllers | New model introduced in this release |
| 8 | [Cisco-IOS-XE-wireless-rrm-emul-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rrm-emul-oper.yang) | Wireless Rrm Emul Oper | Operational | 12 | Wireless Controllers | New model introduced in this release |
| 9 | [Cisco-IOS-XE-wireless-rrm-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rrm-global-oper.yang) | Wireless Rrm Global Oper | Operational | 12 | Wireless Controllers | New model introduced in this release |
| 10 | [Cisco-IOS-XE-wireless-sisf-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-sisf-global-oper.yang) | Wireless Sisf Global Oper | Operational | 33 | Wireless Controllers | New model introduced in this release |

---

## NEW RPC Models (4 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-bgp-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-bgp-actions-rpc.yang) | Bgp Actions Rpc | RPC | 3 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-cli-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-cli-rpc.yang) | Cli Rpc | RPC | 19 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-voice-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-voice-rpc.yang) | Voice Rpc | RPC | 3 | ISR, Voice Gateways | New model introduced in this release |
| 4 | [Cisco-IOS-XE-wireless-client-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-client-rpc.yang) | Wireless Client Rpc | RPC | 8 | Wireless Controllers | New model introduced in this release |

---

## NEW Deviation Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-openconfig-system-grpc-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/cisco-xe-openconfig-system-grpc-deviation.yang) | Cisco Xe Openconfig System Grpc Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 2 | [cisco-xe-routing-openconfig-system-grpc-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/cisco-xe-routing-openconfig-system-grpc-deviation.yang) | Cisco Xe Routing Openconfig System Grpc Deviation | Deviation | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (6 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-banner-internal.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-banner-internal.yang) | Banner Internal | Native | 4 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-location.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-location.yang) | Location | Native | 0 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-loop-detect.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-loop-detect.yang) | Loop Detect | Native | 72 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-mrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-mrp.yang) | Mrp | Native | 13 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-prp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-prp.yang) | Prp | Native | 20 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-transceiver-monitor.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-transceiver-monitor.yang) | Transceiver Monitor | Native | 0 | All Platforms | New model introduced in this release |

---

## NEW OpenConfig Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [openconfig-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/openconfig-license.yang) | Openconfig License | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 2 | [openconfig-messages.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/openconfig-messages.yang) | Openconfig Messages | OpenConfig | 20 | All Platforms | New model introduced in this release |
| 3 | [openconfig-system-grpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/openconfig-system-grpc.yang) | Openconfig System Grpc | OpenConfig | 23 | All Platforms | New model introduced in this release |

---

## NEW Other Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [DIFFSERV-DSCP-TC.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/DIFFSERV-DSCP-TC.yang) | Diffserv Dscp Tc | Other | 0 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v17.8.1 → v17.9.1

**112 Models Modified**

---

## UPDATED Configuration Models (13 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-app-hosting-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-app-hosting-cfg.yang) | App Hosting Cfg | Configuration | +6 / 143 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 2 | [Cisco-IOS-XE-wireless-ap-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-ap-cfg.yang) | Wireless Ap Cfg | Configuration | +4 / 42 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes |
| 3 | [Cisco-IOS-XE-wireless-apf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-apf-cfg.yang) | Wireless Apf Cfg | Configuration | +3 / 73 | Wireless Controllers | [Auto-generated summary] | Added fra-56ghz-state, fra-56ghz-interval, fra-56ghz-freeze |
| 4 | [Cisco-IOS-XE-wireless-dot11-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-dot11-cfg.yang) | Wireless Dot11 Cfg | Configuration | 168 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [Cisco-IOS-XE-wireless-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-general-cfg.yang) | Wireless General Cfg | Configuration | +4 / 117 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; new enum values added; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-wireless-location-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-location-cfg.yang) | Wireless Location Cfg | Configuration | +5 / 28 | Wireless Controllers | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 7 | [Cisco-IOS-XE-wireless-mesh-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-mesh-cfg.yang) | Wireless Mesh Cfg | Configuration | +1 / 78 | Wireless Controllers | [Auto-generated summary] | Added auto-dca-rf-asic-aps |
| 8 | [Cisco-IOS-XE-wireless-radio-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-radio-cfg.yang) | Wireless Radio Cfg | Configuration | +1 / 50 | Wireless Controllers | [Auto-generated summary] | Added dtim-period |
| 9 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless Rf Cfg | Configuration | +8 / 191 | Wireless Controllers | [Auto-generated summary] | Added 8 new data nodes; new enum values added; enhanced validation constraints |
| 10 | [Cisco-IOS-XE-wireless-rogue-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rogue-cfg.yang) | Wireless Rogue Cfg | Configuration | +9 / 85 | Wireless Controllers | [Auto-generated summary] | Added 9 new data nodes; new enum values added; enhanced validation constraints |
| 11 | [Cisco-IOS-XE-wireless-rule-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rule-cfg.yang) | Wireless Rule Cfg | Configuration | +2 / 17 | Wireless Controllers | [Auto-generated summary] | Added group-method, rule-action-mdns-grouping; new enum values added; enhanced validation constraints |
| 12 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | +3 / 355 | Wireless Controllers | [Auto-generated summary] | Added latency-ma, auth-key-mgmt-ft-sae, accounting-interim; enhanced validation constraints |
| 13 | [Cisco-IOS-XE-yang-interfaces-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-yang-interfaces-cfg.yang) | Yang Interfaces Cfg | Configuration | +5 / 24 | All Platforms | [Auto-generated summary] | Added 9 new data nodes |

---

## UPDATED Operational Models (19 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-app-hosting-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-app-hosting-oper.yang) | App Hosting Oper | Operational | +1 / 143 | All Platforms | [Auto-generated summary] | Added mcast-enabled |
| 2 | [Cisco-IOS-XE-appqoe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-appqoe-oper.yang) | Appqoe Oper | Operational | 424 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [Cisco-IOS-XE-appqoe-serv-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-appqoe-serv-oper.yang) | Appqoe Serv Oper | Operational | +1137 / 1198 | All Platforms | [Auto-generated summary] | Added 396 new data nodes; added 4 new imports; new enum values added |
| 4 | [Cisco-IOS-XE-appqoe-sslproxy-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-appqoe-sslproxy-oper.yang) | Appqoe Sslproxy Oper | Operational | +6 / 217 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 5 | [Cisco-IOS-XE-install-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-install-oper.yang) | Install Oper | Operational | +6 / 740 | All Platforms | [Auto-generated summary] | Added version, set-default-param |
| 6 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +58 / 472 | All Platforms | [Auto-generated summary] | Added 34 new data nodes; imported publication; new enum values added |
| 7 | [Cisco-IOS-XE-nwpi-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-nwpi-oper.yang) | Nwpi Oper | Operational | +189 / 499 | All Platforms | [Auto-generated summary] | Added 94 new data nodes; imported ietf-yang-types; new enum values added |
| 8 | [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-platform-software-oper.yang) | Platform Software Oper | Operational | +6 / 93 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 9 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | +2 / 210 | All Platforms | [Auto-generated summary] | Added meter-start-time, metered-energy-value |
| 10 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | +143 / 1128 | Wireless Controllers | [Auto-generated summary] | Added 122 new data nodes; new enum values added |
| 11 | [Cisco-IOS-XE-wireless-ap-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-ap-global-oper.yang) | Wireless Ap Global Oper | Operational | +86 / 115 | Wireless Controllers | [Auto-generated summary] | Added 29 new data nodes |
| 12 | [Cisco-IOS-XE-wireless-ble-ltx-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-ble-ltx-oper.yang) | Wireless Ble Ltx Oper | Operational | +1 / 157 | Wireless Controllers | [Auto-generated summary] | Added ble-hybrid-mode |
| 13 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | 280 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 14 | [Cisco-IOS-XE-wireless-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-events-oper.yang) | Wireless Events Oper | Operational | +17 / 75 | Wireless Controllers | [Auto-generated summary] | Added 15 new data nodes; new enum values added |
| 15 | [Cisco-IOS-XE-wireless-hyperlocation-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-hyperlocation-oper.yang) | Wireless Hyperlocation Oper | Operational | +6 / 12 | Wireless Controllers | [Auto-generated summary] | Added hyperlocation-data, ntp-server; imported Cisco-IOS-XE-wireless-ap-types |
| 16 | [Cisco-IOS-XE-wireless-mesh-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-mesh-oper.yang) | Wireless Mesh Oper | Operational | +98 / 363 | Wireless Controllers | [Auto-generated summary] | Added 48 new data nodes; imported ietf-inet-types; new enum values added |
| 17 | [Cisco-IOS-XE-wireless-rogue-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rogue-oper.yang) | Wireless Rogue Oper | Operational | +24 / 343 | Wireless Controllers | [Auto-generated summary] | Added 22 new data nodes |
| 18 | [Cisco-IOS-XE-wireless-rrm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rrm-oper.yang) | Wireless Rrm Oper | Operational | +27 / 126 | Wireless Controllers | [Auto-generated summary] | Added 19 new data nodes; new enum values added |
| 19 | [Cisco-IOS-XE-wpan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wpan-oper.yang) | Wpan Oper | Operational | +19 / 174 | All Platforms | [Auto-generated summary] | Added 19 new data nodes; new enum values added |

---

## UPDATED RPC Models (9 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-crypto-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-crypto-actions-rpc.yang) | Crypto Actions Rpc | RPC | +11 / 14 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 2 | [Cisco-IOS-XE-crypto-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-crypto-rpc.yang) | Crypto Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | Added fingerprint, clear |
| 3 | [Cisco-IOS-XE-install-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-install-rpc.yang) | Install Rpc | RPC | +4 / 82 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; imported ietf-yang-types; enhanced validation constraints |
| 4 | [Cisco-IOS-XE-nwpi-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-nwpi-rpc.yang) | Nwpi Rpc | RPC | +6 / 43 | All Platforms | [Auto-generated summary] | Added qos-mon, mon-domain, to |
| 5 | [Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang) | Wireless Access Point Cfg Rpc | RPC | +81 / 304 | Wireless Controllers | [Auto-generated summary] | Added 37 new data nodes; new enum values added |
| 6 | [Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang) | Wireless Access Point Cmd Rpc | RPC | +128 / 240 | Wireless Controllers | [Auto-generated summary] | Added 57 new data nodes |
| 7 | [Cisco-IOS-XE-wireless-mesh-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-mesh-rpc.yang) | Wireless Mesh Rpc | RPC | +22 / 140 | Wireless Controllers | [Auto-generated summary] | Added 6 new data nodes |
| 8 | [Cisco-IOS-XE-wireless-rrm-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-rrm-rpc.yang) | Wireless Rrm Rpc | RPC | +8 / 19 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 9 | [Cisco-IOS-XE-xcopy-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-xcopy-rpc.yang) | Xcopy Rpc | RPC | +2 / 14 | All Platforms | [Auto-generated summary] | Added scheduled-start, scheduled-end; imported ietf-yang-types; enhanced validation constraints |

---

## UPDATED Types Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-aaa-types.yang) | Aaa Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 2 | [Cisco-IOS-XE-appqoe-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-appqoe-types.yang) | Appqoe Types | Types | 0 | All Platforms | [Auto-generated summary] | Added alarms-list; new enum values added |
| 3 | [Cisco-IOS-XE-install-event-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-install-event-types.yang) | Install Event Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [Cisco-IOS-XE-install-oper-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-install-oper-types.yang) | Install Oper Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 5 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added serial-console |
| 6 | [Cisco-IOS-XE-wireless-client-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-client-types.yang) | Wireless Client Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added excess-arp-rate, dot11-unspec-qos-reason |
| 7 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless Enum Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 8 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |

---

## UPDATED Deviation Models (10 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cef-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-cef-deviation.yang) | Cef Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 2 | [Cisco-IOS-XE-cts-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-cts-routing-deviation.yang) | Cts Routing Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 3 | [Cisco-IOS-XE-line-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-line-deviation.yang) | Line Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 4 | [Cisco-IOS-XE-poch-lb-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-poch-lb-switch-deviation.yang) | Poch Lb Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |
| 5 | [Cisco-IOS-XE-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-policy-deviation.yang) | Policy Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 6 | [Cisco-IOS-XE-power-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-power-deviation.yang) | Power Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 7 | [cisco-xe-access-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/cisco-xe-access-openconfig-system-deviation.yang) | Cisco Xe Access Openconfig System Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 8 | [cisco-xe-openconfig-access-points-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/cisco-xe-openconfig-access-points-deviation.yang) | Cisco Xe Openconfig Access Points Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 9 | [cisco-xe-routing-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/cisco-xe-routing-openconfig-system-deviation.yang) | Cisco Xe Routing Openconfig System Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [cisco-xe-switching-cat9k-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/cisco-xe-switching-cat9k-openconfig-system-deviation.yang) | Cisco Xe Switching Cat9K Openconfig System Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Native Models (48 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-aaa.yang) | Aaa | Native | 0 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 2 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-bfd.yang) | Bfd | Native | +41 / 373 | All Platforms | [Auto-generated summary] | Added 27 new data nodes; enhanced validation constraints; deprecated 2 nodes |
| 3 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +5874 / 25462 | All Platforms | [Auto-generated summary] | Added 231 new data nodes; imported Cisco-IOS-XE-nhrp, Cisco-IOS-XE-route-map; new enum values added |
| 4 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-cef.yang) | Cef | Native | 0 | All Platforms | [Auto-generated summary] | Added 65 new data nodes; enhanced validation constraints; deprecated 52 nodes |
| 5 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-controller.yang) | Controller | Native | +1 / 605 | All Platforms | [Auto-generated summary] | Added mode; new enum values added |
| 6 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-crypto.yang) | Crypto | Native | +458 / 5556 | All Platforms | [Auto-generated summary] | Added 486 new data nodes; new enum values added; enhanced validation constraints |
| 7 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | 0 | All Platforms | [Auto-generated summary] | Added for, short-lease, short-lease |
| 8 | [Cisco-IOS-XE-digitalio.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-digitalio.yang) | Digitalio | Native | 23 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 9 | [Cisco-IOS-XE-ethernet-cfm-efp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-ethernet-cfm-efp.yang) | Ethernet Cfm Efp | Native | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 10 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | 0 | All Platforms | [Auto-generated summary] | Added mrp, ring |
| 11 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | +1 / 263 | All Platforms | [Auto-generated summary] | Added spread-opt-tables |
| 12 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 13 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-flow.yang) | Flow | Native | 0 | All Platforms | [Auto-generated summary] | Added 10 new data nodes |
| 14 | [Cisco-IOS-XE-hsrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-hsrp.yang) | Hsrp | Native | 0 | All Platforms | [Auto-generated summary] | Added and, bfd-config |
| 15 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-http.yang) | Http | Native | 36 | All Platforms | [Auto-generated summary] | imported Cisco-IOS-XE-features |
| 16 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-igmp.yang) | Igmp | Native | +30 / 5130 | All Platforms | [Auto-generated summary] | Added 33 new data nodes; imported Cisco-IOS-XE-features |
| 17 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 18 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; deprecated 1 node |
| 19 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added to, cef-v2, cef; deprecated 1 node |
| 20 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +26 / 2163 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; imported leaf, {; deprecated 1 node |
| 21 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; new enum values added; deprecated 4 nodes |
| 22 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +105 / 28570 | All Platforms | [Auto-generated summary] | Added 1632 new data nodes; added 20 new imports; new enum values added |
| 23 | [Cisco-IOS-XE-mdns-gateway.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-mdns-gateway.yang) | Mdns Gateway | Native | +9 / 773 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added; enhanced validation constraints |
| 24 | [Cisco-IOS-XE-mdt-oper-v2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-mdt-oper-v2.yang) | Mdt Oper V2 | Native | +3 / 92 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 25 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-multicast.yang) | Multicast | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 26 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-nat.yang) | Nat | Native | +20 / 2559 | All Platforms | [Auto-generated summary] | Added 15 new data nodes |
| 27 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-native.yang) | Native | Native | 0 | All Platforms | [Auto-generated summary] | Added dhcp-config, loopdetect, loopdetect; deprecated 9 nodes |
| 28 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-nbar.yang) | Nbar | Native | -1 / 591 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 29 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-ntp.yang) | Ntp | Native | +1 / 909 | All Platforms | [Auto-generated summary] | Added ptp; imported Cisco-IOS-XE-features |
| 30 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-object-group.yang) | Object Group | Native | 380 | All Platforms | [Auto-generated summary] | Minor refinements |
| 31 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-platform.yang) | Platform | Native | +2 / 141 | All Platforms | [Auto-generated summary] | Added sslvpn, use-pd |
| 32 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-policy.yang) | Policy | Native | +25 / 4865 | All Platforms | [Auto-generated summary] | Added 11 new data nodes |
| 33 | [Cisco-IOS-XE-qfp-stats.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-qfp-stats.yang) | Qfp Stats | Native | +4 / 1047 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 34 | [Cisco-IOS-XE-rawsocket.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-rawsocket.yang) | Rawsocket | Native | 65 | All Platforms | [Auto-generated summary] | Minor refinements |
| 35 | [Cisco-IOS-XE-rmi-dad.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-rmi-dad.yang) | Rmi Dad | Native | +7 / 29 | All Platforms | [Auto-generated summary] | Added 7 new data nodes |
| 36 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +2 / 1087 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; deprecated 9 nodes |
| 37 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-sanet.yang) | Sanet | Native | +2 / 1381 | All Platforms | [Auto-generated summary] | Added wireless, cui-enable |
| 38 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | +10 / 345 | All Platforms | [Auto-generated summary] | Added color-option, rib |
| 39 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-sla.yang) | Sla | Native | 2700 | All Platforms | [Auto-generated summary] | Added to |
| 40 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +11 / 1675 | All Platforms | [Auto-generated summary] | Added 11 new data nodes |
| 41 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | +28 / 400 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 42 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-switch.yang) | Switch | Native | +3 / 6643 | Cat9K, IE3x00 | [Auto-generated summary] | Added boot-container, boot-filename, filename |
| 43 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-udld.yang) | Udld | Native | 105 | All Platforms | [Auto-generated summary] | Minor refinements |
| 44 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-utd.yang) | Utd | Native | +14 / 596 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 45 | [Cisco-IOS-XE-voice-class.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-voice-class.yang) | Voice Class | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added down-interval, up-interval, retry; deprecated 3 nodes |
| 46 | [Cisco-IOS-XE-voice-port.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-voice-port.yang) | Voice Port | Native | 149 | ISR, Voice Gateways | [Auto-generated summary] | Minor refinements |
| 47 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-voice.yang) | Voice | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added profile-config |
| 48 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/Cisco-IOS-XE-zone.yang) | Zone | Native | 58 | All Platforms | [Auto-generated summary] | Added removal"; |

---

## UPDATED OpenConfig Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [openconfig-system.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/openconfig-system.yang) | Openconfig System | OpenConfig | +25 / 401 | All Platforms | [Auto-generated summary] | added 3 new imports |

---

## UPDATED Vendor Models (4 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | +4 / 740 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 2 | [tailf-cli-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/tailf-cli-extensions.yang) | Tailf Cli Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | Added or, must, if; enhanced validation constraints |
| 3 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/tailf-common.yang) | Tailf Common | Vendor | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [tailf-netconf-monitoring.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1791/tailf-netconf-monitoring.yang) | Tailf Netconf Monitoring | Vendor | +2 / 27 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added; deprecated 1 node |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
