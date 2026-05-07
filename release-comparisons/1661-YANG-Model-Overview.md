# All YANG Model Changes: v16.5.1 → v16.6.1
**Summary: 74 New Models & 118 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (74 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Configuration Models](#new-configuration-models)** | 1 | 22 XPaths |
| **[NEW Operational Models](#new-operational-models)** | 5 | 123 XPaths |
| **[NEW Types Models](#new-types-models)** | 8 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 16 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 5 | 407 XPaths |
| **[NEW OpenConfig Models](#new-openconfig-models)** | 26 | 1,323 XPaths |
| **[NEW IETF Models](#new-ietf-models)** | 5 | 334 XPaths |
| **[NEW Vendor Models](#new-vendor-models)** | 6 | 51 XPaths |
| **[NEW Other Models](#new-other-models)** | 2 | 42 XPaths |
| **TOTAL NEW MODELS** | **74** | **2,302 total XPaths** |

---

## UPDATED Models Summary (118 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Operational Models](#updated-operational-models)** | 18 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 1 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 1 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 90 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 5 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 3 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **118** | **See individual models** |

---

## Key Highlights - NEW Models


**74 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-rsvp.yang`: 324 XPaths (Native)

  - `openconfig-if-ip.yang`: 278 XPaths (OpenConfig)

  - `openconfig-network-instance.yang`: 217 XPaths (OpenConfig)


- **Breakdown by category:**

  - OpenConfig: 26 models

  - Deviation: 16 models

  - Types: 8 models

  - Vendor: 6 models

  - Native: 5 models

  - Operational: 5 models

  - IETF: 5 models

  - Other: 2 models

  - Configuration: 1 model


---


## Key Highlights - UPDATED Models


**118 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-bgp.yang`: +7,101 XPaths (now 12,399 total)

  - `Cisco-IOS-XE-tunnel.yang`: +350 XPaths (now 682 total)

  - `Cisco-IOS-XE-rip.yang`: +180 XPaths (now 1,275 total)


- **Significant removals:**

  - `Cisco-IOS-XE-mpls.yang`: -821 XPaths (now 0 total)

  - `Cisco-IOS-XE-acl.yang`: -54 XPaths (now 792 total)

  - `Cisco-IOS-XE-crypto.yang`: -44 XPaths (now 2,088 total)


- **Updates by category:**

  - Native: 90 models

  - Operational: 18 models

  - Vendor: 5 models

  - Other: 3 models

  - RPC: 1 model

  - Types: 1 model


---


## Summary Statistics

### Release v16.6.1 Totals:
- **Total YANG Files:** ~592 files
- **New Files:** 74 models
- **Modified Files:** 118 models
- **Deleted Files:** 9 models
- **New Model XPaths:** 2,302 XPaths across 74 new models

---

# NEW YANG Models in v16.6.1

**74 Brand New Models**

---

## NEW Configuration Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-mdt-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mdt-cfg.yang) | Mdt Cfg | Configuration | 22 | All Platforms | New model introduced in this release |

---

## NEW Operational Models (5 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-bgp-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bgp-common-oper.yang) | Bgp Common Oper | Operational | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-bgp-route-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bgp-route-oper.yang) | Bgp Route Oper | Operational | 0 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-cdp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-cdp-oper.yang) | Cdp Oper | Operational | 44 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-mdt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mdt-oper.yang) | Mdt Oper | Operational | 42 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-platform-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-platform-oper.yang) | Platform Oper | Operational | 37 | All Platforms | New model introduced in this release |

---

## NEW Types Models (8 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [openconfig-lldp-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-lldp-types.yang) | Openconfig Lldp Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [openconfig-network-instance-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-network-instance-types.yang) | Openconfig Network Instance Types | Types | 0 | All Platforms | New model introduced in this release |
| 3 | [openconfig-packet-match-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-packet-match-types.yang) | Openconfig Packet Match Types | Types | 0 | All Platforms | New model introduced in this release |
| 4 | [openconfig-platform-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-platform-types.yang) | Openconfig Platform Types | Types | 0 | All Platforms | New model introduced in this release |
| 5 | [openconfig-policy-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-policy-types.yang) | Openconfig Policy Types | Types | 0 | All Platforms | New model introduced in this release |
| 6 | [openconfig-transport-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-transport-types.yang) | Openconfig Transport Types | Types | 0 | All Platforms | New model introduced in this release |
| 7 | [openconfig-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-types.yang) | Openconfig Types | Types | 0 | All Platforms | New model introduced in this release |
| 8 | [openconfig-vlan-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-vlan-types.yang) | Openconfig Vlan Types | Types | 0 | Cat9K, IE3x00 | New model introduced in this release |

---

## NEW Deviation Models (16 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-ietf-event-notifications-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-ietf-event-notifications-deviation.yang) | Cisco Xe Ietf Event Notifications Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 2 | [cisco-xe-ietf-ip-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-ietf-ip-deviation.yang) | Cisco Xe Ietf Ip Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 3 | [cisco-xe-ietf-ipv4-unicast-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-ietf-ipv4-unicast-routing-deviation.yang) | Cisco Xe Ietf Ipv4 Unicast Routing Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 4 | [cisco-xe-ietf-ipv6-unicast-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-ietf-ipv6-unicast-routing-deviation.yang) | Cisco Xe Ietf Ipv6 Unicast Routing Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 5 | [cisco-xe-ietf-ospf-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-ietf-ospf-deviation.yang) | Cisco Xe Ietf Ospf Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 6 | [cisco-xe-ietf-routing-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-ietf-routing-deviation.yang) | Cisco Xe Ietf Routing Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 7 | [cisco-xe-ietf-yang-push-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-ietf-yang-push-deviation.yang) | Cisco Xe Ietf Yang Push Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 8 | [cisco-xe-openconfig-acl-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-acl-deviation.yang) | Cisco Xe Openconfig Acl Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 9 | [cisco-xe-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-if-ethernet-deviation.yang) | Cisco Xe Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 10 | [cisco-xe-openconfig-if-ip-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-if-ip-deviation.yang) | Cisco Xe Openconfig If Ip Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 11 | [cisco-xe-openconfig-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-interfaces-deviation.yang) | Cisco Xe Openconfig Interfaces Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 12 | [cisco-xe-openconfig-network-instance-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-network-instance-deviation.yang) | Cisco Xe Openconfig Network Instance Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 13 | [cisco-xe-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-platform-deviation.yang) | Cisco Xe Openconfig Platform Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 14 | [cisco-xe-openconfig-routing-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-routing-policy-deviation.yang) | Cisco Xe Openconfig Routing Policy Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 15 | [cisco-xe-openconfig-terminal-device-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-terminal-device-deviation.yang) | Cisco Xe Openconfig Terminal Device Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 16 | [cisco-xe-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-vlan-deviation.yang) | Cisco Xe Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |

---

## NEW Native Models (5 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-arp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-arp.yang) | Arp | Native | 5 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mdt-common-defs.yang) | Mdt Common Defs | Native | 0 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-mmode.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mmode.yang) | Mmode | Native | 18 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-rsvp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-rsvp.yang) | Rsvp | Native | 324 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-template.yang) | Template | Native | 60 | All Platforms | New model introduced in this release |

---

## NEW OpenConfig Models (26 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-openconfig-acl-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-acl-ext.yang) | Cisco Xe Openconfig Acl Ext | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 2 | [cisco-xe-openconfig-if-ethernet-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-if-ethernet-ext.yang) | Cisco Xe Openconfig If Ethernet Ext | OpenConfig | 1 | All Platforms | New model introduced in this release |
| 3 | [cisco-xe-openconfig-interfaces-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-interfaces-ext.yang) | Cisco Xe Openconfig Interfaces Ext | OpenConfig | 6 | All Platforms | New model introduced in this release |
| 4 | [cisco-xe-openconfig-platform-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-xe-openconfig-platform-ext.yang) | Cisco Xe Openconfig Platform Ext | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 5 | [openconfig-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-acl.yang) | Openconfig Acl | OpenConfig | 126 | All Platforms | New model introduced in this release |
| 6 | [openconfig-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-extensions.yang) | Openconfig Extensions | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 7 | [openconfig-if-aggregate.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-if-aggregate.yang) | Openconfig If Aggregate | OpenConfig | 11 | All Platforms | New model introduced in this release |
| 8 | [openconfig-if-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-if-ethernet.yang) | Openconfig If Ethernet | OpenConfig | 28 | All Platforms | New model introduced in this release |
| 9 | [openconfig-if-ip-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-if-ip-ext.yang) | Openconfig If Ip Ext | OpenConfig | 11 | All Platforms | New model introduced in this release |
| 10 | [openconfig-if-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-if-ip.yang) | Openconfig If Ip | OpenConfig | 278 | All Platforms | New model introduced in this release |
| 11 | [openconfig-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-interfaces.yang) | Openconfig Interfaces | OpenConfig | 73 | All Platforms | New model introduced in this release |
| 12 | [openconfig-lacp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-lacp.yang) | Openconfig Lacp | OpenConfig | 42 | All Platforms | New model introduced in this release |
| 13 | [openconfig-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-lldp.yang) | Openconfig Lldp | OpenConfig | 80 | All Platforms | New model introduced in this release |
| 14 | [openconfig-local-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-local-routing.yang) | Openconfig Local Routing | OpenConfig | 43 | All Platforms | New model introduced in this release |
| 15 | [openconfig-network-instance-l2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-network-instance-l2.yang) | Openconfig Network Instance L2 | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 16 | [openconfig-network-instance-l3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-network-instance-l3.yang) | Openconfig Network Instance L3 | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 17 | [openconfig-network-instance.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-network-instance.yang) | Openconfig Network Instance | OpenConfig | 217 | All Platforms | New model introduced in this release |
| 18 | [openconfig-optical-amplifier.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-optical-amplifier.yang) | Openconfig Optical Amplifier | OpenConfig | 27 | All Platforms | New model introduced in this release |
| 19 | [openconfig-packet-match.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-packet-match.yang) | Openconfig Packet Match | OpenConfig | 0 | All Platforms | New model introduced in this release |
| 20 | [openconfig-platform-transceiver.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-platform-transceiver.yang) | Openconfig Platform Transceiver | OpenConfig | 48 | All Platforms | New model introduced in this release |
| 21 | [openconfig-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-platform.yang) | Openconfig Platform | OpenConfig | 32 | All Platforms | New model introduced in this release |
| 22 | [openconfig-routing-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-routing-policy.yang) | Openconfig Routing Policy | OpenConfig | 105 | All Platforms | New model introduced in this release |
| 23 | [openconfig-terminal-device.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-terminal-device.yang) | Openconfig Terminal Device | OpenConfig | 107 | All Platforms | New model introduced in this release |
| 24 | [openconfig-transport-line-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-transport-line-common.yang) | Openconfig Transport Line Common | OpenConfig | 3 | All Platforms | New model introduced in this release |
| 25 | [openconfig-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-vlan.yang) | Openconfig Vlan | OpenConfig | 51 | Cat9K, IE3x00 | New model introduced in this release |
| 26 | [openconfig-wavelength-router.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/openconfig-wavelength-router.yang) | Openconfig Wavelength Router | OpenConfig | 34 | All Platforms | New model introduced in this release |

---

## NEW IETF Models (5 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [ietf-event-notifications.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/ietf-event-notifications.yang) | Ietf Event Notifications | IETF | 155 | All Platforms | New model introduced in this release |
| 2 | [ietf-restconf-monitoring-ann.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/ietf-restconf-monitoring-ann.yang) | Ietf Restconf Monitoring Ann | IETF | 0 | All Platforms | New model introduced in this release |
| 3 | [ietf-restconf-monitoring.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/ietf-restconf-monitoring.yang) | Ietf Restconf Monitoring | IETF | 12 | All Platforms | New model introduced in this release |
| 4 | [ietf-yang-library.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/ietf-yang-library.yang) | Ietf Yang Library | IETF | 18 | All Platforms | New model introduced in this release |
| 5 | [ietf-yang-push.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/ietf-yang-push.yang) | Ietf Yang Push | IETF | 149 | All Platforms | New model introduced in this release |

---

## NEW Vendor Models (6 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [tailf-common-query.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-common-query.yang) | Tailf Common Query | Vendor | 0 | All Platforms | New model introduced in this release |
| 2 | [tailf-netconf-inactive.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-netconf-inactive.yang) | Tailf Netconf Inactive | Vendor | 5 | All Platforms | New model introduced in this release |
| 3 | [tailf-netconf-query.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-netconf-query.yang) | Tailf Netconf Query | Vendor | 33 | All Platforms | New model introduced in this release |
| 4 | [tailf-netconf-transactions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-netconf-transactions.yang) | Tailf Netconf Transactions | Vendor | 13 | All Platforms | New model introduced in this release |
| 5 | [tailf-rest-error.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-rest-error.yang) | Tailf Rest Error | Vendor | 0 | All Platforms | New model introduced in this release |
| 6 | [tailf-rest-query.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-rest-query.yang) | Tailf Rest Query | Vendor | 0 | All Platforms | New model introduced in this release |

---

## NEW Other Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-qos-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-qos-common.yang) | Cisco Qos Common | Other | 0 | All Platforms | New model introduced in this release |
| 2 | [oc-mapping-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/oc-mapping-acl.yang) | Oc Mapping Acl | Other | 42 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.5.1 → v16.6.1

**118 Models Modified**

---

## UPDATED Operational Models (18 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-acl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-acl-oper.yang) | Acl Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; imported ietf-yang-types; deprecated 19 nodes |
| 2 | [Cisco-IOS-XE-bfd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bfd-oper.yang) | Bfd Oper | Operational | 43 | All Platforms | [Auto-generated summary] | Minor refinements |
| 3 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bgp-oper.yang) | Bgp Oper | Operational | +42 / 143 | All Platforms | [Auto-generated summary] | Added 87 new data nodes; added 3 new imports; new enum values added |
| 4 | [Cisco-IOS-XE-cfm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-cfm-oper.yang) | Cfm Oper | Operational | 19 | All Platforms | [Auto-generated summary] | Minor refinements |
| 5 | [Cisco-IOS-XE-checkpoint-archive-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-checkpoint-archive-oper.yang) | Checkpoint Archive Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; deprecated 8 nodes |
| 6 | [Cisco-IOS-XE-diffserv-target-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-diffserv-target-oper.yang) | Diffserv Target Oper | Operational | 29 | All Platforms | [Auto-generated summary] | Minor refinements |
| 7 | [Cisco-IOS-XE-efp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-efp-oper.yang) | Efp Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; imported ietf-yang-types; deprecated 8 nodes |
| 8 | [Cisco-IOS-XE-environment-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-environment-oper.yang) | Environment Oper | Operational | 7 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; new enum values added; deprecated 8 nodes |
| 9 | [Cisco-IOS-XE-flow-monitor-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-flow-monitor-oper.yang) | Flow Monitor Oper | Operational | 18 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; deprecated 18 nodes |
| 10 | [Cisco-IOS-XE-ip-sla-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ip-sla-oper.yang) | Ip Sla Oper | Operational | 101 | All Platforms | [Auto-generated summary] | Added 74 new data nodes; imported ietf-yang-types; new enum values added |
| 11 | [Cisco-IOS-XE-lldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-lldp-oper.yang) | Lldp Oper | Operational | 15 | All Platforms | [Auto-generated summary] | Added 16 new data nodes; deprecated 16 nodes |
| 12 | [Cisco-IOS-XE-memory-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-memory-oper.yang) | Memory Oper | Operational | 8 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; deprecated 9 nodes |
| 13 | [Cisco-IOS-XE-mpls-fwd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mpls-fwd-oper.yang) | Mpls Fwd Oper | Operational | 24 | ASR, ISR, NCS | [Auto-generated summary] | Minor refinements |
| 14 | [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-platform-software-oper.yang) | Platform Software Oper | Operational | -5 / 43 | All Platforms | [Auto-generated summary] | Added 44 new data nodes; new enum values added; deprecated 48 nodes |
| 15 | [Cisco-IOS-XE-process-cpu-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-process-cpu-oper.yang) | Process Cpu Oper | Operational | 17 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; deprecated 18 nodes |
| 16 | [Cisco-IOS-XE-process-memory-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-process-memory-oper.yang) | Process Memory Oper | Operational | 10 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; deprecated 11 nodes |
| 17 | [Cisco-IOS-XE-trustsec-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-trustsec-oper.yang) | Trustsec Oper | Operational | 34 | All Platforms | [Auto-generated summary] | Added 36 new data nodes; imported ietf-inet-types, ietf-yang-types; new enum values added |
| 18 | [Cisco-IOS-XE-virtual-service-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-virtual-service-oper.yang) | Virtual Service Oper | Operational | 81 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED RPC Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | 38 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Types Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |

---

## UPDATED Native Models (90 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +31 / 785 | All Platforms | [Auto-generated summary] | Added 41 new data nodes; new enum values added; deprecated 9 nodes |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-acl.yang) | Acl | Native | -54 / 792 | All Platforms | [Auto-generated summary] | Added group";, data; new enum values added; deprecated 22 nodes |
| 3 | [Cisco-IOS-XE-ap.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ap.yang) | Ap | Native | 103 | All Platforms | [Auto-generated summary] | Minor refinements |
| 4 | [Cisco-IOS-XE-atm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-atm.yang) | Atm | Native | 618 | All Platforms | [Auto-generated summary] | Minor refinements |
| 5 | [Cisco-IOS-XE-bba-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bba-group.yang) | Bba Group | Native | 12 | All Platforms | [Auto-generated summary] | Minor refinements |
| 6 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bfd.yang) | Bfd | Native | 70 | All Platforms | [Auto-generated summary] | imported Cisco-IOS-XE-types |
| 7 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +7101 / 12399 | All Platforms | [Auto-generated summary] | Added 46 new data nodes; imported path";, {; new enum values added |
| 8 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-bridge-domain.yang) | Bridge Domain | Native | 151 | All Platforms | [Auto-generated summary] | Minor refinements |
| 9 | [Cisco-IOS-XE-call-home.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-call-home.yang) | Call Home | Native | 118 | All Platforms | [Auto-generated summary] | Minor refinements |
| 10 | [Cisco-IOS-XE-card.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-card.yang) | Card | Native | 4 | All Platforms | [Auto-generated summary] | Minor refinements |
| 11 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-cdp.yang) | Cdp | Native | 41 | All Platforms | [Auto-generated summary] | Minor refinements |
| 12 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-cef.yang) | Cef | Native | +144 / 167 | All Platforms | [Auto-generated summary] | Added 101 new data nodes; deprecated 14 nodes |
| 13 | [Cisco-IOS-XE-coap.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-coap.yang) | Coap | Native | 3 | All Platforms | [Auto-generated summary] | Minor refinements |
| 14 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-controller.yang) | Controller | Native | 183 | All Platforms | [Auto-generated summary] | Minor refinements |
| 15 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-crypto.yang) | Crypto | Native | -44 / 2088 | All Platforms | [Auto-generated summary] | Added 23 new data nodes; deprecated 15 nodes |
| 16 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-cts.yang) | Cts | Native | +48 / 353 | All Platforms | [Auto-generated summary] | Added 33 new data nodes; imported Cisco-IOS-XE-types; new enum values added |
| 17 | [Cisco-IOS-XE-device-sensor.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-device-sensor.yang) | Device Sensor | Native | 2 | All Platforms | [Auto-generated summary] | Minor refinements |
| 18 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | +15 / 46 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; imported Cisco-IOS-XE-types |
| 19 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +64 / 412 | All Platforms | [Auto-generated summary] | Added 17 new data nodes; imported Cisco-IOS-XE-types; deprecated 4 nodes |
| 20 | [Cisco-IOS-XE-diagnostics.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-diagnostics.yang) | Diagnostics | Native | 316 | All Platforms | [Auto-generated summary] | Minor refinements |
| 21 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | 109 | All Platforms | [Auto-generated summary] | Minor refinements |
| 22 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-eem.yang) | Eem | Native | +6 / 86 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added |
| 23 | [Cisco-IOS-XE-eigrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-eigrp.yang) | Eigrp | Native | +6 / 985 | All Platforms | [Auto-generated summary] | Added ospf, pid-list, process-id |
| 24 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | 2145 | All Platforms | [Auto-generated summary] | Minor refinements |
| 25 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | 136 | All Platforms | [Auto-generated summary] | Minor refinements |
| 26 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 27 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-flow.yang) | Flow | Native | 1865 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 28 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-http.yang) | Http | Native | 22 | All Platforms | [Auto-generated summary] | Minor refinements |
| 29 | [Cisco-IOS-XE-icmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-icmp.yang) | Icmp | Native | +1 / 18 | All Platforms | [Auto-generated summary] | Added DF, time; deprecated 1 node |
| 30 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-igmp.yang) | Igmp | Native | 125 | All Platforms | [Auto-generated summary] | Minor refinements |
| 31 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 32 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 25 new data nodes; deprecated 13 nodes |
| 33 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 59 new data nodes; added 4 new imports; new enum values added |
| 34 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; new enum values added |
| 35 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-isis.yang) | Isis | Native | 3638 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 36 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | 609 | All Platforms | [Auto-generated summary] | Minor refinements |
| 37 | [Cisco-IOS-XE-l3vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-l3vpn.yang) | L3Vpn | Native | 11 | All Platforms | [Auto-generated summary] | Minor refinements |
| 38 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 39 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | deprecated 3 nodes |
| 40 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +16 / 14693 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; deprecated 3 nodes |
| 41 | [Cisco-IOS-XE-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-lldp.yang) | Lldp | Native | +12 / 14 | All Platforms | [Auto-generated summary] | Added lldp, receive, transmit |
| 42 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | Added 36 new data nodes; new enum values added; deprecated 27 nodes |
| 43 | [Cisco-IOS-XE-mka.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mka.yang) | Mka | Native | 17 | All Platforms | [Auto-generated summary] | Minor refinements |
| 44 | [Cisco-IOS-XE-mld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mld.yang) | Mld | Native | 8 | All Platforms | [Auto-generated summary] | Minor refinements |
| 45 | [Cisco-IOS-XE-mpls-ldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mpls-ldp.yang) | Mpls Ldp | Native | 723 | ASR, ISR, NCS | [Auto-generated summary] | Minor refinements |
| 46 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-mpls.yang) | Mpls | Native | -821 / 0 | ASR, ISR, NCS | [Auto-generated summary] | Added 176 new data nodes; imported Cisco-IOS-XE-isis; new enum values added |
| 47 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +36 / 419 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; new enum values added; deprecated 2 nodes |
| 48 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-nat.yang) | Nat | Native | +23 / 359 | All Platforms | [Auto-generated summary] | Added 30 new data nodes; imported Cisco-IOS-XE-types; new enum values added |
| 49 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-native.yang) | Native | Native | +98 / 14634 | All Platforms | [Auto-generated summary] | Added 47 new data nodes; deprecated 132 nodes |
| 50 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-nbar.yang) | Nbar | Native | 65 | All Platforms | [Auto-generated summary] | Minor refinements |
| 51 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-nd.yang) | Nd | Native | +5 / 119 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 52 | [Cisco-IOS-XE-nhrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-nhrp.yang) | Nhrp | Native | 170 | All Platforms | [Auto-generated summary] | Minor refinements |
| 53 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ntp.yang) | Ntp | Native | 259 | All Platforms | [Auto-generated summary] | Minor refinements |
| 54 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-object-group.yang) | Object Group | Native | 74 | All Platforms | [Auto-generated summary] | Minor refinements |
| 55 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +68 / 1887 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; new enum values added; deprecated 12 nodes |
| 56 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | 5167 | All Platforms | [Auto-generated summary] | Added for |
| 57 | [Cisco-IOS-XE-otv.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-otv.yang) | Otv | Native | +5 / 1037 | All Platforms | [Auto-generated summary] | Minor refinements |
| 58 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 59 | [Cisco-IOS-XE-pathmgr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-pathmgr.yang) | Pathmgr | Native | 59 | All Platforms | [Auto-generated summary] | Minor refinements |
| 60 | [Cisco-IOS-XE-pfr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-pfr.yang) | Pfr | Native | 410 | All Platforms | [Auto-generated summary] | Minor refinements |
| 61 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-platform.yang) | Platform | Native | 91 | All Platforms | [Auto-generated summary] | Minor refinements |
| 62 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-policy.yang) | Policy | Native | +12 / 2198 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; deprecated 1 node |
| 63 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-power.yang) | Power | Native | 60 | All Platforms | [Auto-generated summary] | Minor refinements |
| 64 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-ppp.yang) | Ppp | Native | 111 | All Platforms | [Auto-generated summary] | Minor refinements |
| 65 | [Cisco-IOS-XE-qos.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-qos.yang) | Qos | Native | 36 | All Platforms | [Auto-generated summary] | Minor refinements |
| 66 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-rip.yang) | Rip | Native | +180 / 1275 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; deprecated 2 nodes |
| 67 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +1 / 452 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added; deprecated 4 nodes |
| 68 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-sanet.yang) | Sanet | Native | 221 | All Platforms | [Auto-generated summary] | Minor refinements |
| 69 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | +4 / 63 | All Platforms | [Auto-generated summary] | Added attach |
| 70 | [Cisco-IOS-XE-service-chain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-service-chain.yang) | Service Chain | Native | 37 | All Platforms | [Auto-generated summary] | Minor refinements |
| 71 | [Cisco-IOS-XE-service-discovery.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-service-discovery.yang) | Service Discovery | Native | 29 | All Platforms | [Auto-generated summary] | Minor refinements |
| 72 | [Cisco-IOS-XE-service-insertion.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-service-insertion.yang) | Service Insertion | Native | 28 | All Platforms | [Auto-generated summary] | Added enable; deprecated 1 node |
| 73 | [Cisco-IOS-XE-service-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-service-routing.yang) | Service Routing | Native | +1 / 3 | All Platforms | [Auto-generated summary] | Added mdns-sd |
| 74 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-sla.yang) | Sla | Native | 171 | All Platforms | [Auto-generated summary] | Minor refinements |
| 75 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-snmp.yang) | Snmp | Native | 853 | All Platforms | [Auto-generated summary] | Minor refinements |
| 76 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | 165 | All Platforms | [Auto-generated summary] | Minor refinements |
| 77 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-switch.yang) | Switch | Native | -18 / 2577 | Cat9K, IE3x00 | [Auto-generated summary] | Added 5 new data nodes; imported Cisco-IOS-XE-arp; deprecated 8 nodes |
| 78 | [Cisco-IOS-XE-track.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-track.yang) | Track | Native | 72 | All Platforms | [Auto-generated summary] | imported Cisco-IOS-XE-types |
| 79 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | +350 / 682 | All Platforms | [Auto-generated summary] | Added multilsp; imported Cisco-IOS-XE-types; deprecated 46 nodes |
| 80 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-udld.yang) | Udld | Native | 41 | All Platforms | [Auto-generated summary] | Minor refinements |
| 81 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-utd.yang) | Utd | Native | 53 | All Platforms | [Auto-generated summary] | Minor refinements |
| 82 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-vlan.yang) | Vlan | Native | +15 / 591 | Cat9K, IE3x00 | [Auto-generated summary] | Added 10 new data nodes; imported Cisco-IOS-XE-service-routing; new enum values added |
| 83 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-voice.yang) | Voice | Native | 12 | ISR, Voice Gateways | [Auto-generated summary] | Minor refinements |
| 84 | [Cisco-IOS-XE-vpdn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-vpdn.yang) | Vpdn | Native | 4 | All Platforms | [Auto-generated summary] | Minor refinements |
| 85 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-vservice.yang) | Vservice | Native | 31 | All Platforms | [Auto-generated summary] | Minor refinements |
| 86 | [Cisco-IOS-XE-vstack.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-vstack.yang) | Vstack | Native | 2 | All Platforms | [Auto-generated summary] | Minor refinements |
| 87 | [Cisco-IOS-XE-vtp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-vtp.yang) | Vtp | Native | 28 | All Platforms | [Auto-generated summary] | Minor refinements |
| 88 | [Cisco-IOS-XE-wccp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-wccp.yang) | Wccp | Native | 272 | All Platforms | [Auto-generated summary] | Minor refinements |
| 89 | [Cisco-IOS-XE-wsma.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-wsma.yang) | Wsma | Native | 13 | All Platforms | [Auto-generated summary] | Minor refinements |
| 90 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/Cisco-IOS-XE-zone.yang) | Zone | Native | 26 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Vendor Models (5 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | +17 / 550 | All Platforms | [Auto-generated summary] | Added 72 new data nodes; new enum values added; enhanced validation constraints |
| 2 | [tailf-cli-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-cli-extensions.yang) | Tailf Cli Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | Added should |
| 3 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-common.yang) | Tailf Common | Vendor | 0 | All Platforms | [Auto-generated summary] | new enum values added; enhanced validation constraints |
| 4 | [tailf-meta-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-meta-extensions.yang) | Tailf Meta Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [tailf-netconf-monitoring.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/tailf-netconf-monitoring.yang) | Tailf Netconf Monitoring | Vendor | +2 / 20 | All Platforms | [Auto-generated summary] | Added transaction-lock, is, locked-by-session |

---

## UPDATED Other Models (3 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-ia.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-ia.yang) | Cisco Ia | Other | +4 / 74 | All Platforms | [Auto-generated summary] | Added ignore-presrv-paths |
| 2 | [cisco-odm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/cisco-odm.yang) | Cisco Odm | Other | 7 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [iana-crypt-hash.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1661/iana-crypt-hash.yang) | Iana Crypt Hash | Other | 0 | All Platforms | [Auto-generated summary] | Minor refinements |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
