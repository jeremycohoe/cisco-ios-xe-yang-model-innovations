# All YANG Model Changes: v16.6.1 → v16.6.2
**Summary: 4 New Models & 19 Updated Models**

*Generated: May 06, 2026*

---

## NEW Models Summary (4 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Types Models](#new-types-models)** | 2 | 0 XPaths |
| **[NEW Native Models](#new-native-models)** | 1 | 14 XPaths |
| **[NEW IETF Models](#new-ietf-models)** | 1 | 0 XPaths |
| **TOTAL NEW MODELS** | **4** | **14 total XPaths** |

---

## UPDATED Models Summary (19 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Types Models](#updated-types-models)** | 1 | XPath changes vary |
| **[UPDATED Deviation Models](#updated-deviation-models)** | 2 | XPath changes vary |
| **[UPDATED Native Models](#updated-native-models)** | 12 | XPath changes vary |
| **[UPDATED OpenConfig Models](#updated-openconfig-models)** | 2 | XPath changes vary |
| **[UPDATED Vendor Models](#updated-vendor-models)** | 2 | XPath changes vary |
| **TOTAL UPDATED MODELS** | **19** | **See individual models** |

---

## Key Highlights - NEW Models


**4 new models introduced** in this release:


- **Top additions by size:**

  - `Cisco-IOS-XE-umbrella.yang`: 14 XPaths (Native)


- **Breakdown by category:**

  - Types: 2 models

  - Native: 1 model

  - IETF: 1 model


---


## Key Highlights - UPDATED Models


**19 models updated** in this release:


- **Significant additions:**

  - `Cisco-IOS-XE-aaa.yang`: +809 XPaths (now 1,594 total)

  - `Cisco-IOS-XE-utd.yang`: +84 XPaths (now 137 total)

  - `openconfig-acl.yang`: +18 XPaths (now 144 total)


- **Significant removals:**

  - `Cisco-IOS-XE-native.yang`: -46 XPaths (now 14,588 total)


- **Updates by category:**

  - Native: 12 models

  - Deviation: 2 models

  - Vendor: 2 models

  - OpenConfig: 2 models

  - Types: 1 model


---


## Summary Statistics

### Release v16.6.2 Totals:
- **Total YANG Files:** ~423 files
- **New Files:** 4 models
- **Modified Files:** 19 models
- **Deleted Files:** 12 models
- **New Model XPaths:** 14 XPaths across 4 new models

---

# NEW YANG Models in v16.6.2

**4 Brand New Models**

---

## NEW Types Models (2 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [openconfig-inet-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/openconfig-inet-types.yang) | Openconfig Inet Types | Types | 0 | All Platforms | New model introduced in this release |
| 2 | [openconfig-yang-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/openconfig-yang-types.yang) | Openconfig Yang Types | Types | 0 | All Platforms | New model introduced in this release |

---

## NEW Native Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-umbrella.yang) | Umbrella | Native | 14 | All Platforms | New model introduced in this release |

---

## NEW IETF Models (1 models)

| # | YANG Model | Module Name | Type | # XPaths | Platforms | Summary |
|---|------------|-------------|------|----------|-----------|---------|
| 1 | [ietf-restconf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/ietf-restconf.yang) | Ietf Restconf | IETF | 0 | All Platforms | New model introduced in this release |

---

# UPDATED YANG Models: v16.6.1 → v16.6.2

**19 Models Modified**

---

## UPDATED Types Models (1 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [openconfig-packet-match-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/openconfig-packet-match-types.yang) | Openconfig Packet Match Types | Types | 0 | All Platforms | [Auto-generated summary] | imported openconfig-inet-types |

---

## UPDATED Deviation Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [cisco-xe-openconfig-acl-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/cisco-xe-openconfig-acl-deviation.yang) | Cisco Xe Openconfig Acl Deviation | Deviation | 0 | All Platforms | [Auto-generated summary] | imported openconfig-acl; enhanced validation constraints |
| 2 | [cisco-xe-openconfig-vlan-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/cisco-xe-openconfig-vlan-deviation.yang) | Cisco Xe Openconfig Vlan Deviation | Deviation | 0 | Cat9K, IE3x00 | [Auto-generated summary] | Minor refinements |

---

## UPDATED Native Models (12 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-aaa.yang) | Aaa | Native | +809 / 1594 | All Platforms | [Auto-generated summary] | Added 128 new data nodes; new enum values added; deprecated 23 nodes |
| 2 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-acl.yang) | Acl | Native | 792 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 3 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-cts.yang) | Cts | Native | +2 / 355 | All Platforms | [Auto-generated summary] | Added enforcement-only, enforcement |
| 4 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-interfaces.yang) | Interfaces | Native | 0 | All Platforms | [Auto-generated summary] | deprecated 2 nodes |
| 5 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-ip.yang) | Ip | Native | 0 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 6 | [Cisco-IOS-XE-ipv6.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-ipv6.yang) | Ipv6 | Native | 0 | All Platforms | [Auto-generated summary] | Added ospf, id |
| 7 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-nat.yang) | Nat | Native | 359 | All Platforms | [Auto-generated summary] | Added vrf; deprecated 1 node |
| 8 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-native.yang) | Native | Native | -46 / 14588 | All Platforms | [Auto-generated summary] | new enum values added |
| 9 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-policy.yang) | Policy | Native | +3 / 2201 | All Platforms | [Auto-generated summary] | Added regex, pattern, regexp |
| 10 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-tunnel.yang) | Tunnel | Native | 682 | All Platforms | [Auto-generated summary] | updated descriptions and documentation |
| 11 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-utd.yang) | Utd | Native | +84 / 137 | All Platforms | [Auto-generated summary] | Added 109 new data nodes; imported ietf-inet-types; new enum values added |
| 12 | [Cisco-IOS-XE-vservice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/Cisco-IOS-XE-vservice.yang) | Vservice | Native | +1 / 32 | All Platforms | [Auto-generated summary] | Added GigabitEthernet |

---

## UPDATED OpenConfig Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [openconfig-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/openconfig-acl.yang) | Openconfig Acl | OpenConfig | +18 / 144 | All Platforms | [Auto-generated summary] | Added 9 new data nodes; imported openconfig-yang-types; deprecated 2 nodes |
| 2 | [openconfig-packet-match.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/openconfig-packet-match.yang) | Openconfig Packet Match | OpenConfig | 0 | All Platforms | [Auto-generated summary] | Added 12 new data nodes; imported openconfig-inet-types, openconfig-yang-types; deprecated 6 nodes |

---

## UPDATED Vendor Models (2 models)

| # | YANG Model | Module Name | Type | XPaths (Δ/Total) | Platforms | Summary | What Changed |
|---|------------|-------------|------|------------------|-----------|---------|--------------|
| 1 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/confd_dyncfg.yang) | Confd_Dyncfg | Vendor | +2 / 552 | All Platforms | [Auto-generated summary] | Added 4 new data nodes; new enum values added |
| 2 | [tailf-common-query.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/1662/tailf-common-query.yang) | Tailf Common Query | Vendor | 0 | All Platforms | [Auto-generated summary] | Added timeout, timeout |

---

*Note: XPath counts calculated using pyang tree analysis. Summaries generated from diff analysis.*

---

**For questions or issues with this documentation, refer to:**
- [PROJECT_PLAN.md](PROJECT_PLAN.md) - Methodology and replication instructions
