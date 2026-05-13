# All YANG Model Changes: v17.15.1 → v17.16.1
**Summary: 21 New Models & 98 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (21 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Operational Models](#new-operational-models)** | 3 | 254 XPaths |
| **[NEW RPC Models](#new-rpc-models)** | 2 | 9 XPaths |
| **[NEW Events Models](#new-events-models)** | 4 | 58 XPaths |
| **[NEW Types Models](#new-types-models)** | 1 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 8 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 3 | 23 XPaths |
| **TOTAL NEW MODELS** | **21** | **344 total XPaths** |

---

## UPDATED Models Summary (98 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 9 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 15 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 2 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 8 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 2 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 59 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 2 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 1 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **98** | **See individual models** |

---

## Key Highlights - NEW Models


**21 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-qfp-dp-cmn-stats-oper.yang`: 155 XPaths (Operational)

  - `Cisco-IOS-XE-service-chain-oper.yang`: 90 XPaths (Operational)

  - `Cisco-IOS-XE-crypto-events.yang`: 35 XPaths (Events)


- **Breakdown by category:**

  - Deviation: 8 models

  - Events: 4 models

  - Native: 3 models

  - Operational: 3 models

  - RPC: 2 models

  - Types: 1 model


---


## Key Highlights - UPDATED Models


**98 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-native.yang`: +1,429 XPaths (now 114,982 total)

  - `Cisco-IOS-XE-nd.yang`: +881 XPaths (now 3,365 total)

  - `Cisco-IOS-XE-ospf.yang`: +516 XPaths (now 6,801 total)


- **Significant removals:**

  - `Cisco-IOS-XE-ethernet.yang`: -16 XPaths (now 12,779 total)

  - `cisco-ia.yang`: -1 XPaths (now 76 total)


- **Updates by category:**

  - Native: 59 models

  - Operational: 15 models

  - Configuration: 9 models

  - Types: 8 models

  - Deviation: 2 models

  - RPC: 2 models

  - Vendor: 2 models

  - Other: 1 model


---


## Summary Statistics

### Release v17.16.1 Totals:
- **Total YANG Files:** ~519 files
- **New Files:** 21 models
- **Modified Files:** 98 models
- **Deleted Files:** 1 models
- **New Model XPaths:** 344 XPaths across 21 new models

---

# NEW YANG Models in v17.16.1

**21 Brand New Models**

---

## NEW Operational Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-line-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-line-oper.yang) | Line Oper | Operational | 9 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-qfp-dp-cmn-stats-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-qfp-dp-cmn-stats-oper.yang) | Qfp Dp Cmn Stats Oper | Operational | 155 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-service-chain-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-service-chain-oper.yang) | Service Chain Oper | Operational | 90 | All Platforms | New model introduced in this release |

---

## NEW RPC Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-line-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-line-actions-rpc.yang) | Line Actions Rpc | RPC | 3 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-power-supply-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-power-supply-rpc.yang) | Power Supply Rpc | RPC | 6 | All Platforms | New model introduced in this release |

---

## NEW Events Models (4 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-crypto-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-crypto-events.yang) | Crypto Events | Events | 35 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-interface-bw-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-interface-bw-events.yang) | Interface Bw Events | Events | 9 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-line-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-line-events.yang) | Line Events | Events | 6 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-qfp-resource-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-qfp-resource-events.yang) | Qfp Resource Events | Events | 8 | All Platforms | New model introduced in this release |

---

## NEW Types Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-sdwan-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-sdwan-types.yang) | Sdwan Types | Types | 0 | ASR, ISR, C8000 | New model introduced in this release |

---

## NEW Deviation Models (8 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-aaa-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-aaa-deviation.yang) | Aaa Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-ethernet-mcp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ethernet-mcp-deviation.yang) | Ethernet Mcp Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-flow-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-flow-deviation.yang) | Flow Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-interfaces-wlc-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-interfaces-wlc-deviation.yang) | Interfaces Wlc Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-policy-vxe-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-policy-vxe-deviation.yang) | Policy Vxe Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-snmp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-snmp-deviation.yang) | Snmp Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-vlan-ewlc-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-vlan-ewlc-deviation.yang) | Vlan Ewlc Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 8 | [Cisco-IOS-XE-vlan-vxe-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-vlan-vxe-deviation.yang) | Vlan Vxe Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |

---

## NEW Native Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-banner-internal.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-banner-internal.yang) | Banner Internal | Native | 6 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-kron.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-kron.yang) | Kron | Native | 17 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-transport.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-transport.yang) | Transport | Native | 0 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v17.15.1 → v17.16.1

**98 Models Modified**

---

## UPDATED Configuration Models (9 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-wireless-ap-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-ap-cfg.yang) | Wireless Ap Cfg | Configuration | 45 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [Cisco-IOS-XE-wireless-dot11-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-dot11-cfg.yang) | Wireless Dot11 Cfg | Configuration | 175 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 3 | [Cisco-IOS-XE-wireless-mstream-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-mstream-cfg.yang) | Wireless Mstream Cfg | Configuration | 20 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-wireless-radio-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-radio-cfg.yang) | Wireless Radio Cfg | Configuration | 50 | Wireless Controllers | [Auto-generated summary] | Added num-ant-enabled"; |
| 5 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless Rf Cfg | Configuration | 211 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless Site Cfg | Configuration | +7 / 389 | Wireless Controllers | [Auto-generated summary] | Added spaces-conn-cfg, rlan-cfg, onboard-cfg |
| 7 | [Cisco-IOS-XE-wireless-tunnel-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-tunnel-cfg.yang) | Wireless Tunnel Cfg | Configuration | 42 | Wireless Controllers | [Auto-generated summary] | Added to |
| 8 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | +1 / 382 | Wireless Controllers | [Auto-generated summary] | Added multicast-foreign-fw; enhanced validation constraints |
| 9 | [Cisco-IOS-XE-yang-interfaces-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-yang-interfaces-cfg.yang) | Yang Interfaces Cfg | Configuration | +1 / 52 | All Platforms | [Auto-generated summary] | Added tp-name |

---

## UPDATED Operational Models (15 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cellwan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-cellwan-oper.yang) | Cellwan Oper | Operational | +2 / 114 | IR1101, C1100 | [Auto-generated summary] | Added link-uptime, profile-apn |
| 2 | [Cisco-IOS-XE-device-hardware-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-device-hardware-oper.yang) | Device Hardware Oper | Operational | +5 / 62 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 3 | [Cisco-IOS-XE-dhcp-security-track-server-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-dhcp-security-track-server-oper.yang) | Dhcp Security Track Server Oper | Operational | +1 / 17 | All Platforms | [Auto-generated summary] | Added relay-agent-ip |
| 4 | [Cisco-IOS-XE-ha-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ha-oper.yang) | Ha Oper | Operational | +2 / 12 | All Platforms | [Auto-generated summary] | Added switchover-count, standby-failure-count |
| 5 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces Oper | Operational | +2 / 505 | All Platforms | [Auto-generated summary] | Added bw-up-util, bw-down-util |
| 6 | [Cisco-IOS-XE-meraki-connect-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-meraki-connect-oper.yang) | Meraki Connect Oper | Operational | +3 / 98 | All Platforms | [Auto-generated summary] | Added dwnld-run-cfg-http-status, get-presign-http-status, upload-cfg-http-status; new enum values added |
| 7 | [Cisco-IOS-XE-nwpi-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-nwpi-oper.yang) | Nwpi Oper | Operational | +40 / 1192 | All Platforms | [Auto-generated summary] | Added pcap-replay |
| 8 | [Cisco-IOS-XE-perf-measure-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-perf-measure-oper.yang) | Perf Measure Oper | Operational | +6 / 357 | All Platforms | [Auto-generated summary] | Added sid |
| 9 | [Cisco-IOS-XE-pim-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-pim-oper.yang) | Pim Oper | Operational | +12 / 51 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; imported Cisco-IOS-XE-common-types |
| 10 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | +1 / 217 | All Platforms | [Auto-generated summary] | Added ps-c |
| 11 | [Cisco-IOS-XE-spanning-tree-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-spanning-tree-oper.yang) | Spanning Tree Oper | Operational | +1 / 55 | All Platforms | [Auto-generated summary] | Added root-if-name, root-if-name |
| 12 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | +2 / 1484 | Wireless Controllers | [Auto-generated summary] | Added disc-meraki-pkts, disc-meraki-l2-pkts; new enum values added |
| 13 | [Cisco-IOS-XE-wireless-ap-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-ap-global-oper.yang) | Wireless Ap Global Oper | Operational | 188 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 14 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | +3 / 366 | Wireless Controllers | [Auto-generated summary] | Added band-id, multi-link-capable |
| 15 | [Cisco-IOS-XE-yang-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-yang-interfaces-oper.yang) | Yang Interfaces Oper | Operational | +1 / 27 | All Platforms | [Auto-generated summary] | Added tp-name |

---

## UPDATED RPC Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-nwpi-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-nwpi-rpc.yang) | Nwpi Rpc | RPC | +41 / 123 | All Platforms | [Auto-generated summary] | Added pcap-replay |
| 2 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +185 / 1948 | All Platforms | [Auto-generated summary] | Added 101 new data nodes |

---

## UPDATED Types Models (8 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-aaa-types.yang) | Aaa Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 2 | [Cisco-IOS-XE-install-event-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-install-event-types.yang) | Install Event Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 3 | [Cisco-IOS-XE-nwpi-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-nwpi-types.yang) | Nwpi Types | Types | 0 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; new enum values added |
| 4 | [Cisco-IOS-XE-tunnel-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-tunnel-types.yang) | Tunnel Types | Types | 0 | All Platforms | [Auto-generated summary] | Added to; enhanced validation constraints |
| 5 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; new enum values added; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-wireless-client-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-client-types.yang) | Wireless Client Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-wireless-tunnel-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-tunnel-types.yang) | Wireless Tunnel Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | enhanced validation constraints |
| 8 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |

---

## UPDATED Deviation Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-cef-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-cef-deviation.yang) | Cef Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [Cisco-IOS-XE-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-interfaces-deviation.yang) | Interfaces Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Native Models (59 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +28 / 3327 | All Platforms | [Auto-generated summary] | Added 28 new data nodes; new enum values added; enhanced validation constraints |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-acl.yang) | Acl | Native | 1737 | All Platforms | [Auto-generated summary] | Added 'id', mac; deprecated 1 node |
| 3 | [Cisco-IOS-XE-atm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-atm.yang) | Atm | Native | 1482 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-bfd.yang) | Bfd | Native | +11 / 417 | All Platforms | [Auto-generated summary] | Added deprecated |
| 5 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-bgp.yang) | Bgp | Native | +260 / 26419 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; new enum values added; enhanced validation constraints |
| 6 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-bridge-domain.yang) | Bridge Domain | Native | +2 / 331 | All Platforms | [Auto-generated summary] | Added ethernet-tag-vxlan; enhanced validation constraints |
| 7 | [Cisco-IOS-XE-call-home.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-call-home.yang) | Call Home | Native | 241 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 8 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-cdp.yang) | Cdp | Native | 281 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 9 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-cef.yang) | Cef | Native | 227 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-controller.yang) | Controller | Native | +9 / 623 | All Platforms | [Auto-generated summary] | Added 10 new data nodes; new enum values added |
| 11 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-crypto.yang) | Crypto | Native | +136 / 6677 | All Platforms | [Auto-generated summary] | Added 40 new data nodes; new enum values added; deprecated 7 nodes |
| 12 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-cts.yang) | Cts | Native | +43 / 660 | All Platforms | [Auto-generated summary] | Added vlanid, id, sgt; enhanced validation constraints |
| 13 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +3 / 7588 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 14 | [Cisco-IOS-XE-digitalio.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-digitalio.yang) | Digitalio | Native | 23 | All Platforms | [Auto-generated summary] | Added enable; deprecated 1 node |
| 15 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-eem.yang) | Eem | Native | +1 / 458 | All Platforms | [Auto-generated summary] | Added pattern |
| 16 | [Cisco-IOS-XE-ethernet-cfm-efp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ethernet-cfm-efp.yang) | Ethernet Cfm Efp | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 17 | [Cisco-IOS-XE-ethernet-oam.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ethernet-oam.yang) | Ethernet Oam | Native | 0 | All Platforms | [Auto-generated summary] | Added dying-gasp, dying-gasp, type; new enum values added |
| 18 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | -16 / 12779 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 19 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | 306 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 20 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 21 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-flow.yang) | Flow | Native | +16 / 3068 | All Platforms | [Auto-generated summary] | Added 9 new data nodes |
| 22 | [Cisco-IOS-XE-hsrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-hsrp.yang) | Hsrp | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 23 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-http.yang) | Http | Native | +5 / 94 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 24 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-igmp.yang) | Igmp | Native | 5210 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 25 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | Added 100 new data nodes |
| 26 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 155 new data nodes; new enum values added; enhanced validation constraints |
| 27 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; new enum values added |
| 28 | [Cisco-IOS-XE-ipc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ipc.yang) | Ipc | Native | 11 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 29 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 30 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +93 / 2434 | All Platforms | [Auto-generated summary] | Added 29 new data nodes; new enum values added; enhanced validation constraints |
| 31 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added can, script, dialer |
| 32 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-lisp.yang) | Lisp | Native | 28912 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 33 | [Cisco-IOS-XE-mdns-gateway.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-mdns-gateway.yang) | Mdns Gateway | Native | 787 | All Platforms | [Auto-generated summary] | Added IN, OUT; new enum values added; enhanced validation constraints |
| 34 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-mpls.yang) | Mpls | Native | +43 / 1775 | ASR, ISR, NCS | [Auto-generated summary] | Added 7 new data nodes; deprecated 1 node |
| 35 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +2 / 4334 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; deprecated 4 nodes |
| 36 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-nat.yang) | Nat | Native | +155 / 4450 | All Platforms | [Auto-generated summary] | Added 26 new data nodes; enhanced validation constraints |
| 37 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-native.yang) | Native | Native | +1429 / 114982 | All Platforms | [Auto-generated summary] | Added 30 new data nodes; new enum values added; enhanced validation constraints |
| 38 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-nd.yang) | Nd | Native | +881 / 3365 | All Platforms | [Auto-generated summary] | Added 35 new data nodes; enhanced validation constraints |
| 39 | [Cisco-IOS-XE-nhrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-nhrp.yang) | Nhrp | Native | +8 / 9613 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 40 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ntp.yang) | Ntp | Native | 911 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 41 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +516 / 6801 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; enhanced validation constraints; deprecated 1 node |
| 42 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | [Auto-generated summary] | Added configuration; deprecated 1 node |
| 43 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-platform.yang) | Platform | Native | +4 / 175 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 44 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-policy.yang) | Policy | Native | +11 / 6753 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; enhanced validation constraints; deprecated 2 nodes |
| 45 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-power.yang) | Power | Native | +9 / 284 | All Platforms | [Auto-generated summary] | Added one-event |
| 46 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-ppp.yang) | Ppp | Native | +15 / 457 | All Platforms | [Auto-generated summary] | Added ipv6cp, address, unique |
| 47 | [Cisco-IOS-XE-prp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-prp.yang) | Prp | Native | +3 / 23 | All Platforms | [Auto-generated summary] | Added vlan-aware-enable, vlan-aware-reject-untagged, vlan-aware-allowed-vlan |
| 48 | [Cisco-IOS-XE-rawsocket.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-rawsocket.yang) | Rawsocket | Native | 65 | All Platforms | [Auto-generated summary] | Added for |
| 49 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +10 / 1206 | All Platforms | [Auto-generated summary] | Added 10 new data nodes |
| 50 | [Cisco-IOS-XE-service-insertion.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-service-insertion.yang) | Service Insertion | Native | 264 | All Platforms | [Auto-generated summary] | Added cluster-type, cluster-type; new enum values added; enhanced validation constraints |
| 51 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-sla.yang) | Sla | Native | +1 / 2725 | All Platforms | [Auto-generated summary] | Added num-packets |
| 52 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +1 / 1768 | All Platforms | [Auto-generated summary] | Added and, and, expression; new enum values added; deprecated 2 nodes |
| 53 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-template.yang) | Template | Native | +48 / 2892 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; enhanced validation constraints |
| 54 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | 1642 | All Platforms | [Auto-generated summary] | enhanced validation constraints |
| 55 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-utd.yang) | Utd | Native | +18 / 629 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added; deprecated 1 node |
| 56 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-vlan.yang) | Vlan | Native | +4 / 158 | Cat9K, IE3x00 | [Auto-generated summary] | Added 4 new data nodes; new enum values added; enhanced validation constraints |
| 57 | [Cisco-IOS-XE-voice-class.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-voice-class.yang) | Voice Class | Native | 0 | ISR, Voice Gateways | [Auto-generated summary] | Added 4 new data nodes |
| 58 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-voice.yang) | Voice | Native | +10 / 3122 | ISR, Voice Gateways | [Auto-generated summary] | Added 9 new data nodes; new enum values added; enhanced validation constraints |
| 59 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/Cisco-IOS-XE-vrrp.yang) | Vrrp | Native | 1664 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Vendor Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [tailf-cli-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/tailf-cli-extensions.yang) | Tailf Cli Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | Added has, that |
| 2 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/tailf-common.yang) | Tailf Common | Vendor | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |

---

## UPDATED Other Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-ia.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/17161/cisco-ia.yang) | Cisco Ia | Other | -1 / 76 | All Platforms | [Auto-generated summary] | Added full-sync-cli"; |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
