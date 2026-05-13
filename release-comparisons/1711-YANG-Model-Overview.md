# All YANG Model Changes: v16.12.1 → v17.1.1
**Summary: 20 New Models & 244 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (20 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 7 | 550 XPaths |
| **[NEW Events Models](#new-events-models)** | 1 | 8 XPaths |
| **[NEW Types Models](#new-types-models)** | 2 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 5 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 3 | 222 XPaths |
| **[NEW OpenConfig Models](#new-openconfig-models)** | 1 | 0 XPaths |
| **[NEW Other Models](#new-other-models)** | 1 | 0 XPaths |
| **TOTAL NEW MODELS** | **20** | **780 total XPaths** |

---

## UPDATED Models Summary (244 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 11 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 28 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 18 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 8 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 41 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 118 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 1 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 19 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **244** | **See individual models** |

---

## Key Highlights - NEW Models


**20 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-identity-oper.yang`: 404 XPaths (Operational)

  - `Cisco-IOS-XE-scada-gw.yang`: 170 XPaths (Native)

  - `Cisco-IOS-XE-perf-measure.yang`: 40 XPaths (Native)


- **Breakdown by category:**

  - Operational: 7 models

  - Deviation: 5 models

  - Native: 3 models

  - Types: 2 models

  - Events: 1 model

  - Other: 1 model

  - OpenConfig: 1 model


---


## Key Highlights - UPDATED Models


**244 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-nhrp.yang`: +6,303 XPaths (now 8,209 total)

  - `Cisco-IOS-XE-lisp.yang`: +3,000 XPaths (now 23,209 total)

  - `Cisco-IOS-XE-native.yang`: +2,602 XPaths (now 31,537 total)


- **Significant removals:**

  - `Cisco-IOS-XE-crypto.yang`: -4,812 XPaths (now 0 total)

  - `Cisco-IOS-XE-flow.yang`: -78 XPaths (now 2,426 total)

  - `Cisco-IOS-XE-device-tracking.yang`: -3 XPaths (now 50 total)


- **Updates by category:**

  - Native: 118 models

  - Deviation: 41 models

  - Operational: 28 models

  - Other: 19 models

  - RPC: 18 models

  - Configuration: 11 models

  - Types: 8 models

  - OpenConfig: 1 model


---


## Summary Statistics

### Release v17.1.1 Totals:
- **Total YANG Files:** ~664 files
- **New Files:** 20 models
- **Modified Files:** 244 models
- **Deleted Files:** 6 models
- **New Model XPaths:** 780 XPaths across 20 new models

---

# NEW YANG Models in v17.1.1

**20 Brand New Models**

---

## NEW Operational Models (7 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-controller-t1e1-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-controller-t1e1-oper.yang) | Controller T1E1 Oper | Operational | 35 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-identity-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-identity-oper.yang) | Identity Oper | Operational | 404 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-isdn-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-isdn-oper.yang) | Isdn Oper | Operational | 24 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-platform-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-platform-common-oper.yang) | Platform Common Oper | Operational | 0 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-platform-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-platform-events-oper.yang) | Platform Events Oper | Operational | 32 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-sm-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-sm-events-oper.yang) | Sm Events Oper | Operational | 38 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-wireless-awips-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-awips-oper.yang) | Wireless Awips Oper | Operational | 17 | Wireless Controllers | New model introduced in this release |

---

## NEW Events Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-crypto-pki-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-crypto-pki-events.yang) | Crypto Pki Events | Events | 8 | All Platforms | New model introduced in this release |

---

## NEW Types Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-aaa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-aaa-types.yang) | Aaa Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-sm-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-sm-enum-types.yang) | Sm Enum Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Deviation Models (5 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-cdp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cdp-deviation.yang) | Cdp Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-power-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-power-deviation.yang) | Power Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 3 | [cisco-xe-openconfig-access-points-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-access-points-deviation.yang) | Cisco Xe Openconfig Access Points Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 4 | [cisco-xe-openconfig-system-management-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-system-management-deviation.yang) | Cisco Xe Openconfig System Management Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 5 | [cisco-xe-routing-openconfig-system-management-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-routing-openconfig-system-management-deviation.yang) | Cisco Xe Routing Openconfig System Management Deviation | Deviation | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-perf-measure.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-perf-measure.yang) | Perf Measure | Native | 40 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-rmi-dad.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-rmi-dad.yang) | Rmi Dad | Native | 12 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-scada-gw.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-scada-gw.yang) | Scada Gw | Native | 170 | All Platforms | New model introduced in this release |

---

## NEW OpenConfig Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [openconfig-system-management.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/openconfig-system-management.yang) | Openconfig System Management | OpenConfig | 0 | All Platforms | New model introduced in this release |

---

## NEW Other Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-semver-internal.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-semver-internal.yang) | Cisco Semver Internal | Other | 0 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.12.1 → v17.1.1

**244 Models Modified**

---

## UPDATED Configuration Models (11 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-app-hosting-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-app-hosting-cfg.yang) | App Hosting Cfg | Configuration | +5 / 77 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 2 | [Cisco-IOS-XE-wireless-dot11-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-dot11-cfg.yang) | Wireless Dot11 Cfg | Configuration | +3 / 163 | Wireless Controllers | [Auto-generated summary] | Added he-twt-enable, he-twt-broadcast-enable, he-bss-color; enhanced validation constraints |
| 3 | [Cisco-IOS-XE-wireless-flex-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-flex-cfg.yang) | Wireless Flex Cfg | Configuration | +4 / 52 | Wireless Controllers | [Auto-generated summary] | Added 6 new data nodes |
| 4 | [Cisco-IOS-XE-wireless-fqdn-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-fqdn-cfg.yang) | Wireless Fqdn Cfg | Configuration | +8 / 19 | Wireless Controllers | [Auto-generated summary] | Added 9 new data nodes |
| 5 | [Cisco-IOS-XE-wireless-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-general-cfg.yang) | Wireless General Cfg | Configuration | +2 / 69 | Wireless Controllers | [Auto-generated summary] | Added token, token-type, ap-dna-global-config; new enum values added; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-wireless-mobility-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-mobility-cfg.yang) | Wireless Mobility Cfg | Configuration | 26 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 7 | [Cisco-IOS-XE-wireless-radio-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-radio-cfg.yang) | Wireless Radio Cfg | Configuration | +1 / 39 | Wireless Controllers | [Auto-generated summary] | Added roaming-domain |
| 8 | [Cisco-IOS-XE-wireless-rlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-rlan-cfg.yang) | Wireless Rlan Cfg | Configuration | +4 / 66 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes |
| 9 | [Cisco-IOS-XE-wireless-rrm-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-rrm-cfg.yang) | Wireless Rrm Cfg | Configuration | +1 / 68 | Wireless Controllers | [Auto-generated summary] | Added bss-color-mode; new enum values added; enhanced validation constraints |
| 10 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless Site Cfg | Configuration | +18 / 263 | Wireless Controllers | [Auto-generated summary] | Added 12 new data nodes |
| 11 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | +17 / 314 | Wireless Controllers | [Auto-generated summary] | Added 17 new data nodes; new enum values added |

---

## UPDATED Operational Models (28 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-bgp-oper.yang) | Bgp Oper | Operational | +1 / 356 | All Platforms | [Auto-generated summary] | Added encaps-pref; new enum values added |
| 2 | [Cisco-IOS-XE-crypto-pki-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-crypto-pki-oper.yang) | Crypto Pki Oper | Operational | +4 / 8 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 3 | [Cisco-IOS-XE-device-hardware-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-device-hardware-oper.yang) | Device Hardware Oper | Operational | 36 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-docsis-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-docsis-oper.yang) | Docsis Oper | Operational | 386 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [Cisco-IOS-XE-gir-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-gir-oper.yang) | Gir Oper | Operational | 55 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [Cisco-IOS-XE-ha-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ha-oper.yang) | Ha Oper | Operational | 10 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces Oper | Operational | +5 / 428 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 8 | [Cisco-IOS-XE-ios-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ios-common-oper.yang) | Ios Common Oper | Operational | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 9 | [Cisco-IOS-XE-ios-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ios-events-oper.yang) | Ios Events Oper | Operational | +15 / 399 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; new enum values added |
| 10 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +22 / 355 | All Platforms | [Auto-generated summary] | Added 21 new data nodes |
| 11 | [Cisco-IOS-XE-mdt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mdt-oper.yang) | Mdt Oper | Operational | 54 | All Platforms | [Auto-generated summary] | new enum values added |
| 12 | [Cisco-IOS-XE-mka-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mka-oper.yang) | Mka Oper | Operational | 26 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 13 | [Cisco-IOS-XE-platform-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-platform-oper.yang) | Platform Oper | Operational | +1 / 52 | All Platforms | [Auto-generated summary] | Added status-desc; new enum values added |
| 14 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | +104 / 193 | All Platforms | [Auto-generated summary] | Added 72 new data nodes; new enum values added |
| 15 | [Cisco-IOS-XE-scada-gw-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-scada-gw-oper.yang) | Scada Gw Oper | Operational | 57 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 16 | [Cisco-IOS-XE-stack-mgr-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-stack-mgr-events-oper.yang) | Stack Mgr Events Oper | Operational | 9 | All Platforms | [Auto-generated summary] | new enum values added |
| 17 | [Cisco-IOS-XE-transceiver-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-transceiver-oper.yang) | Transceiver Oper | Operational | +2 / 55 | All Platforms | [Auto-generated summary] | Added fault-reason, last-event-time; imported Cisco-IOS-XE-ios-common-oper, ietf-yang-types |
| 18 | [Cisco-IOS-XE-trustsec-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-trustsec-oper.yang) | Trustsec Oper | Operational | +16 / 50 | All Platforms | [Auto-generated summary] | Added cts-rolebased-ipv6-policy |
| 19 | [Cisco-IOS-XE-ucse-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ucse-oper.yang) | Ucse Oper | Operational | 18 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 20 | [Cisco-IOS-XE-utd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-utd-oper.yang) | Utd Oper | Operational | +13 / 53 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; imported ietf-inet-types |
| 21 | [Cisco-IOS-XE-voice-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-voice-oper.yang) | Voice Oper | Operational | +72 / 160 | ISR, Voice Gateways | [Auto-generated summary] | Added 73 new data nodes; imported ietf-yang-types; new enum values added |
| 22 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | +48 / 412 | Wireless Controllers | [Auto-generated summary] | Added 46 new data nodes; new enum values added |
| 23 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | +33 / 214 | Wireless Controllers | [Auto-generated summary] | Added 30 new data nodes; new enum values added |
| 24 | [Cisco-IOS-XE-wireless-mdns-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-mdns-oper.yang) | Wireless Mdns Oper | Operational | +31 / 124 | Wireless Controllers | [Auto-generated summary] | Added glan-id, stats-glan, mdns-glan-stats |
| 25 | [Cisco-IOS-XE-wireless-mesh-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-mesh-oper.yang) | Wireless Mesh Oper | Operational | 264 | Wireless Controllers | [Auto-generated summary] | Added start-time, start-time |
| 26 | [Cisco-IOS-XE-wireless-mobility-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-mobility-oper.yang) | Wireless Mobility Oper | Operational | +5 / 322 | Wireless Controllers | [Auto-generated summary] | Added mblty-domain-info; imported Cisco-IOS-XE-ntp-oper |
| 27 | [Cisco-IOS-XE-wireless-rogue-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-rogue-oper.yang) | Wireless Rogue Oper | Operational | +1 / 302 | Wireless Controllers | [Auto-generated summary] | Added last-heard-ssid |
| 28 | [Cisco-IOS-XE-wireless-rrm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-rrm-oper.yang) | Wireless Rrm Oper | Operational | +10 / 88 | Wireless Controllers | [Auto-generated summary] | Added 10 new data nodes; new enum values added |

---

## UPDATED RPC Models (18 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-aaa-rpc.yang) | Aaa Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [Cisco-IOS-XE-arp-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-arp-rpc.yang) | Arp Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [Cisco-IOS-XE-bgp-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-bgp-rpc.yang) | Bgp Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-cable-diag-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cable-diag-rpc.yang) | Cable Diag Rpc | RPC | 8 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [Cisco-IOS-XE-cellular-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cellular-rpc.yang) | Cellular Rpc | RPC | 46 | IR1101, C1100 | [Auto-generated summary] | Added 16 new data nodes; deprecated 16 nodes |
| 6 | [Cisco-IOS-XE-crypto-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-crypto-rpc.yang) | Crypto Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; imported certificate";, id; deprecated 6 nodes |
| 7 | [Cisco-IOS-XE-cts-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cts-rpc.yang) | Cts Rpc | RPC | 77 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 8 | [Cisco-IOS-XE-dhcp-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-dhcp-rpc.yang) | Dhcp Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 9 | [Cisco-IOS-XE-factory-reset-secure-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-factory-reset-secure-rpc.yang) | Factory Reset Secure Rpc | RPC | 2 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [Cisco-IOS-XE-flow-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-flow-rpc.yang) | Flow Rpc | RPC | 18 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 11 | [Cisco-IOS-XE-ospf-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ospf-rpc.yang) | Ospf Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 12 | [Cisco-IOS-XE-platform-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-platform-rpc.yang) | Platform Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | Added 148 new data nodes; imported ietf-inet-types, Cisco-IOS-XE-types; enhanced validation constraints |
| 13 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +1078 / 1499 | All Platforms | [Auto-generated summary] | Added 26 new data nodes; deprecated 11 nodes |
| 14 | [Cisco-IOS-XE-switch-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-switch-rpc.yang) | Switch Rpc | RPC | +1 / 14 | Cat9K, IE3x00 | [Auto-generated summary] | Added statck, slot; new enum values added; deprecated 1 node |
| 15 | [Cisco-IOS-XE-ucse-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ucse-rpc.yang) | Ucse Rpc | RPC | 30 | All Platforms | [Auto-generated summary] | deprecated 1 node |
| 16 | [Cisco-IOS-XE-umbrella-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-umbrella-rpc.yang) | Umbrella Rpc | RPC | 4 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 17 | [Cisco-IOS-XE-utd-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-utd-rpc.yang) | Utd Rpc | RPC | +11 / 122 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; deprecated 3 nodes |
| 18 | [Cisco-IOS-XE-zone-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-zone-rpc.yang) | Zone Rpc | RPC | 6 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Types Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added; deprecated 1 node |
| 2 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 7 new data nodes; new enum values added |
| 3 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless Enum Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 4 | [Cisco-IOS-XE-wireless-mobility-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-mobility-types.yang) | Wireless Mobility Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes |
| 5 | [Cisco-IOS-XE-wireless-rrm-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-rrm-types.yang) | Wireless Rrm Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 6 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 7 | [common-mpls-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/common-mpls-types.yang) | Common Mpls Types | Types | 0 | ASR, ISR, NCS | [Auto-generated summary] | updated descriptions and documentation |
| 8 | [policy-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/policy-types.yang) | Policy Types | Types | 0 | All Platforms | [Auto-generated summary] | Added feature, feature; imported cisco-semver, ietf-inet-types; new enum values added |

---

## UPDATED Deviation Models (41 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-switch-deviation.yang) | Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [cisco-xe-access-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-access-openconfig-if-ethernet-deviation.yang) | Cisco Xe Access Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [cisco-xe-access-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-access-openconfig-platform-deviation.yang) | Cisco Xe Access Openconfig Platform Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [cisco-xe-access-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-access-openconfig-system-deviation.yang) | Cisco Xe Access Openconfig System Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [cisco-xe-access-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-access-openconfig-vlan-deviation.yang) | Cisco Xe Access Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | imported openconfig-interfaces, openconfig-vlan |
| 6 | [cisco-xe-cbr-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-cbr-openconfig-if-ethernet-deviation.yang) | Cisco Xe Cbr Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [cisco-xe-cbr-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-cbr-openconfig-system-deviation.yang) | Cisco Xe Cbr Openconfig System Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 8 | [cisco-xe-cbr-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-cbr-openconfig-vlan-deviation.yang) | Cisco Xe Cbr Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | imported openconfig-interfaces, openconfig-vlan |
| 9 | [cisco-xe-ietf-ip-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-ietf-ip-deviation.yang) | Cisco Xe Ietf Ip Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [cisco-xe-ietf-ipv4-unicast-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-ietf-ipv4-unicast-routing-deviation.yang) | Cisco Xe Ietf Ipv4 Unicast Routing Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 11 | [cisco-xe-ietf-ipv6-unicast-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-ietf-ipv6-unicast-routing-deviation.yang) | Cisco Xe Ietf Ipv6 Unicast Routing Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 12 | [cisco-xe-ietf-ospf-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-ietf-ospf-deviation.yang) | Cisco Xe Ietf Ospf Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 13 | [cisco-xe-ietf-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-ietf-routing-deviation.yang) | Cisco Xe Ietf Routing Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 14 | [cisco-xe-openconfig-acl-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-acl-deviation.yang) | Cisco Xe Openconfig Acl Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 15 | [cisco-xe-openconfig-aft-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-aft-deviation.yang) | Cisco Xe Openconfig Aft Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 16 | [cisco-xe-openconfig-bgp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-bgp-deviation.yang) | Cisco Xe Openconfig Bgp Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 17 | [cisco-xe-openconfig-bgp-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-bgp-policy-deviation.yang) | Cisco Xe Openconfig Bgp Policy Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 18 | [cisco-xe-openconfig-if-ip-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-if-ip-deviation.yang) | Cisco Xe Openconfig If Ip Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | added 3 new imports |
| 19 | [cisco-xe-openconfig-if-poe-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-if-poe-deviation.yang) | Cisco Xe Openconfig If Poe Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 20 | [cisco-xe-openconfig-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-interfaces-deviation.yang) | Cisco Xe Openconfig Interfaces Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 21 | [cisco-xe-openconfig-isis-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-isis-deviation.yang) | Cisco Xe Openconfig Isis Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 22 | [cisco-xe-openconfig-lldp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-lldp-deviation.yang) | Cisco Xe Openconfig Lldp Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 23 | [cisco-xe-openconfig-mpls-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-mpls-deviation.yang) | Cisco Xe Openconfig Mpls Deviation | Deviation | 0 | ASR, ISR, NCS | [Auto-generated summary] | updated descriptions and documentation |
| 24 | [cisco-xe-openconfig-network-instance-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-network-instance-deviation.yang) | Cisco Xe Openconfig Network Instance Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 25 | [cisco-xe-openconfig-openflow-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-openflow-deviation.yang) | Cisco Xe Openconfig Openflow Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Added not, not; deprecated 2 nodes |
| 26 | [cisco-xe-openconfig-routing-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-routing-policy-deviation.yang) | Cisco Xe Openconfig Routing Policy Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 27 | [cisco-xe-openconfig-segment-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-segment-routing-deviation.yang) | Cisco Xe Openconfig Segment Routing Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 28 | [cisco-xe-openconfig-spanning-tree-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-openconfig-spanning-tree-deviation.yang) | Cisco Xe Openconfig Spanning Tree Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported openconfig-spanning-tree |
| 29 | [cisco-xe-routing-asr-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-routing-asr-openconfig-if-ethernet-deviation.yang) | Cisco Xe Routing Asr Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 30 | [cisco-xe-routing-csr-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-routing-csr-openconfig-platform-deviation.yang) | Cisco Xe Routing Csr Openconfig Platform Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 31 | [cisco-xe-routing-isr-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-routing-isr-openconfig-if-ethernet-deviation.yang) | Cisco Xe Routing Isr Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 32 | [cisco-xe-routing-isr-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-routing-isr-openconfig-platform-deviation.yang) | Cisco Xe Routing Isr Openconfig Platform Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 33 | [cisco-xe-routing-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-routing-openconfig-system-deviation.yang) | Cisco Xe Routing Openconfig System Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 34 | [cisco-xe-routing-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-routing-openconfig-vlan-deviation.yang) | Cisco Xe Routing Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | imported openconfig-interfaces, openconfig-vlan |
| 35 | [cisco-xe-switching-cat9k-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-switching-cat9k-openconfig-system-deviation.yang) | Cisco Xe Switching Cat9K Openconfig System Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | enhanced validation constraints |
| 36 | [cisco-xe-switching-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-switching-openconfig-if-ethernet-deviation.yang) | Cisco Xe Switching Openconfig If Ethernet Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 37 | [cisco-xe-switching-openconfig-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-switching-openconfig-interfaces-deviation.yang) | Cisco Xe Switching Openconfig Interfaces Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 38 | [cisco-xe-switching-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-switching-openconfig-platform-deviation.yang) | Cisco Xe Switching Openconfig Platform Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | enhanced validation constraints |
| 39 | [cisco-xe-switching-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-switching-openconfig-vlan-deviation.yang) | Cisco Xe Switching Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | imported openconfig-interfaces, openconfig-vlan |
| 40 | [cisco-xe-wireless-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-wireless-openconfig-if-ethernet-deviation.yang) | Cisco Xe Wireless Openconfig If Ethernet Deviation | Deviation | 0 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 41 | [cisco-xe-wireless-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-xe-wireless-openconfig-vlan-deviation.yang) | Cisco Xe Wireless Openconfig Vlan Deviation | Deviation | 0 | Wireless Controllers | [Auto-generated summary] | imported openconfig-interfaces, openconfig-vlan |

---

## UPDATED Native Models (118 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +252 / 2336 | All Platforms | [Auto-generated summary] | Added 159 new data nodes; new enum values added; enhanced validation constraints |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-acl.yang) | Acl | Native | 0 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; new enum values added; deprecated 17 nodes |
| 3 | [Cisco-IOS-XE-arp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-arp.yang) | Arp | Native | 13 | All Platforms | [Auto-generated summary] | new enum values added; enhanced validation constraints |
| 4 | [Cisco-IOS-XE-atm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-atm.yang) | Atm | Native | +12 / 1158 | All Platforms | [Auto-generated summary] | Added 42 new data nodes; new enum values added; deprecated 42 nodes |
| 5 | [Cisco-IOS-XE-avb.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-avb.yang) | Avb | Native | 1 | All Platforms | [Auto-generated summary] | Added strict; deprecated 1 node |
| 6 | [Cisco-IOS-XE-bba-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-bba-group.yang) | Bba Group | Native | 12 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-bfd.yang) | Bfd | Native | 296 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; deprecated 13 nodes |
| 8 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +946 / 17624 | All Platforms | [Auto-generated summary] | Added 223 new data nodes; imported configuration";; new enum values added |
| 9 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-bridge-domain.yang) | Bridge Domain | Native | +76 / 245 | All Platforms | [Auto-generated summary] | Added 39 new data nodes; new enum values added; enhanced validation constraints |
| 10 | [Cisco-IOS-XE-call-home.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-call-home.yang) | Call Home | Native | +2 / 161 | All Platforms | [Auto-generated summary] | Added begin-time, begin-time, pattern; new enum values added; deprecated 3 nodes |
| 11 | [Cisco-IOS-XE-card.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-card.yang) | Card | Native | 4 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 12 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cdp.yang) | Cdp | Native | 135 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; enhanced validation constraints; deprecated 15 nodes |
| 13 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cef.yang) | Cef | Native | 167 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; deprecated 8 nodes |
| 14 | [Cisco-IOS-XE-cellular.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cellular.yang) | Cellular | Native | 3 | IR1101, C1100 | [Auto-generated summary] | updated descriptions and documentation |
| 15 | [Cisco-IOS-XE-coap.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-coap.yang) | Coap | Native | 3 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 16 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-controller.yang) | Controller | Native | +8 / 366 | All Platforms | [Auto-generated summary] | Added 52 new data nodes; new enum values added; deprecated 45 nodes |
| 17 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-crypto.yang) | Crypto | Native | -4812 / 0 | All Platforms | [Auto-generated summary] | Added 102 new data nodes; imported url'; new enum values added |
| 18 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-cts.yang) | Cts | Native | +24 / 507 | All Platforms | [Auto-generated summary] | Added 31 new data nodes; new enum values added; enhanced validation constraints |
| 19 | [Cisco-IOS-XE-dapr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-dapr.yang) | Dapr | Native | 129 | All Platforms | [Auto-generated summary] | Added to; deprecated 1 node |
| 20 | [Cisco-IOS-XE-device-sensor.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-device-sensor.yang) | Device Sensor | Native | 4 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 21 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | -3 / 50 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; enhanced validation constraints; deprecated 7 nodes |
| 22 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +44 / 3384 | All Platforms | [Auto-generated summary] | Added 48 new data nodes; imported {, options; enhanced validation constraints |
| 23 | [Cisco-IOS-XE-diagnostics.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-diagnostics.yang) | Diagnostics | Native | 316 | All Platforms | [Auto-generated summary] | Added 25 new data nodes; new enum values added; deprecated 40 nodes |
| 24 | [Cisco-IOS-XE-dialer.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-dialer.yang) | Dialer | Native | 30 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 25 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | +23 / 268 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; enhanced validation constraints; deprecated 10 nodes |
| 26 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-eem.yang) | Eem | Native | 130 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; deprecated 5 nodes |
| 27 | [Cisco-IOS-XE-eigrp-obsolete.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-eigrp-obsolete.yang) | Eigrp Obsolete | Native | 0 | All Platforms | [Auto-generated summary] | Added 250 new data nodes; enhanced validation constraints; deprecated 20 nodes |
| 28 | [Cisco-IOS-XE-eigrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-eigrp.yang) | Eigrp | Native | +417 / 4724 | All Platforms | [Auto-generated summary] | Added 72 new data nodes; new enum values added; enhanced validation constraints |
| 29 | [Cisco-IOS-XE-eta.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-eta.yang) | Eta | Native | 66 | All Platforms | [Auto-generated summary] | imported Cisco-IOS-XE-features; deprecated 1 node |
| 30 | [Cisco-IOS-XE-ethernet-cfm-efp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ethernet-cfm-efp.yang) | Ethernet Cfm Efp | Native | 0 | All Platforms | [Auto-generated summary] | Added 258 new data nodes; new enum values added; enhanced validation constraints |
| 31 | [Cisco-IOS-XE-ethernet-oam.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ethernet-oam.yang) | Ethernet Oam | Native | 0 | All Platforms | [Auto-generated summary] | Added 71 new data nodes; new enum values added; deprecated 56 nodes |
| 32 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | +2237 / 7252 | All Platforms | [Auto-generated summary] | Added 47 new data nodes; imported Cisco-IOS-XE-types; new enum values added |
| 33 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | +15 / 208 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; deprecated 2 nodes |
| 34 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 35 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-flow.yang) | Flow | Native | -78 / 2426 | All Platforms | [Auto-generated summary] | Added 37 new data nodes; new enum values added; deprecated 29 nodes |
| 36 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-http.yang) | Http | Native | 36 | All Platforms | [Auto-generated summary] | new enum values added |
| 37 | [Cisco-IOS-XE-icmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-icmp.yang) | Icmp | Native | +4 / 37 | All Platforms | [Auto-generated summary] | Added icmp, time; deprecated 2 nodes |
| 38 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-igmp.yang) | Igmp | Native | +140 / 4667 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; enhanced validation constraints; deprecated 1 node |
| 39 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | Added interface'";, Async, Async; deprecated 1 node |
| 40 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 71 new data nodes; new enum values added; enhanced validation constraints |
| 41 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 104 new data nodes; imported {; new enum values added |
| 42 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added 30 new data nodes; new enum values added; enhanced validation constraints |
| 43 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-isis.yang) | Isis | Native | +1362 / 4713 | All Platforms | [Auto-generated summary] | Added 163 new data nodes; new enum values added; enhanced validation constraints |
| 44 | [Cisco-IOS-XE-iwanfabric.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-iwanfabric.yang) | Iwanfabric | Native | 134 | All Platforms | [Auto-generated summary] | Added 63 new data nodes; added 6 new imports; deprecated 63 nodes |
| 45 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +119 / 1452 | All Platforms | [Auto-generated summary] | Added 109 new data nodes; imported Cisco-IOS-XE-mpls; new enum values added |
| 46 | [Cisco-IOS-XE-l3vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-l3vpn.yang) | L3Vpn | Native | 11 | All Platforms | [Auto-generated summary] | Added profile-name"; |
| 47 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; new enum values added; enhanced validation constraints |
| 48 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; deprecated 1 node |
| 49 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +3000 / 23209 | All Platforms | [Auto-generated summary] | Added 52 new data nodes; imported {, of; new enum values added |
| 50 | [Cisco-IOS-XE-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-lldp.yang) | Lldp | Native | 114 | All Platforms | [Auto-generated summary] | Added to; deprecated 1 node |
| 51 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | Added 29 new data nodes; new enum values added |
| 52 | [Cisco-IOS-XE-mdns-gateway.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mdns-gateway.yang) | Mdns Gateway | Native | +354 / 381 | All Platforms | [Auto-generated summary] | Added 91 new data nodes; added 5 new imports; new enum values added |
| 53 | [Cisco-IOS-XE-mka.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mka.yang) | Mka | Native | 79 | All Platforms | [Auto-generated summary] | new enum values added |
| 54 | [Cisco-IOS-XE-mld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mld.yang) | Mld | Native | +1 / 466 | All Platforms | [Auto-generated summary] | Added to, mld, dns-leaf; deprecated 1 node |
| 55 | [Cisco-IOS-XE-mmode.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mmode.yang) | Mmode | Native | 30 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 56 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mpls.yang) | Mpls | Native | 0 | ASR, ISR, NCS | [Auto-generated summary] | Added 34 new data nodes; new enum values added; enhanced validation constraints |
| 57 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +27 / 3668 | All Platforms | [Auto-generated summary] | Added 42 new data nodes; new enum values added; enhanced validation constraints |
| 58 | [Cisco-IOS-XE-mvrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-mvrp.yang) | Mvrp | Native | 145 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; deprecated 18 nodes |
| 59 | [Cisco-IOS-XE-nam.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-nam.yang) | Nam | Native | 39 | All Platforms | [Auto-generated summary] | Added analysis-module, monitoring, interface-name; imported cisco-semver; deprecated 3 nodes |
| 60 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-nat.yang) | Nat | Native | +430 / 1348 | All Platforms | [Auto-generated summary] | Added 92 new data nodes; new enum values added; enhanced validation constraints |
| 61 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-native.yang) | Native | Native | +2602 / 31537 | All Platforms | [Auto-generated summary] | Added 189 new data nodes; new enum values added; deprecated 138 nodes |
| 62 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +2 / 571 | All Platforms | [Auto-generated summary] | Added 65 new data nodes; deprecated 65 nodes |
| 63 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-nd.yang) | Nd | Native | +14 / 319 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; deprecated 3 nodes |
| 64 | [Cisco-IOS-XE-nhrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-nhrp.yang) | Nhrp | Native | +6303 / 8209 | All Platforms | [Auto-generated summary] | Added 302 new data nodes; imported Cisco-IOS-XE-features; new enum values added |
| 65 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ntp.yang) | Ntp | Native | +23 / 394 | All Platforms | [Auto-generated summary] | Added 14 new data nodes; enhanced validation constraints; deprecated 3 nodes |
| 66 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-object-group.yang) | Object Group | Native | +9 / 195 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; enhanced validation constraints; deprecated 2 nodes |
| 67 | [Cisco-IOS-XE-ospf-obsolete.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ospf-obsolete.yang) | Ospf Obsolete | Native | 0 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; new enum values added; enhanced validation constraints |
| 68 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ospf.yang) | Ospf | Native | 0 | All Platforms | [Auto-generated summary] | Added 23 new data nodes; new enum values added; enhanced validation constraints |
| 69 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | +318 / 16275 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; new enum values added; enhanced validation constraints |
| 70 | [Cisco-IOS-XE-otv.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-otv.yang) | Otv | Native | +93 / 1074 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 71 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | [Auto-generated summary] | Added parser, privilege; deprecated 2 nodes |
| 72 | [Cisco-IOS-XE-pathmgr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-pathmgr.yang) | Pathmgr | Native | 59 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 73 | [Cisco-IOS-XE-pfr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-pfr.yang) | Pfr | Native | +4 / 454 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 74 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-platform.yang) | Platform | Native | +4 / 119 | All Platforms | [Auto-generated summary] | Added 22 new data nodes; deprecated 18 nodes |
| 75 | [Cisco-IOS-XE-pnp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-pnp.yang) | Pnp | Native | +28 / 37 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; deprecated 4 nodes |
| 76 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-policy.yang) | Policy | Native | +106 / 3004 | All Platforms | [Auto-generated summary] | Added 99 new data nodes; new enum values added; enhanced validation constraints |
| 77 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-power.yang) | Power | Native | +71 / 269 | All Platforms | [Auto-generated summary] | Added 24 new data nodes; deprecated 8 nodes |
| 78 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ppp.yang) | Ppp | Native | 411 | All Platforms | [Auto-generated summary] | Added 84 new data nodes; new enum values added; enhanced validation constraints |
| 79 | [Cisco-IOS-XE-pppoe.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-pppoe.yang) | Pppoe | Native | +2 / 15 | All Platforms | [Auto-generated summary] | Added to, dial-pool-number-list, number |
| 80 | [Cisco-IOS-XE-ptp-pi.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ptp-pi.yang) | Ptp Pi | Native | +84 / 593 | All Platforms | [Auto-generated summary] | Added 26 new data nodes; imported Cisco-IOS-XE-types; new enum values added |
| 81 | [Cisco-IOS-XE-ptp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ptp.yang) | Ptp | Native | 12 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; deprecated 13 nodes |
| 82 | [Cisco-IOS-XE-qfp-stats.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-qfp-stats.yang) | Qfp Stats | Native | 979 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 83 | [Cisco-IOS-XE-qos.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-qos.yang) | Qos | Native | -2 / 36 | All Platforms | [Auto-generated summary] | Added layer-all, marking, error; deprecated 3 nodes |
| 84 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-rip.yang) | Rip | Native | 1311 | All Platforms | [Auto-generated summary] | Added 14 new data nodes; enhanced validation constraints; deprecated 14 nodes |
| 85 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +30 / 1035 | All Platforms | [Auto-generated summary] | Added 279 new data nodes; imported route";; new enum values added |
| 86 | [Cisco-IOS-XE-rsvp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-rsvp.yang) | Rsvp | Native | 642 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 87 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-sanet.yang) | Sanet | Native | +133 / 858 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; new enum values added; deprecated 1 node |
| 88 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | 219 | All Platforms | [Auto-generated summary] | Added name";, type, configuration";; new enum values added; enhanced validation constraints |
| 89 | [Cisco-IOS-XE-serial.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-serial.yang) | Serial | Native | 39 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 90 | [Cisco-IOS-XE-service-discovery.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-service-discovery.yang) | Service Discovery | Native | 29 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; deprecated 7 nodes |
| 91 | [Cisco-IOS-XE-service-insertion.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-service-insertion.yang) | Service Insertion | Native | +181 / 229 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; imported Cisco-IOS-XE-interface-common; new enum values added |
| 92 | [Cisco-IOS-XE-service-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-service-routing.yang) | Service Routing | Native | 6 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 93 | [Cisco-IOS-XE-site-manager.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-site-manager.yang) | Site Manager | Native | 265 | All Platforms | [Auto-generated summary] | new enum values added |
| 94 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-sla.yang) | Sla | Native | +645 / 2601 | All Platforms | [Auto-generated summary] | Added 298 new data nodes; new enum values added; enhanced validation constraints |
| 95 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +468 / 1505 | All Platforms | [Auto-generated summary] | Added 661 new data nodes; new enum values added; enhanced validation constraints |
| 96 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | 372 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; deprecated 4 nodes |
| 97 | [Cisco-IOS-XE-stackwise-virtual.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-stackwise-virtual.yang) | Stackwise Virtual | Native | 8 | All Platforms | [Auto-generated summary] | Added trust, channel-group; deprecated 2 nodes |
| 98 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-switch.yang) | Switch | Native | +602 / 4638 | Cat9K, IE3x00 | [Auto-generated summary] | Added 245 new data nodes; imported Cisco-IOS-XE-device-tracking; new enum values added |
| 99 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-template.yang) | Template | Native | +278 / 1513 | All Platforms | [Auto-generated summary] | Added 114 new data nodes; imported Cisco-IOS-XE-policy; new enum values added |
| 100 | [Cisco-IOS-XE-track.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-track.yang) | Track | Native | 140 | All Platforms | [Auto-generated summary] | Added metric, state; new enum values added; deprecated 2 nodes |
| 101 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | +14 / 1534 | All Platforms | [Auto-generated summary] | Added 16 new data nodes; enhanced validation constraints; deprecated 15 nodes |
| 102 | [Cisco-IOS-XE-ucse.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-ucse.yang) | Ucse | Native | 48 | All Platforms | [Auto-generated summary] | deprecated 10 nodes |
| 103 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-udld.yang) | Udld | Native | 83 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 104 | [Cisco-IOS-XE-umbrella-oper-dp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-umbrella-oper-dp.yang) | Umbrella Oper Dp | Native | 31 | All Platforms | [Auto-generated summary] | new enum values added |
| 105 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-umbrella.yang) | Umbrella | Native | +2 / 204 | All Platforms | [Auto-generated summary] | Added non-global-parameter-map, name; new enum values added; enhanced validation constraints |
| 106 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-utd.yang) | Utd | Native | 365 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added; enhanced validation constraints |
| 107 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-vlan.yang) | Vlan | Native | 109 | Cat9K, IE3x00 | [Auto-generated summary] | Added 10 new data nodes; imported Cisco-IOS-XE-device-tracking; enhanced validation constraints |
| 108 | [Cisco-IOS-XE-voice-register.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-voice-register.yang) | Voice Register | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 8 new data nodes; enhanced validation constraints |
| 109 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-voice.yang) | Voice | Native | +24 / 370 | ISR, Voice Gateways | [Auto-generated summary] | Added 25 new data nodes; new enum values added; deprecated 19 nodes |
| 110 | [Cisco-IOS-XE-vpdn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-vpdn.yang) | Vpdn | Native | 4 | All Platforms | [Auto-generated summary] | Added vpdn; deprecated 1 node |
| 111 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-vrrp.yang) | Vrrp | Native | 960 | All Platforms | [Auto-generated summary] | Added 40 new data nodes; new enum values added; deprecated 44 nodes |
| 112 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-vservice.yang) | Vservice | Native | 36 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 113 | [Cisco-IOS-XE-vstack.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-vstack.yang) | Vstack | Native | 2 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 114 | [Cisco-IOS-XE-vtp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-vtp.yang) | Vtp | Native | 28 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 115 | [Cisco-IOS-XE-vxlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-vxlan.yang) | Vxlan | Native | 2 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 116 | [Cisco-IOS-XE-wccp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wccp.yang) | Wccp | Native | 440 | All Platforms | [Auto-generated summary] | Added wccp; deprecated 1 node |
| 117 | [Cisco-IOS-XE-wsma.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-wsma.yang) | Wsma | Native | 13 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 118 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/Cisco-IOS-XE-zone.yang) | Zone | Native | +2 / 58 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED OpenConfig Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [openconfig-system.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/openconfig-system.yang) | Openconfig System | OpenConfig | +13 / 372 | All Platforms | [Auto-generated summary] | imported openconfig-system-management |

---

## UPDATED Other Models (19 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-bridge-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-bridge-common.yang) | Cisco Bridge Common | Other | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 2 | [cisco-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-bridge-domain.yang) | Cisco Bridge Domain | Other | 252 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added; enhanced validation constraints |
| 3 | [cisco-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-ethernet.yang) | Cisco Ethernet | Other | 14 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; imported ietf-interfaces, iana-if-type; new enum values added |
| 4 | [cisco-ia.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-ia.yang) | Cisco Ia | Other | 84 | All Platforms | [Auto-generated summary] | Added for, cisco-ia, describes; deprecated 9 nodes |
| 5 | [cisco-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-ospf.yang) | Cisco Ospf | Other | 213 | All Platforms | [Auto-generated summary] | Added 30 new data nodes; new enum values added; deprecated 31 nodes |
| 6 | [cisco-policy-filters.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-policy-filters.yang) | Cisco Policy Filters | Other | 167 | All Platforms | [Auto-generated summary] | Added 73 new data nodes; added 3 new imports; enhanced validation constraints |
| 7 | [cisco-policy-target.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-policy-target.yang) | Cisco Policy Target | Other | 1 | All Platforms | [Auto-generated summary] | Added service-policy-type; deprecated 1 node |
| 8 | [cisco-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-policy.yang) | Cisco Policy | Other | 1 | All Platforms | [Auto-generated summary] | Added policy-type; deprecated 1 node |
| 9 | [cisco-pw.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-pw.yang) | Cisco Pw | Other | 165 | All Platforms | [Auto-generated summary] | new enum values added; deprecated 9 nodes |
| 10 | [cisco-routing-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-routing-ext.yang) | Cisco Routing Ext | Other | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 11 | [cisco-self-mgmt.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-self-mgmt.yang) | Cisco Self Mgmt | Other | 1 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 12 | [cisco-semver.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-semver.yang) | Cisco Semver | Other | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 13 | [cisco-smart-license-errors.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-smart-license-errors.yang) | Cisco Smart License Errors | Other | 0 | All Platforms | [Auto-generated summary] | Added is, ";, contains; new enum values added; deprecated 3 nodes |
| 14 | [cisco-smart-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-smart-license.yang) | Cisco Smart License | Other | 191 | All Platforms | [Auto-generated summary] | Added 45 new data nodes; new enum values added; enhanced validation constraints |
| 15 | [cisco-storm-control.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/cisco-storm-control.yang) | Cisco Storm Control | Other | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 16 | [common-mpls-static.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/common-mpls-static.yang) | Common Mpls Static | Other | 296 | ASR, ISR, NCS | [Auto-generated summary] | Added 39 new data nodes; new enum values added; deprecated 40 nodes |
| 17 | [nvo.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/nvo.yang) | Nvo | Other | 21 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 18 | [pim.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/pim.yang) | Pim | Other | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 19 | [policy-attr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1711/policy-attr.yang) | Policy Attr | Other | 0 | All Platforms | [Auto-generated summary] | Added 58 new data nodes; added 3 new imports; new enum values added |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
