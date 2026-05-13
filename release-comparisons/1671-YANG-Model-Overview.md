# All YANG Model Changes: v16.6.2 → v16.7.1
**Summary: 4 New Models & 80 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (4 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 1 | 35 XPaths |
| **[NEW Types Models](#new-types-models)** | 1 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 1 | 119 XPaths |
| **[NEW IETF Models](#new-ietf-models)** | 1 | 18 XPaths |
| **TOTAL NEW MODELS** | **4** | **172 total XPaths** |

---

## UPDATED Models Summary (80 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Operational Models](#updated-operational-models)** | 6 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 1 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 1 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 6 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 57 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 4 | XPath changes vary |
| **[UPDATED IETF Models](#updated-ietf-models)** | 1 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 4 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **80** | **See individual models** |

---

## Key Highlights - NEW Models


**4 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-iwanfabric.yang`: 119 XPaths (Native)

  - `Cisco-IOS-XE-lisp-oper.yang`: 35 XPaths (Operational)

  - `cisco-xe-ietf-yang-push-ext.yang`: 18 XPaths (IETF)


- **Breakdown by category:**

  - Types: 1 model

  - Native: 1 model

  - Operational: 1 model

  - IETF: 1 model


---


## Key Highlights - UPDATED Models


**80 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-native.yang`: +4,387 XPaths (now 18,975 total)

  - `Cisco-IOS-XE-ethernet.yang`: +1,189 XPaths (now 3,334 total)

  - `Cisco-IOS-XE-bgp.yang`: +656 XPaths (now 13,055 total)


- **Significant removals:**

  - `Cisco-IOS-XE-acl.yang`: -792 XPaths (now 0 total)

  - `Cisco-IOS-XE-policy.yang`: -149 XPaths (now 2,052 total)


- **Updates by category:**

  - Native: 57 models

  - Operational: 6 models

  - Deviation: 6 models

  - OpenConfig: 4 models

  - Vendor: 4 models

  - RPC: 1 model

  - Types: 1 model

  - IETF: 1 model


---


## Summary Statistics

### Release v16.7.1 Totals:
- **Total YANG Files:** ~484 files
- **New Files:** 4 models
- **Modified Files:** 80 models
- **Deleted Files:** 13 models
- **New Model XPaths:** 172 XPaths across 4 new models

---

# NEW YANG Models in v16.7.1

**4 Brand New Models**

---

## NEW Operational Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | 35 | All Platforms | New model introduced in this release |

---

## NEW Types Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-common-types.yang) | Common Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-iwanfabric.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-iwanfabric.yang) | Iwanfabric | Native | 119 | All Platforms | New model introduced in this release |

---

## NEW IETF Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-ietf-yang-push-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-ietf-yang-push-ext.yang) | Cisco Xe Ietf Yang Push Ext | IETF | 18 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.6.2 → v16.7.1

**80 Models Modified**

---

## UPDATED Operational Models (6 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-bgp-oper.yang) | Bgp Oper | Operational | +201 / 344 | All Platforms | [Auto-generated summary] | Added bgp-route-rds, bgp-route-rd |
| 2 | [Cisco-IOS-XE-bgp-route-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-bgp-route-oper.yang) | Bgp Route Oper | Operational | 0 | All Platforms | [Auto-generated summary] | Added 82 new data nodes; new enum values added |
| 3 | [Cisco-IOS-XE-cdp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-cdp-oper.yang) | Cdp Oper | Operational | 44 | All Platforms | [Auto-generated summary] | Added cdp-neighbour-details, cdp-neighbor-details, cdp-neighbor-detail; deprecated 2 nodes |
| 4 | [Cisco-IOS-XE-cfm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-cfm-oper.yang) | Cfm Oper | Operational | 19 | All Platforms | [Auto-generated summary] | Added 18 new data nodes; imported ietf-yang-types; new enum values added |
| 5 | [Cisco-IOS-XE-ip-sla-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-ip-sla-oper.yang) | Ip Sla Oper | Operational | 101 | All Platforms | [Auto-generated summary] | new enum values added |
| 6 | [Cisco-IOS-XE-mdt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-mdt-oper.yang) | Mdt Oper | Operational | +6 / 48 | All Platforms | [Auto-generated summary] | Added source-vrf, source-address |

---

## UPDATED RPC Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +34 / 72 | All Platforms | [Auto-generated summary] | Added 19 new data nodes; imported ietf-inet-types; deprecated 1 node |

---

## UPDATED Types Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |

---

## UPDATED Deviation Models (6 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-ietf-event-notifications-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-ietf-event-notifications-deviation.yang) | Cisco Xe Ietf Event Notifications Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [cisco-xe-ietf-yang-push-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-ietf-yang-push-deviation.yang) | Cisco Xe Ietf Yang Push Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported cisco-xe-ietf-yang-push-ext |
| 3 | [cisco-xe-openconfig-acl-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-openconfig-acl-deviation.yang) | Cisco Xe Openconfig Acl Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported tailf-common |
| 4 | [cisco-xe-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-openconfig-if-ethernet-deviation.yang) | Cisco Xe Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | deprecated 1 node |
| 5 | [cisco-xe-openconfig-network-instance-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-openconfig-network-instance-deviation.yang) | Cisco Xe Openconfig Network Instance Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 6 | [cisco-xe-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-openconfig-vlan-deviation.yang) | Cisco Xe Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |

---

## UPDATED Native Models (57 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-acl.yang) | Acl | Native | -792 / 0 | All Platforms | [Auto-generated summary] | Added 35 new data nodes; new enum values added; deprecated 24 nodes |
| 2 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-bfd.yang) | Bfd | Native | +28 / 98 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; deprecated 5 nodes |
| 3 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +656 / 13055 | All Platforms | [Auto-generated summary] | Added 24 new data nodes; imported path, {; new enum values added |
| 4 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-cdp.yang) | Cdp | Native | +18 / 59 | All Platforms | [Auto-generated summary] | Added holdtime, timer |
| 5 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-crypto.yang) | Crypto | Native | +81 / 2169 | All Platforms | [Auto-generated summary] | Added 23 new data nodes; deprecated 1 node |
| 6 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-cts.yang) | Cts | Native | +48 / 403 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | 46 | All Platforms | [Auto-generated summary] | Minor refinements |
| 8 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +73 / 485 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 9 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | +42 / 151 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-eem.yang) | Eem | Native | +9 / 95 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; deprecated 10 nodes |
| 11 | [Cisco-IOS-XE-eigrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-eigrp.yang) | Eigrp | Native | +57 / 1042 | All Platforms | [Auto-generated summary] | Added 14 new data nodes |
| 12 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | +1189 / 3334 | All Platforms | [Auto-generated summary] | Added 21 new data nodes; new enum values added; deprecated 4 nodes |
| 13 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | +6 / 142 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 14 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-flow.yang) | Flow | Native | +56 / 1921 | All Platforms | [Auto-generated summary] | Added vlan; new enum values added |
| 15 | [Cisco-IOS-XE-icmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-icmp.yang) | Icmp | Native | +5 / 23 | All Platforms | [Auto-generated summary] | Added time; deprecated 1 node |
| 16 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-igmp.yang) | Igmp | Native | +30 / 155 | All Platforms | [Auto-generated summary] | Added source; new enum values added |
| 17 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | Added FiveGigabitEthernet, TwentyFiveGigabitEthernet |
| 18 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 65 new data nodes; new enum values added; deprecated 35 nodes |
| 19 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; deprecated 2 nodes |
| 20 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added 7 new data nodes; deprecated 2 nodes |
| 21 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-isis.yang) | Isis | Native | +339 / 3977 | All Platforms | [Auto-generated summary] | Added bfd, disable |
| 22 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +89 / 698 | All Platforms | [Auto-generated summary] | Added mtu |
| 23 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | [Auto-generated summary] | Added ax, security |
| 24 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added session-limit |
| 25 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +28 / 14721 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 26 | [Cisco-IOS-XE-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-lldp.yang) | Lldp | Native | +6 / 20 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 27 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | Added severity |
| 28 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-mdt-common-defs.yang) | Mdt Common Defs | Native | 0 | All Platforms | [Auto-generated summary] | Added source-vrf, source-address, tdl-uri; new enum values added |
| 29 | [Cisco-IOS-XE-mka.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-mka.yang) | Mka | Native | +19 / 36 | All Platforms | [Auto-generated summary] | Added confidentiality-offset, policy, name; new enum values added |
| 30 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-mpls.yang) | Mpls | Native | 0 | ASR, ISR, NCS | [Auto-generated summary] | Added 7 new data nodes; deprecated 5 nodes |
| 31 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +46 / 465 | All Platforms | [Auto-generated summary] | Added pim-mode; new enum values added; deprecated 1 node |
| 32 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-nat.yang) | Nat | Native | +30 / 389 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 33 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-native.yang) | Native | Native | +4387 / 18975 | All Platforms | [Auto-generated summary] | Added 80 new data nodes; new enum values added; enhanced validation constraints |
| 34 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +288 / 353 | All Platforms | [Auto-generated summary] | Added 147 new data nodes; imported ietf-inet-types |
| 35 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-nd.yang) | Nd | Native | +18 / 137 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 36 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-object-group.yang) | Object Group | Native | +1 / 75 | All Platforms | [Auto-generated summary] | Added host, ipv4-host; deprecated 1 node |
| 37 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +331 / 2218 | All Platforms | [Auto-generated summary] | Added enforce, global, restart-interval |
| 38 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | +620 / 5787 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 39 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 40 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-platform.yang) | Platform | Native | 91 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 41 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-policy.yang) | Policy | Native | -149 / 2052 | All Platforms | [Auto-generated summary] | Added 35 new data nodes; new enum values added; deprecated 125 nodes |
| 42 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-power.yang) | Power | Native | +34 / 94 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 43 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-rip.yang) | Rip | Native | +12 / 1287 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 44 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +9 / 461 | All Platforms | [Auto-generated summary] | Added track |
| 45 | [Cisco-IOS-XE-rsvp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-rsvp.yang) | Rsvp | Native | +86 / 410 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 46 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-sanet.yang) | Sanet | Native | +98 / 319 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 47 | [Cisco-IOS-XE-service-insertion.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-service-insertion.yang) | Service Insertion | Native | 28 | All Platforms | [Auto-generated summary] | Minor refinements |
| 48 | [Cisco-IOS-XE-service-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-service-routing.yang) | Service Routing | Native | +3 / 6 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added; deprecated 1 node |
| 49 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-sla.yang) | Sla | Native | 171 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 50 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +38 / 891 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 51 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | +120 / 285 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; deprecated 7 nodes |
| 52 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | +12 / 694 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; deprecated 1 node |
| 53 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-umbrella.yang) | Umbrella | Native | +39 / 53 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 54 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-utd.yang) | Utd | Native | +26 / 163 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 55 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-vlan.yang) | Vlan | Native | +20 / 609 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |
| 56 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-vservice.yang) | Vservice | Native | +2 / 34 | All Platforms | [Auto-generated summary] | Added FiveGigabitEthernet, TwentyFiveGigabitEthernet |
| 57 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/Cisco-IOS-XE-zone.yang) | Zone | Native | +14 / 40 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED OpenConfig Models (4 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-openconfig-if-ethernet-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/cisco-xe-openconfig-if-ethernet-ext.yang) | Cisco Xe Openconfig If Ethernet Ext | OpenConfig | 1 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [openconfig-if-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/openconfig-if-ethernet.yang) | Openconfig If Ethernet | OpenConfig | 28 | All Platforms | [Auto-generated summary] | Minor refinements |
| 3 | [openconfig-network-instance.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/openconfig-network-instance.yang) | Openconfig Network Instance | OpenConfig | 217 | All Platforms | [Auto-generated summary] | Minor refinements |
| 4 | [openconfig-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/openconfig-vlan.yang) | Openconfig Vlan | OpenConfig | 51 | Cat9K, IE3x00 | [Auto-generated summary] | imported iana-if-type |

---

## UPDATED IETF Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [ietf-event-notifications.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/ietf-event-notifications.yang) | Ietf Event Notifications | IETF | +5 / 160 | All Platforms | [Auto-generated summary] | Added identifier, subscription-result |

---

## UPDATED Vendor Models (4 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | +3 / 555 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added; deprecated 4 nodes |
| 2 | [tailf-cli-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/tailf-cli-extensions.yang) | Tailf Cli Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | Added values |
| 3 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/tailf-common.yang) | Tailf Common | Vendor | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [tailf-meta-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1671/tailf-meta-extensions.yang) | Tailf Meta Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
