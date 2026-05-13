# All YANG Model Changes: v16.10.1 → v16.11.1
**Summary: 44 New Models & 189 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (44 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Configuration Models](#new-configuration-models)** | 3 | 106 XPaths |
| **[NEW Operational Models](#new-operational-models)** | 11 | 367 XPaths |
| **[NEW Types Models](#new-types-models)** | 2 | 0 XPaths |
| **[NEW Deviation Models](#new-deviation-models)** | 22 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 6 | 1,433 XPaths |
| **TOTAL NEW MODELS** | **44** | **1,906 total XPaths** |

---

## UPDATED Models Summary (189 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models)** | 21 | XPath changes vary |
| **[UPDATED Operational Models](#updated-operational-models)** | 57 | XPath changes vary |
| **[UPDATED RPC Models](#updated-rpc-models)** | 1 | XPath changes vary |
| **[UPDATED Types Models](#updated-types-models)** | 11 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 4 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 84 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 2 | XPath changes vary |
| **[UPDATED IETF Models](#updated-ietf-models)** | 2 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 4 | XPath changes vary |
| **[UPDATED Other Models](#updated-other-models)** | 3 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **189** | **See individual models** |

---

## Key Highlights - NEW Models


**44 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-qfp-stats.yang`: 979 XPaths (Native)

  - `Cisco-IOS-XE-site-manager.yang`: 265 XPaths (Native)

  - `Cisco-IOS-XE-dapr.yang`: 129 XPaths (Native)


- **Breakdown by category:**

  - Deviation: 22 models

  - Operational: 11 models

  - Native: 6 models

  - Configuration: 3 models

  - Types: 2 models


---


## Key Highlights - UPDATED Models


**189 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-igmp.yang`: +3,191 XPaths (now 3,401 total)

  - `Cisco-IOS-XE-native.yang`: +3,166 XPaths (now 26,461 total)

  - `Cisco-IOS-XE-dhcp.yang`: +2,023 XPaths (now 3,185 total)


- **Significant removals:**

  - `Cisco-IOS-XE-bgp.yang`: -12,671 XPaths (now 0 total)

  - `Cisco-IOS-XE-wireless-access-point-oper.yang`: -713 XPaths (now 256 total)

  - `Cisco-IOS-XE-wireless-client-oper.yang`: -647 XPaths (now 142 total)


- **Updates by category:**

  - Native: 84 models

  - Operational: 57 models

  - Configuration: 21 models

  - Types: 11 models

  - Deviation: 4 models

  - Vendor: 4 models

  - Other: 3 models

  - IETF: 2 models

  - OpenConfig: 2 models

  - RPC: 1 model


---


## Summary Statistics

### Release v16.11.1 Totals:
- **Total YANG Files:** ~633 files
- **New Files:** 44 models
- **Modified Files:** 189 models
- **Deleted Files:** 8 models
- **New Model XPaths:** 1,906 XPaths across 44 new models

---

# NEW YANG Models in v16.11.1

**44 Brand New Models**

---

## NEW Configuration Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-wireless-rlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rlan-cfg.yang) | Wireless Rlan Cfg | Configuration | 60 | Wireless Controllers | New model introduced in this release |
| 2 | [Cisco-IOS-XE-wireless-tunnel-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-tunnel-cfg.yang) | Wireless Tunnel Cfg | Configuration | 38 | Wireless Controllers | New model introduced in this release |
| 3 | [Cisco-IOS-XE-yang-interfaces-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-yang-interfaces-cfg.yang) | Yang Interfaces Cfg | Configuration | 8 | All Platforms | New model introduced in this release |

---

## NEW Operational Models (11 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-cable-diag-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-cable-diag-oper.yang) | Cable Diag Oper | Operational | 11 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-crypto-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-crypto-oper.yang) | Crypto Oper | Operational | 95 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-crypto-pki-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-crypto-pki-oper.yang) | Crypto Pki Oper | Operational | 4 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-eigrp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-eigrp-oper.yang) | Eigrp Oper | Operational | 94 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-stacking-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-stacking-oper.yang) | Stacking Oper | Operational | 16 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-tunnel-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-tunnel-oper.yang) | Tunnel Oper | Operational | 55 | All Platforms | New model introduced in this release |
| 7 | [Cisco-IOS-XE-umbrella-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-umbrella-oper.yang) | Umbrella Oper | Operational | 12 | All Platforms | New model introduced in this release |
| 8 | [Cisco-IOS-XE-vrf-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-vrf-oper.yang) | Vrf Oper | Operational | 6 | All Platforms | New model introduced in this release |
| 9 | [Cisco-IOS-XE-wireless-ble-mgmt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-ble-mgmt-oper.yang) | Wireless Ble Mgmt Oper | Operational | 16 | Wireless Controllers | New model introduced in this release |
| 10 | [Cisco-IOS-XE-wireless-general-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-general-oper.yang) | Wireless General Oper | Operational | 10 | Wireless Controllers | New model introduced in this release |
| 11 | [Cisco-IOS-XE-wireless-mdns-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mdns-oper.yang) | Wireless Mdns Oper | Operational | 48 | Wireless Controllers | New model introduced in this release |

---

## NEW Types Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-tunnel-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-tunnel-types.yang) | Tunnel Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-wireless-tunnel-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-tunnel-types.yang) | Wireless Tunnel Types | Types | 0 | Wireless Controllers | New model introduced in this release |

---

## NEW Deviation Models (22 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [cisco-xe-access-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-access-openconfig-if-ethernet-deviation.yang) | Cisco Xe Access Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 2 | [cisco-xe-access-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-access-openconfig-platform-deviation.yang) | Cisco Xe Access Openconfig Platform Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 3 | [cisco-xe-access-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-access-openconfig-system-deviation.yang) | Cisco Xe Access Openconfig System Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 4 | [cisco-xe-access-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-access-openconfig-vlan-deviation.yang) | Cisco Xe Access Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 5 | [cisco-xe-cbr-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-cbr-openconfig-if-ethernet-deviation.yang) | Cisco Xe Cbr Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 6 | [cisco-xe-cbr-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-cbr-openconfig-platform-deviation.yang) | Cisco Xe Cbr Openconfig Platform Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 7 | [cisco-xe-cbr-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-cbr-openconfig-system-deviation.yang) | Cisco Xe Cbr Openconfig System Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 8 | [cisco-xe-cbr-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-cbr-openconfig-vlan-deviation.yang) | Cisco Xe Cbr Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 9 | [cisco-xe-routing-asr-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-routing-asr-openconfig-if-ethernet-deviation.yang) | Cisco Xe Routing Asr Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 10 | [cisco-xe-routing-csr-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-routing-csr-openconfig-platform-deviation.yang) | Cisco Xe Routing Csr Openconfig Platform Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 11 | [cisco-xe-routing-isr-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-routing-isr-openconfig-if-ethernet-deviation.yang) | Cisco Xe Routing Isr Openconfig If Ethernet Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 12 | [cisco-xe-routing-isr-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-routing-isr-openconfig-platform-deviation.yang) | Cisco Xe Routing Isr Openconfig Platform Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 13 | [cisco-xe-routing-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-routing-openconfig-system-deviation.yang) | Cisco Xe Routing Openconfig System Deviation | Deviation | 0 | All Platforms | New model introduced in this release |
| 14 | [cisco-xe-routing-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-routing-openconfig-vlan-deviation.yang) | Cisco Xe Routing Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 15 | [cisco-xe-switching-cat9k-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-switching-cat9k-openconfig-system-deviation.yang) | Cisco Xe Switching Cat9K Openconfig System Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 16 | [cisco-xe-switching-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-switching-openconfig-if-ethernet-deviation.yang) | Cisco Xe Switching Openconfig If Ethernet Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 17 | [cisco-xe-switching-openconfig-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-switching-openconfig-interfaces-deviation.yang) | Cisco Xe Switching Openconfig Interfaces Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 18 | [cisco-xe-switching-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-switching-openconfig-platform-deviation.yang) | Cisco Xe Switching Openconfig Platform Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 19 | [cisco-xe-switching-openconfig-system-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-switching-openconfig-system-deviation.yang) | Cisco Xe Switching Openconfig System Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 20 | [cisco-xe-switching-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-switching-openconfig-vlan-deviation.yang) | Cisco Xe Switching Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | New model introduced in this release |
| 21 | [cisco-xe-wireless-openconfig-if-ethernet-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-wireless-openconfig-if-ethernet-deviation.yang) | Cisco Xe Wireless Openconfig If Ethernet Deviation | Deviation | 0 | Wireless Controllers | New model introduced in this release |
| 22 | [cisco-xe-wireless-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-wireless-openconfig-vlan-deviation.yang) | Cisco Xe Wireless Openconfig Vlan Deviation | Deviation | 0 | Wireless Controllers | New model introduced in this release |

---

## NEW Native Models (6 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-dapr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-dapr.yang) | Dapr | Native | 129 | All Platforms | New model introduced in this release |
| 2 | [Cisco-IOS-XE-mdns-gateway.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mdns-gateway.yang) | Mdns Gateway | Native | 27 | All Platforms | New model introduced in this release |
| 3 | [Cisco-IOS-XE-qfp-stats.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-qfp-stats.yang) | Qfp Stats | Native | 979 | All Platforms | New model introduced in this release |
| 4 | [Cisco-IOS-XE-site-manager.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-site-manager.yang) | Site Manager | Native | 265 | All Platforms | New model introduced in this release |
| 5 | [Cisco-IOS-XE-umbrella-oper-dp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-umbrella-oper-dp.yang) | Umbrella Oper Dp | Native | 31 | All Platforms | New model introduced in this release |
| 6 | [Cisco-IOS-XE-vxlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-vxlan.yang) | Vxlan | Native | 2 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.10.1 → v16.11.1

**189 Models Modified**

---

## UPDATED Configuration Models (21 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-app-hosting-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-app-hosting-cfg.yang) | App Hosting Cfg | Configuration | +10 / 63 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; new enum values added; enhanced validation constraints |
| 2 | [Cisco-IOS-XE-mdt-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mdt-cfg.yang) | Mdt Cfg | Configuration | 58 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [Cisco-IOS-XE-wireless-ap-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-ap-cfg.yang) | Wireless Ap Cfg | Configuration | 35 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-wireless-apf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-apf-cfg.yang) | Wireless Apf Cfg | Configuration | -27 / 48 | Wireless Controllers | [Auto-generated summary] | Added 11 new data nodes; new enum values added; enhanced validation constraints |
| 5 | [Cisco-IOS-XE-wireless-cts-sxp-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-cts-sxp-cfg.yang) | Wireless Cts Sxp Cfg | Configuration | 16 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [Cisco-IOS-XE-wireless-dot11-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-dot11-cfg.yang) | Wireless Dot11 Cfg | Configuration | +8 / 160 | Wireless Controllers | [Auto-generated summary] | Added 23 new data nodes; imported Cisco-IOS-XE-wireless-types; new enum values added |
| 7 | [Cisco-IOS-XE-wireless-fabric-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-fabric-cfg.yang) | Wireless Fabric Cfg | Configuration | 27 | Wireless Controllers | [Auto-generated summary] | Added netmask; deprecated 1 node |
| 8 | [Cisco-IOS-XE-wireless-flex-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-flex-cfg.yang) | Wireless Flex Cfg | Configuration | -64 / 48 | Wireless Controllers | [Auto-generated summary] | Added 10 new data nodes; enhanced validation constraints; deprecated 73 nodes |
| 9 | [Cisco-IOS-XE-wireless-fqdn-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-fqdn-cfg.yang) | Wireless Fqdn Cfg | Configuration | 11 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [Cisco-IOS-XE-wireless-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-general-cfg.yang) | Wireless General Cfg | Configuration | +1 / 59 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; enhanced validation constraints; deprecated 2 nodes |
| 11 | [Cisco-IOS-XE-wireless-location-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-location-cfg.yang) | Wireless Location Cfg | Configuration | 23 | Wireless Controllers | [Auto-generated summary] | Minor refinements |
| 12 | [Cisco-IOS-XE-wireless-mesh-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mesh-cfg.yang) | Wireless Mesh Cfg | Configuration | 58 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 13 | [Cisco-IOS-XE-wireless-mobility-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mobility-cfg.yang) | Wireless Mobility Cfg | Configuration | +4 / 26 | Wireless Controllers | [Auto-generated summary] | Added 4 new data nodes; enhanced validation constraints |
| 14 | [Cisco-IOS-XE-wireless-mstream-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mstream-cfg.yang) | Wireless Mstream Cfg | Configuration | 21 | Wireless Controllers | [Auto-generated summary] | Added multicast-direct-state; deprecated 1 node |
| 15 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless Rf Cfg | Configuration | -6 / 148 | Wireless Controllers | [Auto-generated summary] | Added 21 new data nodes; new enum values added; deprecated 25 nodes |
| 16 | [Cisco-IOS-XE-wireless-rfid-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rfid-cfg.yang) | Wireless Rfid Cfg | Configuration | 8 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 17 | [Cisco-IOS-XE-wireless-rogue-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rogue-cfg.yang) | Wireless Rogue Cfg | Configuration | 72 | Wireless Controllers | [Auto-generated summary] | Added marked |
| 18 | [Cisco-IOS-XE-wireless-rrm-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rrm-cfg.yang) | Wireless Rrm Cfg | Configuration | -6 / 67 | Wireless Controllers | [Auto-generated summary] | Added 5 new data nodes; imported Cisco-IOS-XE-wireless-types; new enum values added |
| 19 | [Cisco-IOS-XE-wireless-security-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-security-cfg.yang) | Wireless Security Cfg | Configuration | 16 | Wireless Controllers | [Auto-generated summary] | Added key-size; new enum values added; deprecated 1 node |
| 20 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless Site Cfg | Configuration | -44 / 216 | Wireless Controllers | [Auto-generated summary] | Added 20 new data nodes; deprecated 54 nodes |
| 21 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless Wlan Cfg | Configuration | -19 / 243 | Wireless Controllers | [Auto-generated summary] | Added 90 new data nodes; new enum values added; enhanced validation constraints |

---

## UPDATED Operational Models (57 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-aaa-oper.yang) | Aaa Oper | Operational | 61 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [Cisco-IOS-XE-acl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-acl-oper.yang) | Acl Oper | Operational | 8 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [Cisco-IOS-XE-app-hosting-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-app-hosting-oper.yang) | App Hosting Oper | Operational | +27 / 118 | All Platforms | [Auto-generated summary] | Added 30 new data nodes; new enum values added |
| 4 | [Cisco-IOS-XE-bfd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-bfd-oper.yang) | Bfd Oper | Operational | 45 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 5 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-bgp-oper.yang) | Bgp Oper | Operational | 351 | All Platforms | [Auto-generated summary] | Added name; deprecated 1 node |
| 6 | [Cisco-IOS-XE-bgp-route-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-bgp-route-oper.yang) | Bgp Route Oper | Operational | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 7 | [Cisco-IOS-XE-boot-integrity-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-boot-integrity-oper.yang) | Boot Integrity Oper | Operational | 23 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 8 | [Cisco-IOS-XE-breakout-port-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-breakout-port-oper.yang) | Breakout Port Oper | Operational | 5 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 9 | [Cisco-IOS-XE-bridge-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-bridge-oper.yang) | Bridge Oper | Operational | 36 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [Cisco-IOS-XE-cellwan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-cellwan-oper.yang) | Cellwan Oper | Operational | 101 | IR1101, C1100 | [Auto-generated summary] | updated descriptions and documentation |
| 11 | [Cisco-IOS-XE-cfm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-cfm-oper.yang) | Cfm Oper | Operational | 19 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 12 | [Cisco-IOS-XE-checkpoint-archive-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-checkpoint-archive-oper.yang) | Checkpoint Archive Oper | Operational | 8 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 13 | [Cisco-IOS-XE-controller-vdsl-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-controller-vdsl-oper.yang) | Controller Vdsl Oper | Operational | 26 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 14 | [Cisco-IOS-XE-device-hardware-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-device-hardware-oper.yang) | Device Hardware Oper | Operational | +5 / 36 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; new enum values added |
| 15 | [Cisco-IOS-XE-dhcp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-dhcp-oper.yang) | Dhcp Oper | Operational | +69 / 103 | All Platforms | [Auto-generated summary] | Added 69 new data nodes; new enum values added |
| 16 | [Cisco-IOS-XE-environment-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-environment-oper.yang) | Environment Oper | Operational | +1 / 12 | All Platforms | [Auto-generated summary] | Added sensor-name, of; new enum values added; deprecated 1 node |
| 17 | [Cisco-IOS-XE-fib-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-fib-oper.yang) | Fib Oper | Operational | 25 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 18 | [Cisco-IOS-XE-flow-monitor-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-flow-monitor-oper.yang) | Flow Monitor Oper | Operational | 73 | All Platforms | [Auto-generated summary] | Added for |
| 19 | [Cisco-IOS-XE-fw-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-fw-oper.yang) | Fw Oper | Operational | +1 / 128 | All Platforms | [Auto-generated summary] | Added 5 new data nodes; deprecated 4 nodes |
| 20 | [Cisco-IOS-XE-gir-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-gir-oper.yang) | Gir Oper | Operational | 55 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 21 | [Cisco-IOS-XE-ha-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ha-oper.yang) | Ha Oper | Operational | 10 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 22 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces Oper | Operational | 397 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 23 | [Cisco-IOS-XE-ios-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ios-common-oper.yang) | Ios Common Oper | Operational | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 24 | [Cisco-IOS-XE-ios-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ios-events-oper.yang) | Ios Events Oper | Operational | +67 / 381 | All Platforms | [Auto-generated summary] | Added 60 new data nodes; new enum values added |
| 25 | [Cisco-IOS-XE-ip-sla-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ip-sla-oper.yang) | Ip Sla Oper | Operational | +102 / 966 | All Platforms | [Auto-generated summary] | Added 38 new data nodes; new enum values added |
| 26 | [Cisco-IOS-XE-ipv6-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ipv6-oper.yang) | Ipv6 Oper | Operational | 9 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 27 | [Cisco-IOS-XE-lisp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-lisp-oper.yang) | Lisp Oper | Operational | +65 / 321 | All Platforms | [Auto-generated summary] | Added 55 new data nodes; new enum values added |
| 28 | [Cisco-IOS-XE-lldp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-lldp-oper.yang) | Lldp Oper | Operational | +15 / 80 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; new enum values added |
| 29 | [Cisco-IOS-XE-mdt-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mdt-oper.yang) | Mdt Oper | Operational | 54 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; imported ietf-yang-types; deprecated 10 nodes |
| 30 | [Cisco-IOS-XE-mlppp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mlppp-oper.yang) | Mlppp Oper | Operational | 46 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 31 | [Cisco-IOS-XE-mpls-forwarding-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mpls-forwarding-oper.yang) | Mpls Forwarding Oper | Operational | 41 | ASR, ISR, NCS | [Auto-generated summary] | updated descriptions and documentation |
| 32 | [Cisco-IOS-XE-nat-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-nat-oper.yang) | Nat Oper | Operational | 38 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 33 | [Cisco-IOS-XE-ntp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ntp-oper.yang) | Ntp Oper | Operational | 52 | All Platforms | [Auto-generated summary] | new enum values added |
| 34 | [Cisco-IOS-XE-ospf-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ospf-oper.yang) | Ospf Oper | Operational | 835 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 35 | [Cisco-IOS-XE-platform-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-platform-oper.yang) | Platform Oper | Operational | 35 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 36 | [Cisco-IOS-XE-platform-software-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-platform-software-oper.yang) | Platform Software Oper | Operational | +2 / 71 | All Platforms | [Auto-generated summary] | Added high-availability-state, chassis-state |
| 37 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-poe-oper.yang) | Poe Oper | Operational | +83 / 89 | All Platforms | [Auto-generated summary] | Added 83 new data nodes; imported ietf-yang-types; new enum values added |
| 38 | [Cisco-IOS-XE-ppp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ppp-oper.yang) | Ppp Oper | Operational | 40 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 39 | [Cisco-IOS-XE-process-cpu-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-process-cpu-oper.yang) | Process Cpu Oper | Operational | 17 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 40 | [Cisco-IOS-XE-transceiver-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-transceiver-oper.yang) | Transceiver Oper | Operational | 53 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 41 | [Cisco-IOS-XE-trustsec-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-trustsec-oper.yang) | Trustsec Oper | Operational | 34 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 42 | [Cisco-IOS-XE-utd-common-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-utd-common-oper.yang) | Utd Common Oper | Operational | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 43 | [Cisco-IOS-XE-utd-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-utd-oper.yang) | Utd Oper | Operational | +8 / 40 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; new enum values added |
| 44 | [Cisco-IOS-XE-vlan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-vlan-oper.yang) | Vlan Oper | Operational | 11 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 45 | [Cisco-IOS-XE-voice-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-voice-oper.yang) | Voice Oper | Operational | +12 / 41 | ISR, Voice Gateways | [Auto-generated summary] | Added 13 new data nodes; new enum values added |
| 46 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless Access Point Oper | Operational | -713 / 256 | Wireless Controllers | [Auto-generated summary] | Added 227 new data nodes; new enum values added; deprecated 816 nodes |
| 47 | [Cisco-IOS-XE-wireless-client-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-client-oper.yang) | Wireless Client Oper | Operational | -647 / 142 | Wireless Controllers | [Auto-generated summary] | Added 100 new data nodes; added 5 new imports; new enum values added |
| 48 | [Cisco-IOS-XE-wireless-cts-sxp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-cts-sxp-oper.yang) | Wireless Cts Sxp Oper | Operational | 9 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 49 | [Cisco-IOS-XE-wireless-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-events-oper.yang) | Wireless Events Oper | Operational | 24 | Wireless Controllers | [Auto-generated summary] | Added 9 new data nodes; new enum values added; deprecated 9 nodes |
| 50 | [Cisco-IOS-XE-wireless-lisp-agent-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-lisp-agent-oper.yang) | Wireless Lisp Agent Oper | Operational | 84 | Wireless Controllers | [Auto-generated summary] | Added lisp-agent-client-history; deprecated 1 node |
| 51 | [Cisco-IOS-XE-wireless-mcast-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mcast-oper.yang) | Wireless Mcast Oper | Operational | -45 / 112 | Wireless Controllers | [Auto-generated summary] | Added 23 new data nodes; new enum values added; deprecated 68 nodes |
| 52 | [Cisco-IOS-XE-wireless-mesh-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mesh-oper.yang) | Wireless Mesh Oper | Operational | -43 / 264 | Wireless Controllers | [Auto-generated summary] | Added 62 new data nodes; imported Cisco-IOS-XE-wireless-enum-types; new enum values added |
| 53 | [Cisco-IOS-XE-wireless-mobility-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mobility-oper.yang) | Wireless Mobility Oper | Operational | +43 / 309 | Wireless Controllers | [Auto-generated summary] | Added 17 new data nodes; deprecated 69 nodes |
| 54 | [Cisco-IOS-XE-wireless-nmsp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-nmsp-oper.yang) | Wireless Nmsp Oper | Operational | +2 / 110 | Wireless Controllers | [Auto-generated summary] | Added rssi-ms-associated-only |
| 55 | [Cisco-IOS-XE-wireless-rfid-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rfid-oper.yang) | Wireless Rfid Oper | Operational | -23 / 52 | Wireless Controllers | [Auto-generated summary] | Added time-stamp, rfid-last-heard-second; deprecated 26 nodes |
| 56 | [Cisco-IOS-XE-wireless-rogue-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rogue-oper.yang) | Wireless Rogue Oper | Operational | -3 / 291 | Wireless Controllers | [Auto-generated summary] | Added enq-count, snmp-traps-per-type, proc-time; deprecated 11 nodes |
| 57 | [Cisco-IOS-XE-wireless-rrm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rrm-oper.yang) | Wireless Rrm Oper | Operational | -276 / 69 | Wireless Controllers | [Auto-generated summary] | Added 26 new data nodes; new enum values added; deprecated 247 nodes |

---

## UPDATED RPC Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-rpc.yang) | Rpc | RPC | +201 / 675 | All Platforms | [Auto-generated summary] | Added 106 new data nodes; imported Cisco-IOS-XE-types; new enum values added |

---

## UPDATED Types Models (11 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-common-types.yang) | Common Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added; deprecated 1 node |
| 2 | [Cisco-IOS-XE-event-history-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-event-history-types.yang) | Event History Types | Types | 0 | All Platforms | [Auto-generated summary] | Added value, description, counters |
| 3 | [Cisco-IOS-XE-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-types.yang) | Types | Types | 0 | All Platforms | [Auto-generated summary] | Added for; new enum values added |
| 4 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless Ap Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 17 new data nodes; new enum values added; enhanced validation constraints |
| 5 | [Cisco-IOS-XE-wireless-client-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-client-types.yang) | Wireless Client Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 6 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless Enum Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | new enum values added |
| 7 | [Cisco-IOS-XE-wireless-mobility-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-mobility-types.yang) | Wireless Mobility Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added 87 new data nodes; deprecated 1 node |
| 8 | [Cisco-IOS-XE-wireless-rogue-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rogue-types.yang) | Wireless Rogue Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | updated descriptions and documentation |
| 9 | [Cisco-IOS-XE-wireless-rrm-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-rrm-types.yang) | Wireless Rrm Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added static; deprecated 3 nodes |
| 10 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wireless-types.yang) | Wireless Types | Types | 0 | Wireless Controllers | [Auto-generated summary] | Added has; new enum values added; deprecated 1 node |
| 11 | [Cisco-IOS-XE-wsa-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wsa-types.yang) | Wsa Types | Types | 0 | All Platforms | [Auto-generated summary] | new enum values added |

---

## UPDATED Deviation Models (4 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-ietf-event-notifications-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-ietf-event-notifications-deviation.yang) | Cisco Xe Ietf Event Notifications Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 2 | [cisco-xe-ietf-yang-push-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-ietf-yang-push-deviation.yang) | Cisco Xe Ietf Yang Push Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [cisco-xe-openconfig-if-poe-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-openconfig-if-poe-deviation.yang) | Cisco Xe Openconfig If Poe Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 4 | [cisco-xe-openconfig-routing-policy-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-openconfig-routing-policy-deviation.yang) | Cisco Xe Openconfig Routing Policy Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED Native Models (84 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +260 / 2058 | All Platforms | [Auto-generated summary] | Added 76 new data nodes; new enum values added; enhanced validation constraints |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-acl.yang) | Acl | Native | 0 | All Platforms | [Auto-generated summary] | Added 37 new data nodes; imported Cisco-IOS-XE-object-group; new enum values added |
| 3 | [Cisco-IOS-XE-atm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-atm.yang) | Atm | Native | +174 / 1146 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 4 | [Cisco-IOS-XE-bfd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-bfd.yang) | Bfd | Native | +6 / 133 | All Platforms | [Auto-generated summary] | Added for |
| 5 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-bgp.yang) | Bgp | Native | -12671 / 0 | All Platforms | [Auto-generated summary] | Added 122 new data nodes; added 3 new imports; new enum values added |
| 6 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-bridge-domain.yang) | Bridge Domain | Native | 165 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 7 | [Cisco-IOS-XE-call-home.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-call-home.yang) | Call Home | Native | +6 / 138 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 8 | [Cisco-IOS-XE-cdp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-cdp.yang) | Cdp | Native | +8 / 91 | All Platforms | [Auto-generated summary] | Added for |
| 9 | [Cisco-IOS-XE-cef.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-cef.yang) | Cef | Native | 167 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 10 | [Cisco-IOS-XE-coap.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-coap.yang) | Coap | Native | 3 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 11 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-controller.yang) | Controller | Native | 358 | All Platforms | [Auto-generated summary] | Added VDSL{; new enum values added; deprecated 1 node |
| 12 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-crypto.yang) | Crypto | Native | +966 / 3497 | All Platforms | [Auto-generated summary] | Added 450 new data nodes; new enum values added; enhanced validation constraints |
| 13 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-cts.yang) | Cts | Native | +24 / 471 | All Platforms | [Auto-generated summary] | Added for |
| 14 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-device-tracking.yang) | Device Tracking | Native | 49 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 15 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-dhcp.yang) | Dhcp | Native | +2023 / 3185 | All Platforms | [Auto-generated summary] | Added 49 new data nodes; added 3 new imports; deprecated 16 nodes |
| 16 | [Cisco-IOS-XE-diagnostics.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-diagnostics.yang) | Diagnostics | Native | 316 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 17 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-dot1x.yang) | Dot1X | Native | +21 / 237 | All Platforms | [Auto-generated summary] | Added for |
| 18 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-eem.yang) | Eem | Native | +1 / 130 | All Platforms | [Auto-generated summary] | Added wait |
| 19 | [Cisco-IOS-XE-eigrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-eigrp.yang) | Eigrp | Native | +189 / 1291 | All Platforms | [Auto-generated summary] | Added 27 new data nodes; imported Cisco-IOS-XE-features; deprecated 6 nodes |
| 20 | [Cisco-IOS-XE-eta.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-eta.yang) | Eta | Native | +6 / 52 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 21 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ethernet.yang) | Ethernet | Native | +307 / 4613 | All Platforms | [Auto-generated summary] | Added for, dhcp-border-relay; new enum values added |
| 22 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ezpm.yang) | Ezpm | Native | +37 / 193 | All Platforms | [Auto-generated summary] | Added 5 new data nodes |
| 23 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-features.yang) | Features | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 24 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-flow.yang) | Flow | Native | +357 / 2451 | All Platforms | [Auto-generated summary] | Added 46 new data nodes; imported Cisco-IOS-XE-features; deprecated 2 nodes |
| 25 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-http.yang) | Http | Native | +6 / 32 | All Platforms | [Auto-generated summary] | Added 11 new data nodes; new enum values added; deprecated 1 node |
| 26 | [Cisco-IOS-XE-icmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-icmp.yang) | Icmp | Native | +4 / 33 | All Platforms | [Auto-generated summary] | Added for |
| 27 | [Cisco-IOS-XE-igmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-igmp.yang) | Igmp | Native | +3191 / 3401 | All Platforms | [Auto-generated summary] | Added 51 new data nodes; imported Cisco-IOS-XE-types, Cisco-IOS-XE-interface-common; new enum values added |
| 28 | [Cisco-IOS-XE-interface-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-interface-common.yang) | Interface Common | Native | 0 | All Platforms | [Auto-generated summary] | Added for, AppGigabitEthernet |
| 29 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | Added 43 new data nodes; new enum values added; enhanced validation constraints |
| 30 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | Added 23 new data nodes; new enum values added; enhanced validation constraints |
| 31 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 32 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-isis.yang) | Isis | Native | +273 / 4581 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; imported Cisco-IOS-XE-features; deprecated 1 node |
| 33 | [Cisco-IOS-XE-iwanfabric.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-iwanfabric.yang) | Iwanfabric | Native | +5 / 134 | All Platforms | [Auto-generated summary] | Added for |
| 34 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-l2vpn.yang) | L2Vpn | Native | +43 / 1254 | All Platforms | [Auto-generated summary] | Added 26 new data nodes; new enum values added; enhanced validation constraints |
| 35 | [Cisco-IOS-XE-license.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-license.yang) | License | Native | 0 | All Platforms | [Auto-generated summary] | Added suite, suite-name; imported Cisco-IOS-XE-features; new enum values added |
| 36 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-line.yang) | Line | Native | 0 | All Platforms | [Auto-generated summary] | Added commands; deprecated 1 node |
| 37 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-lisp.yang) | Lisp | Native | +642 / 19501 | All Platforms | [Auto-generated summary] | Added 31 new data nodes; imported Cisco-IOS-XE-features; new enum values added |
| 38 | [Cisco-IOS-XE-lldp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-lldp.yang) | Lldp | Native | +6 / 69 | All Platforms | [Auto-generated summary] | Added for |
| 39 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-logging.yang) | Logging | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 40 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mdt-common-defs.yang) | Mdt Common Defs | Native | 0 | All Platforms | [Auto-generated summary] | Added 4 new data nodes |
| 41 | [Cisco-IOS-XE-mka.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mka.yang) | Mka | Native | +6 / 62 | All Platforms | [Auto-generated summary] | Added for |
| 42 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mpls.yang) | Mpls | Native | 0 | ASR, ISR, NCS | [Auto-generated summary] | Added 5 new data nodes |
| 43 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-multicast.yang) | Multicast | Native | +267 / 1157 | All Platforms | [Auto-generated summary] | Added 13 new data nodes; deprecated 1 node |
| 44 | [Cisco-IOS-XE-mvrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-mvrp.yang) | Mvrp | Native | +14 / 145 | All Platforms | [Auto-generated summary] | Added for |
| 45 | [Cisco-IOS-XE-nam.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-nam.yang) | Nam | Native | +3 / 39 | All Platforms | [Auto-generated summary] | Added for |
| 46 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-nat.yang) | Nat | Native | +185 / 746 | All Platforms | [Auto-generated summary] | Added 94 new data nodes; enhanced validation constraints; deprecated 9 nodes |
| 47 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-native.yang) | Native | Native | +3166 / 26461 | All Platforms | [Auto-generated summary] | Added 66 new data nodes; new enum values added; deprecated 1 node |
| 48 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-nbar.yang) | Nbar | Native | +32 / 551 | All Platforms | [Auto-generated summary] | Added 7 new data nodes |
| 49 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-nd.yang) | Nd | Native | +30 / 275 | All Platforms | [Auto-generated summary] | Added for |
| 50 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ntp.yang) | Ntp | Native | +32 / 365 | All Platforms | [Auto-generated summary] | Added 24 new data nodes; new enum values added; enhanced validation constraints |
| 51 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-object-group.yang) | Object Group | Native | +3 / 186 | All Platforms | [Auto-generated summary] | Added 151 new data nodes; deprecated 145 nodes |
| 52 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ospf.yang) | Ospf | Native | +193 / 3169 | All Platforms | [Auto-generated summary] | Added 8 new data nodes; imported Cisco-IOS-XE-features; enhanced validation constraints |
| 53 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ospfv3.yang) | Ospfv3 | Native | +526 / 7553 | All Platforms | [Auto-generated summary] | Added for |
| 54 | [Cisco-IOS-XE-parser.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-parser.yang) | Parser | Native | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 55 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-platform.yang) | Platform | Native | +9 / 114 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; new enum values added; deprecated 4 nodes |
| 56 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-policy.yang) | Policy | Native | +168 / 2850 | All Platforms | [Auto-generated summary] | Added 59 new data nodes; new enum values added; enhanced validation constraints |
| 57 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-power.yang) | Power | Native | +18 / 171 | All Platforms | [Auto-generated summary] | Added for |
| 58 | [Cisco-IOS-XE-ppp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-ppp.yang) | Ppp | Native | +52 / 338 | All Platforms | [Auto-generated summary] | Added 20 new data nodes; deprecated 15 nodes |
| 59 | [Cisco-IOS-XE-pppoe.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-pppoe.yang) | Pppoe | Native | 13 | All Platforms | [Auto-generated summary] | Minor refinements |
| 60 | [Cisco-IOS-XE-qos.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-qos.yang) | Qos | Native | 36 | All Platforms | [Auto-generated summary] | Minor refinements |
| 61 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-rip.yang) | Rip | Native | +6 / 1311 | All Platforms | [Auto-generated summary] | Added for |
| 62 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-route-map.yang) | Route Map | Native | +10 / 989 | All Platforms | [Auto-generated summary] | Added 27 new data nodes; imported Cisco-IOS-XE-features; deprecated 18 nodes |
| 63 | [Cisco-IOS-XE-rsvp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-rsvp.yang) | Rsvp | Native | +103 / 642 | All Platforms | [Auto-generated summary] | Added 6 new data nodes |
| 64 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-sanet.yang) | Sanet | Native | +58 / 524 | All Platforms | [Auto-generated summary] | Added 10 new data nodes |
| 65 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-segment-routing.yang) | Segment Routing | Native | +133 / 196 | All Platforms | [Auto-generated summary] | Added 85 new data nodes; added 3 new imports; new enum values added |
| 66 | [Cisco-IOS-XE-serial.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-serial.yang) | Serial | Native | +1 / 39 | All Platforms | [Auto-generated summary] | Added hdlc |
| 67 | [Cisco-IOS-XE-service-insertion.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-service-insertion.yang) | Service Insertion | Native | +15 / 43 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; new enum values added |
| 68 | [Cisco-IOS-XE-sla.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-sla.yang) | Sla | Native | +749 / 1175 | All Platforms | [Auto-generated summary] | Added 93 new data nodes; new enum values added; deprecated 7 nodes |
| 69 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-snmp.yang) | Snmp | Native | +42 / 1012 | All Platforms | [Auto-generated summary] | Added 8 new data nodes |
| 70 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-spanning-tree.yang) | Spanning Tree | Native | +28 / 369 | All Platforms | [Auto-generated summary] | Added for |
| 71 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-switch.yang) | Switch | Native | +170 / 2987 | Cat9K, IE3x00 | [Auto-generated summary] | Added 4 new data nodes; deprecated 19 nodes |
| 72 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-template.yang) | Template | Native | +216 / 1079 | All Platforms | [Auto-generated summary] | Added 15 new data nodes; new enum values added |
| 73 | [Cisco-IOS-XE-track.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-track.yang) | Track | Native | +8 / 85 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; deprecated 4 nodes |
| 74 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | +12 / 706 | All Platforms | [Auto-generated summary] | Added 6 new data nodes; imported ietf-interfaces; enhanced validation constraints |
| 75 | [Cisco-IOS-XE-udld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-udld.yang) | Udld | Native | +7 / 83 | All Platforms | [Auto-generated summary] | Added for |
| 76 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-umbrella.yang) | Umbrella | Native | +127 / 187 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; new enum values added; enhanced validation constraints |
| 77 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-utd.yang) | Utd | Native | +35 / 330 | All Platforms | [Auto-generated summary] | Added 34 new data nodes; new enum values added; enhanced validation constraints |
| 78 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-vlan.yang) | Vlan | Native | 98 | Cat9K, IE3x00 | [Auto-generated summary] | updated descriptions and documentation |
| 79 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-voice.yang) | Voice | Native | +15 / 35 | ISR, Voice Gateways | [Auto-generated summary] | Added 15 new data nodes; imported ietf-inet-types; new enum values added |
| 80 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-vrrp.yang) | Vrrp | Native | +96 / 768 | All Platforms | [Auto-generated summary] | Added for; imported Cisco-IOS-XE-features; new enum values added |
| 81 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-vservice.yang) | Vservice | Native | +1 / 36 | All Platforms | [Auto-generated summary] | Added for, AppGigabitEthernet |
| 82 | [Cisco-IOS-XE-vtp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-vtp.yang) | Vtp | Native | 28 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 83 | [Cisco-IOS-XE-wccp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-wccp.yang) | Wccp | Native | +28 / 440 | All Platforms | [Auto-generated summary] | Added for |
| 84 | [Cisco-IOS-XE-zone.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/Cisco-IOS-XE-zone.yang) | Zone | Native | +4 / 50 | All Platforms | [Auto-generated summary] | Added for |

---

## UPDATED OpenConfig Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-openconfig-platform-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-openconfig-platform-ext.yang) | Cisco Xe Openconfig Platform Ext | OpenConfig | +6 / 6 | All Platforms | [Auto-generated summary] | Added 7 new data nodes |
| 2 | [openconfig-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/openconfig-platform.yang) | Openconfig Platform | OpenConfig | 37 | All Platforms | [Auto-generated summary] | Minor refinements |

---

## UPDATED IETF Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-ietf-yang-push-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-xe-ietf-yang-push-ext.yang) | Cisco Xe Ietf Yang Push Ext | IETF | 18 | All Platforms | [Auto-generated summary] | Minor refinements |
| 2 | [ietf-event-notifications.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/ietf-event-notifications.yang) | Ietf Event Notifications | IETF | +5 / 160 | All Platforms | [Auto-generated summary] | Added identifier, subscription-result |

---

## UPDATED Vendor Models (4 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | +7 / 589 | All Platforms | [Auto-generated summary] | Added 7 new data nodes |
| 2 | [tailf-cli-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/tailf-cli-extensions.yang) | Tailf Cli Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | Minor refinements |
| 3 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/tailf-common.yang) | Tailf Common | Vendor | 0 | All Platforms | [Auto-generated summary] | new enum values added |
| 4 | [tailf-meta-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/tailf-meta-extensions.yang) | Tailf Meta Extensions | Vendor | 0 | All Platforms | [Auto-generated summary] | enhanced validation constraints |

---

## UPDATED Other Models (3 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-ia.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-ia.yang) | Cisco Ia | Other | 85 | All Platforms | [Auto-generated summary] | Minor refinements |
| 2 | [cisco-routing-ext.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-routing-ext.yang) | Cisco Routing Ext | Other | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [cisco-storm-control.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/16111/cisco-storm-control.yang) | Cisco Storm Control | Other | 0 | All Platforms | [Auto-generated summary] | Minor refinements |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
