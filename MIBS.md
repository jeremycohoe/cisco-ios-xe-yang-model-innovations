# Cisco IOS XE MIB Documentation

> **Single source of truth** for every SMIv2 MIB (delivered as YANG conversions) shipped in the IOS XE YANG models repo at `reference/xe/`. Covers what each MIB does, when it was added/removed across releases, which platforms expose it, and the follow-up work still on the backlog.

---

## Executive summary

Cisco ships every IOS XE release with a set of SMIv2 MIBs, machine-translated into YANG so they can be served over NETCONF and YANG-driven telemetry pipelines. This document catalogues that set across all 32 releases in the repo (16.3.1 → 17.18.1, plus 26.1.1) and across all 10 platform families.

**Headline numbers:**

| Metric | Value |
|---|---|
| Releases scanned | **32** (16.3.1 → 17.18.1, plus 26.1.1) |
| MIBs in latest release (26.1.1 / 17.18.1) | **184** |
| Total unique MIBs ever shipped in this tree | **212** |
| Platform capability XMLs in 17.18.1 | **10** |
| Platforms advertising SMIv2 MIBs | **9** (wireless is YANG-only) |
| MIBs on Cat9300/9400/9500/9600 (`cat9k`) | **137** |
| MIBs on ASR1000 (`asr1k`) | **176** |
| Releases since the last MIB churn | **8** (stable from 17.11.1 → 26.1.1) |

**Key takeaways:**

1. **The MIB inventory has stabilised.** From 17.11.1 onward (and including the 26.1.1 jump) the YANG-converted MIB set is a steady **184 modules**. Most product churn now happens in the native YANG operational models, not the legacy MIBs.
2. **Cat9k is a strict subset of ASR1k.** Catalyst 9k switches advertise 39 fewer MIBs than the routing platforms — they drop WAN-only modules (ATM, DS1/DS3, SONET, Frame Relay), voice/SBC, MPLS-TE/LDP, and pseudowire. This matters when porting MDT pipelines between routing and switching footprints.
3. **The wireless controller (9800) advertises zero SMIv2 MIBs** in its NETCONF capability XML — it is a YANG-only platform from the management-protocol view.
4. **DOCSIS / cable MIBs are no longer in this tree.** They appeared in 16.9.1 (CBR platform support), churned through 17.4 / 17.5 / 17.8, and have been absent since 17.8.1. New cable work lives in a separate repo.
5. **For MDT / Cat9300 work, prefer the `Cisco-IOS-XE-*-oper` YANG models over polling these MIBs.** Use this document when (a) a YANG model isn't available, (b) you're integrating with a legacy SNMP NMS in parallel with MDT, or (c) you need to map an OID-based alarm or trap to its MDT equivalent.

**How to use this document:**

- **Operations / NMS engineer** → start with [§4 Cheat-sheet](#4-quick-what-should-i-poll-for-x-cheat-sheet) and [§3 Per-platform matrix](#3-per-platform-availability-matrix).
- **MDT pipeline owner** → start with [§5 MDT relevance](#5-notes-on-relevance-to-mdt--telemetry), then [§6 Future work](#6-future-work--not-done-today) for the migration crosswalk backlog.
- **Release engineer / changelog reviewer** → start with [§1 Per-release inventory](#1-per-release-inventory).
- **Feature triage** → start with [§2 Functional MIB reference](#2-functional-mib-reference) (categorised field guide).

---

## Table of contents

- [Executive summary](#executive-summary)
- [1. Per-release inventory](#1-per-release-inventory)
  - [1.1 Per-release totals](#11-per-release-totals)
  - [1.2 Additions and removals by release](#12-additions-and-removals-by-release)
  - [1.3 Themes](#13-themes)
  - [1.4 Net delta 16.3.1 → 17.18.1](#14-net-delta-1631--17181)
  - [1.5 Appendix — Full MIB list in latest release](#15-appendix--full-mib-list-in-latest-release-17181)
- [2. Functional MIB reference](#2-functional-mib-reference)
  - [2.1 SMI / framework / textual conventions](#21-smi--framework--textual-conventions)
  - [2.2 SNMP protocol infrastructure](#22-snmp-protocol-infrastructure)
  - [2.3 System & host](#23-system--host)
  - [2.4 Interfaces & link layer](#24-interfaces--link-layer)
  - [2.5 Bridging, VLAN, STP](#25-bridging-vlan-stp)
  - [2.6 LLDP / CDP discovery](#26-lldp--cdp-discovery)
  - [2.7 IP, TCP, UDP](#27-ip-tcp-udp)
  - [2.8 Routing protocols](#28-routing-protocols)
  - [2.9 Multicast](#29-multicast)
  - [2.10 MPLS / L3VPN / Pseudowire](#210-mpls--l3vpn--pseudowire)
  - [2.11 QoS, DiffServ, NBAR](#211-qos-diffserv-nbar)
  - [2.12 Security / IPsec / Firewall / AAA](#212-security--ipsec--firewall--aaa)
  - [2.13 HSRP, VRRP, redundancy](#213-hsrp-vrrp-redundancy)
  - [2.14 Entity / hardware / environment](#214-entity--hardware--environment)
  - [2.15 PoE](#215-poe-power-over-ethernet)
  - [2.16 Stackwise](#216-stackwise)
  - [2.17 SONET / DS1 / DS3 / ATM / Frame Relay](#217-sonet--ds1--ds3--atm--frame-relay)
  - [2.18 IP SLA / RTTMON / ping](#218-ip-sla--rttmon--ping)
  - [2.19 RMON / Expression / DISMAN events](#219-rmon--expression--disman-events)
  - [2.20 Voice / SBC / dial / media gateway](#220-voice--sbc--dial--media-gateway)
  - [2.21 Subscriber / dynamic templates / VPDN / IP pools](#221-subscriber--dynamic-templates--vpdn--ip-pools)
  - [2.22 PTP / NTP / NetSync (timing)](#222-ptp--ntp--netsync-timing)
  - [2.23 Image / config / file / EEM / syslog / license](#223-image--config--file--eem--syslog--license)
  - [2.24 Lawful intercept](#224-lawful-intercept)
  - [2.25 Misc / legacy](#225-misc--legacy)
- [3. Per-platform availability matrix](#3-per-platform-availability-matrix)
  - [3.1 MIB count per platform](#31-mib-count-per-platform)
  - [3.2 Core MIBs common to every non-wireless platform](#32-core-mibs-common-to-every-non-wireless-platform-136)
  - [3.3 Routing-family additions (not on Cat9k)](#33-routing-family-additions-routers-not-on-cat9k-switches)
  - [3.4 Cat9k vs ASR1k diff](#34-cat9k-vs-asr1k-diff)
  - [3.5 Full availability matrix](#35-full-availability-matrix)
- [4. Quick "what should I poll for X?" cheat-sheet](#4-quick-what-should-i-poll-for-x-cheat-sheet)
- [5. Notes on relevance to MDT / telemetry](#5-notes-on-relevance-to-mdt--telemetry)
- [6. Future work — not done today](#6-future-work--not-done-today)
  - [6.1 MIB → YANG operational-model crosswalk](#61-mib--yang-operational-model-crosswalk-highest-priority)
  - [6.2 OID-to-MIB index](#62-oid-to-mib-index-high-priority-for-trapalerting-work)
  - [6.3 Trap / notification inventory](#63-trap--notification-inventory)
  - [6.4 Deprecated / obsolete object scan](#64-deprecated--obsolete-object-scan)
  - [6.5 Index / landing page](#65-index--landing-page)
  - [6.6 cEdge MIB comparison](#66-cedge-mib-comparison)
  - [6.7 Per-MIB object / table count](#67-per-mib-object--table-count)
  - [6.8 Capability-XML revision-date tracking](#68-capability-xml-revision-date-tracking)
  - [Explicitly out-of-scope](#explicitly-out-of-scope)

---

## 1. Per-release inventory

Source: `reference/xe/<release>/MIBS/*.yang` — SMIv2 MIBs converted to YANG.

- Releases scanned: **32** (16.3.1 → 17.18.1, plus 26.1.1)
- Latest release in tree: **26.1.1** (184 MIBs)

### 1.1 Per-release totals

| Release | Total MIBs | Added | Removed |
|---|---:|---:|---:|
| 16.3.1 | 176 | 176 (initial) | 0 |
| 16.3.2 | 170 | 0 | 6 |
| 16.4.1 | 170 | 0 | 0 |
| 16.5.1 | 171 | 9 | 8 |
| 16.6.1 | 181 | 10 | 0 |
| 16.6.2 | 181 | 0 | 0 |
| 16.7.1 | 180 | 0 | 1 |
| 16.8.1 | 183 | 3 | 0 |
| 16.9.1 | 196 | 13 | 0 |
| 16.9.3 | 196 | 0 | 0 |
| 16.10.1 | 196 | 0 | 0 |
| 16.11.1 | 196 | 0 | 0 |
| 16.12.1 | 198 | 2 | 0 |
| 17.1.1 | 198 | 0 | 0 |
| 17.2.1 | 198 | 0 | 0 |
| 17.3.1 | 198 | 0 | 0 |
| 17.4.1 | 184 | 0 | 14 |
| 17.5.1 | 198 | 14 | 0 |
| 17.6.1 | 198 | 0 | 0 |
| 17.7.1 | 198 | 0 | 0 |
| 17.8.1 | 184 | 0 | 14 |
| 17.9.1 | 183 | 0 | 1 |
| 17.10.1 | 184 | 1 | 0 |
| 17.11.1 | 184 | 0 | 0 |
| 17.12.1 | 184 | 0 | 0 |
| 17.13.1 | 184 | 0 | 0 |
| 17.14.1 | 184 | 0 | 0 |
| 17.15.1 | 184 | 0 | 0 |
| 17.16.1 | 184 | 0 | 0 |
| 17.17.1 | 184 | 0 | 0 |
| 17.18.1 | 184 | 0 | 0 |
| 26.1.1 | 184 | 0 | 0 |

### 1.2 Additions and removals by release

#### 16.3.1 — initial baseline (176 MIBs)

See *Section 2* for descriptions of each MIB. Initial set listed in Appendix at end of this section.

#### 16.3.2 (170 MIBs)

**Removed (6):**

- `SNMP-FRAMEWORK-MIB-ann`
- `SNMP-MPD-MIB-ann`
- `SNMP-TARGET-MIB-ann`
- `SNMP-USER-BASED-SM-MIB-ann`
- `SNMPv2-MIB-ann`
- `ietf-yang-smiv2`

#### 16.5.1 (171 MIBs)

**Added (9):**

- `CISCO-CEF-MIB`
- `CISCO-ENHANCED-MEMPOOL-MIB`
- `CISCO-ENTITY-EXT-MIB`
- `CISCO-ENTITY-QFP-MIB`
- `CISCO-FLASH-MIB`
- `CISCO-IGMP-FILTER-MIB`
- `CISCO-IPSEC-MIB`
- `CISCO-NETSYNC-MIB`
- `MPLS-VPN-MIB`

**Removed (8):**

- `IPV6-TC`
- `SNMP-COMMUNITY-MIB`
- `SNMP-MPD-MIB`
- `SNMP-NOTIFICATION-MIB`
- `SNMP-USER-BASED-SM-MIB`
- `SNMP-VIEW-BASED-ACM-MIB`
- `SNMPv2-SMI`
- `TRANSPORT-ADDRESS-MIB`

#### 16.6.1 (181 MIBs)

**Added (10):**

- `CISCO-ETHER-CFM-MIB`
- `CISCO-LICENSE-MGMT-MIB`
- `CISCO-PROCESS-MIB`
- `CISCO-RTTMON-MIB`
- `CISCO-SIP-UA-MIB`
- `CISCO-UNIFIED-FIREWALL-MIB`
- `LLDP-MIB`
- `Q-BRIDGE-MIB`
- `RFC1213-MIB`
- `RMON2-MIB`

#### 16.7.1 (180 MIBs)

**Removed (1):**

- `CISCO-ENVMON-MIB`

#### 16.8.1 (183 MIBs)

**Added (3):**

- `CISCO-ENVMON-MIB`
- `CISCO-POWER-ETHERNET-EXT-MIB`
- `POWER-ETHERNET-MIB`

#### 16.9.1 (196 MIBs)

**Added (13):**

- `CISCO-CABLE-SPECTRUM-MIB`
- `CISCO-CABLE-WIDEBAND-MIB`
- `CISCO-DOCS-EXT-MIB`
- `CLAB-DEF-MIB`
- `CLAB-TOPO-MIB`
- `DOCS-CABLE-DEVICE-MIB`
- `DOCS-IETF-BPI2-MIB`
- `DOCS-IF-MIB`
- `DOCS-IF3-MIB`
- `DOCS-L2VPN-MIB`
- `DOCS-QOS-MIB`
- `DOCS-SUBMGT3-MIB`
- `OLD-CISCO-INTERFACES-MIB`

#### 16.12.1 (198 MIBs)

**Added (2):**

- `CISCO-STACKWISE-MIB`
- `DOCS-IF31-MIB`

#### 17.4.1 (184 MIBs)

**Removed (14):**

- `CISCO-CABLE-SPECTRUM-MIB`
- `CISCO-CABLE-WIDEBAND-MIB`
- `CISCO-DOCS-EXT-MIB`
- `CLAB-DEF-MIB`
- `CLAB-TOPO-MIB`
- `DOCS-CABLE-DEVICE-MIB`
- `DOCS-IETF-BPI2-MIB`
- `DOCS-IF-MIB`
- `DOCS-IF3-MIB`
- `DOCS-IF31-MIB`
- `DOCS-L2VPN-MIB`
- `DOCS-QOS-MIB`
- `DOCS-SUBMGT3-MIB`
- `OLD-CISCO-INTERFACES-MIB`

#### 17.5.1 (198 MIBs)

**Added (14):**

- `CISCO-CABLE-SPECTRUM-MIB`
- `CISCO-CABLE-WIDEBAND-MIB`
- `CISCO-DOCS-EXT-MIB`
- `CLAB-DEF-MIB`
- `CLAB-TOPO-MIB`
- `DOCS-CABLE-DEVICE-MIB`
- `DOCS-IETF-BPI2-MIB`
- `DOCS-IF-MIB`
- `DOCS-IF3-MIB`
- `DOCS-IF31-MIB`
- `DOCS-L2VPN-MIB`
- `DOCS-QOS-MIB`
- `DOCS-SUBMGT3-MIB`
- `OLD-CISCO-INTERFACES-MIB`

#### 17.8.1 (184 MIBs)

**Removed (14):**

- `CISCO-CABLE-SPECTRUM-MIB`
- `CISCO-CABLE-WIDEBAND-MIB`
- `CISCO-DOCS-EXT-MIB`
- `CLAB-DEF-MIB`
- `CLAB-TOPO-MIB`
- `DOCS-CABLE-DEVICE-MIB`
- `DOCS-IETF-BPI2-MIB`
- `DOCS-IF-MIB`
- `DOCS-IF3-MIB`
- `DOCS-IF31-MIB`
- `DOCS-L2VPN-MIB`
- `DOCS-QOS-MIB`
- `DOCS-SUBMGT3-MIB`
- `OLD-CISCO-INTERFACES-MIB`

#### 17.9.1 (183 MIBs)

**Removed (1):**

- `DIFFSERV-DSCP-TC`

#### 17.10.1 (184 MIBs)

**Added (1):**

- `DIFFSERV-DSCP-TC`

### 1.3 Themes

- **16.3.2:** removed 6 helper modules (the `*-ann` annotation files and `ietf-yang-smiv2`).
- **16.5.1:** SNMP framework cleanup — removed standalone `SNMP-*` MIBs, `SNMPv2-SMI`, `IPV6-TC`, `TRANSPORT-ADDRESS-MIB`. Added CEF, QFP, mempool, flash, IPSEC, NetSync, MPLS-VPN MIBs.
- **16.6.1:** added LLDP, Q-BRIDGE, RMON2, RFC1213, process, license, Ether-CFM, RTTMON, SIP-UA, unified firewall.
- **16.8.1:** PoE support — added `POWER-ETHERNET-MIB`, `CISCO-POWER-ETHERNET-EXT-MIB`, restored `CISCO-ENVMON-MIB`.
- **16.9.1:** DOCSIS / cable wave — 13 cable/DOCS MIBs added (CBR platform support).
- **16.12.1:** added `CISCO-STACKWISE-MIB` and `DOCS-IF31-MIB`.
- **17.4.1 / 17.8.1:** the DOCSIS/cable MIB bundle (14 modules) drops out, then returns in 17.5.1; from 17.8.1 onward those cable MIBs are gone for good in this tree.
- **17.9.1 → 17.10.1:** brief `DIFFSERV-DSCP-TC` removal/restoration.
- **17.11.1 – 17.18.1 and 26.1.1:** stable at 184 MIBs — no churn for ~8 releases.

### 1.4 Net delta 16.3.1 → 17.18.1

- Net additions: **22**
- Net removals: **14**

**Net new MIBs since 16.3.1:**

- `CISCO-CEF-MIB`
- `CISCO-ENHANCED-MEMPOOL-MIB`
- `CISCO-ENTITY-EXT-MIB`
- `CISCO-ENTITY-QFP-MIB`
- `CISCO-ETHER-CFM-MIB`
- `CISCO-FLASH-MIB`
- `CISCO-IGMP-FILTER-MIB`
- `CISCO-IPSEC-MIB`
- `CISCO-LICENSE-MGMT-MIB`
- `CISCO-NETSYNC-MIB`
- `CISCO-POWER-ETHERNET-EXT-MIB`
- `CISCO-PROCESS-MIB`
- `CISCO-RTTMON-MIB`
- `CISCO-SIP-UA-MIB`
- `CISCO-STACKWISE-MIB`
- `CISCO-UNIFIED-FIREWALL-MIB`
- `LLDP-MIB`
- `MPLS-VPN-MIB`
- `POWER-ETHERNET-MIB`
- `Q-BRIDGE-MIB`
- `RFC1213-MIB`
- `RMON2-MIB`

**MIBs present in 16.3.1 but not in 17.18.1:**

- `IPV6-TC`
- `SNMP-COMMUNITY-MIB`
- `SNMP-FRAMEWORK-MIB-ann`
- `SNMP-MPD-MIB`
- `SNMP-MPD-MIB-ann`
- `SNMP-NOTIFICATION-MIB`
- `SNMP-TARGET-MIB-ann`
- `SNMP-USER-BASED-SM-MIB`
- `SNMP-USER-BASED-SM-MIB-ann`
- `SNMP-VIEW-BASED-ACM-MIB`
- `SNMPv2-MIB-ann`
- `SNMPv2-SMI`
- `TRANSPORT-ADDRESS-MIB`
- `ietf-yang-smiv2`

### 1.5 Appendix — Full MIB list in latest release (17.18.1)

- `ATM-FORUM-TC-MIB`
- `ATM-MIB`
- `ATM-TC-MIB`
- `BGP4-MIB`
- `BRIDGE-MIB`
- `CISCO-AAA-SERVER-MIB`
- `CISCO-AAA-SESSION-MIB`
- `CISCO-AAL5-MIB`
- `CISCO-ATM-EXT-MIB`
- `CISCO-ATM-PVCTRAP-EXTN-MIB`
- `CISCO-ATM-QOS-MIB`
- `CISCO-BGP-POLICY-ACCOUNTING-MIB`
- `CISCO-BGP4-MIB`
- `CISCO-BULK-FILE-MIB`
- `CISCO-CBP-TARGET-MIB`
- `CISCO-CBP-TARGET-TC-MIB`
- `CISCO-CBP-TC-MIB`
- `CISCO-CDP-MIB`
- `CISCO-CEF-MIB`
- `CISCO-CEF-TC`
- `CISCO-CONFIG-COPY-MIB`
- `CISCO-CONFIG-MAN-MIB`
- `CISCO-CONTEXT-MAPPING-MIB`
- `CISCO-DATA-COLLECTION-MIB`
- `CISCO-DIAL-CONTROL-MIB`
- `CISCO-DOT3-OAM-MIB`
- `CISCO-DYNAMIC-TEMPLATE-MIB`
- `CISCO-DYNAMIC-TEMPLATE-TC-MIB`
- `CISCO-EIGRP-MIB`
- `CISCO-EMBEDDED-EVENT-MGR-MIB`
- `CISCO-ENHANCED-MEMPOOL-MIB`
- `CISCO-ENTITY-ALARM-MIB`
- `CISCO-ENTITY-EXT-MIB`
- `CISCO-ENTITY-FRU-CONTROL-MIB`
- `CISCO-ENTITY-QFP-MIB`
- `CISCO-ENTITY-SENSOR-MIB`
- `CISCO-ENTITY-VENDORTYPE-OID-MIB`
- `CISCO-ENVMON-MIB`
- `CISCO-ETHER-CFM-MIB`
- `CISCO-ETHERLIKE-EXT-MIB`
- `CISCO-FIREWALL-TC`
- `CISCO-FLASH-MIB`
- `CISCO-FTP-CLIENT-MIB`
- `CISCO-HSRP-EXT-MIB`
- `CISCO-HSRP-MIB`
- `CISCO-IETF-ATM2-PVCTRAP-MIB`
- `CISCO-IETF-ATM2-PVCTRAP-MIB-EXTN`
- `CISCO-IETF-BFD-MIB`
- `CISCO-IETF-FRR-MIB`
- `CISCO-IETF-ISIS-MIB`
- `CISCO-IETF-MPLS-ID-STD-03-MIB`
- `CISCO-IETF-MPLS-TE-EXT-STD-03-MIB`
- `CISCO-IETF-PW-ATM-MIB`
- `CISCO-IETF-PW-ENET-MIB`
- `CISCO-IETF-PW-MIB`
- `CISCO-IETF-PW-MPLS-MIB`
- `CISCO-IETF-PW-TC-MIB`
- `CISCO-IETF-PW-TDM-MIB`
- `CISCO-IF-EXTENSION-MIB`
- `CISCO-IGMP-FILTER-MIB`
- `CISCO-IMAGE-LICENSE-MGMT-MIB`
- `CISCO-IMAGE-MIB`
- `CISCO-IP-LOCAL-POOL-MIB`
- `CISCO-IP-TAP-MIB`
- `CISCO-IP-URPF-MIB`
- `CISCO-IPMROUTE-MIB`
- `CISCO-IPSEC-FLOW-MONITOR-MIB`
- `CISCO-IPSEC-MIB`
- `CISCO-IPSEC-POLICY-MAP-MIB`
- `CISCO-IPSLA-AUTOMEASURE-MIB`
- `CISCO-IPSLA-ECHO-MIB`
- `CISCO-IPSLA-JITTER-MIB`
- `CISCO-IPSLA-TC-MIB`
- `CISCO-LICENSE-MGMT-MIB`
- `CISCO-MEDIA-GATEWAY-MIB`
- `CISCO-MPLS-LSR-EXT-STD-MIB`
- `CISCO-MPLS-TC-EXT-STD-MIB`
- `CISCO-NBAR-PROTOCOL-DISCOVERY-MIB`
- `CISCO-NETSYNC-MIB`
- `CISCO-NTP-MIB`
- `CISCO-OSPF-MIB`
- `CISCO-OSPF-TRAP-MIB`
- `CISCO-PIM-MIB`
- `CISCO-PING-MIB`
- `CISCO-POWER-ETHERNET-EXT-MIB`
- `CISCO-PROCESS-MIB`
- `CISCO-PRODUCTS-MIB`
- `CISCO-PTP-MIB`
- `CISCO-QOS-PIB-MIB`
- `CISCO-RADIUS-EXT-MIB`
- `CISCO-RF-MIB`
- `CISCO-RTTMON-MIB`
- `CISCO-RTTMON-TC-MIB`
- `CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB`
- `CISCO-SESS-BORDER-CTRLR-STATS-MIB`
- `CISCO-SIP-UA-MIB`
- `CISCO-SMI`
- `CISCO-SONET-MIB`
- `CISCO-ST-TC`
- `CISCO-STACKWISE-MIB`
- `CISCO-STP-EXTENSIONS-MIB`
- `CISCO-SUBSCRIBER-IDENTITY-TC-MIB`
- `CISCO-SUBSCRIBER-SESSION-MIB`
- `CISCO-SUBSCRIBER-SESSION-TC-MIB`
- `CISCO-SYSLOG-MIB`
- `CISCO-TAP2-MIB`
- `CISCO-TC`
- `CISCO-UBE-MIB`
- `CISCO-UNIFIED-FIREWALL-MIB`
- `CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB`
- `CISCO-VLAN-MEMBERSHIP-MIB`
- `CISCO-VOICE-COMMON-DIAL-CONTROL-MIB`
- `CISCO-VOICE-DIAL-CONTROL-MIB`
- `CISCO-VOICE-DNIS-MIB`
- `CISCO-VPDN-MGMT-MIB`
- `CISCO-VTP-MIB`
- `DIAL-CONTROL-MIB`
- `DIFFSERV-DSCP-TC`
- `DIFFSERV-MIB`
- `DISMAN-EVENT-MIB`
- `DISMAN-EXPRESSION-MIB`
- `DRAFT-MSDP-MIB`
- `DS1-MIB`
- `DS3-MIB`
- `ENTITY-MIB`
- `ENTITY-SENSOR-MIB`
- `ENTITY-STATE-MIB`
- `ENTITY-STATE-TC-MIB`
- `ETHER-WIS`
- `EXPRESSION-MIB`
- `EtherLike-MIB`
- `FRAME-RELAY-DTE-MIB`
- `HCNUM-TC`
- `IANA-ADDRESS-FAMILY-NUMBERS-MIB`
- `IANA-RTPROTO-MIB`
- `IANAifType-MIB`
- `IEEE8021-TC-MIB`
- `IF-MIB`
- `IGMP-STD-MIB`
- `INET-ADDRESS-MIB`
- `INT-SERV-MIB`
- `INTEGRATED-SERVICES-MIB`
- `IP-FORWARD-MIB`
- `IP-MIB`
- `IPMROUTE-STD-MIB`
- `IPV6-FLOW-LABEL-MIB`
- `LLDP-MIB`
- `MPLS-L3VPN-STD-MIB`
- `MPLS-LDP-GENERIC-STD-MIB`
- `MPLS-LDP-STD-MIB`
- `MPLS-LSR-STD-MIB`
- `MPLS-TC-MIB`
- `MPLS-TC-STD-MIB`
- `MPLS-TE-STD-MIB`
- `MPLS-VPN-MIB`
- `NHRP-MIB`
- `NOTIFICATION-LOG-MIB`
- `OSPF-MIB`
- `OSPF-TRAP-MIB`
- `P-BRIDGE-MIB`
- `PIM-MIB`
- `POWER-ETHERNET-MIB`
- `PerfHist-TC-MIB`
- `Q-BRIDGE-MIB`
- `RFC-1212`
- `RFC-1215`
- `RFC1155-SMI`
- `RFC1213-MIB`
- `RFC1315-MIB`
- `RMON-MIB`
- `RMON2-MIB`
- `RSVP-MIB`
- `SNMP-FRAMEWORK-MIB`
- `SNMP-PROXY-MIB`
- `SNMP-TARGET-MIB`
- `SNMPv2-MIB`
- `SNMPv2-TC`
- `SONET-MIB`
- `TCP-MIB`
- `TOKEN-RING-RMON-MIB`
- `TOKENRING-MIB`
- `TUNNEL-MIB`
- `UDP-MIB`
- `VPN-TC-STD-MIB`

---

## 2. Functional MIB reference

Categorized field guide to all 184 MIBs in `17181/MIBS/`. Conventions: `CISCO-*` MIBs are Cisco-proprietary (enterprise OID `1.3.6.1.4.1.9`); others are IETF/IEEE/IANA standards. `-TC` / `TC-MIB` modules contain only textual conventions (data types) and have no instrumented objects of their own.

### 2.1. SMI / framework / textual conventions

These are the foundation modules. They define data types and OID anchors used by every other MIB. None of them produce telemetry on their own.

| MIB | Role |
|---|---|
| `RFC1155-SMI` | SMIv1 macro definitions (legacy MIB compiler input). |
| `RFC-1212` | SMIv1 concise object definition format. |
| `RFC-1215` | SMIv1 trap definition format. |
| `SNMPv2-TC` | Standard SMIv2 textual conventions (`DisplayString`, `RowStatus`, `TimeStamp`, etc.). |
| `SNMPv2-MIB` | Core `system`, `snmp`, `snmpSet` groups (sysUpTime, sysName, snmpInPkts…). |
| `HCNUM-TC` | High-Capacity number TC (`Counter64`-derived `CounterBasedGauge64`). |
| `IANAifType-MIB` | IANA-maintained interface-type enumeration (`ethernetCsmacd(6)`, etc.). |
| `IANA-ADDRESS-FAMILY-NUMBERS-MIB` | AFI registry (IPv4=1, IPv6=2…). |
| `IANA-RTPROTO-MIB` | Routing protocol enumeration (BGP, OSPF, ISIS…). |
| `INET-ADDRESS-MIB` | `InetAddressType` / `InetAddress` TC for protocol-agnostic addressing. |
| `IPV6-FLOW-LABEL-MIB` | TC for IPv6 20-bit flow label. |
| `IEEE8021-TC-MIB` | IEEE 802.1 textual conventions (port lists, priority, etc.). |
| `CISCO-SMI` | Cisco enterprise OID anchor (`ciscoMgmt`, `ciscoExperiment`, `ciscoProducts`). |
| `CISCO-TC` | Cisco-wide textual conventions (e.g. `Unsigned32`, `CountryCode`). |
| `CISCO-ST-TC` | Cisco SONET TC. |
| `CISCO-CEF-TC` | Cisco CEF TC. |
| `CISCO-FIREWALL-TC` | Firewall TC. |
| `CISCO-PRODUCTS-MIB` | Per-platform `sysObjectID` registrations (one OID per Cisco product). |
| `CISCO-ENTITY-VENDORTYPE-OID-MIB` | OIDs identifying every FRU type (line cards, transceivers, fans). |
| `CISCO-SUBSCRIBER-IDENTITY-TC-MIB` | Subscriber-ID TC. |
| `CISCO-SUBSCRIBER-SESSION-TC-MIB` | Subscriber-session TC. |
| `CISCO-DYNAMIC-TEMPLATE-TC-MIB` | Dynamic-template TC. |
| `CISCO-CBP-TARGET-TC-MIB`, `CISCO-CBP-TC-MIB` | Class-Based Policy TC. |
| `CISCO-IPSLA-TC-MIB` | IP SLA TC. |
| `CISCO-RTTMON-TC-MIB` | RTTMON TC. |
| `CISCO-MPLS-TC-EXT-STD-MIB` | Cisco MPLS TC extensions. |
| `CISCO-IETF-PW-TC-MIB` | Pseudowire TC. |
| `MPLS-TC-MIB`, `MPLS-TC-STD-MIB` | Standard MPLS TC. |
| `ENTITY-STATE-TC-MIB` | RFC4268 state TC (admin/oper/usage/standby). |
| `DIFFSERV-DSCP-TC` | DSCP codepoint TC. |
| `PerfHist-TC-MIB` | 15-min/24-hr performance-history TC (used by SONET/DS1/DS3). |
| `VPN-TC-STD-MIB` | VPN TC (RD, RT formatting). |

---

### 2.2. SNMP protocol infrastructure

| MIB | Description |
|---|---|
| `SNMP-FRAMEWORK-MIB` | RFC3411 — engine ID, security model, message processing model. |
| `SNMP-TARGET-MIB` | RFC3413 — notification target/recipient address tables. |
| `SNMP-PROXY-MIB` | RFC3413 — SNMP proxy forwarding configuration. |
| `NOTIFICATION-LOG-MIB` | RFC3014 — local log of generated notifications/traps. |
| `DISMAN-EVENT-MIB` | RFC2981 — distributed event/alarm trigger objects (mteTrigger, mteEvent). |
| `DISMAN-EXPRESSION-MIB` | RFC2982 — derive new MIB objects via formulas over existing ones. |

> Note: in 16.5.1 the standalone `SNMP-COMMUNITY-MIB`, `SNMP-MPD-MIB`, `SNMP-NOTIFICATION-MIB`, `SNMP-USER-BASED-SM-MIB`, and `SNMP-VIEW-BASED-ACM-MIB` were dropped from the YANG conversion (still implemented natively).

---

### 2.3. System & host

| MIB | Description |
|---|---|
| `RFC1213-MIB` | The original "MIB-II" — `system`, `interfaces`, `at`, `ip`, `icmp`, `tcp`, `udp`, `egp`, `snmp` groups. Most leaves are now sourced from successor MIBs. |
| `SNMPv2-MIB` | Modern `system` group (sysDescr, sysObjectID, sysContact, sysName, sysLocation, sysServices, sysORTable). |
| `CISCO-PROCESS-MIB` | Per-process CPU and memory utilization (`cpmCPUTotal*`, `cpmProcessExtTable`). Critical for CPU monitoring. |
| `CISCO-ENHANCED-MEMPOOL-MIB` | Enhanced multi-pool memory utilization (Processor, IO, Reserve, Lsmpi). Replaces the older `CISCO-MEMORY-POOL-MIB`. |
| `CISCO-FLASH-MIB` | Flash device inventory and free/used bytes per partition. |
| `CISCO-IMAGE-MIB` | IOS image string and feature tags. |

---

### 2.4. Interfaces & link layer

| MIB | Description |
|---|---|
| `IF-MIB` | RFC2863 — `ifTable`/`ifXTable` (admin/oper status, counters, hi-counters, ifAlias, ifName). The single most-polled MIB. |
| `EtherLike-MIB` | RFC3635 — Ethernet-like statistics (CRC, FCS, late collisions, alignment errors). |
| `ETHER-WIS` | WAN Interface Sublayer for 10GBASE-W (SONET-framed Ethernet). |
| `CISCO-ETHERLIKE-EXT-MIB` | Extends `EtherLike-MIB` with Cisco-specific Ethernet counters. |
| `CISCO-IF-EXTENSION-MIB` | Cisco-specific `ifTable` extensions: input/output rates, CRC, throttles, resets, queue stats. |
| `CISCO-DOT3-OAM-MIB` | 802.3ah link-OAM extensions (loopback, link-monitoring events). |

---

### 2.5. Bridging, VLAN, STP

| MIB | Description |
|---|---|
| `BRIDGE-MIB` | RFC4188 — base 802.1D bridge group: STP state, FDB (mac address table), port table. |
| `P-BRIDGE-MIB` | RFC4363 — priority/traffic-class extensions to BRIDGE-MIB. |
| `Q-BRIDGE-MIB` | RFC4363 — VLAN-aware bridge: VLAN static/dynamic FDB, VLAN-membership ports, GVRP. |
| `CISCO-VTP-MIB` | VLAN Trunking Protocol — VTP domain, mode, revision, VLAN database. |
| `CISCO-VLAN-MEMBERSHIP-MIB` | Per-port VLAN membership (access/trunk, VMPS). |
| `CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB` | Maps VLAN ifIndex ↔ physical port ifIndex. |
| `CISCO-STP-EXTENSIONS-MIB` | UplinkFast, BackboneFast, BPDU guard/filter, root guard, loop guard, PortFast. |
| `CISCO-ETHER-CFM-MIB` | 802.1ag Connectivity Fault Management (MEPs, MAs, CCM stats, loopback/linktrace). |

---

### 2.6. LLDP / CDP discovery

| MIB | Description |
|---|---|
| `LLDP-MIB` | IEEE 802.1AB — Link Layer Discovery Protocol local/remote tables (chassis ID, port ID, neighbor capabilities). |
| `CISCO-CDP-MIB` | Cisco Discovery Protocol — `cdpCacheTable` (neighbor device, platform, capabilities, native VLAN, version). |

---

### 2.7. IP, TCP, UDP

| MIB | Description |
|---|---|
| `IP-MIB` | RFC4293 — IPv4 & IPv6 unified counters, address tables, netToMedia (ARP/ND). |
| `IP-FORWARD-MIB` | RFC4292 — IPv4/v6 forwarding (RIB) table — `inetCidrRouteTable`. |
| `TCP-MIB` | RFC4022 — TCP connection table & per-protocol counters. |
| `UDP-MIB` | RFC4113 — UDP listener table & datagram counters. |
| `TUNNEL-MIB` | RFC4087 — generic IP tunnel (GRE, IP-in-IP, 6to4) endpoint table. |
| `NHRP-MIB` | RFC2677 — Next Hop Resolution Protocol (used by DMVPN). |
| `CISCO-IP-URPF-MIB` | uRPF drop/check counters per interface. |
| `CISCO-IP-LOCAL-POOL-MIB` | Local IP-address-pool usage (PPP/dialer/IKEv2). |

---

### 2.8. Routing protocols

| MIB | Description |
|---|---|
| `OSPF-MIB` | RFC4750 — OSPFv2 area, neighbor, LSA, virtual-link tables. |
| `OSPF-TRAP-MIB` | OSPFv2 notification varbinds. |
| `CISCO-OSPF-MIB` | Cisco OSPFv2 extensions (NSSA, sham-link, SPF stats). |
| `CISCO-OSPF-TRAP-MIB` | Cisco OSPF trap extensions. |
| `BGP4-MIB` | RFC4273 — BGPv4 peer table, received-prefixes, basic counters. |
| `CISCO-BGP4-MIB` | Cisco BGP4 extensions: per-AF peer state, capabilities, route-refresh, GR. |
| `CISCO-BGP-POLICY-ACCOUNTING-MIB` | BGP policy accounting buckets. |
| `CISCO-EIGRP-MIB` | EIGRP topology, neighbors, traffic stats per AS. |
| `CISCO-IETF-ISIS-MIB` | IS-IS LSDB, adjacencies (Cisco implementation of draft-ietf-isis-wg-mib). |
| `IPMROUTE-STD-MIB`, `CISCO-IPMROUTE-MIB` | IPv4 multicast routing tables (mroute, MFIB). |
| `CISCO-IETF-FRR-MIB` | MPLS-TE / IP Fast Reroute backup-tunnel state. |
| `CISCO-IETF-BFD-MIB` | RFC7331 — BFD session table, discriminators, state. |

---

### 2.9. Multicast

| MIB | Description |
|---|---|
| `IGMP-STD-MIB` | RFC2933 — IGMP cache, interface table, joins. |
| `CISCO-IGMP-FILTER-MIB` | IGMP filter / max-groups / per-port joins. |
| `PIM-MIB` | RFC5060 — PIM neighbors, interfaces, RP-set. |
| `CISCO-PIM-MIB` | Cisco PIM extensions (BSR, Auto-RP, register stats). |
| `DRAFT-MSDP-MIB` | MSDP peers, SA cache (for inter-domain multicast). |

---

### 2.10. MPLS / L3VPN / Pseudowire

| MIB | Description |
|---|---|
| `MPLS-LSR-STD-MIB` | RFC3813 — generic MPLS LSR: in/out segments, XC table, label stack. |
| `MPLS-LDP-STD-MIB` | RFC3815 — LDP entity, peer, session, advertisement tables. |
| `MPLS-LDP-GENERIC-STD-MIB` | LDP MIB for "generic" label space (Ethernet/PPP/HDLC). |
| `MPLS-TE-STD-MIB` | RFC3812 — MPLS-TE tunnel head-end tables, ERO/RRO. |
| `MPLS-L3VPN-STD-MIB` | RFC4382 — L3VPN VRFs, RTs, per-VRF route counters. |
| `MPLS-VPN-MIB` | Pre-standard L3VPN MIB (still queried by older NMS). |
| `CISCO-MPLS-LSR-EXT-STD-MIB` | Cisco MPLS-LSR extensions. |
| `CISCO-IETF-MPLS-ID-STD-03-MIB` | MPLS identifiers (router-id, LSR-id) per draft-03. |
| `CISCO-IETF-MPLS-TE-EXT-STD-03-MIB` | MPLS-TE extensions per draft-03 (SRLG, FRR detail). |
| `CISCO-IETF-PW-MIB` | Pseudowire generic table (peer, encap, status). |
| `CISCO-IETF-PW-MPLS-MIB` | PW over MPLS PSN. |
| `CISCO-IETF-PW-ENET-MIB` | Ethernet PW (VPLS / EoMPLS). |
| `CISCO-IETF-PW-ATM-MIB` | ATM PW. |
| `CISCO-IETF-PW-TDM-MIB` | TDM (DS1/DS3/SONET) PW (CESoPSN, SAToP). |

---

### 2.11. QoS, DiffServ, NBAR

| MIB | Description |
|---|---|
| `DIFFSERV-MIB` | RFC3289 — DiffServ classifiers, meters, queues, schedulers. |
| `INTEGRATED-SERVICES-MIB`, `INT-SERV-MIB` | RFC2213 — RSVP/IntServ flow & reservation tables. |
| `RSVP-MIB` | RFC2206 — RSVP sessions, senders, neighbors. |
| `CISCO-CBP-TARGET-MIB` | Class-Based-Policy attachment points (per-interface service-policy state). |
| `CISCO-QOS-PIB-MIB` | Cisco QoS Policy Information Base. |
| `CISCO-NBAR-PROTOCOL-DISCOVERY-MIB` | NBAR per-protocol byte/packet counters per interface. |

---

### 2.12. Security / IPSec / Firewall / AAA

| MIB | Description |
|---|---|
| `CISCO-IPSEC-MIB` | IPsec global stats, IKE/Phase-1 SA table. |
| `CISCO-IPSEC-FLOW-MONITOR-MIB` | Per-tunnel IPsec SA counters (legacy IPsec MIB). |
| `CISCO-IPSEC-POLICY-MAP-MIB` | IPsec policy-map / crypto-map definitions. |
| `CISCO-UNIFIED-FIREWALL-MIB` | ZBFW / inspection engine policy and counter tables. |
| `CISCO-AAA-SERVER-MIB` | Configured RADIUS/TACACS+ servers, request/response stats. |
| `CISCO-AAA-SESSION-MIB` | Per-AAA-session table (subscriber accounting). |
| `CISCO-RADIUS-EXT-MIB` | Cisco RADIUS extensions (CoA, Accounting). |

---

### 2.13. HSRP, VRRP, redundancy

| MIB | Description |
|---|---|
| `CISCO-HSRP-MIB` | HSRP groups, virtual IP/MAC, state, priority. |
| `CISCO-HSRP-EXT-MIB` | HSRP tracking, secondary virtual IPs, IPv6 HSRP. |
| `CISCO-RF-MIB` | Redundancy Framework — active/standby supervisor state, switchover history. |

---

### 2.14. Entity / hardware / environment

| MIB | Description |
|---|---|
| `ENTITY-MIB` | RFC6933 — physical entity tree (chassis → modules → ports), entity-aliasing. |
| `ENTITY-SENSOR-MIB` | RFC3433 — generic sensor table (temperature, voltage, current, dBm). |
| `ENTITY-STATE-MIB` | RFC4268 — admin/oper/usage/alarm/standby state per entity. |
| `CISCO-ENTITY-EXT-MIB` | Extra per-entity attributes (HA, monitoring). |
| `CISCO-ENTITY-FRU-CONTROL-MIB` | Power, reset, OIR control of FRUs (modules, fans, PSUs). |
| `CISCO-ENTITY-SENSOR-MIB` | Cisco extensions to ENTITY-SENSOR-MIB (threshold severity). |
| `CISCO-ENTITY-ALARM-MIB` | Alarm severity, source, description per entity. |
| `CISCO-ENTITY-QFP-MIB` | Quantum Flow Processor utilization, throughput, drops. |
| `CISCO-ENVMON-MIB` | Legacy environmental monitor (temperature, voltage, fan, supply state). |

---

### 2.15. PoE (Power-over-Ethernet)

| MIB | Description |
|---|---|
| `POWER-ETHERNET-MIB` | RFC3621 — PSE port table, power/class/priority, MainPse table. |
| `CISCO-POWER-ETHERNET-EXT-MIB` | Cisco PoE+ / UPOE extensions (per-port watts, policing, perpetual-PoE). |

---

### 2.16. Stackwise

| MIB | Description |
|---|---|
| `CISCO-STACKWISE-MIB` | StackWise / StackWise-Virtual member table, role, port speed, switchover events. |

---

### 2.17. SONET / DS1 / DS3 / ATM / Frame Relay

| MIB | Description |
|---|---|
| `SONET-MIB` | RFC3592 — SONET/SDH section, line, far-end, path layer counters. |
| `CISCO-SONET-MIB` | Cisco SONET extensions (BER, K1/K2, APS). |
| `DS1-MIB` | RFC4805 — T1/E1 near/far-end ES, SES, UAS counters. |
| `DS3-MIB` | RFC3896 — T3/E3 ES, SES, UAS counters, line/path layer. |
| `ATM-MIB` | RFC2515 — ATM interfaces, VCL/VPL, AAL5 stats. |
| `ATM-TC-MIB`, `ATM-FORUM-TC-MIB` | ATM textual conventions (cell types, traffic descriptors). |
| `CISCO-ATM-EXT-MIB` | Cisco ATM extensions (CoS queues, OAM). |
| `CISCO-ATM-QOS-MIB` | ATM QoS class table. |
| `CISCO-ATM-PVCTRAP-EXTN-MIB` | ATM PVC up/down trap extensions. |
| `CISCO-IETF-ATM2-PVCTRAP-MIB`, `-EXTN` | ATM2 PVC trap/extension. |
| `CISCO-AAL5-MIB` | AAL5 segmentation/reassembly counters. |
| `FRAME-RELAY-DTE-MIB` | RFC2115 — Frame Relay DLCI table, PVC stats. |
| `TOKENRING-MIB`, `TOKEN-RING-RMON-MIB`, `RFC1315-MIB` | Token Ring (legacy, retained for archive). |

---

### 2.18. IP SLA / RTTMON / ping

| MIB | Description |
|---|---|
| `CISCO-PING-MIB` | Schedules ICMP/ping operations and reads results. |
| `CISCO-RTTMON-MIB` | RTTMON / IP SLA — operation table, history, statistics, reactions, latest-RTT. The main **IP SLA** instrumentation MIB. |
| `CISCO-IPSLA-AUTOMEASURE-MIB` | IP SLA "auto" measurement profile config. |
| `CISCO-IPSLA-ECHO-MIB` | IP SLA echo (UDP echo, ICMP echo). |
| `CISCO-IPSLA-JITTER-MIB` | IP SLA UDP/ICMP jitter (one-way / two-way). |

---

### 2.19. RMON / Expression / DISMAN events

| MIB | Description |
|---|---|
| `RMON-MIB` | RFC2819 — RMON1: statistics, history, alarm, event, hostTopN, matrix, filter, capture. |
| `RMON2-MIB` | RFC4502 — RMON2: protocolDir, network/application-layer host & matrix. |
| `EXPRESSION-MIB` | Same as `DISMAN-EXPRESSION-MIB` — derived objects via formulas. |

---

### 2.20. Voice / SBC / dial / media gateway

| MIB | Description |
|---|---|
| `CISCO-MEDIA-GATEWAY-MIB` | Media gateway (MGCP/H.248) state. |
| `CISCO-SIP-UA-MIB` | SIP user-agent stats (registrations, calls, retransmits). |
| `CISCO-UBE-MIB` | Unified Border Element call counters and resource state. |
| `CISCO-SESS-BORDER-CTRLR-STATS-MIB` | SBC global session statistics. |
| `CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB` | SBC per-call statistics. |
| `DIAL-CONTROL-MIB` | RFC2128 — generic dial-control peer table. |
| `CISCO-DIAL-CONTROL-MIB` | Cisco dial-control extensions (call history, modem stats). |
| `CISCO-VOICE-COMMON-DIAL-CONTROL-MIB` | Common voice dial-control attributes. |
| `CISCO-VOICE-DIAL-CONTROL-MIB` | Voice-specific dial-peer table. |
| `CISCO-VOICE-DNIS-MIB` | DNIS-mapped voice peers. |

---

### 2.21. Subscriber / dynamic templates / VPDN / IP pools

| MIB | Description |
|---|---|
| `CISCO-SUBSCRIBER-SESSION-MIB` | Per-subscriber session state and stats (BNG/ISG). |
| `CISCO-DYNAMIC-TEMPLATE-MIB` | Dynamic-template definitions and instance bindings. |
| `CISCO-CONTEXT-MAPPING-MIB` | Maps SNMP contexts to internal feature contexts. |
| `CISCO-VPDN-MGMT-MIB` | Virtual Private Dial Network — L2TP/PPTP tunnels & sessions. |

---

### 2.22. PTP / NTP / NetSync (timing)

| MIB | Description |
|---|---|
| `CISCO-PTP-MIB` | IEEE 1588 PTP — clock dataset, port dataset, parent/foreign masters. |
| `CISCO-NTP-MIB` | NTP associations, leap, stratum, offset, jitter. |
| `CISCO-NETSYNC-MIB` | SyncE / Network synchronization clock-selection state and ESMC QL. |

---

### 2.23. Image / config / file / EEM / syslog / license

| MIB | Description |
|---|---|
| `CISCO-CONFIG-COPY-MIB` | Trigger copy operations (running ↔ startup ↔ tftp/scp/ftp). |
| `CISCO-CONFIG-MAN-MIB` | Last-changed / last-saved running-config timestamps & traps. |
| `CISCO-FTP-CLIENT-MIB` | Built-in FTP client status. |
| `CISCO-DATA-COLLECTION-MIB` | Bulk data collection (BulkFile periodic dump) — successor to `CISCO-BULK-FILE-MIB`. |
| `CISCO-EMBEDDED-EVENT-MGR-MIB` | EEM applets / policies registration & last-execution stats. |
| `CISCO-SYSLOG-MIB` | Syslog history table & configuration. |
| `CISCO-LICENSE-MGMT-MIB` | Smart Licensing (slot-based) state. |
| `CISCO-IMAGE-LICENSE-MGMT-MIB` | Older image-based licensing (RTU). |

---

### 2.24. Lawful intercept

| MIB | Description |
|---|---|
| `CISCO-TAP2-MIB` | Lawful-intercept tap administration (mediation device, stream control). |
| `CISCO-IP-TAP-MIB` | IP-stream lawful-intercept tap (filter table). |

---

### 2.25. Misc / legacy

| MIB | Description |
|---|---|
| `RFC1213-MIB` | The original MIB-II (kept for legacy NMS). |
| `RMON-MIB` / `RMON2-MIB` / `TOKEN-RING-RMON-MIB` | RMON family (see §19). |
| `EtherLike-MIB` | (see §4). |
| `BRIDGE-MIB` | (see §5). |

---

---

## 3. Per-platform availability matrix

Source: `reference/xe/17181/capability-*.xml` — each file is the NETCONF `<hello>` capability advertisement for one platform family. Every `module=<MIB>` query parameter declares a MIB the platform implements (i.e. an SNMP agent will respond to walks of that MIB).

- Capability XMLs found: **10**
- Platforms advertising MIBs: **9**
- `wireless` advertises **no** SMIv2 MIBs in NETCONF capabilities — it ships YANG-only capabilities.
- Total distinct MIBs across all platforms: **183**

### 3.1 MIB count per platform

| Platform | MIBs advertised | Notes |
|---|---:|---|
| `asr1k` | 179 | ASR 1000 series (RP/ESP) |
| `c8000v` | 179 | Catalyst 8000V (virtual router) / SD-WAN cEdge |
| `c8500` | 179 | Catalyst 8500 series |
| `cat9200` | 140 | Catalyst 9200 access switch |
| `cat9k` | 140 | Catalyst 9300 / 9400 / 9500 / 9600 family |
| `ess3x00` | 180 | Embedded Services Switch ESS3x00 |
| `ie3x00` | 180 | Industrial Ethernet IE3x00 |
| `ir1101` | 179 | IR1101 ruggedized router |
| `isr1k` | 179 | ISR1000 series |
| `wireless` | 0 | Wireless Controller (9800) — YANG-only capabilities |

### 3.2 Core MIBs common to every non-wireless platform (136)

Baseline MIBs every routing/switching IOS XE platform implements.

- `BGP4-MIB`
- `BRIDGE-MIB`
- `CISCO-AAA-SERVER-MIB`
- `CISCO-AAA-SESSION-MIB`
- `CISCO-BGP-POLICY-ACCOUNTING-MIB`
- `CISCO-BGP4-MIB`
- `CISCO-BULK-FILE-MIB`
- `CISCO-CBP-TARGET-MIB`
- `CISCO-CBP-TARGET-TC-MIB`
- `CISCO-CBP-TC-MIB`
- `CISCO-CDP-MIB`
- `CISCO-CEF-MIB`
- `CISCO-CEF-TC`
- `CISCO-CONFIG-COPY-MIB`
- `CISCO-CONFIG-MAN-MIB`
- `CISCO-CONTEXT-MAPPING-MIB`
- `CISCO-DATA-COLLECTION-MIB`
- `CISCO-DOT3-OAM-MIB`
- `CISCO-DYNAMIC-TEMPLATE-MIB`
- `CISCO-DYNAMIC-TEMPLATE-TC-MIB`
- `CISCO-EIGRP-MIB`
- `CISCO-EMBEDDED-EVENT-MGR-MIB`
- `CISCO-ENHANCED-MEMPOOL-MIB`
- `CISCO-ENTITY-ALARM-MIB`
- `CISCO-ENTITY-EXT-MIB`
- `CISCO-ENTITY-FRU-CONTROL-MIB`
- `CISCO-ENTITY-QFP-MIB`
- `CISCO-ENTITY-SENSOR-MIB`
- `CISCO-ENTITY-VENDORTYPE-OID-MIB`
- `CISCO-ETHER-CFM-MIB`
- `CISCO-ETHERLIKE-EXT-MIB`
- `CISCO-FIREWALL-TC`
- `CISCO-FLASH-MIB`
- `CISCO-FTP-CLIENT-MIB`
- `CISCO-HSRP-EXT-MIB`
- `CISCO-HSRP-MIB`
- `CISCO-IETF-BFD-MIB`
- `CISCO-IETF-ISIS-MIB`
- `CISCO-IF-EXTENSION-MIB`
- `CISCO-IGMP-FILTER-MIB`
- `CISCO-IMAGE-LICENSE-MGMT-MIB`
- `CISCO-IMAGE-MIB`
- `CISCO-IP-LOCAL-POOL-MIB`
- `CISCO-IP-TAP-MIB`
- `CISCO-IP-URPF-MIB`
- `CISCO-IPMROUTE-MIB`
- `CISCO-IPSEC-FLOW-MONITOR-MIB`
- `CISCO-IPSEC-MIB`
- `CISCO-IPSEC-POLICY-MAP-MIB`
- `CISCO-IPSLA-AUTOMEASURE-MIB`
- `CISCO-IPSLA-ECHO-MIB`
- `CISCO-IPSLA-JITTER-MIB`
- `CISCO-IPSLA-TC-MIB`
- `CISCO-LICENSE-MGMT-MIB`
- `CISCO-MEDIA-GATEWAY-MIB`
- `CISCO-NBAR-PROTOCOL-DISCOVERY-MIB`
- `CISCO-NETSYNC-MIB`
- `CISCO-NTP-MIB`
- `CISCO-OSPF-MIB`
- `CISCO-OSPF-TRAP-MIB`
- `CISCO-PIM-MIB`
- `CISCO-PING-MIB`
- `CISCO-PROCESS-MIB`
- `CISCO-PRODUCTS-MIB`
- `CISCO-PTP-MIB`
- `CISCO-QOS-PIB-MIB`
- `CISCO-RADIUS-EXT-MIB`
- `CISCO-RF-MIB`
- `CISCO-RTTMON-MIB`
- `CISCO-RTTMON-TC-MIB`
- `CISCO-SIP-UA-MIB`
- `CISCO-SMI`
- `CISCO-ST-TC`
- `CISCO-STP-EXTENSIONS-MIB`
- `CISCO-SYSLOG-MIB`
- `CISCO-TAP2-MIB`
- `CISCO-TC`
- `CISCO-UBE-MIB`
- `CISCO-UNIFIED-FIREWALL-MIB`
- `CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB`
- `CISCO-VLAN-MEMBERSHIP-MIB`
- `CISCO-VPDN-MGMT-MIB`
- `CISCO-VTP-MIB`
- `DIFFSERV-DSCP-TC`
- `DIFFSERV-MIB`
- `DISMAN-EVENT-MIB`
- `DISMAN-EXPRESSION-MIB`
- `DRAFT-MSDP-MIB`
- `ENTITY-MIB`
- `ENTITY-SENSOR-MIB`
- `ENTITY-STATE-MIB`
- `ENTITY-STATE-TC-MIB`
- `ETHER-WIS`
- `EXPRESSION-MIB`
- `EtherLike-MIB`
- `HCNUM-TC`
- `IANA-ADDRESS-FAMILY-NUMBERS-MIB`
- `IANA-RTPROTO-MIB`
- `IANAifType-MIB`
- `IF-MIB`
- `IGMP-STD-MIB`
- `INET-ADDRESS-MIB`
- `INT-SERV-MIB`
- `INTEGRATED-SERVICES-MIB`
- `IP-FORWARD-MIB`
- `IP-MIB`
- `IPMROUTE-STD-MIB`
- `IPV6-FLOW-LABEL-MIB`
- `LLDP-MIB`
- `MPLS-VPN-MIB`
- `NHRP-MIB`
- `NOTIFICATION-LOG-MIB`
- `OSPF-MIB`
- `OSPF-TRAP-MIB`
- `P-BRIDGE-MIB`
- `PIM-MIB`
- `PerfHist-TC-MIB`
- `Q-BRIDGE-MIB`
- `RFC-1212`
- `RFC-1215`
- `RFC1155-SMI`
- `RFC1213-MIB`
- `RFC1315-MIB`
- `RMON-MIB`
- `RMON2-MIB`
- `SNMP-FRAMEWORK-MIB`
- `SNMP-PROXY-MIB`
- `SNMP-TARGET-MIB`
- `SNMPv2-MIB`
- `SNMPv2-TC`
- `TCP-MIB`
- `TOKEN-RING-RMON-MIB`
- `TOKENRING-MIB`
- `TUNNEL-MIB`
- `UDP-MIB`
- `VPN-TC-STD-MIB`

### 3.3 Routing-family additions (routers, NOT on Cat9k switches)

43 MIBs the routing platforms expose that the Catalyst 9k switches do not (mostly WAN/voice/MPLS-TE/pseudowire):

- `ATM-FORUM-TC-MIB`
- `ATM-MIB`
- `ATM-TC-MIB`
- `CISCO-AAL5-MIB`
- `CISCO-ATM-EXT-MIB`
- `CISCO-ATM-PVCTRAP-EXTN-MIB`
- `CISCO-ATM-QOS-MIB`
- `CISCO-DIAL-CONTROL-MIB`
- `CISCO-IETF-ATM2-PVCTRAP-MIB`
- `CISCO-IETF-FRR-MIB`
- `CISCO-IETF-MPLS-ID-STD-03-MIB`
- `CISCO-IETF-MPLS-TE-EXT-STD-03-MIB`
- `CISCO-IETF-PW-ATM-MIB`
- `CISCO-IETF-PW-ENET-MIB`
- `CISCO-IETF-PW-MIB`
- `CISCO-IETF-PW-MPLS-MIB`
- `CISCO-IETF-PW-TC-MIB`
- `CISCO-IETF-PW-TDM-MIB`
- `CISCO-MPLS-LSR-EXT-STD-MIB`
- `CISCO-MPLS-TC-EXT-STD-MIB`
- `CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB`
- `CISCO-SESS-BORDER-CTRLR-STATS-MIB`
- `CISCO-SONET-MIB`
- `CISCO-SUBSCRIBER-IDENTITY-TC-MIB`
- `CISCO-SUBSCRIBER-SESSION-MIB`
- `CISCO-SUBSCRIBER-SESSION-TC-MIB`
- `CISCO-VOICE-COMMON-DIAL-CONTROL-MIB`
- `CISCO-VOICE-DIAL-CONTROL-MIB`
- `CISCO-VOICE-DNIS-MIB`
- `DIAL-CONTROL-MIB`
- `DS1-MIB`
- `DS3-MIB`
- `FRAME-RELAY-DTE-MIB`
- `IEEE8021-TC-MIB`
- `MPLS-L3VPN-STD-MIB`
- `MPLS-LDP-GENERIC-STD-MIB`
- `MPLS-LDP-STD-MIB`
- `MPLS-LSR-STD-MIB`
- `MPLS-TC-MIB`
- `MPLS-TC-STD-MIB`
- `MPLS-TE-STD-MIB`
- `RSVP-MIB`
- `SONET-MIB`

### 3.4 Cat9k vs ASR1k diff

**MIBs on `cat9k` but NOT on `asr1k` (4):**

- `CISCO-ENVMON-MIB`
- `CISCO-POWER-ETHERNET-EXT-MIB`
- `CISCO-STACKWISE-MIB`
- `POWER-ETHERNET-MIB`

**MIBs on `asr1k` but NOT on `cat9k` (43):**

- `ATM-FORUM-TC-MIB`
- `ATM-MIB`
- `ATM-TC-MIB`
- `CISCO-AAL5-MIB`
- `CISCO-ATM-EXT-MIB`
- `CISCO-ATM-PVCTRAP-EXTN-MIB`
- `CISCO-ATM-QOS-MIB`
- `CISCO-DIAL-CONTROL-MIB`
- `CISCO-IETF-ATM2-PVCTRAP-MIB`
- `CISCO-IETF-FRR-MIB`
- `CISCO-IETF-MPLS-ID-STD-03-MIB`
- `CISCO-IETF-MPLS-TE-EXT-STD-03-MIB`
- `CISCO-IETF-PW-ATM-MIB`
- `CISCO-IETF-PW-ENET-MIB`
- `CISCO-IETF-PW-MIB`
- `CISCO-IETF-PW-MPLS-MIB`
- `CISCO-IETF-PW-TC-MIB`
- `CISCO-IETF-PW-TDM-MIB`
- `CISCO-MPLS-LSR-EXT-STD-MIB`
- `CISCO-MPLS-TC-EXT-STD-MIB`
- `CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB`
- `CISCO-SESS-BORDER-CTRLR-STATS-MIB`
- `CISCO-SONET-MIB`
- `CISCO-SUBSCRIBER-IDENTITY-TC-MIB`
- `CISCO-SUBSCRIBER-SESSION-MIB`
- `CISCO-SUBSCRIBER-SESSION-TC-MIB`
- `CISCO-VOICE-COMMON-DIAL-CONTROL-MIB`
- `CISCO-VOICE-DIAL-CONTROL-MIB`
- `CISCO-VOICE-DNIS-MIB`
- `DIAL-CONTROL-MIB`
- `DS1-MIB`
- `DS3-MIB`
- `FRAME-RELAY-DTE-MIB`
- `IEEE8021-TC-MIB`
- `MPLS-L3VPN-STD-MIB`
- `MPLS-LDP-GENERIC-STD-MIB`
- `MPLS-LDP-STD-MIB`
- `MPLS-LSR-STD-MIB`
- `MPLS-TC-MIB`
- `MPLS-TC-STD-MIB`
- `MPLS-TE-STD-MIB`
- `RSVP-MIB`
- `SONET-MIB`

### 3.5 Full availability matrix

Legend: ✓ = MIB advertised in the platform's capability XML, — = not advertised. `wireless` is omitted (no SMIv2 MIBs declared).

| MIB | asr1k | c8000v | c8500 | cat9200 | cat9k | ess3x00 | ie3x00 | ir1101 | isr1k |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ATM-FORUM-TC-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `ATM-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `ATM-TC-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `BGP4-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `BRIDGE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-AAA-SERVER-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-AAA-SESSION-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-AAL5-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ATM-EXT-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ATM-PVCTRAP-EXTN-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ATM-QOS-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-BGP-POLICY-ACCOUNTING-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-BGP4-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-BULK-FILE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CBP-TARGET-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CBP-TARGET-TC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CBP-TC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CDP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CEF-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CEF-TC` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CONFIG-COPY-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CONFIG-MAN-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-CONTEXT-MAPPING-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-DATA-COLLECTION-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-DIAL-CONTROL-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-DOT3-OAM-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-DYNAMIC-TEMPLATE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-DYNAMIC-TEMPLATE-TC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-EIGRP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-EMBEDDED-EVENT-MGR-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENHANCED-MEMPOOL-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENTITY-ALARM-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENTITY-EXT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENTITY-FRU-CONTROL-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENTITY-QFP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENTITY-SENSOR-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENTITY-VENDORTYPE-OID-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ENVMON-MIB` | — | — | — | ✓ | ✓ | ✓ | ✓ | — | — |
| `CISCO-ETHER-CFM-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ETHERLIKE-EXT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-FIREWALL-TC` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-FLASH-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-FTP-CLIENT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-HSRP-EXT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-HSRP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-ATM2-PVCTRAP-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-BFD-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-FRR-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-ISIS-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-MPLS-ID-STD-03-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-MPLS-TE-EXT-STD-03-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-PW-ATM-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-PW-ENET-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-PW-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-PW-MPLS-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-PW-TC-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IETF-PW-TDM-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IF-EXTENSION-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IGMP-FILTER-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IMAGE-LICENSE-MGMT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IMAGE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IP-LOCAL-POOL-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IP-TAP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IP-URPF-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPMROUTE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPSEC-FLOW-MONITOR-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPSEC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPSEC-POLICY-MAP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPSLA-AUTOMEASURE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPSLA-ECHO-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPSLA-JITTER-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-IPSLA-TC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-LICENSE-MGMT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-MEDIA-GATEWAY-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-MPLS-LSR-EXT-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-MPLS-TC-EXT-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-NBAR-PROTOCOL-DISCOVERY-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-NETSYNC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-NTP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-OSPF-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-OSPF-TRAP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-PIM-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-PING-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-POWER-ETHERNET-EXT-MIB` | — | — | — | ✓ | ✓ | — | — | — | — |
| `CISCO-PROCESS-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-PRODUCTS-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-PTP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-QOS-PIB-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-RADIUS-EXT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-RF-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-RTTMON-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-RTTMON-TC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SESS-BORDER-CTRLR-STATS-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SIP-UA-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SMI` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SONET-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-ST-TC` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-STACKWISE-MIB` | — | — | — | ✓ | ✓ | — | — | — | — |
| `CISCO-STP-EXTENSIONS-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SUBSCRIBER-IDENTITY-TC-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SUBSCRIBER-SESSION-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SUBSCRIBER-SESSION-TC-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-SYSLOG-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-TAP2-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-TC` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-UBE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-UNIFIED-FIREWALL-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-VLAN-IFTABLE-RELATIONSHIP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-VLAN-MEMBERSHIP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-VOICE-COMMON-DIAL-CONTROL-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-VOICE-DIAL-CONTROL-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-VOICE-DNIS-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `CISCO-VPDN-MGMT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `CISCO-VTP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `DIAL-CONTROL-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `DIFFSERV-DSCP-TC` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `DIFFSERV-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `DISMAN-EVENT-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `DISMAN-EXPRESSION-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `DRAFT-MSDP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `DS1-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `DS3-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `ENTITY-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ENTITY-SENSOR-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ENTITY-STATE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ENTITY-STATE-TC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `ETHER-WIS` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `EXPRESSION-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `EtherLike-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `FRAME-RELAY-DTE-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `HCNUM-TC` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IANA-ADDRESS-FAMILY-NUMBERS-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IANA-RTPROTO-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IANAifType-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IEEE8021-TC-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `IF-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IGMP-STD-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `INET-ADDRESS-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `INT-SERV-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `INTEGRATED-SERVICES-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IP-FORWARD-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IPMROUTE-STD-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `IPV6-FLOW-LABEL-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `LLDP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `MPLS-L3VPN-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `MPLS-LDP-GENERIC-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `MPLS-LDP-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `MPLS-LSR-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `MPLS-TC-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `MPLS-TC-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `MPLS-TE-STD-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `MPLS-VPN-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `NHRP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `NOTIFICATION-LOG-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `OSPF-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `OSPF-TRAP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `P-BRIDGE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `PIM-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `POWER-ETHERNET-MIB` | — | — | — | ✓ | ✓ | — | — | — | — |
| `PerfHist-TC-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `Q-BRIDGE-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RFC-1212` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RFC-1215` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RFC1155-SMI` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RFC1213-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RFC1315-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RMON-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RMON2-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `RSVP-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `SNMP-FRAMEWORK-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `SNMP-PROXY-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `SNMP-TARGET-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `SNMPv2-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `SNMPv2-TC` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `SONET-MIB` | ✓ | ✓ | ✓ | — | — | ✓ | ✓ | ✓ | ✓ |
| `TCP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `TOKEN-RING-RMON-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `TOKENRING-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `TUNNEL-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `UDP-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `VPN-TC-STD-MIB` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## 4. Quick "what should I poll for X?" cheat-sheet

| Goal | Primary MIB(s) |
|---|---|
| CPU per process | `CISCO-PROCESS-MIB` |
| Memory pools | `CISCO-ENHANCED-MEMPOOL-MIB` |
| Interface counters | `IF-MIB` (+ `CISCO-IF-EXTENSION-MIB`) |
| Ethernet errors | `EtherLike-MIB`, `CISCO-ETHERLIKE-EXT-MIB` |
| Hardware inventory | `ENTITY-MIB` + `CISCO-ENTITY-FRU-CONTROL-MIB` |
| Temperature / fans / PSUs | `ENTITY-SENSOR-MIB`, `CISCO-ENVMON-MIB` |
| Optics (DOM) | `ENTITY-SENSOR-MIB` (per-lane sensors under transceiver entity) |
| PoE | `POWER-ETHERNET-MIB`, `CISCO-POWER-ETHERNET-EXT-MIB` |
| Stack members | `CISCO-STACKWISE-MIB` |
| BGP peers | `CISCO-BGP4-MIB` |
| OSPF | `OSPF-MIB`, `CISCO-OSPF-MIB` |
| BFD | `CISCO-IETF-BFD-MIB` |
| MPLS LSP / LDP | `MPLS-LSR-STD-MIB`, `MPLS-LDP-STD-MIB` |
| VRF / L3VPN | `MPLS-L3VPN-STD-MIB` |
| LLDP / CDP neighbors | `LLDP-MIB`, `CISCO-CDP-MIB` |
| IP SLA | `CISCO-RTTMON-MIB` (+ jitter / echo extensions) |
| IPsec tunnels | `CISCO-IPSEC-FLOW-MONITOR-MIB` |
| HSRP groups | `CISCO-HSRP-MIB` |
| Config-change trap | `CISCO-CONFIG-MAN-MIB` |
| Smart Licensing | `CISCO-LICENSE-MGMT-MIB` |
| Syslog history | `CISCO-SYSLOG-MIB` |
| EEM applets | `CISCO-EMBEDDED-EVENT-MGR-MIB` |

---

## 5. Notes on relevance to MDT / telemetry

For Catalyst 9300 MDT pipelines, **most of these MIBs are superseded by YANG operational models** (e.g. `Cisco-IOS-XE-process-cpu-oper`, `-memory-oper`, `-interfaces-oper`, `-environment-oper`). Use this MIB inventory when:

1. A YANG model isn't available for a given feature on the running release.
2. You're integrating with a legacy SNMP-based NMS in parallel with MDT.
3. You need to map an OID alarm/trap to its MDT equivalent.

For platform-specific MIB advertisement, see the matrix in *Section 3* (parsed from `17181/capability-*.xml`).

Cat9k advertises **fewer** MIBs than the routing platforms because it omits WAN-only modules (ATM, DS1/DS3, SONET, Frame Relay, voice/SBC, MPLS-TE/LDP, pseudowire). The cat9k focus is L2/L3 access-switching telemetry.

Presence in a capability XML ≠ guarantee that every object in the MIB is instrumented; it means the agent claims support for that MIB module. Some MIBs implement only a partial object subset.

---

## 6. Future work — not done today

The following items were identified as useful additions but are intentionally **not** implemented in this initial pass. Listed in rough order of value to the MDT migration goal.

### 6.1 MIB → YANG operational-model crosswalk *(highest priority)*

A table mapping each legacy MIB to its modern YANG replacement on Cat9k 17.x — e.g.:

| Legacy MIB | YANG operational model |
|---|---|
| `CISCO-PROCESS-MIB` | `Cisco-IOS-XE-process-cpu-oper`, `-process-memory-oper` |
| `IF-MIB` | `Cisco-IOS-XE-interfaces-oper` |
| `ENTITY-SENSOR-MIB` | `Cisco-IOS-XE-environment-oper` |

**Why it matters:** directly supports the "stop polling MIB X, subscribe to YANG model Y instead" workflow described in `AGENTS.md`. Would let you check off legacy SNMP poll patterns one-by-one against the MDT subscription set.

**Effort:** medium. Requires walking each MIB's top-level groups, then mapping to the closest XPath in `Cisco-IOS-XE-*-oper` modules.

### 6.2 OID-to-MIB index *(high priority for trap/alerting work)*

Extract the root OID from each MIB's `smiv2:oid` annotation and build a sortable OID → MIB lookup table.

**Use cases:**

- Looking up "what MIB owns OID `1.3.6.1.4.1.9.9.109`" when triaging an unknown trap.
- Mapping unknown SNMP traps to a MIB and a likely feature area.
- Building decoder pipelines for `snmptrapd` → log/event collectors.

**Effort:** low. Can be regex-extracted from the YANG conversions in `<release>/MIBS/*.yang`.

### 6.3 Trap / notification inventory

Extract every `notification` definition from the 184 MIBs into a single index (notification name, MIB, varbinds, severity).

**Why it matters:** drives SNMP-trap → syslog → MDT alerting pipelines. Today we have a poll-side inventory but no notification-side counterpart.

**Effort:** medium. Each YANG-converted MIB has `notification` blocks that can be parsed with `pyang` or simple regex.

### 6.4 Deprecated / obsolete object scan

Grep each MIB for `status deprecated` / `status obsolete` to flag objects that should not be used in new dashboards.

**Why it matters:** prevents building new MDT dashboards or correlation rules on deprecated SNMP objects whose semantics may change.

**Effort:** low. Pure regex pass over `<release>/MIBS/*.yang`.

### 6.5 Index / landing page

Single short entry-point doc (e.g. update top-level `README.md`) pointing at this consolidated `MIBS.md`. With the merge into one file this is now mostly a one-liner README addition.

**Effort:** trivial.

### 6.6 cEdge MIB comparison

The `cedge/` tree (alongside the main `xe/` tree) likely ships its own MIB set for SD-WAN. Diff it against the main XE tree to highlight cEdge-only or cEdge-missing MIBs.

**Why it matters:** if the MDT pipeline expands to SD-WAN edge devices, we need to know which MIBs survive the move to the cEdge image.

**Effort:** low. Same per-release-diff approach used for *Section 1*.

### 6.7 Per-MIB object / table count

Count scalar leaves and conceptual tables per MIB to give a "size / complexity" indicator. Useful for prioritizing which MIBs are worth full instrumentation review.

**Effort:** medium. Requires parsing the YANG conversion (or running `pyang --tree` and counting nodes).

### 6.8 Capability-XML revision-date tracking

Each `module=X` URL in a capability XML carries `&revision=YYYY-MM-DD`. Tracking these per platform and per release tells you when each platform last refreshed its MIB module version — a useful signal for image-bug triage and "is my view of the MIB current?" questions.

**Effort:** low. Same parsing as *Section 3* with the revision regex extracted alongside the module name.

---

### Explicitly out-of-scope

The following were considered and rejected — **not** planned:

- **Full leaf-by-leaf object dictionaries.** Already present in the `.yang` files under each release; duplicating them in markdown adds size without insight.
- **Per-trap varbind decoder tables.** Huge volume, rarely consulted, and trap decoders live better in tooling (snmptrapd / mibbrowser) than in markdown.

