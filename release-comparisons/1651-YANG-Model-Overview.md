# All YANG Model Changes: v16.4.1 → v16.5.1
**Summary: 126 New Models & 9 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (126 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 18 | 579 XPaths |
| **[NEW RPC Models](#new-rpc-models)** | 1 | 38 XPaths |
| **[NEW Types Models](#new-types-models)** | 4 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 1 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 90 | 71,418 XPaths |
| **[NEW IETF Models](#new-ietf-models)** | 8 | 333 XPaths |
| **[NEW Vendor Models](#new-vendor-models)** | 2 | 586 XPaths |
| **[NEW Other Models](#new-other-models)** | 2 | 0 XPaths |
| **TOTAL NEW MODELS** | **126** | **72,954 total XPaths** |

---

## UPDATED Models Summary (9 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED IETF Models](#updated-ietf-models)** | 1 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 2 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 6 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **9** | **See individual models** |

---

## Key Highlights - NEW Models


**126 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-lisp.yang`: 14,677 XPaths (Native)

  - `Cisco-IOS-XE-native.yang`: 14,536 XPaths (Native)

  - `Cisco-IOS-XE-bgp.yang`: 5,298 XPaths (Native)


- **Breakdown by category:**

  - Native: 90 models

  - Operational: 18 models

  - IETF: 8 models

  - Types: 4 models

  - Vendor: 2 models

  - Other: 2 models

  - RPC: 1 model

  - Deviation: 1 model


---


## Key Highlights - UPDATED Models


**9 models updated** in this release:


- **Significant additions:**

  - `ietf-ospf.yang`: +822 XPaths (now 822 total)

  - `cisco-bridge-domain.yang`: +252 XPaths (now 252 total)

  - `cisco-pw.yang`: +165 XPaths (now 165 total)


- **Updates by category:**

  - Other: 6 models

  - Vendor: 2 models

  - IETF: 1 model


---


## Summary Statistics

### Release v16.5.1 Totals:
- **Total YANG Files:** ~535 files
- **New Files:** 126 models
- **Modified Files:** 9 models
- **Deleted Files:** 30 models
- **New Model XPaths:** 72,954 XPaths across 126 new models

---

# NEW YANG Models in v16.5.1

**126 Brand New Models**

---

## NEW Operational Models (18 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-acl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-acl-oper.yang) | Acl Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-bfd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-bfd-oper.yang) | Bfd Oper | Operational | 43 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-bgp-oper.yang) | Bgp Oper | Operational | 101 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-cfm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-cfm-oper.yang) | Cfm Oper | Operational | 19 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-checkpoint-archive-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-checkpoint-archive-oper.yang) | Checkpoint Archive Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-diffserv-target-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-diffserv-target-oper.yang) | Diffserv Target Oper | Operational | 29 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-efp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-efp-oper.yang) | Efp Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-environment-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-environment-oper.yang) | Environment Oper | Operational | 7 | All Platforms | New model introduced in this release |
| 9 | [Cisco-IOS-XE-flow-monitor-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-flow-monitor-oper.yang) | Flow Monitor Oper | Operational | 18 | All Platforms | New model introduced in this release |
| 10 | [Cisco-IOS-XE-ip-sla-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ip-sla-oper.yang) | Ip Sla Oper | Operational | 101 | All Platforms | New model introduced in this release |
| 11 | [Cisco-IOS-XE-lldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-lldp-oper.yang) | Lldp Oper | Operational | 15 | All Platforms | New model introduced in this release |
| 12 | [Cisco-IOS-XE-memory-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-memory-oper.yang) | Memory Oper | Operational | 8 | All Platforms | New model introduced in this release |
| 13 | [Cisco-IOS-XE-mpls-fwd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-mpls-fwd-oper.yang) | Mpls Fwd Oper | Operational | 24 | ASR, ISR, NCS | New model introduced in this release |
| 14 | [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-platform-software-oper.yang) | Platform Software Oper | Operational | 48 | All Platforms | New model introduced in this release |
| 15 | [Cisco-IOS-XE-process-cpu-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-process-cpu-oper.yang) | Process Cpu Oper | Operational | 17 | All Platforms | New model introduced in this release |
| 16 | [Cisco-IOS-XE-process-memory-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-process-memory-oper.yang) | Process Memory Oper | Operational | 10 | All Platforms | New model introduced in this release |
| 17 | [Cisco-IOS-XE-trustsec-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-trustsec-oper.yang) | Trustsec Oper | Operational | 34 | All Platforms | New model introduced in this release |
| 18 | [Cisco-IOS-XE-virtual-service-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-virtual-service-oper.yang) | Virtual Service Oper | Operational | 81 | All Platforms | New model introduced in this release |

---

## NEW RPC Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | 38 | All Platforms | New model introduced in this release |

---

## NEW Types Models (4 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [ietf-inet-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-inet-types.yang) | Ietf Inet Types | Types | 0 | All Platforms | New model introduced in this release |
| 3 | [ietf-yang-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-yang-types.yang) | Ietf Yang Types | Types | 0 | All Platforms | New model introduced in this release |
| 4 | [tailf-xsd-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/tailf-xsd-types.yang) | Tailf Xsd Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Deviation Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-switch-deviation.yang) | Switch Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |

---

## NEW Native Models (90 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-aaa.yang) | Aaa | Native | 754 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-acl.yang) | Acl | Native | 846 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-ap.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ap.yang) | Ap | Native | 103 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-atm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-atm.yang) | Atm | Native | 618 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-bba-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-bba-group.yang) | Bba Group | Native | 12 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-bfd.yang) | Bfd | Native | 70 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-bgp.yang) | Bgp | Native | 5298 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-bridge-domain.yang) | Bridge Domain | Native | 151 | All Platforms | New model introduced in this release |
| 9 | [Cisco-IOS-XE-call-home.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-call-home.yang) | Call Home | Native | 118 | All Platforms | New model introduced in this release |
| 10 | [Cisco-IOS-XE-card.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-card.yang) | Card | Native | 4 | All Platforms | New model introduced in this release |
| 11 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-cdp.yang) | Cdp | Native | 41 | All Platforms | New model introduced in this release |
| 12 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-cef.yang) | Cef | Native | 23 | All Platforms | New model introduced in this release |
| 13 | [Cisco-IOS-XE-coap.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-coap.yang) | Coap | Native | 3 | All Platforms | New model introduced in this release |
| 14 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-controller.yang) | Controller | Native | 183 | All Platforms | New model introduced in this release |
| 15 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-crypto.yang) | Crypto | Native | 2132 | All Platforms | New model introduced in this release |
| 16 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-cts.yang) | Cts | Native | 305 | All Platforms | New model introduced in this release |
| 17 | [Cisco-IOS-XE-device-sensor.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-device-sensor.yang) | Device Sensor | Native | 2 | All Platforms | New model introduced in this release |
| 18 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | 31 | All Platforms | New model introduced in this release |
| 19 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | 348 | All Platforms | New model introduced in this release |
| 20 | [Cisco-IOS-XE-diagnostics.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-diagnostics.yang) | Diagnostics | Native | 316 | All Platforms | New model introduced in this release |
| 21 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | 109 | All Platforms | New model introduced in this release |
| 22 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-eem.yang) | Eem | Native | 80 | All Platforms | New model introduced in this release |
| 23 | [Cisco-IOS-XE-eigrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-eigrp.yang) | Eigrp | Native | 979 | All Platforms | New model introduced in this release |
| 24 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | 2145 | All Platforms | New model introduced in this release |
| 25 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | 136 | All Platforms | New model introduced in this release |
| 26 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | New model introduced in this release |
| 27 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-flow.yang) | Flow | Native | 1865 | All Platforms | New model introduced in this release |
| 28 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-http.yang) | Http | Native | 22 | All Platforms | New model introduced in this release |
| 29 | [Cisco-IOS-XE-icmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-icmp.yang) | Icmp | Native | 17 | All Platforms | New model introduced in this release |
| 30 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-igmp.yang) | Igmp | Native | 125 | All Platforms | New model introduced in this release |
| 31 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | New model introduced in this release |
| 32 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | New model introduced in this release |
| 33 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | New model introduced in this release |
| 34 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | New model introduced in this release |
| 35 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-isis.yang) | Isis | Native | 3638 | All Platforms | New model introduced in this release |
| 36 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | 609 | All Platforms | New model introduced in this release |
| 37 | [Cisco-IOS-XE-l3vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-l3vpn.yang) | L3Vpn | Native | 11 | All Platforms | New model introduced in this release |
| 38 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | New model introduced in this release |
| 39 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | New model introduced in this release |
| 40 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-lisp.yang) | Lisp | Native | 14677 | All Platforms | New model introduced in this release |
| 41 | [Cisco-IOS-XE-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-lldp.yang) | Lldp | Native | 2 | All Platforms | New model introduced in this release |
| 42 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | New model introduced in this release |
| 43 | [Cisco-IOS-XE-mka.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-mka.yang) | Mka | Native | 17 | All Platforms | New model introduced in this release |
| 44 | [Cisco-IOS-XE-mld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-mld.yang) | Mld | Native | 8 | All Platforms | New model introduced in this release |
| 45 | [Cisco-IOS-XE-mpls-ldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-mpls-ldp.yang) | Mpls Ldp | Native | 723 | ASR, ISR, NCS | New model introduced in this release |
| 46 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-mpls.yang) | Mpls | Native | 821 | ASR, ISR, NCS | New model introduced in this release |
| 47 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-multicast.yang) | Multicast | Native | 383 | All Platforms | New model introduced in this release |
| 48 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-nat.yang) | Nat | Native | 336 | All Platforms | New model introduced in this release |
| 49 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-native.yang) | Native | Native | 14536 | All Platforms | New model introduced in this release |
| 50 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-nbar.yang) | Nbar | Native | 65 | All Platforms | New model introduced in this release |
| 51 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-nd.yang) | Nd | Native | 114 | All Platforms | New model introduced in this release |
| 52 | [Cisco-IOS-XE-nhrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-nhrp.yang) | Nhrp | Native | 170 | All Platforms | New model introduced in this release |
| 53 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ntp.yang) | Ntp | Native | 259 | All Platforms | New model introduced in this release |
| 54 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-object-group.yang) | Object Group | Native | 74 | All Platforms | New model introduced in this release |
| 55 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ospf.yang) | Ospf | Native | 1819 | All Platforms | New model introduced in this release |
| 56 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | 5167 | All Platforms | New model introduced in this release |
| 57 | [Cisco-IOS-XE-otv.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-otv.yang) | Otv | Native | 1032 | All Platforms | New model introduced in this release |
| 58 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | New model introduced in this release |
| 59 | [Cisco-IOS-XE-pathmgr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-pathmgr.yang) | Pathmgr | Native | 59 | All Platforms | New model introduced in this release |
| 60 | [Cisco-IOS-XE-pfr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-pfr.yang) | Pfr | Native | 410 | All Platforms | New model introduced in this release |
| 61 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-platform.yang) | Platform | Native | 91 | All Platforms | New model introduced in this release |
| 62 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-policy.yang) | Policy | Native | 2186 | All Platforms | New model introduced in this release |
| 63 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-power.yang) | Power | Native | 60 | All Platforms | New model introduced in this release |
| 64 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-ppp.yang) | Ppp | Native | 111 | All Platforms | New model introduced in this release |
| 65 | [Cisco-IOS-XE-qos.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-qos.yang) | Qos | Native | 36 | All Platforms | New model introduced in this release |
| 66 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-rip.yang) | Rip | Native | 1095 | All Platforms | New model introduced in this release |
| 67 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-route-map.yang) | Route Map | Native | 451 | All Platforms | New model introduced in this release |
| 68 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-sanet.yang) | Sanet | Native | 221 | All Platforms | New model introduced in this release |
| 69 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | 59 | All Platforms | New model introduced in this release |
| 70 | [Cisco-IOS-XE-service-chain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-service-chain.yang) | Service Chain | Native | 37 | All Platforms | New model introduced in this release |
| 71 | [Cisco-IOS-XE-service-discovery.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-service-discovery.yang) | Service Discovery | Native | 29 | All Platforms | New model introduced in this release |
| 72 | [Cisco-IOS-XE-service-insertion.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-service-insertion.yang) | Service Insertion | Native | 28 | All Platforms | New model introduced in this release |
| 73 | [Cisco-IOS-XE-service-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-service-routing.yang) | Service Routing | Native | 2 | All Platforms | New model introduced in this release |
| 74 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-sla.yang) | Sla | Native | 171 | All Platforms | New model introduced in this release |
| 75 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-snmp.yang) | Snmp | Native | 853 | All Platforms | New model introduced in this release |
| 76 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | 165 | All Platforms | New model introduced in this release |
| 77 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-switch.yang) | Switch | Native | 2595 | Cat9K, IE3x00 | New model introduced in this release |
| 78 | [Cisco-IOS-XE-track.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-track.yang) | Track | Native | 72 | All Platforms | New model introduced in this release |
| 79 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | 332 | All Platforms | New model introduced in this release |
| 80 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-udld.yang) | Udld | Native | 41 | All Platforms | New model introduced in this release |
| 81 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-utd.yang) | Utd | Native | 53 | All Platforms | New model introduced in this release |
| 82 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-vlan.yang) | Vlan | Native | 576 | Cat9K, IE3x00 | New model introduced in this release |
| 83 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-voice.yang) | Voice | Native | 12 | ISR, Voice Gateways | New model introduced in this release |
| 84 | [Cisco-IOS-XE-vpdn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-vpdn.yang) | Vpdn | Native | 4 | All Platforms | New model introduced in this release |
| 85 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-vservice.yang) | Vservice | Native | 31 | All Platforms | New model introduced in this release |
| 86 | [Cisco-IOS-XE-vstack.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-vstack.yang) | Vstack | Native | 2 | All Platforms | New model introduced in this release |
| 87 | [Cisco-IOS-XE-vtp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-vtp.yang) | Vtp | Native | 28 | All Platforms | New model introduced in this release |
| 88 | [Cisco-IOS-XE-wccp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-wccp.yang) | Wccp | Native | 272 | All Platforms | New model introduced in this release |
| 89 | [Cisco-IOS-XE-wsma.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-wsma.yang) | Wsma | Native | 13 | All Platforms | New model introduced in this release |
| 90 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/Cisco-IOS-XE-zone.yang) | Zone | Native | 26 | All Platforms | New model introduced in this release |

---

## NEW IETF Models (8 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [ietf-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-interfaces.yang) | Ietf Interfaces | IETF | 34 | All Platforms | New model introduced in this release |
| 2 | [ietf-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-ip.yang) | Ietf Ip | IETF | 59 | All Platforms | New model introduced in this release |
| 3 | [ietf-netconf-acm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-netconf-acm.yang) | Ietf Netconf Acm | IETF | 29 | All Platforms | New model introduced in this release |
| 4 | [ietf-netconf-monitoring.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-netconf-monitoring.yang) | Ietf Netconf Monitoring | IETF | 53 | All Platforms | New model introduced in this release |
| 5 | [ietf-netconf-notifications.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-netconf-notifications.yang) | Ietf Netconf Notifications | IETF | 41 | All Platforms | New model introduced in this release |
| 6 | [ietf-netconf-with-defaults.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-netconf-with-defaults.yang) | Ietf Netconf With Defaults | IETF | 3 | All Platforms | New model introduced in this release |
| 7 | [ietf-netconf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-netconf.yang) | Ietf Netconf | IETF | 114 | All Platforms | New model introduced in this release |
| 8 | [ietf-yang-smiv2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-yang-smiv2.yang) | Ietf Yang Smiv2 | IETF | 0 | All Platforms | New model introduced in this release |

---

## NEW Vendor Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | 533 | All Platforms | New model introduced in this release |
| 2 | [tailf-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/tailf-aaa.yang) | Tailf Aaa | Vendor | 53 | All Platforms | New model introduced in this release |

---

## NEW Other Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [iana-crypt-hash.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/iana-crypt-hash.yang) | Iana Crypt Hash | Other | 0 | All Platforms | New model introduced in this release |
| 2 | [iana-if-type.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/iana-if-type.yang) | Iana If Type | Other | 0 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.4.1 → v16.5.1

**9 Models Modified**

---

## UPDATED IETF Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [ietf-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/ietf-ospf.yang) | Ietf Ospf | IETF | +822 / 822 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Vendor Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [tailf-cli-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/tailf-cli-extensions.yang) | Tailf Cli Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | Added should, of; new enum values added |
| 2 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/tailf-common.yang) | Tailf Common | Vendor | 0 | All Platforms | [Auto-generated summary] | new enum values added; enhanced validation constraints |

---

## UPDATED Other Models (6 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-bridge-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/cisco-bridge-common.yang) | Cisco Bridge Common | Other | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [cisco-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/cisco-bridge-domain.yang) | Cisco Bridge Domain | Other | +252 / 252 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [cisco-ia.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/cisco-ia.yang) | Cisco Ia | Other | +70 / 70 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; imported confd_dyncfg; new enum values added |
| 4 | [cisco-odm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/cisco-odm.yang) | Cisco Odm | Other | 7 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [cisco-pw.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/cisco-pw.yang) | Cisco Pw | Other | +165 / 165 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [cisco-storm-control.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1651/cisco-storm-control.yang) | Cisco Storm Control | Other | 0 | All Platforms | [Auto-generated summary] | imported tailf-common; new enum values added |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
