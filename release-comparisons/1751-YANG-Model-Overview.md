# All YANG Model Changes: v17.4.1 → v17.5.1
**Summary: 31 New Models & 274 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (31 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 9 | 870 XPaths |
| **[NEW RPC Models](#new-rpc-models)** | 4 | 27 XPaths |
| **[NEW Events Models](#new-events-models)** | 6 | 47 XPaths |
| **[NEW Types Models](#new-types-models)** | 1 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 6 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 4 | 33 XPaths |
| **[NEW Vendor Models](#new-vendor-models)** | 1 | 11 XPaths |
| **TOTAL NEW MODELS** | **31** | **988 total XPaths** |

---

## UPDATED Models Summary (274 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 32 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 126 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 8 | XPath changes vary |
| **[UPDATED Events Models](#updated-events-models)** | 8 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 17 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 4 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 74 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 1 | XPath changes vary |
| **[UPDATED IETF Models](#updated-ietf-models)** | 1 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 1 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 2 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **274** | **See individual models** |

---

## Key Highlights - NEW Models


**31 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-dre-oper.yang`: 395 XPaths (Operational)

  - `Cisco-IOS-XE-docsis-oper.yang`: 386 XPaths (Operational)

  - `Cisco-IOS-XE-adsl.yang`: 29 XPaths (Native)


- **Breakdown by category:**

  - Operational: 9 models

  - Deviation: 6 models

  - Events: 6 models

  - Native: 4 models

  - RPC: 4 models

  - Types: 1 model

  - Vendor: 1 model


---


## Key Highlights - UPDATED Models


**274 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-ethernet.yang`: +1,476 XPaths (now 11,132 total)

  - `Cisco-IOS-XE-lisp.yang`: +1,248 XPaths (now 27,253 total)

  - `Cisco-IOS-XE-nd.yang`: +831 XPaths (now 1,726 total)


- **Significant removals:**

  - `Cisco-IOS-XE-wireless-rogue-oper.yang`: -5 XPaths (now 308 total)

  - `Cisco-IOS-XE-boot-integrity-oper.yang`: -3 XPaths (now 20 total)


- **Updates by category:**

  - Operational: 126 models

  - Native: 74 models

  - Configuration: 32 models

  - Types: 17 models

  - Events: 8 models

  - RPC: 8 models

  - Deviation: 4 models

  - Other: 2 models

  - Vendor: 1 model

  - IETF: 1 model

  - OpenConfig: 1 model


---


## Summary Statistics

### Release v17.5.1 Totals:
- **Total YANG Files:** ~705 files
- **New Files:** 31 models
- **Modified Files:** 274 models
- **Deleted Files:** 3 models
- **New Model XPaths:** 988 XPaths across 31 new models

---

# NEW YANG Models in v17.5.1

**31 Brand New Models**

---

## NEW Operational Models (9 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-docsis-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-docsis-oper.yang) | Docsis Oper | Operational | 386 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-dre-cp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-dre-cp-oper.yang) | Dre Cp Oper | Operational | 6 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-dre-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-dre-oper.yang) | Dre Oper | Operational | 395 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-geo-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-geo-oper.yang) | Geo Oper | Operational | 5 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-gnss-dr-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-gnss-dr-oper.yang) | Gnss Dr Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-netconf-diag-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-netconf-diag-oper.yang) | Netconf Diag Oper | Operational | 13 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-psecure-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-psecure-oper.yang) | Psecure Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-switch-cp-svl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-switch-cp-svl-oper.yang) | Switch Cp Svl Oper | Operational | 29 | Cat9K, IE3x00 | New model introduced in this release |
| 9 | [Cisco-IOS-XE-wireless-ap-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-ap-global-oper.yang) | Wireless Ap Global Oper | Operational | 20 | Wireless Controllers | New model introduced in this release |

---

## NEW RPC Models (4 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-crypto-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-crypto-actions-rpc.yang) | Crypto Actions Rpc | RPC | 3 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-geo-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-geo-rpc.yang) | Geo Rpc | RPC | 7 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-netconf-diag-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-netconf-diag-rpc.yang) | Netconf Diag Rpc | RPC | 6 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-xcopy-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-xcopy-rpc.yang) | Xcopy Rpc | RPC | 11 | All Platforms | New model introduced in this release |

---

## NEW Events Models (6 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-dca-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-dca-events.yang) | Dca Events | Events | 6 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-geo-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-geo-events.yang) | Geo Events | Events | 4 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-l2vpn-pw-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-l2vpn-pw-events.yang) | L2Vpn Pw Events | Events | 4 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-platform-software-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-platform-software-events.yang) | Platform Software Events | Events | 11 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-vrrp-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-vrrp-events.yang) | Vrrp Events | Events | 8 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-xcopy-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-xcopy-events.yang) | Xcopy Events | Events | 14 | All Platforms | New model introduced in this release |

---

## NEW Types Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-vrrp-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-vrrp-types.yang) | Vrrp Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Deviation Models (6 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-cts-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cts-routing-deviation.yang) | Cts Routing Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-line-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-line-deviation.yang) | Line Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 3 | [cisco-xe-cbr-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-xe-cbr-openconfig-if-ethernet-deviation.yang) | Cisco Xe Cbr Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 4 | [cisco-xe-cbr-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-xe-cbr-openconfig-system-deviation.yang) | Cisco Xe Cbr Openconfig System Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 5 | [cisco-xe-cbr-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-xe-cbr-openconfig-vlan-deviation.yang) | Cisco Xe Cbr Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 6 | [cisco-xe-openconfig-local-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-xe-openconfig-local-routing-deviation.yang) | Cisco Xe Openconfig Local Routing Deviation | Deviation | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (4 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-adsl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-adsl.yang) | Adsl | Native | 29 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-fqdn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-fqdn.yang) | Fqdn | Native | 2 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-geo.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-geo.yang) | Geo | Native | 2 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-sip-ua.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-sip-ua.yang) | Sip Ua | Native | 0 | ISR, Voice Gateways | New model introduced in this release |

---

## NEW Vendor Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [tailf-netconf-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/tailf-netconf-extensions.yang) | Tailf Netconf Extensions | Vendor | 11 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v17.4.1 → v17.5.1

**274 Models Modified**

---

## UPDATED Configuration Models (32 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-app-hosting-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-app-hosting-cfg.yang) | App Hosting Cfg | Configuration | +44 / 137 | All Platforms | [Auto-generated summary] | Added 37 new data nodes; new enum values added; enhanced validation constraints |
| 2 | [Cisco-IOS-XE-mdt-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mdt-cfg.yang) | Mdt Cfg | Configuration | 142 | All Platforms | [Auto-generated summary] | new enum values added; enhanced validation constraints |
| 3 | [Cisco-IOS-XE-ncch-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ncch-cfg.yang) | Ncch Cfg | Configuration | 24 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [Cisco-IOS-XE-wireless-ap-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-ap-cfg.yang) | Wireless Ap Cfg | Configuration | 38 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 5 | [Cisco-IOS-XE-wireless-apf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-apf-cfg.yang) | Wireless Apf Cfg | Configuration | +2 / 59 | Wireless Controllers | [Auto-generated summary] | Added 5 new data nodes; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-wireless-cts-sxp-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-cts-sxp-cfg.yang) | Wireless Cts Sxp Cfg | Configuration | 16 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-wireless-dot11-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-dot11-cfg.yang) | Wireless Dot11 Cfg | Configuration | +1 / 168 | Wireless Controllers | [Auto-generated summary] | Added edca-client-load-based; enhanced validation constraints |
| 8 | [Cisco-IOS-XE-wireless-dot15-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-dot15-cfg.yang) | Wireless Dot15 Cfg | Configuration | 3 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 9 | [Cisco-IOS-XE-wireless-fabric-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-fabric-cfg.yang) | Wireless Fabric Cfg | Configuration | 27 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 10 | [Cisco-IOS-XE-wireless-file-transfer-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-file-transfer-cfg.yang) | Wireless File Transfer Cfg | Configuration | 55 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 11 | [Cisco-IOS-XE-wireless-flex-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-flex-cfg.yang) | Wireless Flex Cfg | Configuration | 58 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 12 | [Cisco-IOS-XE-wireless-fqdn-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-fqdn-cfg.yang) | Wireless Fqdn Cfg | Configuration | 19 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 13 | [Cisco-IOS-XE-wireless-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-general-cfg.yang) | Wireless General Cfg | Configuration | +15 / 105 | Wireless Controllers | [Auto-generated summary] | Added 15 new data nodes; enhanced validation constraints |
| 14 | [Cisco-IOS-XE-wireless-hotspot-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-hotspot-cfg.yang) | Wireless Hotspot Cfg | Configuration | +1 / 119 | Wireless Controllers | [Auto-generated summary] | Added aaa-operator-name; new enum values added |
| 15 | [Cisco-IOS-XE-wireless-image-download-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-image-download-cfg.yang) | Wireless Image Download Cfg | Configuration | +2 / 28 | Wireless Controllers | [Auto-generated summary] | Added auto-path; new enum values added; enhanced validation constraints |
| 16 | [Cisco-IOS-XE-wireless-location-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-location-cfg.yang) | Wireless Location Cfg | Configuration | 23 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 17 | [Cisco-IOS-XE-wireless-me-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-me-general-cfg.yang) | Wireless Me General Cfg | Configuration | 9 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 18 | [Cisco-IOS-XE-wireless-mesh-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mesh-cfg.yang) | Wireless Mesh Cfg | Configuration | 59 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 19 | [Cisco-IOS-XE-wireless-mobility-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mobility-cfg.yang) | Wireless Mobility Cfg | Configuration | +1 / 27 | Wireless Controllers | [Auto-generated summary] | Added mm-dtls-high-cipher; enhanced validation constraints |
| 20 | [Cisco-IOS-XE-wireless-mstream-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mstream-cfg.yang) | Wireless Mstream Cfg | Configuration | 20 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 21 | [Cisco-IOS-XE-wireless-radio-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-radio-cfg.yang) | Wireless Radio Cfg | Configuration | +2 / 41 | Wireless Controllers | [Auto-generated summary] | Added 5 new data nodes |
| 22 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless Rf Cfg | Configuration | +2 / 154 | Wireless Controllers | [Auto-generated summary] | Added ndp-mode, ndp-mode; new enum values added; enhanced validation constraints |
| 23 | [Cisco-IOS-XE-wireless-rfid-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rfid-cfg.yang) | Wireless Rfid Cfg | Configuration | 8 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 24 | [Cisco-IOS-XE-wireless-rlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rlan-cfg.yang) | Wireless Rlan Cfg | Configuration | 66 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 25 | [Cisco-IOS-XE-wireless-rogue-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rogue-cfg.yang) | Wireless Rogue Cfg | Configuration | 76 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 26 | [Cisco-IOS-XE-wireless-rrm-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rrm-cfg.yang) | Wireless Rrm Cfg | Configuration | 68 | Wireless Controllers | [Auto-generated summary] | Added rf-profile-default-entries,; enhanced validation constraints |
| 27 | [Cisco-IOS-XE-wireless-rule-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rule-cfg.yang) | Wireless Rule Cfg | Configuration | 15 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 28 | [Cisco-IOS-XE-wireless-security-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-security-cfg.yang) | Wireless Security Cfg | Configuration | 16 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 29 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless Site Cfg | Configuration | +16 / 297 | Wireless Controllers | [Auto-generated summary] | Added oeap, stats-monitor, ap-dtls-config |
| 30 | [Cisco-IOS-XE-wireless-tunnel-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-tunnel-cfg.yang) | Wireless Tunnel Cfg | Configuration | 42 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 31 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | +4 / 331 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; enhanced validation constraints |
| 32 | [Cisco-IOS-XE-yang-interfaces-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-yang-interfaces-cfg.yang) | Yang Interfaces Cfg | Configuration | 15 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Operational Models (126 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-aaa-oper.yang) | Aaa Oper | Operational | 77 | All Platforms | [Auto-generated summary] | new enum values added |
| 2 | [Cisco-IOS-XE-acl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-acl-oper.yang) | Acl Oper | Operational | 207 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [Cisco-IOS-XE-app-hosting-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-app-hosting-oper.yang) | App Hosting Oper | Operational | +2 / 132 | All Platforms | [Auto-generated summary] | Added iox-enabled, app-globals; new enum values added |
| 4 | [Cisco-IOS-XE-appqoe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-appqoe-oper.yang) | Appqoe Oper | Operational | 6 | All Platforms | [Auto-generated summary] | Minor refinements |
| 5 | [Cisco-IOS-XE-arp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-arp-oper.yang) | Arp Oper | Operational | 12 | All Platforms | [Auto-generated summary] | new enum values added |
| 6 | [Cisco-IOS-XE-bfd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-bfd-oper.yang) | Bfd Oper | Operational | +63 / 108 | All Platforms | [Auto-generated summary] | Added 19 new data nodes; new enum values added |
| 7 | [Cisco-IOS-XE-bgp-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-bgp-common-oper.yang) | Bgp Common Oper | Operational | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 8 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-bgp-oper.yang) | Bgp Oper | Operational | 486 | All Platforms | [Auto-generated summary] | new enum values added |
| 9 | [Cisco-IOS-XE-bgp-route-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-bgp-route-oper.yang) | Bgp Route Oper | Operational | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 10 | [Cisco-IOS-XE-boot-integrity-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-boot-integrity-oper.yang) | Boot Integrity Oper | Operational | -3 / 20 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; deprecated 11 nodes |
| 11 | [Cisco-IOS-XE-breakout-port-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-breakout-port-oper.yang) | Breakout Port Oper | Operational | 5 | All Platforms | [Auto-generated summary] | new enum values added |
| 12 | [Cisco-IOS-XE-bridge-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-bridge-oper.yang) | Bridge Oper | Operational | 36 | All Platforms | [Auto-generated summary] | new enum values added |
| 13 | [Cisco-IOS-XE-cable-diag-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cable-diag-oper.yang) | Cable Diag Oper | Operational | 12 | All Platforms | [Auto-generated summary] | new enum values added |
| 14 | [Cisco-IOS-XE-cdp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cdp-oper.yang) | Cdp Oper | Operational | 45 | All Platforms | [Auto-generated summary] | new enum values added |
| 15 | [Cisco-IOS-XE-cellwan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cellwan-oper.yang) | Cellwan Oper | Operational | 101 | IR1101, C1100 | [Auto-generated summary] | new enum values added |
| 16 | [Cisco-IOS-XE-cfm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cfm-oper.yang) | Cfm Oper | Operational | +63 / 82 | All Platforms | [Auto-generated summary] | Added 55 new data nodes; imported ietf-inet-types; new enum values added |
| 17 | [Cisco-IOS-XE-checkpoint-archive-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-checkpoint-archive-oper.yang) | Checkpoint Archive Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Minor refinements |
| 18 | [Cisco-IOS-XE-controller-shdsl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-controller-shdsl-oper.yang) | Controller Shdsl Oper | Operational | 97 | All Platforms | [Auto-generated summary] | Minor refinements |
| 19 | [Cisco-IOS-XE-controller-t1e1-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-controller-t1e1-oper.yang) | Controller T1E1 Oper | Operational | 35 | All Platforms | [Auto-generated summary] | new enum values added |
| 20 | [Cisco-IOS-XE-controller-vdsl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-controller-vdsl-oper.yang) | Controller Vdsl Oper | Operational | +11 / 160 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; new enum values added |
| 21 | [Cisco-IOS-XE-crypto-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-crypto-oper.yang) | Crypto Oper | Operational | +291 / 427 | All Platforms | [Auto-generated summary] | Added 345 new data nodes; imported ietf-yang-types, cisco-semver; new enum values added |
| 22 | [Cisco-IOS-XE-crypto-pki-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-crypto-pki-oper.yang) | Crypto Pki Oper | Operational | +27 / 35 | All Platforms | [Auto-generated summary] | Added 27 new data nodes; imported ietf-yang-types; new enum values added |
| 23 | [Cisco-IOS-XE-device-hardware-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-device-hardware-oper.yang) | Device Hardware Oper | Operational | +3 / 41 | All Platforms | [Auto-generated summary] | Added lifetime; new enum values added |
| 24 | [Cisco-IOS-XE-dhcp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-dhcp-oper.yang) | Dhcp Oper | Operational | 103 | All Platforms | [Auto-generated summary] | new enum values added |
| 25 | [Cisco-IOS-XE-dhcp-security-track-server-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-dhcp-security-track-server-oper.yang) | Dhcp Security Track Server Oper | Operational | 15 | All Platforms | [Auto-generated summary] | Minor refinements |
| 26 | [Cisco-IOS-XE-digital-io-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-digital-io-oper.yang) | Digital Io Oper | Operational | 15 | All Platforms | [Auto-generated summary] | new enum values added |
| 27 | [Cisco-IOS-XE-efp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-efp-oper.yang) | Efp Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Minor refinements |
| 28 | [Cisco-IOS-XE-eigrp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-eigrp-oper.yang) | Eigrp Oper | Operational | 94 | All Platforms | [Auto-generated summary] | new enum values added |
| 29 | [Cisco-IOS-XE-endpoint-tracker-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-endpoint-tracker-oper.yang) | Endpoint Tracker Oper | Operational | 7 | All Platforms | [Auto-generated summary] | new enum values added |
| 30 | [Cisco-IOS-XE-environment-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-environment-oper.yang) | Environment Oper | Operational | 12 | All Platforms | [Auto-generated summary] | new enum values added |
| 31 | [Cisco-IOS-XE-eogre-tunnel-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-eogre-tunnel-oper.yang) | Eogre Tunnel Oper | Operational | 55 | All Platforms | [Auto-generated summary] | Minor refinements |
| 32 | [Cisco-IOS-XE-fib-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-fib-oper.yang) | Fib Oper | Operational | 103 | All Platforms | [Auto-generated summary] | new enum values added |
| 33 | [Cisco-IOS-XE-flow-monitor-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-flow-monitor-oper.yang) | Flow Monitor Oper | Operational | 73 | All Platforms | [Auto-generated summary] | new enum values added |
| 34 | [Cisco-IOS-XE-fw-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-fw-oper.yang) | Fw Oper | Operational | 132 | All Platforms | [Auto-generated summary] | Minor refinements |
| 35 | [Cisco-IOS-XE-gir-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-gir-oper.yang) | Gir Oper | Operational | 55 | All Platforms | [Auto-generated summary] | new enum values added |
| 36 | [Cisco-IOS-XE-gnss-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-gnss-oper.yang) | Gnss Oper | Operational | 20 | All Platforms | [Auto-generated summary] | new enum values added |
| 37 | [Cisco-IOS-XE-ha-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ha-oper.yang) | Ha Oper | Operational | 10 | All Platforms | [Auto-generated summary] | new enum values added |
| 38 | [Cisco-IOS-XE-hsrp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-hsrp-oper.yang) | Hsrp Oper | Operational | 19 | All Platforms | [Auto-generated summary] | new enum values added |
| 39 | [Cisco-IOS-XE-identity-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-identity-oper.yang) | Identity Oper | Operational | 410 | All Platforms | [Auto-generated summary] | new enum values added |
| 40 | [Cisco-IOS-XE-im-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-im-events-oper.yang) | Im Events Oper | Operational | 10 | All Platforms | [Auto-generated summary] | new enum values added |
| 41 | [Cisco-IOS-XE-install-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-install-oper.yang) | Install Oper | Operational | +33 / 537 | All Platforms | [Auto-generated summary] | Added 25 new data nodes; new enum values added |
| 42 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces Oper | Operational | +2 / 491 | All Platforms | [Auto-generated summary] | Added auto-upstream-bandwidth, auto-downstream-bandwidth; new enum values added |
| 43 | [Cisco-IOS-XE-ios-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ios-common-oper.yang) | Ios Common Oper | Operational | 0 | All Platforms | [Auto-generated summary] | Added {; new enum values added |
| 44 | [Cisco-IOS-XE-ios-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ios-events-oper.yang) | Ios Events Oper | Operational | 398 | All Platforms | [Auto-generated summary] | new enum values added |
| 45 | [Cisco-IOS-XE-ip-sla-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ip-sla-oper.yang) | Ip Sla Oper | Operational | +456 / 1422 | All Platforms | [Auto-generated summary] | Added 165 new data nodes; new enum values added; deprecated 2 nodes |
| 46 | [Cisco-IOS-XE-ipv6-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ipv6-oper.yang) | Ipv6 Oper | Operational | 9 | All Platforms | [Auto-generated summary] | new enum values added |
| 47 | [Cisco-IOS-XE-isdn-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-isdn-oper.yang) | Isdn Oper | Operational | 24 | All Platforms | [Auto-generated summary] | new enum values added |
| 48 | [Cisco-IOS-XE-isis-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-isis-oper.yang) | Isis Oper | Operational | 11 | All Platforms | [Auto-generated summary] | new enum values added |
| 49 | [Cisco-IOS-XE-l2tp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-l2tp-oper.yang) | L2Tp Oper | Operational | 69 | All Platforms | [Auto-generated summary] | new enum values added |
| 50 | [Cisco-IOS-XE-lacp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-lacp-oper.yang) | Lacp Oper | Operational | 10 | All Platforms | [Auto-generated summary] | new enum values added |
| 51 | [Cisco-IOS-XE-linecard-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-linecard-oper.yang) | Linecard Oper | Operational | 5 | All Platforms | [Auto-generated summary] | Minor refinements |
| 52 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +22 / 384 | All Platforms | [Auto-generated summary] | Added 22 new data nodes; imported site, publication";; new enum values added |
| 53 | [Cisco-IOS-XE-lldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-lldp-oper.yang) | Lldp Oper | Operational | 91 | All Platforms | [Auto-generated summary] | new enum values added |
| 54 | [Cisco-IOS-XE-macsec-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-macsec-oper.yang) | Macsec Oper | Operational | +8 / 30 | All Platforms | [Auto-generated summary] | Added 8 new data nodes |
| 55 | [Cisco-IOS-XE-matm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-matm-oper.yang) | Matm Oper | Operational | 12 | All Platforms | [Auto-generated summary] | new enum values added |
| 56 | [Cisco-IOS-XE-mdt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mdt-oper.yang) | Mdt Oper | Operational | 55 | All Platforms | [Auto-generated summary] | new enum values added |
| 57 | [Cisco-IOS-XE-memory-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-memory-oper.yang) | Memory Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Minor refinements |
| 58 | [Cisco-IOS-XE-mka-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mka-oper.yang) | Mka Oper | Operational | 26 | All Platforms | [Auto-generated summary] | Minor refinements |
| 59 | [Cisco-IOS-XE-mlppp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mlppp-oper.yang) | Mlppp Oper | Operational | 46 | All Platforms | [Auto-generated summary] | new enum values added |
| 60 | [Cisco-IOS-XE-mpls-forwarding-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mpls-forwarding-oper.yang) | Mpls Forwarding Oper | Operational | 87 | ASR, ISR, NCS | [Auto-generated summary] | new enum values added |
| 61 | [Cisco-IOS-XE-mpls-ldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mpls-ldp-oper.yang) | Mpls Ldp Oper | Operational | 175 | ASR, ISR, NCS | [Auto-generated summary] | new enum values added |
| 62 | [Cisco-IOS-XE-mroute-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mroute-oper.yang) | Mroute Oper | Operational | 159 | All Platforms | [Auto-generated summary] | new enum values added |
| 63 | [Cisco-IOS-XE-nat-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nat-oper.yang) | Nat Oper | Operational | 38 | All Platforms | [Auto-generated summary] | Minor refinements |
| 64 | [Cisco-IOS-XE-ncch-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ncch-oper.yang) | Ncch Oper | Operational | 6 | All Platforms | [Auto-generated summary] | new enum values added |
| 65 | [Cisco-IOS-XE-ntp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ntp-oper.yang) | Ntp Oper | Operational | 52 | All Platforms | [Auto-generated summary] | new enum values added |
| 66 | [Cisco-IOS-XE-nwpi-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nwpi-oper.yang) | Nwpi Oper | Operational | 146 | All Platforms | [Auto-generated summary] | new enum values added |
| 67 | [Cisco-IOS-XE-ospf-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ospf-oper.yang) | Ospf Oper | Operational | 966 | All Platforms | [Auto-generated summary] | new enum values added |
| 68 | [Cisco-IOS-XE-perf-measure-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-perf-measure-oper.yang) | Perf Measure Oper | Operational | 299 | All Platforms | [Auto-generated summary] | new enum values added |
| 69 | [Cisco-IOS-XE-pim-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-pim-oper.yang) | Pim Oper | Operational | 39 | All Platforms | [Auto-generated summary] | new enum values added |
| 70 | [Cisco-IOS-XE-platform-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-platform-common-oper.yang) | Platform Common Oper | Operational | 0 | All Platforms | [Auto-generated summary] | Added {; new enum values added |
| 71 | [Cisco-IOS-XE-platform-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-platform-events-oper.yang) | Platform Events Oper | Operational | 31 | All Platforms | [Auto-generated summary] | new enum values added |
| 72 | [Cisco-IOS-XE-platform-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-platform-oper.yang) | Platform Oper | Operational | 52 | All Platforms | [Auto-generated summary] | Added {; new enum values added |
| 73 | [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-platform-software-oper.yang) | Platform Software Oper | Operational | +5 / 87 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 74 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | +5 / 201 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 75 | [Cisco-IOS-XE-ppp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ppp-oper.yang) | Ppp Oper | Operational | 40 | All Platforms | [Auto-generated summary] | new enum values added |
| 76 | [Cisco-IOS-XE-process-cpu-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-process-cpu-oper.yang) | Process Cpu Oper | Operational | 17 | All Platforms | [Auto-generated summary] | Minor refinements |
| 77 | [Cisco-IOS-XE-process-memory-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-process-memory-oper.yang) | Process Memory Oper | Operational | 10 | All Platforms | [Auto-generated summary] | Minor refinements |
| 78 | [Cisco-IOS-XE-ptp-synce-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ptp-synce-oper.yang) | Ptp Synce Oper | Operational | 61 | All Platforms | [Auto-generated summary] | new enum values added |
| 79 | [Cisco-IOS-XE-qfp-classification-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-qfp-classification-oper.yang) | Qfp Classification Oper | Operational | 15 | All Platforms | [Auto-generated summary] | Minor refinements |
| 80 | [Cisco-IOS-XE-qfp-resource-utilization-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-qfp-resource-utilization-oper.yang) | Qfp Resource Utilization Oper | Operational | 32 | All Platforms | [Auto-generated summary] | new enum values added |
| 81 | [Cisco-IOS-XE-qfp-stats-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-qfp-stats-oper.yang) | Qfp Stats Oper | Operational | 997 | All Platforms | [Auto-generated summary] | Minor refinements |
| 82 | [Cisco-IOS-XE-rawsocket-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-rawsocket-oper.yang) | Rawsocket Oper | Operational | 63 | All Platforms | [Auto-generated summary] | new enum values added |
| 83 | [Cisco-IOS-XE-scada-gw-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-scada-gw-oper.yang) | Scada Gw Oper | Operational | 57 | All Platforms | [Auto-generated summary] | Minor refinements |
| 84 | [Cisco-IOS-XE-sd-vxlan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-sd-vxlan-oper.yang) | Sd Vxlan Oper | Operational | 95 | All Platforms | [Auto-generated summary] | new enum values added |
| 85 | [Cisco-IOS-XE-service-insertion-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-service-insertion-oper.yang) | Service Insertion Oper | Operational | 9 | All Platforms | [Auto-generated summary] | Minor refinements |
| 86 | [Cisco-IOS-XE-sm-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-sm-events-oper.yang) | Sm Events Oper | Operational | 38 | All Platforms | [Auto-generated summary] | Minor refinements |
| 87 | [Cisco-IOS-XE-spanning-tree-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-spanning-tree-oper.yang) | Spanning Tree Oper | Operational | 49 | All Platforms | [Auto-generated summary] | new enum values added |
| 88 | [Cisco-IOS-XE-stack-member-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-stack-member-oper.yang) | Stack Member Oper | Operational | +31 / 65 | All Platforms | [Auto-generated summary] | Added 25 new data nodes; new enum values added |
| 89 | [Cisco-IOS-XE-stack-mgr-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-stack-mgr-events-oper.yang) | Stack Mgr Events Oper | Operational | +86 / 94 | All Platforms | [Auto-generated summary] | Added 56 new data nodes; imported ietf-yang-types; new enum values added |
| 90 | [Cisco-IOS-XE-stack-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-stack-oper.yang) | Stack Oper | Operational | +1 / 37 | All Platforms | [Auto-generated summary] | Added stack-boottime; new enum values added |
| 91 | [Cisco-IOS-XE-stacking-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-stacking-oper.yang) | Stacking Oper | Operational | 15 | All Platforms | [Auto-generated summary] | new enum values added |
| 92 | [Cisco-IOS-XE-switch-dp-mac-learning-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-switch-dp-mac-learning-oper.yang) | Switch Dp Mac Learning Oper | Operational | 20 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |
| 93 | [Cisco-IOS-XE-switch-dp-punt-inject-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-switch-dp-punt-inject-oper.yang) | Switch Dp Punt Inject Oper | Operational | 16 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |
| 94 | [Cisco-IOS-XE-switch-dp-resources-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-switch-dp-resources-oper.yang) | Switch Dp Resources Oper | Operational | 33 | Cat9K, IE3x00 | [Auto-generated summary] | Added is; new enum values added; deprecated 1 node |
| 95 | [Cisco-IOS-XE-tcam-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-tcam-oper.yang) | Tcam Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Minor refinements |
| 96 | [Cisco-IOS-XE-transceiver-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-transceiver-oper.yang) | Transceiver Oper | Operational | 55 | All Platforms | [Auto-generated summary] | new enum values added |
| 97 | [Cisco-IOS-XE-trustsec-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-trustsec-oper.yang) | Trustsec Oper | Operational | 93 | All Platforms | [Auto-generated summary] | new enum values added |
| 98 | [Cisco-IOS-XE-tunnel-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-tunnel-oper.yang) | Tunnel Oper | Operational | 90 | All Platforms | [Auto-generated summary] | Minor refinements |
| 99 | [Cisco-IOS-XE-ucse-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ucse-oper.yang) | Ucse Oper | Operational | 18 | All Platforms | [Auto-generated summary] | Minor refinements |
| 100 | [Cisco-IOS-XE-umbrella-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-umbrella-oper.yang) | Umbrella Oper | Operational | 12 | All Platforms | [Auto-generated summary] | Minor refinements |
| 101 | [Cisco-IOS-XE-utd-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-utd-common-oper.yang) | Utd Common Oper | Operational | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 102 | [Cisco-IOS-XE-utd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-utd-oper.yang) | Utd Oper | Operational | +10 / 63 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; new enum values added |
| 103 | [Cisco-IOS-XE-vlan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-vlan-oper.yang) | Vlan Oper | Operational | 11 | Cat9K, IE3x00 | [Auto-generated summary] | new enum values added |
| 104 | [Cisco-IOS-XE-voice-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-voice-oper.yang) | Voice Oper | Operational | 160 | ISR, Voice Gateways | [Auto-generated summary] | new enum values added |
| 105 | [Cisco-IOS-XE-vrf-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-vrf-oper.yang) | Vrf Oper | Operational | 6 | All Platforms | [Auto-generated summary] | new enum values added |
| 106 | [Cisco-IOS-XE-vrrp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-vrrp-oper.yang) | Vrrp Oper | Operational | +2 / 37 | All Platforms | [Auto-generated summary] | Added bfd-enabled, bfd-state; imported Cisco-IOS-XE-vrrp-types; new enum values added |
| 107 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | +154 / 744 | Wireless Controllers | [Auto-generated summary] | Added 131 new data nodes; imported Cisco-IOS-XE-event-history-types; new enum values added |
| 108 | [Cisco-IOS-XE-wireless-awips-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-awips-oper.yang) | Wireless Awips Oper | Operational | 42 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 109 | [Cisco-IOS-XE-wireless-ble-ltx-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-ble-ltx-oper.yang) | Wireless Ble Ltx Oper | Operational | 142 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 110 | [Cisco-IOS-XE-wireless-ble-mgmt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-ble-mgmt-oper.yang) | Wireless Ble Mgmt Oper | Operational | 16 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 111 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | +2 / 264 | Wireless Controllers | [Auto-generated summary] | Added group-mgmt-cipher-suite, group-cipher-suite; new enum values added |
| 112 | [Cisco-IOS-XE-wireless-cts-sxp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-cts-sxp-oper.yang) | Wireless Cts Sxp Oper | Operational | 9 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 113 | [Cisco-IOS-XE-wireless-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-events-oper.yang) | Wireless Events Oper | Operational | 49 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 114 | [Cisco-IOS-XE-wireless-general-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-general-oper.yang) | Wireless General Oper | Operational | 22 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 115 | [Cisco-IOS-XE-wireless-hyperlocation-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-hyperlocation-oper.yang) | Wireless Hyperlocation Oper | Operational | 6 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 116 | [Cisco-IOS-XE-wireless-lisp-agent-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-lisp-agent-oper.yang) | Wireless Lisp Agent Oper | Operational | 84 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 117 | [Cisco-IOS-XE-wireless-location-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-location-oper.yang) | Wireless Location Oper | Operational | 12 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 118 | [Cisco-IOS-XE-wireless-mcast-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mcast-oper.yang) | Wireless Mcast Oper | Operational | 112 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 119 | [Cisco-IOS-XE-wireless-mdns-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mdns-oper.yang) | Wireless Mdns Oper | Operational | 124 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 120 | [Cisco-IOS-XE-wireless-mesh-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mesh-oper.yang) | Wireless Mesh Oper | Operational | 265 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 121 | [Cisco-IOS-XE-wireless-mobility-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mobility-oper.yang) | Wireless Mobility Oper | Operational | +4 / 327 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 122 | [Cisco-IOS-XE-wireless-nmsp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-nmsp-oper.yang) | Wireless Nmsp Oper | Operational | 110 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 123 | [Cisco-IOS-XE-wireless-rfid-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rfid-oper.yang) | Wireless Rfid Oper | Operational | 53 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 124 | [Cisco-IOS-XE-wireless-rogue-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rogue-oper.yang) | Wireless Rogue Oper | Operational | -5 / 308 | Wireless Controllers | [Auto-generated summary] | new enum values added; enhanced validation constraints; deprecated 3 nodes |
| 125 | [Cisco-IOS-XE-wireless-rrm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rrm-oper.yang) | Wireless Rrm Oper | Operational | 88 | Wireless Controllers | [Auto-generated summary] | Added nodes; new enum values added; deprecated 1 node |
| 126 | [Cisco-IOS-XE-wireless-rule-mdns-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rule-mdns-oper.yang) | Wireless Rule Mdns Oper | Operational | 13 | Wireless Controllers | [Auto-generated summary] | Minor refinements |

---

## UPDATED RPC Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-install-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-install-rpc.yang) | Install Rpc | RPC | +5 / 67 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 2 | [Cisco-IOS-XE-nwpi-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nwpi-rpc.yang) | Nwpi Rpc | RPC | 20 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +1 / 1693 | All Platforms | [Auto-generated summary] | Added keep-licensing-info |
| 4 | [Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang) | Wireless Access Point Cfg Rpc | RPC | +12 / 190 | Wireless Controllers | [Auto-generated summary] | Added 7 new data nodes; new enum values added |
| 5 | [Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-access-point-cmd-rpc.yang) | Wireless Access Point Cmd Rpc | RPC | +7 / 112 | Wireless Controllers | [Auto-generated summary] | Added ap-name, mac-addr; new enum values added |
| 6 | [Cisco-IOS-XE-wireless-ble-mgmt-cmd-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-ble-mgmt-cmd-rpc.yang) | Wireless Ble Mgmt Cmd Rpc | RPC | 81 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 7 | [Cisco-IOS-XE-wireless-mobility-express-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mobility-express-rpc.yang) | Wireless Mobility Express Rpc | RPC | 1 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 8 | [Cisco-IOS-XE-wireless-rrm-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rrm-rpc.yang) | Wireless Rrm Rpc | RPC | 11 | Wireless Controllers | [Auto-generated summary] | Minor refinements |

---

## UPDATED Events Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-appqoe-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-appqoe-events.yang) | Appqoe Events | Events | +3 / 25 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 2 | [Cisco-IOS-XE-controller-shdsl-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-controller-shdsl-events.yang) | Controller Shdsl Events | Events | 41 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [Cisco-IOS-XE-crypto-pki-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-crypto-pki-events.yang) | Crypto Pki Events | Events | 20 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [Cisco-IOS-XE-hsrp-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-hsrp-events.yang) | Hsrp Events | Events | 8 | All Platforms | [Auto-generated summary] | new enum values added |
| 5 | [Cisco-IOS-XE-install-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-install-events.yang) | Install Events | Events | 7 | All Platforms | [Auto-generated summary] | Added of; new enum values added |
| 6 | [Cisco-IOS-XE-ip-sla-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ip-sla-events.yang) | Ip Sla Events | Events | 129 | All Platforms | [Auto-generated summary] | new enum values added |
| 7 | [Cisco-IOS-XE-ospf-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ospf-events.yang) | Ospf Events | Events | 20 | All Platforms | [Auto-generated summary] | new enum values added |
| 8 | [Cisco-IOS-XE-perf-measure-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-perf-measure-events.yang) | Perf Measure Events | Events | 6 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Types Models (17 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-aaa-types.yang) | Aaa Types | Types | 0 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; new enum values added |
| 2 | [Cisco-IOS-XE-appqoe-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-appqoe-types.yang) | Appqoe Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [Cisco-IOS-XE-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-common-types.yang) | Common Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [Cisco-IOS-XE-event-history-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-event-history-types.yang) | Event History Types | Types | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 5 | [Cisco-IOS-XE-nwpi-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nwpi-types.yang) | Nwpi Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 6 | [Cisco-IOS-XE-sm-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-sm-enum-types.yang) | Sm Enum Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 7 | [Cisco-IOS-XE-tunnel-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-tunnel-types.yang) | Tunnel Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 8 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 9 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 13 new data nodes; new enum values added; enhanced validation constraints |
| 10 | [Cisco-IOS-XE-wireless-client-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-client-types.yang) | Wireless Client Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 11 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless Enum Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added {; new enum values added |
| 12 | [Cisco-IOS-XE-wireless-mobility-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-mobility-types.yang) | Wireless Mobility Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added {; new enum values added |
| 13 | [Cisco-IOS-XE-wireless-rogue-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rogue-types.yang) | Wireless Rogue Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 14 | [Cisco-IOS-XE-wireless-rrm-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-rrm-types.yang) | Wireless Rrm Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 15 | [Cisco-IOS-XE-wireless-tunnel-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-tunnel-types.yang) | Wireless Tunnel Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 16 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 5 new data nodes; new enum values added; deprecated 3 nodes |
| 17 | [Cisco-IOS-XE-wsa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-wsa-types.yang) | Wsa Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |

---

## UPDATED Deviation Models (4 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cdp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cdp-deviation.yang) | Cdp Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [Cisco-IOS-XE-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-switch-deviation.yang) | Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |
| 3 | [cisco-xe-openconfig-openflow-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-xe-openconfig-openflow-deviation.yang) | Cisco Xe Openconfig Openflow Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 4 | [cisco-xe-switching-cat9k-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-xe-switching-cat9k-openconfig-system-deviation.yang) | Cisco Xe Switching Cat9K Openconfig System Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |

---

## UPDATED Native Models (74 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +129 / 2664 | All Platforms | [Auto-generated summary] | Added 74 new data nodes; new enum values added; enhanced validation constraints |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-acl.yang) | Acl | Native | 0 | All Platforms | [Auto-generated summary] | Added 80 new data nodes; imported Cisco-IOS-XE-features; new enum values added |
| 3 | [Cisco-IOS-XE-app-hosting.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-app-hosting.yang) | App Hosting | Native | 31 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +153 / 18383 | All Platforms | [Auto-generated summary] | Added 16 new data nodes; enhanced validation constraints; deprecated 4 nodes |
| 5 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cdp.yang) | Cdp | Native | +30 / 165 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-controller-shdsl-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-controller-shdsl-common.yang) | Controller Shdsl Common | Native | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 7 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-controller.yang) | Controller | Native | +13 / 592 | All Platforms | [Auto-generated summary] | Added 14 new data nodes |
| 8 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-crypto.yang) | Crypto | Native | 4939 | All Platforms | [Auto-generated summary] | Added and, to; enhanced validation constraints; deprecated 2 nodes |
| 9 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-cts.yang) | Cts | Native | +25 / 584 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; imported Cisco-IOS-XE-crypto; enhanced validation constraints |
| 10 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | +152 / 202 | All Platforms | [Auto-generated summary] | Added 108 new data nodes; new enum values added; enhanced validation constraints |
| 11 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +286 / 3807 | All Platforms | [Auto-generated summary] | Added 34 new data nodes; new enum values added; enhanced validation constraints |
| 12 | [Cisco-IOS-XE-dialer.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-dialer.yang) | Dialer | Native | 32 | All Platforms | [Auto-generated summary] | Minor refinements |
| 13 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-eem.yang) | Eem | Native | 132 | All Platforms | [Auto-generated summary] | Minor refinements |
| 14 | [Cisco-IOS-XE-eigrp-obsolete.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-eigrp-obsolete.yang) | Eigrp Obsolete | Native | 0 | All Platforms | [Auto-generated summary] | Added eigrp; deprecated 1 node |
| 15 | [Cisco-IOS-XE-eigrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-eigrp.yang) | Eigrp | Native | +36 / 4820 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 16 | [Cisco-IOS-XE-eta.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-eta.yang) | Eta | Native | 66 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 17 | [Cisco-IOS-XE-ethernet-cfm-efp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ethernet-cfm-efp.yang) | Ethernet Cfm Efp | Native | 0 | All Platforms | [Auto-generated summary] | Added 26 new data nodes; imported Cisco-IOS-XE-native; new enum values added |
| 18 | [Cisco-IOS-XE-ethernet-oam.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ethernet-oam.yang) | Ethernet Oam | Native | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 19 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | +1476 / 11132 | All Platforms | [Auto-generated summary] | Added 34 new data nodes; new enum values added; enhanced validation constraints |
| 20 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | 252 | All Platforms | [Auto-generated summary] | Added application-response-time |
| 21 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 22 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-flow.yang) | Flow | Native | +8 / 2727 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; enhanced validation constraints |
| 23 | [Cisco-IOS-XE-icmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-icmp.yang) | Icmp | Native | +2 / 107 | All Platforms | [Auto-generated summary] | Added od-length, enable |
| 24 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-igmp.yang) | Igmp | Native | 4867 | All Platforms | [Auto-generated summary] | Minor refinements |
| 25 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 26 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 9 new data nodes |
| 27 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 28 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; deprecated 2 nodes |
| 29 | [Cisco-IOS-XE-isdn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-isdn.yang) | Isdn | Native | +9 / 37 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; new enum values added |
| 30 | [Cisco-IOS-XE-isg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-isg.yang) | Isg | Native | 386 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 31 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-isis.yang) | Isis | Native | +32 / 4944 | All Platforms | [Auto-generated summary] | Added 11 new data nodes |
| 32 | [Cisco-IOS-XE-iwanfabric.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-iwanfabric.yang) | Iwanfabric | Native | 134 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 33 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +172 / 1685 | All Platforms | [Auto-generated summary] | Added 117 new data nodes; imported {; new enum values added |
| 34 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 35 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 36 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +1248 / 27253 | All Platforms | [Auto-generated summary] | Added 13 new data nodes |
| 37 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; enhanced validation constraints |
| 38 | [Cisco-IOS-XE-mdns-gateway.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mdns-gateway.yang) | Mdns Gateway | Native | 636 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 39 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mdt-common-defs.yang) | Mdt Common Defs | Native | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 40 | [Cisco-IOS-XE-mdt-oper-v2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-mdt-oper-v2.yang) | Mdt Oper V2 | Native | 88 | All Platforms | [Auto-generated summary] | new enum values added |
| 41 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +7 / 4069 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; enhanced validation constraints |
| 42 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nat.yang) | Nat | Native | +6 / 2453 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 43 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-native.yang) | Native | Native | 0 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; new enum values added |
| 44 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +2 / 581 | All Platforms | [Auto-generated summary] | Added classify-by-domain-with-default |
| 45 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nd.yang) | Nd | Native | +831 / 1726 | All Platforms | [Auto-generated summary] | Added 39 new data nodes; new enum values added; enhanced validation constraints |
| 46 | [Cisco-IOS-XE-nhrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-nhrp.yang) | Nhrp | Native | 9298 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 47 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ntp.yang) | Ntp | Native | 641 | All Platforms | [Auto-generated summary] | Added ipaddress |
| 48 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-object-group.yang) | Object Group | Native | +142 / 360 | All Platforms | [Auto-generated summary] | Added 144 new data nodes |
| 49 | [Cisco-IOS-XE-ospf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ospf-common.yang) | Ospf Common | Native | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 50 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +73 / 6132 | All Platforms | [Auto-generated summary] | Added 19 new data nodes; new enum values added |
| 51 | [Cisco-IOS-XE-perf-measure.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-perf-measure.yang) | Perf Measure | Native | +76 / 157 | All Platforms | [Auto-generated summary] | Added 11 new data nodes |
| 52 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-platform.yang) | Platform | Native | +5 / 138 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; enhanced validation constraints |
| 53 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-policy.yang) | Policy | Native | +197 / 4561 | All Platforms | [Auto-generated summary] | Added 52 new data nodes; new enum values added; enhanced validation constraints |
| 54 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ppp.yang) | Ppp | Native | +10 / 441 | All Platforms | [Auto-generated summary] | Added mask, request |
| 55 | [Cisco-IOS-XE-ptp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-ptp.yang) | Ptp | Native | 99 | All Platforms | [Auto-generated summary] | Minor refinements |
| 56 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-rip.yang) | Rip | Native | +4 / 1315 | All Platforms | [Auto-generated summary] | Added bfd |
| 57 | [Cisco-IOS-XE-rmi-dad.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-rmi-dad.yang) | Rmi Dad | Native | 13 | All Platforms | [Auto-generated summary] | Minor refinements |
| 58 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-route-map.yang) | Route Map | Native | 1075 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 59 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-sanet.yang) | Sanet | Native | 1364 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 60 | [Cisco-IOS-XE-scada-gw.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-scada-gw.yang) | Scada Gw | Native | +4 / 174 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 61 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | +31 / 320 | All Platforms | [Auto-generated summary] | Added 67 new data nodes; new enum values added; enhanced validation constraints |
| 62 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-sla.yang) | Sla | Native | +24 / 2645 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; new enum values added; enhanced validation constraints |
| 63 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +16 / 1605 | All Platforms | [Auto-generated summary] | Added snmp, trap, link-status |
| 64 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-switch.yang) | Switch | Native | +160 / 6371 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 65 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-template.yang) | Template | Native | +349 / 2326 | All Platforms | [Auto-generated summary] | Added 55 new data nodes; imported Cisco-IOS-XE-l2vpn; new enum values added |
| 66 | [Cisco-IOS-XE-track.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-track.yang) | Track | Native | 141 | All Platforms | [Auto-generated summary] | Added interface"; |
| 67 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | +2 / 1570 | All Platforms | [Auto-generated summary] | Added mpls-ip-only; enhanced validation constraints |
| 68 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-utd.yang) | Utd | Native | 379 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 69 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-vlan.yang) | Vlan | Native | +3 / 112 | Cat9K, IE3x00 | [Auto-generated summary] | Added destination-guard, attach-policy, shutdown |
| 70 | [Cisco-IOS-XE-voice-class.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-voice-class.yang) | Voice Class | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 31 new data nodes; imported ietf-inet-types; enhanced validation constraints |
| 71 | [Cisco-IOS-XE-voice-dspfarm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-voice-dspfarm.yang) | Voice Dspfarm | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 7 new data nodes; imported Cisco-IOS-XE-interface-common |
| 72 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-voice.yang) | Voice | Native | +213 / 1463 | ISR, Voice Gateways | [Auto-generated summary] | Added 11 new data nodes; new enum values added; enhanced validation constraints |
| 73 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-vrrp.yang) | Vrrp | Native | +100 / 1060 | All Platforms | [Auto-generated summary] | Added 8 new data nodes |
| 74 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/Cisco-IOS-XE-zone.yang) | Zone | Native | 58 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED OpenConfig Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [openconfig-wifi-phy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/openconfig-wifi-phy.yang) | Openconfig Wifi Phy | OpenConfig | 59 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED IETF Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [ietf-yang-push.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/ietf-yang-push.yang) | Ietf Yang Push | IETF | 149 | All Platforms | [Auto-generated summary] | deprecated 2 nodes |

---

## UPDATED Vendor Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | +1 / 637 | All Platforms | [Auto-generated summary] | Added keepalive |

---

## UPDATED Other Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-smart-license-errors.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-smart-license-errors.yang) | Cisco Smart License Errors | Other | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 2 | [cisco-smart-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1751/cisco-smart-license.yang) | Cisco Smart License | Other | +92 / 358 | All Platforms | [Auto-generated summary] | Added 60 new data nodes; imported overwrote; new enum values added |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
