# All YANG Model Changes: v16.9.3 → v16.10.1
**Summary: 59 New Models & 92 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (59 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Configuration Models](#new-configuration-models)** | 20 | 1,508 XPaths |
| **[NEW Operational Models](#new-operational-models)** | 24 | 4,045 XPaths |
| **[NEW Types Models](#new-types-models)** | 9 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 1 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 3 | 81 XPaths |
| **[NEW OpenConfig Models](#new-openconfig-models)** | 2 | 122 XPaths |
| **TOTAL NEW MODELS** | **59** | **5,756 total XPaths** |

---

## UPDATED Models Summary (92 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 1 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 15 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 1 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 2 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 5 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 66 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 1 | XPath changes vary |
| **[UPDATED IETF Models](#updated-ietf-models)** | 1 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **92** | **See individual models** |

---

## Key Highlights - NEW Models


**59 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-wireless-access-point-oper.yang`: 969 XPaths (Operational)

  - `Cisco-IOS-XE-wireless-client-oper.yang`: 789 XPaths (Operational)

  - `Cisco-IOS-XE-wireless-rrm-oper.yang`: 345 XPaths (Operational)


- **Breakdown by category:**

  - Operational: 24 models

  - Configuration: 20 models

  - Types: 9 models

  - Native: 3 models

  - OpenConfig: 2 models

  - Deviation: 1 model


---


## Key Highlights - UPDATED Models


**92 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-lisp.yang`: +1,336 XPaths (now 18,859 total)

  - `Cisco-IOS-XE-native.yang`: +1,179 XPaths (now 23,295 total)

  - `Cisco-IOS-XE-ip-sla-oper.yang`: +763 XPaths (now 864 total)


- **Significant removals:**

  - `Cisco-IOS-XE-vlan.yang`: -536 XPaths (now 98 total)

  - `Cisco-IOS-XE-bgp.yang`: -132 XPaths (now 12,671 total)

  - `Cisco-IOS-XE-crypto.yang`: -130 XPaths (now 2,531 total)


- **Updates by category:**

  - Native: 66 models

  - Operational: 15 models

  - Deviation: 5 models

  - Types: 2 models

  - Configuration: 1 model

  - RPC: 1 model

  - IETF: 1 model

  - OpenConfig: 1 model


---


## Summary Statistics

### Release v16.10.1 Totals:
- **Total YANG Files:** ~551 files
- **New Files:** 59 models
- **Modified Files:** 92 models
- **Deleted Files:** 2 models
- **New Model XPaths:** 5,756 XPaths across 59 new models

---

# NEW YANG Models in v16.10.1

**59 Brand New Models**

---

## NEW Configuration Models (20 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-app-hosting-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-app-hosting-cfg.yang) | App Hosting Cfg | Configuration | 53 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-wireless-ap-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-ap-cfg.yang) | Wireless Ap Cfg | Configuration | 35 | Wireless Controllers | New model introduced in this release |
| 3 | [Cisco-IOS-XE-wireless-apf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-apf-cfg.yang) | Wireless Apf Cfg | Configuration | 75 | Wireless Controllers | New model introduced in this release |
| 4 | [Cisco-IOS-XE-wireless-cts-sxp-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-cts-sxp-cfg.yang) | Wireless Cts Sxp Cfg | Configuration | 16 | Wireless Controllers | New model introduced in this release |
| 5 | [Cisco-IOS-XE-wireless-dot11-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-dot11-cfg.yang) | Wireless Dot11 Cfg | Configuration | 152 | Wireless Controllers | New model introduced in this release |
| 6 | [Cisco-IOS-XE-wireless-fabric-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-fabric-cfg.yang) | Wireless Fabric Cfg | Configuration | 27 | Wireless Controllers | New model introduced in this release |
| 7 | [Cisco-IOS-XE-wireless-flex-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-flex-cfg.yang) | Wireless Flex Cfg | Configuration | 112 | Wireless Controllers | New model introduced in this release |
| 8 | [Cisco-IOS-XE-wireless-fqdn-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-fqdn-cfg.yang) | Wireless Fqdn Cfg | Configuration | 11 | Wireless Controllers | New model introduced in this release |
| 9 | [Cisco-IOS-XE-wireless-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-general-cfg.yang) | Wireless General Cfg | Configuration | 58 | Wireless Controllers | New model introduced in this release |
| 10 | [Cisco-IOS-XE-wireless-location-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-location-cfg.yang) | Wireless Location Cfg | Configuration | 23 | Wireless Controllers | New model introduced in this release |
| 11 | [Cisco-IOS-XE-wireless-mesh-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-mesh-cfg.yang) | Wireless Mesh Cfg | Configuration | 58 | Wireless Controllers | New model introduced in this release |
| 12 | [Cisco-IOS-XE-wireless-mobility-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-mobility-cfg.yang) | Wireless Mobility Cfg | Configuration | 22 | Wireless Controllers | New model introduced in this release |
| 13 | [Cisco-IOS-XE-wireless-mstream-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-mstream-cfg.yang) | Wireless Mstream Cfg | Configuration | 21 | Wireless Controllers | New model introduced in this release |
| 14 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless Rf Cfg | Configuration | 154 | Wireless Controllers | New model introduced in this release |
| 15 | [Cisco-IOS-XE-wireless-rfid-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rfid-cfg.yang) | Wireless Rfid Cfg | Configuration | 8 | Wireless Controllers | New model introduced in this release |
| 16 | [Cisco-IOS-XE-wireless-rogue-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rogue-cfg.yang) | Wireless Rogue Cfg | Configuration | 72 | Wireless Controllers | New model introduced in this release |
| 17 | [Cisco-IOS-XE-wireless-rrm-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rrm-cfg.yang) | Wireless Rrm Cfg | Configuration | 73 | Wireless Controllers | New model introduced in this release |
| 18 | [Cisco-IOS-XE-wireless-security-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-security-cfg.yang) | Wireless Security Cfg | Configuration | 16 | Wireless Controllers | New model introduced in this release |
| 19 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless Site Cfg | Configuration | 260 | Wireless Controllers | New model introduced in this release |
| 20 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | 262 | Wireless Controllers | New model introduced in this release |

---

## NEW Operational Models (24 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-app-hosting-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-app-hosting-oper.yang) | App Hosting Oper | Operational | 91 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-gir-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-gir-oper.yang) | Gir Oper | Operational | 55 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-ha-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ha-oper.yang) | Ha Oper | Operational | 10 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-im-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-im-events-oper.yang) | Im Events Oper | Operational | 11 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-ios-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ios-events-oper.yang) | Ios Events Oper | Operational | 314 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-mlppp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-mlppp-oper.yang) | Mlppp Oper | Operational | 46 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-stack-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-stack-oper.yang) | Stack Oper | Operational | 12 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-voice-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-voice-oper.yang) | Voice Oper | Operational | 29 | ISR, Voice Gateways | New model introduced in this release |
| 9 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | 969 | Wireless Controllers | New model introduced in this release |
| 10 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | 789 | Wireless Controllers | New model introduced in this release |
| 11 | [Cisco-IOS-XE-wireless-cts-sxp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-cts-sxp-oper.yang) | Wireless Cts Sxp Oper | Operational | 9 | Wireless Controllers | New model introduced in this release |
| 12 | [Cisco-IOS-XE-wireless-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-events-oper.yang) | Wireless Events Oper | Operational | 24 | Wireless Controllers | New model introduced in this release |
| 13 | [Cisco-IOS-XE-wireless-fqdn-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-fqdn-oper.yang) | Wireless Fqdn Oper | Operational | 22 | Wireless Controllers | New model introduced in this release |
| 14 | [Cisco-IOS-XE-wireless-hyperlocation-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-hyperlocation-oper.yang) | Wireless Hyperlocation Oper | Operational | 6 | Wireless Controllers | New model introduced in this release |
| 15 | [Cisco-IOS-XE-wireless-lisp-agent-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-lisp-agent-oper.yang) | Wireless Lisp Agent Oper | Operational | 84 | Wireless Controllers | New model introduced in this release |
| 16 | [Cisco-IOS-XE-wireless-location-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-location-oper.yang) | Wireless Location Oper | Operational | 12 | Wireless Controllers | New model introduced in this release |
| 17 | [Cisco-IOS-XE-wireless-mcast-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-mcast-oper.yang) | Wireless Mcast Oper | Operational | 157 | Wireless Controllers | New model introduced in this release |
| 18 | [Cisco-IOS-XE-wireless-mesh-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-mesh-oper.yang) | Wireless Mesh Oper | Operational | 307 | Wireless Controllers | New model introduced in this release |
| 19 | [Cisco-IOS-XE-wireless-mobility-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-mobility-oper.yang) | Wireless Mobility Oper | Operational | 266 | Wireless Controllers | New model introduced in this release |
| 20 | [Cisco-IOS-XE-wireless-nmsp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-nmsp-oper.yang) | Wireless Nmsp Oper | Operational | 108 | Wireless Controllers | New model introduced in this release |
| 21 | [Cisco-IOS-XE-wireless-rf-profile-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rf-profile-oper.yang) | Wireless Rf Profile Oper | Operational | 10 | Wireless Controllers | New model introduced in this release |
| 22 | [Cisco-IOS-XE-wireless-rfid-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rfid-oper.yang) | Wireless Rfid Oper | Operational | 75 | Wireless Controllers | New model introduced in this release |
| 23 | [Cisco-IOS-XE-wireless-rogue-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rogue-oper.yang) | Wireless Rogue Oper | Operational | 294 | Wireless Controllers | New model introduced in this release |
| 24 | [Cisco-IOS-XE-wireless-rrm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rrm-oper.yang) | Wireless Rrm Oper | Operational | 345 | Wireless Controllers | New model introduced in this release |

---

## NEW Types Models (9 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | New model introduced in this release |
| 2 | [Cisco-IOS-XE-wireless-client-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-client-types.yang) | Wireless Client Types | Types | 0 | Wireless Controllers | New model introduced in this release |
| 3 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless Enum Types | Types | 0 | Wireless Controllers | New model introduced in this release |
| 4 | [Cisco-IOS-XE-wireless-mobility-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-mobility-types.yang) | Wireless Mobility Types | Types | 0 | Wireless Controllers | New model introduced in this release |
| 5 | [Cisco-IOS-XE-wireless-rogue-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rogue-types.yang) | Wireless Rogue Types | Types | 0 | Wireless Controllers | New model introduced in this release |
| 6 | [Cisco-IOS-XE-wireless-rrm-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-rrm-types.yang) | Wireless Rrm Types | Types | 0 | Wireless Controllers | New model introduced in this release |
| 7 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | New model introduced in this release |
| 8 | [Cisco-IOS-XE-wsa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-wsa-types.yang) | Wsa Types | Types | 0 | All Platforms | New model introduced in this release |
| 9 | [openconfig-lldp-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/openconfig-lldp-types.yang) | Openconfig Lldp Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Deviation Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-openconfig-lldp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/cisco-xe-openconfig-lldp-deviation.yang) | Cisco Xe Openconfig Lldp Deviation | Deviation | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-dialer.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-dialer.yang) | Dialer | Native | 30 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-pppoe.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-pppoe.yang) | Pppoe | Native | 13 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-serial.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-serial.yang) | Serial | Native | 38 | All Platforms | New model introduced in this release |

---

## NEW OpenConfig Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [openconfig-lacp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/openconfig-lacp.yang) | Openconfig Lacp | OpenConfig | 42 | All Platforms | New model introduced in this release |
| 2 | [openconfig-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/openconfig-lldp.yang) | Openconfig Lldp | OpenConfig | 80 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.9.3 → v16.10.1

**92 Models Modified**

---

## UPDATED Configuration Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-mdt-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-mdt-cfg.yang) | Mdt Cfg | Configuration | +2 / 58 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Operational Models (15 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-aaa-oper.yang) | Aaa Oper | Operational | 61 | All Platforms | [Auto-generated summary] | Minor refinements |
| 2 | [Cisco-IOS-XE-arp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-arp-oper.yang) | Arp Oper | Operational | 12 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [Cisco-IOS-XE-bgp-route-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-bgp-route-oper.yang) | Bgp Route Oper | Operational | 0 | All Platforms | [Auto-generated summary] | Added path-origin; new enum values added |
| 4 | [Cisco-IOS-XE-controller-vdsl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-controller-vdsl-oper.yang) | Controller Vdsl Oper | Operational | +2 / 26 | All Platforms | [Auto-generated summary] | Added modem-serial |
| 5 | [Cisco-IOS-XE-device-hardware-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-device-hardware-oper.yang) | Device Hardware Oper | Operational | +9 / 31 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; new enum values added |
| 6 | [Cisco-IOS-XE-dhcp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-dhcp-oper.yang) | Dhcp Oper | Operational | 34 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-fw-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-fw-oper.yang) | Fw Oper | Operational | +19 / 127 | All Platforms | [Auto-generated summary] | Added 22 new data nodes |
| 8 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces Oper | Operational | +23 / 397 | All Platforms | [Auto-generated summary] | Added 22 new data nodes; new enum values added |
| 9 | [Cisco-IOS-XE-ip-sla-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ip-sla-oper.yang) | Ip Sla Oper | Operational | +763 / 864 | All Platforms | [Auto-generated summary] | Added 168 new data nodes; imported ietf-inet-types; new enum values added |
| 10 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +32 / 256 | All Platforms | [Auto-generated summary] | Added 31 new data nodes; new enum values added; deprecated 1 node |
| 11 | [Cisco-IOS-XE-lldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-lldp-oper.yang) | Lldp Oper | Operational | +50 / 65 | All Platforms | [Auto-generated summary] | Added 36 new data nodes; new enum values added |
| 12 | [Cisco-IOS-XE-mdt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-mdt-oper.yang) | Mdt Oper | Operational | +2 / 54 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 13 | [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-platform-software-oper.yang) | Platform Software Oper | Operational | 69 | All Platforms | [Auto-generated summary] | imported Cisco-IOS-XE-common-types; deprecated 4 nodes |
| 14 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | 6 | All Platforms | [Auto-generated summary] | Minor refinements |
| 15 | [Cisco-IOS-XE-utd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-utd-oper.yang) | Utd Oper | Operational | +5 / 32 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |

---

## UPDATED RPC Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +178 / 474 | All Platforms | [Auto-generated summary] | Added 84 new data nodes; deprecated 10 nodes |

---

## UPDATED Types Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-common-types.yang) | Common Types | Types | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 2 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |

---

## UPDATED Deviation Models (5 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-switch-deviation.yang) | Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | deprecated 1 node |
| 2 | [cisco-xe-openconfig-bgp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/cisco-xe-openconfig-bgp-deviation.yang) | Cisco Xe Openconfig Bgp Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Added under |
| 3 | [cisco-xe-openconfig-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/cisco-xe-openconfig-interfaces-deviation.yang) | Cisco Xe Openconfig Interfaces Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [cisco-xe-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/cisco-xe-openconfig-platform-deviation.yang) | Cisco Xe Openconfig Platform Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 5 | [cisco-xe-openconfig-routing-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/cisco-xe-openconfig-routing-policy-deviation.yang) | Cisco Xe Openconfig Routing Policy Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Native Models (66 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +20 / 1798 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; deprecated 10 nodes |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-acl.yang) | Acl | Native | 0 | All Platforms | [Auto-generated summary] | Added 37 new data nodes |
| 3 | [Cisco-IOS-XE-arp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-arp.yang) | Arp | Native | 13 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-atm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-atm.yang) | Atm | Native | +186 / 972 | All Platforms | [Auto-generated summary] | Added 25 new data nodes; imported Cisco-IOS-XE-pppoe; deprecated 7 nodes |
| 5 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-bfd.yang) | Bfd | Native | 127 | All Platforms | [Auto-generated summary] | Minor refinements |
| 6 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-bgp.yang) | Bgp | Native | -132 / 12671 | All Platforms | [Auto-generated summary] | Added 14 new data nodes; deprecated 6 nodes |
| 7 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-bridge-domain.yang) | Bridge Domain | Native | +14 / 165 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; imported Cisco-IOS-XE-l2vpn |
| 8 | [Cisco-IOS-XE-call-home.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-call-home.yang) | Call Home | Native | -2 / 132 | All Platforms | [Auto-generated summary] | deprecated 4 nodes |
| 9 | [Cisco-IOS-XE-card.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-card.yang) | Card | Native | +1 / 4 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added; deprecated 3 nodes |
| 10 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-cef.yang) | Cef | Native | 167 | All Platforms | [Auto-generated summary] | Minor refinements |
| 11 | [Cisco-IOS-XE-cellular.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-cellular.yang) | Cellular | Native | -22 / 3 | IR1101, C1100 | [Auto-generated summary] | deprecated 23 nodes |
| 12 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-controller.yang) | Controller | Native | +18 / 358 | All Platforms | [Auto-generated summary] | Added 20 new data nodes; new enum values added; deprecated 2 nodes |
| 13 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-crypto.yang) | Crypto | Native | -130 / 2531 | All Platforms | [Auto-generated summary] | Added 16 new data nodes; new enum values added; deprecated 123 nodes |
| 14 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-cts.yang) | Cts | Native | 447 | All Platforms | [Auto-generated summary] | Minor refinements |
| 15 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | 49 | All Platforms | [Auto-generated summary] | Minor refinements |
| 16 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +251 / 1162 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; imported Cisco-IOS-XE-atm; deprecated 9 nodes |
| 17 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | 216 | All Platforms | [Auto-generated summary] | Minor refinements |
| 18 | [Cisco-IOS-XE-eta.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-eta.yang) | Eta | Native | 46 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 19 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | +112 / 4306 | All Platforms | [Auto-generated summary] | Added cos; imported Cisco-IOS-XE-pppoe; enhanced validation constraints |
| 20 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | +5 / 156 | All Platforms | [Auto-generated summary] | Added assurance-monitor, cache-size, interval-timeout; new enum values added |
| 21 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-flow.yang) | Flow | Native | +70 / 2094 | All Platforms | [Auto-generated summary] | Added 35 new data nodes; deprecated 1 node |
| 22 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-igmp.yang) | Igmp | Native | +11 / 210 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 23 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | Added interface'";, Dialer, interface; deprecated 1 node |
| 24 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; new enum values added; enhanced validation constraints |
| 25 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; enhanced validation constraints; deprecated 35 nodes |
| 26 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 27 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-isis.yang) | Isis | Native | +8 / 4308 | All Platforms | [Auto-generated summary] | Minor refinements |
| 28 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +82 / 1211 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; imported Cisco-IOS-XE-types |
| 29 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 30 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; new enum values added; deprecated 3 nodes |
| 31 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +1336 / 18859 | All Platforms | [Auto-generated summary] | Added 40 new data nodes; imported of; enhanced validation constraints |
| 32 | [Cisco-IOS-XE-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-lldp.yang) | Lldp | Native | +37 / 63 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; new enum values added |
| 33 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | Added size, size-value, severity; deprecated 3 nodes |
| 34 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-mdt-common-defs.yang) | Mdt Common Defs | Native | 0 | All Platforms | [Auto-generated summary] | Added nested-uri; new enum values added |
| 35 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-mpls.yang) | Mpls | Native | 0 | ASR, ISR, NCS | [Auto-generated summary] | Added Tunnel, name; deprecated 1 node |
| 36 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +379 / 890 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; imported Cisco-IOS-XE-interface-common; deprecated 2 nodes |
| 37 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-nat.yang) | Nat | Native | +41 / 561 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; imported Cisco-IOS-XE-atm; deprecated 8 nodes |
| 38 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-native.yang) | Native | Native | +1179 / 23295 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; deprecated 9 nodes |
| 39 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +11 / 519 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 40 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-nd.yang) | Nd | Native | +78 / 245 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; imported Cisco-IOS-XE-types; new enum values added |
| 41 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ntp.yang) | Ntp | Native | +2 / 333 | All Platforms | [Auto-generated summary] | Minor refinements |
| 42 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-object-group.yang) | Object Group | Native | +108 / 183 | All Platforms | [Auto-generated summary] | Added 113 new data nodes; new enum values added; deprecated 5 nodes |
| 43 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +348 / 2976 | All Platforms | [Auto-generated summary] | Added auth-key";; enhanced validation constraints |
| 44 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | +310 / 7027 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 45 | [Cisco-IOS-XE-otv.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-otv.yang) | Otv | Native | +15 / 1141 | All Platforms | [Auto-generated summary] | Minor refinements |
| 46 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-platform.yang) | Platform | Native | 105 | All Platforms | [Auto-generated summary] | Minor refinements |
| 47 | [Cisco-IOS-XE-pnp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-pnp.yang) | Pnp | Native | +7 / 9 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; imported ietf-inet-types |
| 48 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-policy.yang) | Policy | Native | +267 / 2682 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; imported Cisco-IOS-XE-atm |
| 49 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-ppp.yang) | Ppp | Native | +172 / 286 | All Platforms | [Auto-generated summary] | Added 36 new data nodes; new enum values added; deprecated 2 nodes |
| 50 | [Cisco-IOS-XE-qos.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-qos.yang) | Qos | Native | 36 | All Platforms | [Auto-generated summary] | Minor refinements |
| 51 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-rip.yang) | Rip | Native | 1305 | All Platforms | [Auto-generated summary] | Minor refinements |
| 52 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +16 / 979 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; deprecated 22 nodes |
| 53 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | 63 | All Platforms | [Auto-generated summary] | Minor refinements |
| 54 | [Cisco-IOS-XE-service-insertion.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-service-insertion.yang) | Service Insertion | Native | 28 | All Platforms | [Auto-generated summary] | Minor refinements |
| 55 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-sla.yang) | Sla | Native | +217 / 426 | All Platforms | [Auto-generated summary] | Added 125 new data nodes; new enum values added; deprecated 36 nodes |
| 56 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +15 / 970 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; deprecated 9 nodes |
| 57 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | 341 | All Platforms | [Auto-generated summary] | Minor refinements |
| 58 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-switch.yang) | Switch | Native | -60 / 2817 | Cat9K, IE3x00 | [Auto-generated summary] | deprecated 3 nodes |
| 59 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | 694 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 60 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-umbrella.yang) | Umbrella | Native | 60 | All Platforms | [Auto-generated summary] | Minor refinements |
| 61 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-utd.yang) | Utd | Native | +2 / 295 | All Platforms | [Auto-generated summary] | Added cloud-lookup; enhanced validation constraints |
| 62 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-vlan.yang) | Vlan | Native | -536 / 98 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 63 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-voice.yang) | Voice | Native | +8 / 20 | ISR, Voice Gateways | [Auto-generated summary] | Added 8 new data nodes; new enum values added |
| 64 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-vrrp.yang) | Vrrp | Native | 672 | All Platforms | [Auto-generated summary] | new enum values added |
| 65 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-vservice.yang) | Vservice | Native | 35 | All Platforms | [Auto-generated summary] | Minor refinements |
| 66 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/Cisco-IOS-XE-zone.yang) | Zone | Native | +2 / 46 | All Platforms | [Auto-generated summary] | Added vpn, id |

---

## UPDATED OpenConfig Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-openconfig-interfaces-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/cisco-xe-openconfig-interfaces-ext.yang) | Cisco Xe Openconfig Interfaces Ext | OpenConfig | -4 / 2 | All Platforms | [Auto-generated summary] | deprecated 4 nodes |

---

## UPDATED IETF Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-ietf-yang-push-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16101/cisco-xe-ietf-yang-push-ext.yang) | Cisco Xe Ietf Yang Push Ext | IETF | 18 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
