# All YANG Model Changes: v16.7.1 → v16.8.1
**Summary: 73 New Models & 93 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (73 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 15 | 1,413 XPaths |
| **[NEW Types Models](#new-types-models)** | 8 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 7 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 12 | 3,203 XPaths |
| **[NEW OpenConfig Models](#new-openconfig-models)** | 28 | 2,342 XPaths |
| **[NEW IETF Models](#new-ietf-models)** | 1 | 29 XPaths |
| **[NEW Other Models](#new-other-models)** | 2 | 191 XPaths |
| **TOTAL NEW MODELS** | **73** | **7,178 total XPaths** |

---

## UPDATED Models Summary (93 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 1 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 11 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 1 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 6 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 5 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 59 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 5 | XPath changes vary |
| **[UPDATED IETF Models](#updated-ietf-models)** | 2 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 1 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 2 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **93** | **See individual models** |

---

## Key Highlights - NEW Models


**73 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-switch.yang`: 2,877 XPaths (Native)

  - `openconfig-bgp.yang`: 832 XPaths (OpenConfig)

  - `Cisco-IOS-XE-ospf-oper.yang`: 666 XPaths (Operational)


- **Breakdown by category:**

  - OpenConfig: 28 models

  - Operational: 15 models

  - Native: 12 models

  - Types: 8 models

  - Deviation: 7 models

  - Other: 2 models

  - IETF: 1 model


---


## Key Highlights - UPDATED Models


**93 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-ospfv3.yang`: +930 XPaths (now 6,717 total)

  - `Cisco-IOS-XE-native.yang`: +924 XPaths (now 19,899 total)

  - `openconfig-network-instance.yang`: +832 XPaths (now 1,049 total)


- **Significant removals:**

  - `ietf-event-notifications.yang`: -5 XPaths (now 155 total)

  - `Cisco-IOS-XE-platform-oper.yang`: -2 XPaths (now 35 total)


- **Updates by category:**

  - Native: 59 models

  - Operational: 11 models

  - Types: 6 models

  - Deviation: 5 models

  - OpenConfig: 5 models

  - Other: 2 models

  - IETF: 2 models

  - Configuration: 1 model

  - RPC: 1 model

  - Vendor: 1 model


---


## Summary Statistics

### Release v16.8.1 Totals:
- **Total YANG Files:** ~566 files
- **New Files:** 73 models
- **Modified Files:** 93 models
- **Deleted Files:** 1 models
- **New Model XPaths:** 7,178 XPaths across 73 new models

---

# NEW YANG Models in v16.8.1

**73 Brand New Models**

---

## NEW Operational Models (15 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-aaa-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-aaa-oper.yang) | Aaa Oper | Operational | 9 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-cellwan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-cellwan-oper.yang) | Cellwan Oper | Operational | 69 | IR1101, C1100 | New model introduced in this release |
| 3 | [Cisco-IOS-XE-device-hardware-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-device-hardware-oper.yang) | Device Hardware Oper | Operational | 22 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-dhcp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-dhcp-oper.yang) | Dhcp Oper | Operational | 32 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-fib-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-fib-oper.yang) | Fib Oper | Operational | 24 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces Oper | Operational | 365 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-ipv6-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ipv6-oper.yang) | Ipv6 Oper | Operational | 9 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-nat-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-nat-oper.yang) | Nat Oper | Operational | 37 | All Platforms | New model introduced in this release |
| 9 | [Cisco-IOS-XE-ntp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ntp-oper.yang) | Ntp Oper | Operational | 43 | All Platforms | New model introduced in this release |
| 10 | [Cisco-IOS-XE-ospf-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ospf-oper.yang) | Ospf Oper | Operational | 666 | All Platforms | New model introduced in this release |
| 11 | [Cisco-IOS-XE-ppp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ppp-oper.yang) | Ppp Oper | Operational | 38 | All Platforms | New model introduced in this release |
| 12 | [Cisco-IOS-XE-spanning-tree-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-spanning-tree-oper.yang) | Spanning Tree Oper | Operational | 49 | All Platforms | New model introduced in this release |
| 13 | [Cisco-IOS-XE-tcam-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-tcam-oper.yang) | Tcam Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 14 | [Cisco-IOS-XE-vlan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-vlan-oper.yang) | Vlan Oper | Operational | 8 | Cat9K, IE3x00 | New model introduced in this release |
| 15 | [Cisco-IOS-XE-vrrp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-vrrp-oper.yang) | Vrrp Oper | Operational | 34 | All Platforms | New model introduced in this release |

---

## NEW Types Models (8 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [openconfig-aaa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-aaa-types.yang) | Openconfig Aaa Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [openconfig-bgp-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-types.yang) | Openconfig Bgp Types | Types | 0 | All Platforms | New model introduced in this release |
| 3 | [openconfig-lldp-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-lldp-types.yang) | Openconfig Lldp Types | Types | 0 | All Platforms | New model introduced in this release |
| 4 | [openconfig-openflow-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-openflow-types.yang) | Openconfig Openflow Types | Types | 0 | All Platforms | New model introduced in this release |
| 5 | [openconfig-platform-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-platform-types.yang) | Openconfig Platform Types | Types | 0 | All Platforms | New model introduced in this release |
| 6 | [openconfig-rib-bgp-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-rib-bgp-types.yang) | Openconfig Rib Bgp Types | Types | 0 | All Platforms | New model introduced in this release |
| 7 | [openconfig-spanning-tree-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-spanning-tree-types.yang) | Openconfig Spanning Tree Types | Types | 0 | All Platforms | New model introduced in this release |
| 8 | [openconfig-transport-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-transport-types.yang) | Openconfig Transport Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Deviation Models (7 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-switch-deviation.yang) | Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 2 | [cisco-xe-openconfig-bgp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-bgp-deviation.yang) | Cisco Xe Openconfig Bgp Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 3 | [cisco-xe-openconfig-bgp-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-bgp-policy-deviation.yang) | Cisco Xe Openconfig Bgp Policy Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 4 | [cisco-xe-openconfig-openflow-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-openflow-deviation.yang) | Cisco Xe Openconfig Openflow Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 5 | [cisco-xe-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-platform-deviation.yang) | Cisco Xe Openconfig Platform Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 6 | [cisco-xe-openconfig-spanning-tree-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-spanning-tree-deviation.yang) | Cisco Xe Openconfig Spanning Tree Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 7 | [cisco-xe-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-system-deviation.yang) | Cisco Xe Openconfig System Deviation | Deviation | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (12 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-avb.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-avb.yang) | Avb | Native | 1 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-cellular.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-cellular.yang) | Cellular | Native | 25 | IR1101, C1100 | New model introduced in this release |
| 3 | [Cisco-IOS-XE-coap.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-coap.yang) | Coap | Native | 3 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-device-sensor.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-device-sensor.yang) | Device Sensor | Native | 4 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-eta.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-eta.yang) | Eta | Native | 44 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-mmode.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-mmode.yang) | Mmode | Native | 20 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-mvrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-mvrp.yang) | Mvrp | Native | 131 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-ptp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ptp.yang) | Ptp | Native | 12 | All Platforms | New model introduced in this release |
| 9 | [Cisco-IOS-XE-stackwise-virtual.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-stackwise-virtual.yang) | Stackwise Virtual | Native | 8 | All Platforms | New model introduced in this release |
| 10 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-switch.yang) | Switch | Native | 2877 | Cat9K, IE3x00 | New model introduced in this release |
| 11 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-udld.yang) | Udld | Native | 76 | All Platforms | New model introduced in this release |
| 12 | [Cisco-IOS-XE-vstack.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-vstack.yang) | Vstack | Native | 2 | All Platforms | New model introduced in this release |

---

## NEW OpenConfig Models (28 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-openconfig-platform-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-platform-ext.yang) | Cisco Xe Openconfig Platform Ext | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 2 | [cisco-xe-openconfig-rib-bgp-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-rib-bgp-ext.yang) | Cisco Xe Openconfig Rib Bgp Ext | OpenConfig | 342 | All Platforms | New model introduced in this release |
| 3 | [cisco-xe-openconfig-spanning-tree-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-spanning-tree-ext.yang) | Cisco Xe Openconfig Spanning Tree Ext | OpenConfig | 2 | All Platforms | New model introduced in this release |
| 4 | [cisco-xe-openconfig-system-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-system-ext.yang) | Cisco Xe Openconfig System Ext | OpenConfig | 6 | All Platforms | New model introduced in this release |
| 5 | [cisco-xe-openconfig-vlan-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-vlan-ext.yang) | Cisco Xe Openconfig Vlan Ext | OpenConfig | 7 | Cat9K, IE3x00 | New model introduced in this release |
| 6 | [openconfig-aaa-radius.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-aaa-radius.yang) | Openconfig Aaa Radius | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 7 | [openconfig-aaa-tacacs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-aaa-tacacs.yang) | Openconfig Aaa Tacacs | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 8 | [openconfig-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-aaa.yang) | Openconfig Aaa | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 9 | [openconfig-bgp-common-multiprotocol.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-common-multiprotocol.yang) | Openconfig Bgp Common Multiprotocol | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 10 | [openconfig-bgp-common-structure.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-common-structure.yang) | Openconfig Bgp Common Structure | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 11 | [openconfig-bgp-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-common.yang) | Openconfig Bgp Common | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 12 | [openconfig-bgp-global.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-global.yang) | Openconfig Bgp Global | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 13 | [openconfig-bgp-neighbor.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-neighbor.yang) | Openconfig Bgp Neighbor | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 14 | [openconfig-bgp-peer-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-peer-group.yang) | Openconfig Bgp Peer Group | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 15 | [openconfig-bgp-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp-policy.yang) | Openconfig Bgp Policy | OpenConfig | 128 | All Platforms | New model introduced in this release |
| 16 | [openconfig-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-bgp.yang) | Openconfig Bgp | OpenConfig | 832 | All Platforms | New model introduced in this release |
| 17 | [openconfig-lacp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-lacp.yang) | Openconfig Lacp | OpenConfig | 42 | All Platforms | New model introduced in this release |
| 18 | [openconfig-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-lldp.yang) | Openconfig Lldp | OpenConfig | 80 | All Platforms | New model introduced in this release |
| 19 | [openconfig-openflow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-openflow.yang) | Openconfig Openflow | OpenConfig | 41 | All Platforms | New model introduced in this release |
| 20 | [openconfig-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-platform.yang) | Openconfig Platform | OpenConfig | 37 | All Platforms | New model introduced in this release |
| 21 | [openconfig-procmon.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-procmon.yang) | Openconfig Procmon | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 22 | [openconfig-rib-bgp-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-rib-bgp-ext.yang) | Openconfig Rib Bgp Ext | OpenConfig | 10 | All Platforms | New model introduced in this release |
| 23 | [openconfig-rib-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-rib-bgp.yang) | Openconfig Rib Bgp | OpenConfig | 342 | All Platforms | New model introduced in this release |
| 24 | [openconfig-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-spanning-tree.yang) | Openconfig Spanning Tree | OpenConfig | 192 | All Platforms | New model introduced in this release |
| 25 | [openconfig-system-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-system-logging.yang) | Openconfig System Logging | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 26 | [openconfig-system-terminal.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-system-terminal.yang) | Openconfig System Terminal | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 27 | [openconfig-system.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-system.yang) | Openconfig System | OpenConfig | 278 | All Platforms | New model introduced in this release |
| 28 | [openconfig-transport-line-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-transport-line-common.yang) | Openconfig Transport Line Common | OpenConfig | 3 | All Platforms | New model introduced in this release |

---

## NEW IETF Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [ietf-netconf-acm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/ietf-netconf-acm.yang) | Ietf Netconf Acm | IETF | 29 | All Platforms | New model introduced in this release |

---

## NEW Other Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-smart-license-errors.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-smart-license-errors.yang) | Cisco Smart License Errors | Other | 0 | All Platforms | New model introduced in this release |
| 2 | [cisco-smart-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-smart-license.yang) | Cisco Smart License | Other | 191 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.7.1 → v16.8.1

**93 Models Modified**

---

## UPDATED Configuration Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-mdt-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-mdt-cfg.yang) | Mdt Cfg | Configuration | +30 / 56 | All Platforms | [Auto-generated summary] | Added 28 new data nodes; new enum values added |

---

## UPDATED Operational Models (11 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-bfd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-bfd-oper.yang) | Bfd Oper | Operational | +2 / 45 | All Platforms | [Auto-generated summary] | Added 29 new data nodes; imported ietf-inet-types; new enum values added |
| 2 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-bgp-oper.yang) | Bgp Oper | Operational | +3 / 347 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 3 | [Cisco-IOS-XE-bgp-route-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-bgp-route-oper.yang) | Bgp Route Oper | Operational | 0 | All Platforms | [Auto-generated summary] | Added ordering"; |
| 4 | [Cisco-IOS-XE-environment-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-environment-oper.yang) | Environment Oper | Operational | +4 / 11 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 5 | [Cisco-IOS-XE-flow-monitor-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-flow-monitor-oper.yang) | Flow Monitor Oper | Operational | +55 / 73 | All Platforms | [Auto-generated summary] | Added 52 new data nodes; imported ietf-yang-types; new enum values added |
| 6 | [Cisco-IOS-XE-ip-sla-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ip-sla-oper.yang) | Ip Sla Oper | Operational | 101 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +179 / 214 | All Platforms | [Auto-generated summary] | Added 160 new data nodes; imported ietf-inet-types; new enum values added |
| 8 | [Cisco-IOS-XE-mdt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-mdt-oper.yang) | Mdt Oper | Operational | +4 / 52 | All Platforms | [Auto-generated summary] | Added security-profile, security-profile |
| 9 | [Cisco-IOS-XE-platform-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-platform-oper.yang) | Platform Oper | Operational | -2 / 35 | All Platforms | [Auto-generated summary] | new enum values added; deprecated 2 nodes |
| 10 | [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-platform-software-oper.yang) | Platform Software Oper | Operational | +12 / 55 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; imported ietf-yang-types |
| 11 | [Cisco-IOS-XE-virtual-service-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-virtual-service-oper.yang) | Virtual Service Oper | Operational | +9 / 90 | All Platforms | [Auto-generated summary] | Added 88 new data nodes; imported ietf-inet-types, ietf-yang-types; deprecated 82 nodes |

---

## UPDATED RPC Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +171 / 243 | All Platforms | [Auto-generated summary] | Added 86 new data nodes; deprecated 2 nodes |

---

## UPDATED Types Models (6 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-common-types.yang) | Common Types | Types | 0 | All Platforms | [Auto-generated summary] | Added ordering; new enum values added |
| 2 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [openconfig-inet-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-inet-types.yang) | Openconfig Inet Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [openconfig-packet-match-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-packet-match-types.yang) | Openconfig Packet Match Types | Types | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 5 | [openconfig-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-types.yang) | Openconfig Types | Types | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [openconfig-yang-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-yang-types.yang) | Openconfig Yang Types | Types | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Deviation Models (5 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-ietf-ospf-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-ietf-ospf-deviation.yang) | Cisco Xe Ietf Ospf Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [cisco-xe-openconfig-acl-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-acl-deviation.yang) | Cisco Xe Openconfig Acl Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 3 | [cisco-xe-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-if-ethernet-deviation.yang) | Cisco Xe Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [cisco-xe-openconfig-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-interfaces-deviation.yang) | Cisco Xe Openconfig Interfaces Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [cisco-xe-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-vlan-deviation.yang) | Cisco Xe Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | imported cisco-xe-openconfig-vlan-ext |

---

## UPDATED Native Models (59 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +162 / 1768 | All Platforms | [Auto-generated summary] | Added 70 new data nodes; new enum values added; deprecated 12 nodes |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-acl.yang) | Acl | Native | 0 | All Platforms | [Auto-generated summary] | Added src, dst |
| 3 | [Cisco-IOS-XE-arp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-arp.yang) | Arp | Native | +6 / 11 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added; deprecated 4 nodes |
| 4 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-bfd.yang) | Bfd | Native | +18 / 116 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +348 / 13403 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-cdp.yang) | Cdp | Native | +24 / 83 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-controller.yang) | Controller | Native | +30 / 213 | All Platforms | [Auto-generated summary] | Added 30 new data nodes; new enum values added |
| 8 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-crypto.yang) | Crypto | Native | +47 / 2216 | All Platforms | [Auto-generated summary] | Added 19 new data nodes; imported url'; new enum values added |
| 9 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-cts.yang) | Cts | Native | +44 / 447 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +157 / 642 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; deprecated 1 node |
| 11 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | +63 / 214 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 12 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-eem.yang) | Eem | Native | +34 / 129 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; new enum values added; deprecated 3 nodes |
| 13 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | +337 / 3671 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; new enum values added; deprecated 7 nodes |
| 14 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | +9 / 151 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 15 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 16 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-flow.yang) | Flow | Native | +101 / 2022 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; deprecated 2 nodes |
| 17 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-http.yang) | Http | Native | +4 / 26 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 18 | [Cisco-IOS-XE-icmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-icmp.yang) | Icmp | Native | +6 / 29 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 19 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-igmp.yang) | Igmp | Native | +44 / 199 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 20 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; deprecated 1 node |
| 21 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; new enum values added; deprecated 2 nodes |
| 22 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added ip-list, ip-list; deprecated 2 nodes |
| 23 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-isis.yang) | Isis | Native | +315 / 4292 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 24 | [Cisco-IOS-XE-iwanfabric.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-iwanfabric.yang) | Iwanfabric | Native | +10 / 129 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 25 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +132 / 830 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 26 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | [Auto-generated summary] | Added 34 new data nodes; new enum values added; enhanced validation constraints |
| 27 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +42 / 14763 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 28 | [Cisco-IOS-XE-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-lldp.yang) | Lldp | Native | +6 / 26 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 29 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; deprecated 5 nodes |
| 30 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-mdt-common-defs.yang) | Mdt Common Defs | Native | 0 | All Platforms | [Auto-generated summary] | Added transform-name; new enum values added |
| 31 | [Cisco-IOS-XE-mka.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-mka.yang) | Mka | Native | +20 / 56 | All Platforms | [Auto-generated summary] | Added key-server, priority |
| 32 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-mpls.yang) | Mpls | Native | 0 | ASR, ISR, NCS | [Auto-generated summary] | updated descriptions and documentation |
| 33 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +46 / 511 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 34 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-nat.yang) | Nat | Native | +89 / 478 | All Platforms | [Auto-generated summary] | Added 18 new data nodes |
| 35 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-native.yang) | Native | Native | +924 / 19899 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; new enum values added |
| 36 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +79 / 432 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 37 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-nd.yang) | Nd | Native | +30 / 167 | All Platforms | [Auto-generated summary] | Added suppress, policy, nd-suppress-policy-name |
| 38 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ntp.yang) | Ntp | Native | +66 / 329 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 39 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +408 / 2626 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 40 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | +930 / 6717 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 41 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | [Auto-generated summary] | Added 21 new data nodes; new enum values added |
| 42 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-platform.yang) | Platform | Native | +4 / 95 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 43 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-policy.yang) | Policy | Native | +123 / 2175 | All Platforms | [Auto-generated summary] | Added 62 new data nodes; new enum values added |
| 44 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-power.yang) | Power | Native | +59 / 153 | All Platforms | [Auto-generated summary] | Added perpetual-poe-ha |
| 45 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-ppp.yang) | Ppp | Native | +3 / 114 | All Platforms | [Auto-generated summary] | Added disable |
| 46 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-rip.yang) | Rip | Native | +18 / 1305 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 47 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +482 / 943 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; new enum values added; deprecated 4 nodes |
| 48 | [Cisco-IOS-XE-rsvp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-rsvp.yang) | Rsvp | Native | +129 / 539 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 49 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-sanet.yang) | Sanet | Native | +147 / 466 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 50 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-sla.yang) | Sla | Native | 171 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 51 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +58 / 949 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; deprecated 2 nodes |
| 52 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | +56 / 341 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 53 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-template.yang) | Template | Native | +803 / 863 | All Platforms | [Auto-generated summary] | Added 77 new data nodes; imported Cisco-IOS-XE-features |
| 54 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-umbrella.yang) | Umbrella | Native | +3 / 56 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 55 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-utd.yang) | Utd | Native | +121 / 284 | All Platforms | [Auto-generated summary] | Added 53 new data nodes; new enum values added; deprecated 17 nodes |
| 56 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-vlan.yang) | Vlan | Native | +15 / 624 | Cat9K, IE3x00 | [Auto-generated summary] | Added 7 new data nodes; imported Cisco-IOS-XE-types |
| 57 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-vservice.yang) | Vservice | Native | +1 / 35 | All Platforms | [Auto-generated summary] | Added TwentyFiveGigE, TwoGigabitEthernet; deprecated 1 node |
| 58 | [Cisco-IOS-XE-wccp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-wccp.yang) | Wccp | Native | +140 / 412 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 59 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/Cisco-IOS-XE-zone.yang) | Zone | Native | +2 / 42 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED OpenConfig Models (5 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-openconfig-if-ethernet-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-xe-openconfig-if-ethernet-ext.yang) | Cisco Xe Openconfig If Ethernet Ext | OpenConfig | +1 / 2 | All Platforms | [Auto-generated summary] | Added switchport |
| 2 | [openconfig-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-acl.yang) | Openconfig Acl | OpenConfig | 144 | All Platforms | [Auto-generated summary] | Minor refinements |
| 3 | [openconfig-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-extensions.yang) | Openconfig Extensions | OpenConfig | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [openconfig-network-instance.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-network-instance.yang) | Openconfig Network Instance | OpenConfig | +832 / 1049 | All Platforms | [Auto-generated summary] | imported openconfig-bgp |
| 5 | [openconfig-packet-match.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/openconfig-packet-match.yang) | Openconfig Packet Match | OpenConfig | 0 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED IETF Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [ietf-event-notifications.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/ietf-event-notifications.yang) | Ietf Event Notifications | IETF | -5 / 155 | All Platforms | [Auto-generated summary] | deprecated 2 nodes |
| 2 | [ietf-restconf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/ietf-restconf.yang) | Ietf Restconf | IETF | 0 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Vendor Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | +2 / 557 | All Platforms | [Auto-generated summary] | Added rest, authCacheTTL |

---

## UPDATED Other Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-ia.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/cisco-ia.yang) | Cisco Ia | Other | 74 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [common-mpls-static-devs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1681/common-mpls-static-devs.yang) | Common Mpls Static Devs | Other | 0 | ASR, ISR, NCS | [Auto-generated summary] | updated descriptions and documentation |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
