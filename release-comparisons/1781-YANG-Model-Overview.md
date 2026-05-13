# All YANG Model Changes: v17.7.1 → v17.8.1
**Summary: 45 New Models & 120 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (45 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Configuration Models](#new-configuration-models)** | 8 | 172 XPaths |
| **[NEW Operational Models](#new-operational-models)** | 5 | 297 XPaths |
| **[NEW RPC Models](#new-rpc-models)** | 2 | 45 XPaths |
| **[NEW Events Models](#new-events-models)** | 2 | 22 XPaths |
| **[NEW Types Models](#new-types-models)** | 9 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 1 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 1 | 0 XPaths |
| **[NEW OpenConfig Models](#new-openconfig-models)** | 17 | 87 XPaths |
| **TOTAL NEW MODELS** | **45** | **623 total XPaths** |

---

## UPDATED Models Summary (120 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 9 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 19 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 5 | XPath changes vary |
| **[UPDATED Events Models](#updated-events-models)** | 1 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 8 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 15 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 54 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 8 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 1 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **120** | **See individual models** |

---

## Key Highlights - NEW Models


**45 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-wpan-oper.yang`: 155 XPaths (Operational)

  - `Cisco-IOS-XE-packet-core-5gc-cfg.yang`: 77 XPaths (Configuration)

  - `Cisco-IOS-XE-bbu-oper.yang`: 55 XPaths (Operational)


- **Breakdown by category:**

  - OpenConfig: 17 models

  - Types: 9 models

  - Configuration: 8 models

  - Operational: 5 models

  - RPC: 2 models

  - Events: 2 models

  - Deviation: 1 model

  - Native: 1 model


---


## Key Highlights - UPDATED Models


**120 models updated** in this release:


- **Significant additions:**

  - `openconfig-network-instance.yang`: +885 XPaths (now 3,884 total)

  - `Cisco-IOS-XE-bgp.yang`: +476 XPaths (now 19,588 total)

  - `Cisco-IOS-XE-wccp.yang`: +413 XPaths (now 853 total)


- **Significant removals:**

  - `Cisco-IOS-XE-aaa.yang`: -2,695 XPaths (now 0 total)

  - `cisco-evpn-service.yang`: -87 XPaths (now 152 total)

  - `openconfig-bfd.yang`: -18 XPaths (now 88 total)


- **Updates by category:**

  - Native: 54 models

  - Operational: 19 models

  - Deviation: 15 models

  - Configuration: 9 models

  - Types: 8 models

  - OpenConfig: 8 models

  - RPC: 5 models

  - Events: 1 model

  - Other: 1 model


---


## Summary Statistics

### Release v17.8.1 Totals:
- **Total YANG Files:** ~565 files
- **New Files:** 45 models
- **Modified Files:** 120 models
- **Deleted Files:** 4 models
- **New Model XPaths:** 623 XPaths across 45 new models

---

# NEW YANG Models in v17.8.1

**45 Brand New Models**

---

## NEW Configuration Models (8 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-packet-core-5gc-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-5gc-cfg.yang) | Packet Core 5Gc Cfg | Configuration | 77 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-packet-core-gtpu-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-gtpu-cfg.yang) | Packet Core Gtpu Cfg | Configuration | 10 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-packet-core-plmn-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-plmn-cfg.yang) | Packet Core Plmn Cfg | Configuration | 12 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-packet-core-policy-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-policy-cfg.yang) | Packet Core Policy Cfg | Configuration | 12 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-packet-core-sctp-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-sctp-cfg.yang) | Packet Core Sctp Cfg | Configuration | 11 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-packet-core-timer-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-timer-cfg.yang) | Packet Core Timer Cfg | Configuration | 14 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-packet-core-upf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-upf-cfg.yang) | Packet Core Upf Cfg | Configuration | 5 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-wireless-power-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-power-cfg.yang) | Wireless Power Cfg | Configuration | 31 | Wireless Controllers | New model introduced in this release |

---

## NEW Operational Models (5 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-bbu-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-bbu-oper.yang) | Bbu Oper | Operational | 55 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-mdt-stats-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-mdt-stats-oper.yang) | Mdt Stats Oper | Operational | 19 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-qfp-crypto-dp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-qfp-crypto-dp-oper.yang) | Qfp Crypto Dp Oper | Operational | 13 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-wireless-mesh-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-mesh-global-oper.yang) | Wireless Mesh Global Oper | Operational | 55 | Wireless Controllers | New model introduced in this release |
| 5 | [Cisco-IOS-XE-wpan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wpan-oper.yang) | Wpan Oper | Operational | 155 | All Platforms | New model introduced in this release |

---

## NEW RPC Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-chassis-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-chassis-rpc.yang) | Chassis Rpc | RPC | 8 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-port-security-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-port-security-rpc.yang) | Port Security Rpc | RPC | 37 | All Platforms | New model introduced in this release |

---

## NEW Events Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-fib-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-fib-events.yang) | Fib Events | Events | 12 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-nat-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-nat-events.yang) | Nat Events | Events | 10 | All Platforms | New model introduced in this release |

---

## NEW Types Models (9 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-install-event-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-install-event-types.yang) | Install Event Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-install-oper-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-install-oper-types.yang) | Install Oper Types | Types | 0 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-packet-core-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-packet-core-types.yang) | Packet Core Types | Types | 0 | All Platforms | New model introduced in this release |
| 4 | [openconfig-evpn-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-evpn-types.yang) | Openconfig Evpn Types | Types | 0 | All Platforms | New model introduced in this release |
| 5 | [openconfig-if-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-if-types.yang) | Openconfig If Types | Types | 0 | All Platforms | New model introduced in this release |
| 6 | [openconfig-igmp-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-igmp-types.yang) | Openconfig Igmp Types | Types | 0 | All Platforms | New model introduced in this release |
| 7 | [openconfig-ospf-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospf-types.yang) | Openconfig Ospf Types | Types | 0 | All Platforms | New model introduced in this release |
| 8 | [openconfig-pim-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-pim-types.yang) | Openconfig Pim Types | Types | 0 | All Platforms | New model introduced in this release |
| 9 | [openconfig-segment-routing-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-segment-routing-types.yang) | Openconfig Segment Routing Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Deviation Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-cef-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-cef-deviation.yang) | Cef Deviation | Deviation | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-hsrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-hsrp.yang) | Hsrp | Native | 0 | All Platforms | New model introduced in this release |

---

## NEW OpenConfig Models (17 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-openconfig-network-instance-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/cisco-xe-openconfig-network-instance-ext.yang) | Cisco Xe Openconfig Network Instance Ext | OpenConfig | 30 | All Platforms | New model introduced in this release |
| 2 | [openconfig-evpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-evpn.yang) | Openconfig Evpn | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 3 | [openconfig-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-igmp.yang) | Openconfig Igmp | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 4 | [openconfig-network-instance-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-network-instance-policy.yang) | Openconfig Network Instance Policy | OpenConfig | 7 | All Platforms | New model introduced in this release |
| 5 | [openconfig-ospf-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospf-policy.yang) | Openconfig Ospf Policy | OpenConfig | 17 | All Platforms | New model introduced in this release |
| 6 | [openconfig-ospfv2-area-interface.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospfv2-area-interface.yang) | Openconfig Ospfv2 Area Interface | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 7 | [openconfig-ospfv2-area.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospfv2-area.yang) | Openconfig Ospfv2 Area | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 8 | [openconfig-ospfv2-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospfv2-common.yang) | Openconfig Ospfv2 Common | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 9 | [openconfig-ospfv2-global.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospfv2-global.yang) | Openconfig Ospfv2 Global | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 10 | [openconfig-ospfv2-lsdb.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospfv2-lsdb.yang) | Openconfig Ospfv2 Lsdb | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 11 | [openconfig-ospfv2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-ospfv2.yang) | Openconfig Ospfv2 | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 12 | [openconfig-pf-forwarding-policies.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-pf-forwarding-policies.yang) | Openconfig Pf Forwarding Policies | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 13 | [openconfig-pf-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-pf-interfaces.yang) | Openconfig Pf Interfaces | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 14 | [openconfig-pf-path-groups.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-pf-path-groups.yang) | Openconfig Pf Path Groups | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 15 | [openconfig-pf-srte.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-pf-srte.yang) | Openconfig Pf Srte | OpenConfig | 33 | All Platforms | New model introduced in this release |
| 16 | [openconfig-pim.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-pim.yang) | Openconfig Pim | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 17 | [openconfig-policy-forwarding.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-policy-forwarding.yang) | Openconfig Policy Forwarding | OpenConfig | 0 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v17.7.1 → v17.8.1

**120 Models Modified**

---

## UPDATED Configuration Models (9 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-mdt-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-mdt-cfg.yang) | Mdt Cfg | Configuration | +4 / 146 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 2 | [Cisco-IOS-XE-wireless-apf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-apf-cfg.yang) | Wireless Apf Cfg | Configuration | +3 / 70 | Wireless Controllers | [Auto-generated summary] | Added enable-https, upgrade-method-https, ble-streaming; imported Cisco-IOS-XE-wireless-general-cfg; enhanced validation constraints |
| 3 | [Cisco-IOS-XE-wireless-flex-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-flex-cfg.yang) | Wireless Flex Cfg | Configuration | +1 / 59 | Wireless Controllers | [Auto-generated summary] | Added pmk-dist-method; new enum values added |
| 4 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless Rf Cfg | Configuration | 183 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 5 | [Cisco-IOS-XE-wireless-rlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-rlan-cfg.yang) | Wireless Rlan Cfg | Configuration | +7 / 74 | Wireless Controllers | [Auto-generated summary] | Added 7 new data nodes; new enum values added; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-wireless-rogue-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-rogue-cfg.yang) | Wireless Rogue Cfg | Configuration | 76 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 7 | [Cisco-IOS-XE-wireless-rule-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-rule-cfg.yang) | Wireless Rule Cfg | Configuration | 15 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 8 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless Site Cfg | Configuration | +17 / 335 | Wireless Controllers | [Auto-generated summary] | Added 12 new data nodes; imported Cisco-IOS-XE-wireless-general-cfg, Cisco-IOS-XE-wireless-wlan-cfg; new enum values added |
| 9 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | +4 / 352 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; enhanced validation constraints |

---

## UPDATED Operational Models (19 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-appqoe-serv-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-appqoe-serv-oper.yang) | Appqoe Serv Oper | Operational | +33 / 61 | All Platforms | [Auto-generated summary] | Added 21 new data nodes |
| 2 | [Cisco-IOS-XE-cdp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-cdp-oper.yang) | Cdp Oper | Operational | +1 / 46 | All Platforms | [Auto-generated summary] | Added neighbor-port-mac; imported ietf-yang-types |
| 3 | [Cisco-IOS-XE-fib-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-fib-oper.yang) | Fib Oper | Operational | 239 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [Cisco-IOS-XE-gnss-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-gnss-oper.yang) | Gnss Oper | Operational | +7 / 27 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; imported ietf-yang-types; new enum values added |
| 5 | [Cisco-IOS-XE-install-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-install-oper.yang) | Install Oper | Operational | +175 / 734 | All Platforms | [Auto-generated summary] | Added 51 new data nodes; imported Cisco-IOS-XE-install-event-types, Cisco-IOS-XE-install-oper-types; new enum values added |
| 6 | [Cisco-IOS-XE-ios-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ios-events-oper.yang) | Ios Events Oper | Operational | -1 / 400 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +15 / 414 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 8 | [Cisco-IOS-XE-lldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-lldp-oper.yang) | Lldp Oper | Operational | +1 / 92 | All Platforms | [Auto-generated summary] | Added peer-src-mac; imported ietf-yang-types |
| 9 | [Cisco-IOS-XE-netconf-diag-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-netconf-diag-oper.yang) | Netconf Diag Oper | Operational | -1 / 12 | All Platforms | [Auto-generated summary] | Added status; new enum values added; deprecated 2 nodes |
| 10 | [Cisco-IOS-XE-nwpi-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-nwpi-oper.yang) | Nwpi Oper | Operational | 310 | All Platforms | [Auto-generated summary] | new enum values added |
| 11 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | +3 / 208 | All Platforms | [Auto-generated summary] | Added prot-pd-highest-req-pwr, prot-req-state, pwr-state; new enum values added |
| 12 | [Cisco-IOS-XE-psecure-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-psecure-oper.yang) | Psecure Oper | Operational | +3 / 11 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 13 | [Cisco-IOS-XE-stack-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-stack-oper.yang) | Stack Oper | Operational | +11 / 48 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; imported ietf-inet-types; new enum values added |
| 14 | [Cisco-IOS-XE-transceiver-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-transceiver-oper.yang) | Transceiver Oper | Operational | +6 / 61 | All Platforms | [Auto-generated summary] | Added interval |
| 15 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | +140 / 985 | Wireless Controllers | [Auto-generated summary] | Added 116 new data nodes; new enum values added |
| 16 | [Cisco-IOS-XE-wireless-ble-ltx-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-ble-ltx-oper.yang) | Wireless Ble Ltx Oper | Operational | +13 / 156 | Wireless Controllers | [Auto-generated summary] | Added 11 new data nodes; new enum values added |
| 17 | [Cisco-IOS-XE-wireless-client-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-client-global-oper.yang) | Wireless Client Global Oper | Operational | +173 / 521 | Wireless Controllers | [Auto-generated summary] | Added 147 new data nodes; imported Cisco-IOS-XE-wireless-types, ietf-yang-types |
| 18 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | +5 / 280 | Wireless Controllers | [Auto-generated summary] | Added 5 new data nodes |
| 19 | [Cisco-IOS-XE-wireless-rrm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-rrm-oper.yang) | Wireless Rrm Oper | Operational | +3 / 99 | Wireless Controllers | [Auto-generated summary] | Added rapid-update-enable, last-run, cntrlr-secondary-ip-addr |

---

## UPDATED RPC Models (5 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-install-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-install-rpc.yang) | Install Rpc | RPC | +5 / 78 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; enhanced validation constraints |
| 2 | [Cisco-IOS-XE-netconf-diag-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-netconf-diag-rpc.yang) | Netconf Diag Rpc | RPC | -3 / 3 | All Platforms | [Auto-generated summary] | deprecated 1 node |
| 3 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang) | Wireless Access Point Cfg Rpc | RPC | +22 / 223 | Wireless Controllers | [Auto-generated summary] | Added 12 new data nodes; new enum values added; enhanced validation constraints |
| 5 | [Cisco-IOS-XE-xcopy-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-xcopy-rpc.yang) | Xcopy Rpc | RPC | +1 / 12 | All Platforms | [Auto-generated summary] | Added timeout |

---

## UPDATED Events Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-install-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-install-events.yang) | Install Events | Events | 7 | All Platforms | [Auto-generated summary] | imported Cisco-IOS-XE-install-event-types; deprecated 7 nodes |

---

## UPDATED Types Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-aaa-types.yang) | Aaa Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 2 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; imported Cisco-IOS-XE-wireless-power-cfg; enhanced validation constraints |
| 3 | [Cisco-IOS-XE-wireless-client-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-client-types.yang) | Wireless Client Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 8 new data nodes |
| 4 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless Enum Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 5 | [Cisco-IOS-XE-wireless-mobility-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-mobility-types.yang) | Wireless Mobility Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 6 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 12 new data nodes; new enum values added |
| 7 | [openconfig-aaa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-aaa-types.yang) | Openconfig Aaa Types | Types | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 8 | [openconfig-network-instance-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-network-instance-types.yang) | Openconfig Network Instance Types | Types | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Deviation Models (15 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cdp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-cdp-deviation.yang) | Cdp Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 2 | [Cisco-IOS-XE-cts-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-cts-routing-deviation.yang) | Cts Routing Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 3 | [Cisco-IOS-XE-line-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-line-deviation.yang) | Line Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 4 | [Cisco-IOS-XE-lisp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-lisp-deviation.yang) | Lisp Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 5 | [Cisco-IOS-XE-nd-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-nd-deviation.yang) | Nd Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 6 | [Cisco-IOS-XE-ospf-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ospf-deviation.yang) | Ospf Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 7 | [Cisco-IOS-XE-ospfv3-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ospfv3-deviation.yang) | Ospfv3 Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 8 | [Cisco-IOS-XE-poch-lb-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-poch-lb-switch-deviation.yang) | Poch Lb Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | imported cisco-semver |
| 9 | [Cisco-IOS-XE-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-policy-deviation.yang) | Policy Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 10 | [Cisco-IOS-XE-policy-mcp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-policy-mcp-deviation.yang) | Policy Mcp Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 11 | [Cisco-IOS-XE-power-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-power-deviation.yang) | Power Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-semver |
| 12 | [Cisco-IOS-XE-sanet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-sanet-deviation.yang) | Sanet Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 13 | [cisco-xe-openconfig-if-poe-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/cisco-xe-openconfig-if-poe-deviation.yang) | Cisco Xe Openconfig If Poe Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 14 | [cisco-xe-openconfig-network-instance-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/cisco-xe-openconfig-network-instance-deviation.yang) | Cisco Xe Openconfig Network Instance Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 15 | [cisco-xe-switching-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/cisco-xe-switching-openconfig-platform-deviation.yang) | Cisco Xe Switching Openconfig Platform Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Native Models (54 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-aaa.yang) | Aaa | Native | -2695 / 0 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; new enum values added; deprecated 3 nodes |
| 2 | [Cisco-IOS-XE-adsl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-adsl.yang) | Adsl | Native | 30 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +476 / 19588 | All Platforms | [Auto-generated summary] | Added 87 new data nodes; imported Cisco-IOS-XE-snmp; new enum values added |
| 4 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-cdp.yang) | Cdp | Native | +112 / 277 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 5 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-cef.yang) | Cef | Native | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; deprecated 1 node |
| 6 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-controller.yang) | Controller | Native | +7 / 604 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; imported Cisco-IOS-XE-features; deprecated 3 nodes |
| 7 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-crypto.yang) | Crypto | Native | +55 / 5098 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; deprecated 9 nodes |
| 8 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | 0 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; imported Cisco-IOS-XE-features, container; new enum values added |
| 9 | [Cisco-IOS-XE-dialer.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-dialer.yang) | Dialer | Native | +2 / 34 | All Platforms | [Auto-generated summary] | Added watch-group, watch-group-list; enhanced validation constraints |
| 10 | [Cisco-IOS-XE-ethernet-cfm-efp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ethernet-cfm-efp.yang) | Ethernet Cfm Efp | Native | 0 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; new enum values added |
| 11 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | 262 | All Platforms | [Auto-generated summary] | new enum values added |
| 12 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 13 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-igmp.yang) | Igmp | Native | 5100 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 14 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 15 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; new enum values added; enhanced validation constraints |
| 16 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added ack-tuning, ratio; enhanced validation constraints |
| 17 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added error-interval, interval, bucket |
| 18 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-isis.yang) | Isis | Native | +4 / 5183 | All Platforms | [Auto-generated summary] | Added set-attached-bit, route-map; deprecated 2 nodes |
| 19 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +324 / 2137 | All Platforms | [Auto-generated summary] | Added 12 new data nodes |
| 20 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added 151 new data nodes; new enum values added; deprecated 1 node |
| 21 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +96 / 28465 | All Platforms | [Auto-generated summary] | Added bridged-vm |
| 22 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 23 | [Cisco-IOS-XE-mdns-gateway.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-mdns-gateway.yang) | Mdns Gateway | Native | +8 / 764 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; imported Cisco-IOS-XE-types; enhanced validation constraints |
| 24 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-mdt-common-defs.yang) | Mdt Common Defs | Native | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 25 | [Cisco-IOS-XE-mdt-oper-v2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-mdt-oper-v2.yang) | Mdt Oper V2 | Native | 89 | All Platforms | [Auto-generated summary] | new enum values added |
| 26 | [Cisco-IOS-XE-mld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-mld.yang) | Mld | Native | 0 | All Platforms | [Auto-generated summary] | Added 26 new data nodes |
| 27 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-nat.yang) | Nat | Native | +5 / 2539 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; new enum values added; enhanced validation constraints |
| 28 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-native.yang) | Native | Native | 0 | All Platforms | [Auto-generated summary] | Added and |
| 29 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +2 / 592 | All Platforms | [Auto-generated summary] | Added domains, vxlan |
| 30 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-nd.yang) | Nd | Native | 0 | All Platforms | [Auto-generated summary] | Added and, server-list, instead";; imported Cisco-IOS-XE-features |
| 31 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ntp.yang) | Ntp | Native | +235 / 908 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 32 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-object-group.yang) | Object Group | Native | 380 | All Platforms | [Auto-generated summary] | Minor refinements |
| 33 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ospf.yang) | Ospf | Native | 0 | All Platforms | [Auto-generated summary] | Added interface-old; enhanced validation constraints |
| 34 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | 0 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 35 | [Cisco-IOS-XE-otv.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-otv.yang) | Otv | Native | +31 / 1335 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 36 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-platform.yang) | Platform | Native | +1 / 139 | All Platforms | [Auto-generated summary] | Added limit-offload |
| 37 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-policy.yang) | Policy | Native | +193 / 4840 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; new enum values added; enhanced validation constraints |
| 38 | [Cisco-IOS-XE-qfp-stats.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-qfp-stats.yang) | Qfp Stats | Native | +2 / 1043 | All Platforms | [Auto-generated summary] | Added cable-arp-autoreply-pkts, cable-arp-autoreply-octets |
| 39 | [Cisco-IOS-XE-rawsocket.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-rawsocket.yang) | Rawsocket | Native | +39 / 65 | All Platforms | [Auto-generated summary] | Added 27 new data nodes; new enum values added |
| 40 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-route-map.yang) | Route Map | Native | 1085 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 41 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-sanet.yang) | Sanet | Native | +2 / 1379 | All Platforms | [Auto-generated summary] | Added bridge-mode, vm-policy |
| 42 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-sla.yang) | Sla | Native | +2 / 2700 | All Platforms | [Auto-generated summary] | Added source-interface, source-interface; enhanced validation constraints |
| 43 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +1 / 1664 | All Platforms | [Auto-generated summary] | Added 21 new data nodes; new enum values added; deprecated 18 nodes |
| 44 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-switch.yang) | Switch | Native | +266 / 6640 | Cat9K, IE3x00 | [Auto-generated summary] | Added 33 new data nodes; imported Cisco-IOS-XE-types; new enum values added |
| 45 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-template.yang) | Template | Native | +36 / 2612 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; deprecated 1 node |
| 46 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | +2 / 1610 | All Platforms | [Auto-generated summary] | Added dual-overlay |
| 47 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-udld.yang) | Udld | Native | +22 / 105 | All Platforms | [Auto-generated summary] | Added node, alert |
| 48 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-vlan.yang) | Vlan | Native | +1 / 140 | Cat9K, IE3x00 | [Auto-generated summary] | Added for, protected |
| 49 | [Cisco-IOS-XE-voice-class.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-voice-class.yang) | Voice Class | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 4 new data nodes |
| 50 | [Cisco-IOS-XE-voice-dspfarm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-voice-dspfarm.yang) | Voice Dspfarm | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | imported cisco-semver |
| 51 | [Cisco-IOS-XE-voice-port.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-voice-port.yang) | Voice Port | Native | +22 / 149 | ISR, Voice Gateways | [Auto-generated summary] | Added 15 new data nodes; new enum values added |
| 52 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-voice.yang) | Voice | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 11 new data nodes; enhanced validation constraints |
| 53 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-vrrp.yang) | Vrrp | Native | 1536 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 54 | [Cisco-IOS-XE-wccp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/Cisco-IOS-XE-wccp.yang) | Wccp | Native | +413 / 853 | All Platforms | [Auto-generated summary] | Added 12 new data nodes |

---

## UPDATED OpenConfig Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [openconfig-aaa-radius.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-aaa-radius.yang) | Openconfig Aaa Radius | OpenConfig | 0 | All Platforms | [Auto-generated summary] | Added secret-key-hashed |
| 2 | [openconfig-aaa-tacacs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-aaa-tacacs.yang) | Openconfig Aaa Tacacs | OpenConfig | 0 | All Platforms | [Auto-generated summary] | Added secret-key-hashed |
| 3 | [openconfig-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-aaa.yang) | Openconfig Aaa | OpenConfig | 0 | All Platforms | [Auto-generated summary] | Added of |
| 4 | [openconfig-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-bfd.yang) | Openconfig Bfd | OpenConfig | -18 / 88 | All Platforms | [Auto-generated summary] | imported openconfig-if-types |
| 5 | [openconfig-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-extensions.yang) | Openconfig Extensions | OpenConfig | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [openconfig-network-instance-l2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-network-instance-l2.yang) | Openconfig Network Instance L2 | OpenConfig | 0 | All Platforms | [Auto-generated summary] | Added evi, vlan, key";; added 3 new imports |
| 7 | [openconfig-network-instance-l3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-network-instance-l3.yang) | Openconfig Network Instance L3 | OpenConfig | 0 | All Platforms | [Auto-generated summary] | Added 14 new data nodes |
| 8 | [openconfig-network-instance.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/openconfig-network-instance.yang) | Openconfig Network Instance | OpenConfig | +885 / 3884 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; added 5 new imports; new enum values added |

---

## UPDATED Other Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-evpn-service.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1781/cisco-evpn-service.yang) | Cisco Evpn Service | Other | -87 / 152 | All Platforms | [Auto-generated summary] | Added 167 new data nodes; added 12 new imports; new enum values added |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
