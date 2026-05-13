# All Updated YANG Models: v17.18.1 → v26.11
**Comprehensive Table: 28 New Models & 147 Updated Models**

*Last Updated: May 5, 2026*

---

## NEW Models Summary (28 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[NEW Configuration Models](#new-configuration-models-9-models)** | 9 | 66 XPaths |
| **[NEW Operational Models](#new-operational-models-10-models)** | 10 | 262 XPaths |
| **[NEW RPC Models](#new-rpc-models-3-models)** | 3 | 70 XPaths |
| **[NEW Event Notification Models](#new-event-notification-models-4-models)** | 4 | 64 XPaths |
| **[NEW Open Standard](#new-open-standard-6-models)** | 6 | 480 XPaths (OpenConfig QoS + submodules + Tailf) |
| **TOTAL NEW MODELS** | **28** | **1,084 total XPaths** |

*Note: 28 independent models + 5 submodules/extensions = 33 files total*

---

## UPDATED Models Summary (147 models)

| Category | Count | Jump to Section |
|----------|-------|----------------|
| **[UPDATED Configuration Models](#updated-configuration-models-9-models)** | 9 standalone | +38 XPaths |
| **[UPDATED Operational Models](#updated-operational-models-20-models)** | 20 | +122 XPaths |
| **[UPDATED RPC Models](#updated-rpc-models-13-models)** | 13 | +110 XPaths |
| **[UPDATED Native Models](#updated-native-models-76-models)** | 76 | +329 XPaths (including Native +58) |
| **[UPDATED Wireless Models](#updated-wireless-models-11-additional-models-not-in-other-sections)** | 11 | +41 XPaths |
| **[UPDATED Type Definitions](#updated-type-definitions-8-models---partial-list)** | 8 | Typedef/grouping changes |
| **[UPDATED Deviation Models](#updated-deviation-models-10-models)** | 10 | Platform-specific restrictions |
| **[UPDATED Open Standard](#updated-open-standard-12-models)** | 12 | +65 XPaths, -26 removed |
| **TOTAL UPDATED MODELS** | **147** | **~600+ XPaths modified** |

*Most Changed: Native (+58), Crypto RPC (+50), Crypto (+51), Wireless AP Oper (+106)*

---

## Key Highlights - NEW Models

### Security & Compliance:
- **DNS Defense** - Configuration and operational monitoring for DNS attack protection
- **System Security** - Events and operational data for security posture monitoring
- **DPI Events** - Deep Packet Inspection notifications

### Industrial Automation:
- **HSR** (High-availability Seamless Redundancy) - IEC 62439-3 for IE3x00/ESS3x00
- **SCADA** - Industrial automation protocol support
- **CIP** - Channel Interface Processor for mainframe connectivity

### SD-WAN & Networking:
- **SD-WAN IPsec Oper** - Comprehensive IPsec tunnel monitoring (93 XPaths)
- **AutoVPN Events** - Dynamic VPN establishment notifications
- **Service Chain** - Traffic steering and service insertion
- **Segment Routing Oper** - MPLS and SRv6 operational data

### Wireless:
- **Ultra-Reliable Wireless Backhaul (URWB)** - 50 XPaths operational data
- **Cisco Spaces RPC** - Location services integration

### Switching (Cat9K):
- **SSE** (Switching Silicon Engine) - Actions, events, and operational data
- **Stack Info Oper** - Stackable switch information

### Management & Operations:
- **Rollback RPC** - Configuration rollback operations
- **Alarm** - Comprehensive alarm management (66 XPaths)
- **Statistics** - Collection and sampling configuration
- **RIB Oper** - Routing Information Base visibility

### OpenConfig:
- **QoS Suite** - Complete OpenConfig QoS model with 469 XPaths (5 files total)

---

## Key Highlights - UPDATED Models

### Most Significant Updates by XPath Count:
1. **Native** (+58 XPaths) - Foundation for all configuration
2. **Crypto RPC** (+50 XPaths) - Extensive new crypto operations
3. **Crypto** (+51 XPaths) - Enhanced security configuration
4. **Wireless Access Point Oper** (+106 XPaths) - Comprehensive AP monitoring

### Critical Infrastructure Models:
- **Native, Interfaces, BGP, OSPF, Crypto** - Core routing and security
- **CLI-RPC, GNMI-cfg** - Programmability and automation
- **BGP-oper, Interfaces-oper** - Telemetry and monitoring

### New Technology Support:
- **Async CLI infrastructure** - Transaction-completion-notification
- **Two-stage commit** - PREPARE/COMMIT phases
- **Ultra-Reliable Wireless** - URWB enhancements
- **6GHz wireless** - New spectrum support
- **MACsec** - Enhanced layer 2 security
- **IoT integration** - Cisco Spaces and orchestration

### Platform Coverage:
- **All Platforms**: Most configuration, operational, and RPC models
- **Wireless Controllers**: All wireless-specific models (20)
- **Catalyst 9000**: Switch-specific features, PoE, uplink autoconfig
- **Industrial (IE3x00)**: PRP, MRP industrial protocols
- **ISR/ASR Routers**: Voice, cellular WAN, UTD

---

# NEW YANG Models in v26.11

**28 Brand New Models** (plus 4 OpenConfig submodules, 1 vendor extension)

---

## NEW Configuration Models (9 models)

| # | YANG Model | Module Name | Type | # XPaths (Total) | Platforms Supported | Summary |
|---|------------|-------------|------|------------------|---------------------|---------|
| 1 | [Cisco-IOS-XE-alarm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-alarm.yang) | Alarm | Configuration | 66 | All Platforms | Alarm management system configuration for monitoring and alerting |
| 2 | [Cisco-IOS-XE-banner-internal.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-banner-internal.yang) | Banner internal | Configuration | 14 | All Platforms | Internal banner settings and message management |
| 3 | [Cisco-IOS-XE-cip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-cip.yang) | CIP | Configuration | 14 | Specialized Hardware | Channel Interface Processor configuration for legacy mainframe connectivity |
| 4 | [Cisco-IOS-XE-dns-defense.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-dns-defense.yang) | DNS defense | Configuration | 19 | All Platforms | DNS defense configuration for protection against DNS-based attacks |
| 5 | [Cisco-IOS-XE-hsr.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-hsr.yang) | HSR | Configuration | 41 | IE3x00, ESS3x00 | High-availability Seamless Redundancy (IEC 62439-3) for industrial networks |
| 6 | [Cisco-IOS-XE-scada.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-scada.yang) | SCADA | Configuration | 10 | IE3x00, IR1101 | SCADA protocol support for industrial automation and control systems |
| 7 | [Cisco-IOS-XE-service-chain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-service-chain.yang) | Service chain | Configuration | 40 | ASR1K, Cat9K, C8000V | Service chain configuration for traffic steering and service insertion |
| 8 | [Cisco-IOS-XE-statistics.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-statistics.yang) | Statistics | Configuration | 7 | All Platforms | Statistics collection configuration and sampling parameters |
| 9 | [Cisco-IOS-XE-webauth-banner-internal.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-webauth-banner-internal.yang) | Webauth banner internal | Configuration | 8 | All Platforms | Web authentication banner internal settings for guest access |

---

## NEW Operational Models (10 models)

| # | YANG Model | Module Name | Type | # XPaths (Total) | Platforms Supported | Summary |
|---|------------|-------------|------|------------------|---------------------|---------|
| 1 | [Cisco-IOS-XE-dns-defense-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-dns-defense-oper.yang) | DNS defense oper | Operational Data | 14 | All Platforms | DNS defense operational monitoring and telemetry |
| 2 | [Cisco-IOS-XE-iad-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-iad-oper.yang) | IAD oper | Operational Data | 17 | ISR1K, IR1101 | Integrated Access Device operational data and telemetry |
| 3 | [Cisco-IOS-XE-matm-state-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-matm-state-oper.yang) | MATM state oper | Operational Data | 16 | Specialized Platforms | MATM (Multi-ATM) state operational data |
| 4 | [Cisco-IOS-XE-rib-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-rib-oper.yang) | RIB oper | Operational Data | 8 | All Platforms | Routing Information Base operational state and route visibility |
| 5 | [Cisco-IOS-XE-sdwan-ipsec-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sdwan-ipsec-oper.yang) | SD-WAN IPsec oper | Operational Data | 93 | ASR1K, ISR1K, C8000V, C8500 | SD-WAN IPsec tunnel operational monitoring and statistics |
| 6 | [Cisco-IOS-XE-sr-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sr-oper.yang) | SR oper | Operational Data | 9 | ASR1K, ISR4K, NCS | Segment Routing operational data for MPLS and SRv6 |
| 7 | [Cisco-IOS-XE-sse-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sse-oper.yang) | SSE oper | Operational Data | 15 | Cat9K | SSE operational data and hardware telemetry |
| 8 | [Cisco-IOS-XE-stack-info-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-stack-info-oper.yang) | Stack info oper | Operational Data | 28 | Cat9K Stackable | Stack information operational data for stackable switches |
| 9 | [Cisco-IOS-XE-system-security-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-system-security-oper.yang) | System security oper | Operational Data | 12 | All Platforms | System security operational data including security posture |
| 10 | [Cisco-IOS-XE-wireless-urwb-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-urwb-oper.yang) | Wireless URWB oper | Operational Data | 50 | Wireless Controllers | Ultra-Reliable Wireless Backhaul operational data and telemetry |

---

## NEW RPC Models (3 models)

| # | YANG Model | Module Name | Type | # XPaths (Total) | Platforms Supported | Summary |
|---|------------|-------------|------|------------------|---------------------|---------|
| 1 | [Cisco-IOS-XE-rollback-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-rollback-rpc.yang) | Rollback RPC | RPC | 13 | All Platforms | Configuration rollback RPC operations for change management |
| 2 | [Cisco-IOS-XE-sse-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sse-actions-rpc.yang) | SSE actions RPC | RPC | 49 | Cat9K | SSE (Switching Silicon Engine) action RPCs |
| 3 | [Cisco-IOS-XE-wireless-cisco-spaces-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-cisco-spaces-rpc.yang) | Wireless Cisco Spaces RPC | RPC | 8 | Wireless Controllers | Cisco Spaces wireless location services RPCs |

---

## NEW Event Notification Models (4 models)

| # | YANG Model | Module Name | Type | # XPaths (Total) | Platforms Supported | Summary |
|---|------------|-------------|------|------------------|---------------------|---------|
| 1 | [Cisco-IOS-XE-autovpn-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-autovpn-events.yang) | AutoVPN events | Event Notification | 21 | ASR1K, ISR1K, CSR1K | AutoVPN event notifications for dynamic VPN establishment |
| 2 | [Cisco-IOS-XE-dpi-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-dpi-events.yang) | DPI events | Event Notification | 13 | ASR1K, ISR4K, Cat9K | Deep Packet Inspection event notifications and alerts |
| 3 | [Cisco-IOS-XE-sse-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sse-events.yang) | SSE events | Event Notification | 14 | Cat9K | SSE event notifications for switching hardware events |
| 4 | [Cisco-IOS-XE-system-security-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-system-security-events.yang) | System security events | Event Notification | 16 | All Platforms | System security event notifications for compliance and monitoring |

---

## NEW Open Standard (6 models)

| # | YANG Model | Module Name | Type | # XPaths (Total) | Platforms Supported | Summary |
|---|------------|-------------|------|------------------|---------------------|---------|
| 1 | [openconfig-qos.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-qos.yang) | OC QoS | OpenConfig Standard | 469 | All Platforms | Main OpenConfig QoS model (includes submodules below) |
| 2 | [openconfig-qos-elements.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-qos-elements.yang) | OC QoS elements | OpenConfig Submodule | (in #1) | All Platforms | QoS classifier, queue, scheduler elements |
| 3 | [openconfig-qos-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-qos-interfaces.yang) | OC QoS interfaces | OpenConfig Submodule | (in #1) | All Platforms | QoS interface configuration |
| 4 | [openconfig-qos-mem-mgmt.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-qos-mem-mgmt.yang) | OC QoS mem mgmt | OpenConfig Submodule | (in #1) | All Platforms | QoS buffer memory management |
| 5 | [openconfig-qos-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-qos-types.yang) | OC QoS types | OpenConfig Types | (in #1) | All Platforms | QoS type definitions and enumerations |
| 6 | [tailf-netconf-rollback.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/tailf-netconf-rollback.yang) | Tailf NETCONF rollback | Vendor Extension | 11 | All Platforms | Tailf NETCONF rollback support for configuration management |

---

# UPDATED YANG Models: v17.18.1 → v26.11

**147 Models Modified**

---

## UPDATED Configuration Models (9 models)
*Standalone configuration models with -cfg suffix or wireless-specific configs*

| # | YANG Model | Module Name | Type | # XPaths (Updated/Total) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 1 | [Cisco-IOS-XE-app-hosting-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-app-hosting-cfg.yang) | App hosting cfg | Configuration | +3 / 138 | All Platforms | Container and application hosting updates, resource management enhancements | Added manifest-path, package-path, and app-install container for improved application package management. |
| 2 | [Cisco-IOS-XE-aws-common-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-aws-common-cfg.yang) | AWS common cfg | Configuration | 1 / 7 | Cat9K | AWS integration configuration updates and refinements | Modified 1 constraint: secret-access-key pattern expanded to support AES-encrypted values with special characters. |
| 3 | [Cisco-IOS-XE-cloud-services-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-cloud-services-cfg.yang) | Cloud services cfg | Configuration | +2 / 7 | All Platforms | Multi-cloud services configuration enhancements, new service parameters | Added cisco-spaces-url configuration and no-proxy-list for enhanced multi-cloud service integration. |
| 4 | [Cisco-IOS-XE-ctrl-mng-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ctrl-mng-cfg.yang) | Ctrl mng cfg | Configuration | 1 / 27 | All Platforms | Control management plane configuration updates | Modified 1 constraint: Fixed typo in bind pattern regex for Five Gigabit Ethernet interface support (changed "Five/Ten" to "Five|Ten"). |
| 5 | [Cisco-IOS-XE-gnmi-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-gnmi-cfg.yang) | GNMI cfg | Configuration | +3 / 17 | All Platforms | gNMI certificate handling for ACR TP-self-signed, secure/insecure port configuration | Added ACL IPv4/IPv6 access control and enhanced certificate handling for ACR TP-self-signed certificates. |
| 6 | [Cisco-IOS-XE-mdt-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-mdt-cfg.yang) | MDT cfg | Configuration | +9 / 95 | All Platforms | Model-driven telemetry configuration enhancements, new subscription parameters | Added 9 new subscription parameters for enhanced telemetry configuration including custom encodings and filters. |
| 7 | [Cisco-IOS-XE-wireless-apf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-apf-cfg.yang) | Wireless apf cfg | Configuration | +4 / 81 | Wireless Controllers | Secure RF network name encryption, HTTPS file operations for download/upload | Added secure RF network name encryption configuration and HTTPS file operations for secure AP firmware. |
| 14 | [Cisco-IOS-XE-wireless-rf-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-rf-cfg.yang) | Wireless rf cfg | Configuration | +2 / 215 | Wireless Controllers | WiFi-IOT coexistence, basic data rate constraints, deprecated ATF policy parameters | Added IoT coexistence mode configuration and basic data rate constraints; deprecated legacy ATF parameters. |
| 15 | [Cisco-IOS-XE-wireless-urwb-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-urwb-cfg.yang) | Wireless urwb cfg | Configuration | +12 / 27 | Wireless Controllers | Ultra-reliable wireless reliability parameters, enhanced passphrase validation | Added 13 new ultra-reliable wireless backhaul parameters including reliability thresholds and MCS rates. |

---

## UPDATED Operational Models (20 models)

| # | YANG Model | Module Name | Type | # XPaths (Updated/Total) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 1 | [Cisco-IOS-XE-app-hosting-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-app-hosting-oper.yang) | App hosting oper | Operational Data | +16 / 157 | All Platforms | Container operational state monitoring, resource utilization telemetry updates | Added 16 new operational nodes for container resource utilization monitoring including CPU, memory, disk usage. |
| 2 | [Cisco-IOS-XE-bgp-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-bgp-oper.yang) | BGP oper | Operational Data | 1 / 162 | All Platforms | BGP operational state telemetry enhancements, neighbor state visibility | Modified 1 enum status: Marked fsm-nonnegotiated enum as obsolete in BGP FSM state; updated description to indicate non-negotiated state should not be used. |
| 3 | [Cisco-IOS-XE-bgp-rib-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-bgp-rib-oper.yang) | BGP RIB oper | Operational Data | +5 / 71 | All Platforms | BGP routing table operational data, enhanced route visibility and attributes | Added 7 new routing table operational nodes for enhanced BGP route attributes and path visibility. |
| 4 | [Cisco-IOS-XE-cellwan-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-cellwan-oper.yang) | Cellwan oper | Operational Data | +23 / 137 | IR1101, C1100 | 5G/LTE cellular WAN monitoring, signal strength and connection statistics | Added 23 new 5G/LTE cellular WAN telemetry fields for signal strength and connection quality statistics. |
| 5 | [Cisco-IOS-XE-crypto-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-crypto-oper.yang) | Crypto oper | Operational Data | +24 / 591 | All Platforms | Cryptographic operations monitoring, IPsec tunnel statistics, key management visibility | Added 24 new cryptographic operation monitoring nodes for IPsec tunnel stats and key management visibility. |
| 6 | [Cisco-IOS-XE-crypto-pki-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-crypto-pki-oper.yang) | Crypto PKI oper | Operational Data | +1 / 36 | All Platforms | Public key infrastructure certificate monitoring and validation status | Added is-ca-cert field to distinguish CA certificates from end-entity certificates in PKI monitoring output. |
| 7 | [Cisco-IOS-XE-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-interfaces-oper.yang) | Interfaces oper | Operational Data | +4 / 337 | All Platforms | Interface operational state, statistics, and performance metrics for all interface types | Added 4 new operational nodes for enhanced interface statistics including error counters and performance metrics. |
| 14 | [Cisco-IOS-XE-mdt-oper-v2.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-mdt-oper-v2.yang) | MDT oper v2 | Operational Data | +5 / 59 | All Platforms | Model-driven telemetry operational state, subscription status and streaming statistics | Added 5 new telemetry operational fields for subscription status, streaming statistics, and connection state. |
| 15 | [Cisco-IOS-XE-meraki-connect-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-meraki-connect-oper.yang) | Meraki connect oper | Operational Data | +20 / 135 | All Platforms | Meraki cloud management integration operational data and connection status | Added 23 new Meraki cloud management integration fields for connection status and sync state. |
| 16 | [Cisco-IOS-XE-poe-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-poe-oper.yang) | POE oper | Operational Data | +2 / 189 | Cat9K, IE3x00 | Power over Ethernet operational monitoring, power consumption and port status | Added flex-poe-config and flex-poe-actv fields for flexible Power over Ethernet monitoring. |
| 17 | [Cisco-IOS-XE-rawsocket-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-rawsocket-oper.yang) | Rawsocket oper | Operational Data | +10 / 46 | All Platforms | Raw socket operational state for low-level network packet operations | Added 13 new raw socket operational nodes for low-level network packet operation statistics. |
| 18 | [Cisco-IOS-XE-rif-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-rif-oper.yang) | RIF oper | Operational Data | +6 / 69 | All Platforms | Routing information framework operational state and statistics | Added 6 new routing information framework operational nodes for route installation and redistribution statistics. |
| 19 | [Cisco-IOS-XE-sm-events-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sm-events-oper.yang) | SM events oper | Operational Data | +2 / 25 | All Platforms | Service manager event monitoring and system state notifications | Added avg-rtt and trans-count fields for service manager transaction monitoring and round-trip time telemetry. |
| 20 | [Cisco-IOS-XE-spanning-tree-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-spanning-tree-oper.yang) | Spanning tree oper | Operational Data | +2 / 113 | All Platforms | Spanning Tree Protocol operational state, topology visibility and port states | Added vlan-rb and mst-rb root bridge tracking fields for enhanced STP topology visibility. |
| 21 | [Cisco-IOS-XE-uplink-autoconfig-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-uplink-autoconfig-oper.yang) | Uplink autoconfig oper | Operational Data | +6 / 33 | Cat9K, Wireless | Uplink auto-configuration provisioning status and operational state | Added 7 new uplink auto-configuration operational nodes for provisioning status and port state visibility. |
| 22 | [Cisco-IOS-XE-wireless-access-point-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-access-point-oper.yang) | Wireless access point oper | Operational Data | +106 / 1405 | Wireless Controllers | AP operational monitoring, MACsec status, Spaces telemetry, gRPC statistics | Added 107 new AP telemetry nodes including MACsec status, Cisco Spaces integration, gRPC statistics, UWB data. |
| 23 | [Cisco-IOS-XE-wireless-ap-global-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-ap-global-oper.yang) | Wireless ap global oper | Operational Data | +2 / 130 | Wireless Controllers | Global AP infrastructure visibility, client join counters for multi-radio slots | Added clients-on-slot2 and clients-on-slot3 counters for multi-radio AP client join statistics. |
| 24 | [Cisco-IOS-XE-wireless-cisco-spaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-cisco-spaces-oper.yang) | Wireless cisco spaces oper | Operational Data | +11 / 25 | Wireless Controllers | Cisco Spaces location services, IoT Orchestrator auto-config, web-socket endpoints | Added 11 new Cisco Spaces operational nodes for IoT Orchestrator auto-config and location services. |
| 25 | [Cisco-IOS-XE-wireless-rrm-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-rrm-oper.yang) | Wireless RRM oper | Operational Data | 1 / 136 | Wireless Controllers | Radio resource management operational data, RF name field description updates | Modified 1 description: Updated rf-name leaf description from "RF name" to "Encrypted or un-encrypted RF name" for security clarity. |
| 26 | [Cisco-IOS-XE-wireless-urwbnet-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-urwbnet-oper.yang) | Wireless URWBNET oper | Operational Data | +6 / 79 | Wireless Controllers | Ultra-reliable wireless backhaul network telemetry, MCS data rates, NSS information | Added 6 new ultra-reliable wireless backhaul network fields for MCS data rates and link quality metrics. |

---

## UPDATED RPC Models (13 models)

| # | YANG Model | Module Name | Type | # XPaths (Updated/Total) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 1 | [Cisco-IOS-XE-bgp-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-bgp-rpc.yang) | BGP RPC | RPC | +7 / 10 | All Platforms | BGP operational commands and administrative operations | Added 9 new BGP operational command RPCs for enhanced route clearing, neighbor reset, and administrative control. |
| 2 | [Cisco-IOS-XE-cli-preview-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-cli-preview-rpc.yang) | CLI preview RPC | RPC | +2 / 6 | All Platforms | CLI command preview and validation operations before execution | Added 4 new CLI preview nodes for command validation and syntax checking before execution with impact analysis. |
| 3 | [Cisco-IOS-XE-cli-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-cli-rpc.yang) | CLI RPC | RPC | +2 / 20 | All Platforms | CLI execution with transaction-completion-notification, async CLI handling infrastructure | Added transaction-completion-notification fields (to, label, comment) for async CLI handling and execution tracking. |
| 4 | [Cisco-IOS-XE-cloud-services-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-cloud-services-rpc.yang) | Cloud services RPC | RPC | +1 / 3 | All Platforms | Cloud service operational commands and management operations | Added otp-pkey for one-time password public key operations in cloud service management and authentication. |
| 5 | [Cisco-IOS-XE-crypto-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-crypto-rpc.yang) | Crypto RPC | RPC | +50 / 186 | All Platforms | Cryptographic operations, certificate management, key generation, IPsec tunnel management | Added 50 new cryptographic operation RPCs for certificate management, key generation, IPsec tunnel control, and PKI. |
| 6 | [Cisco-IOS-XE-install-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-install-rpc.yang) | Install RPC | RPC | +1 / 46 | All Platforms | Software installation and upgrade operational commands | Added xfsu (extended fast software upgrade) parameter for enhanced software installation and upgrade commands. |
| 7 | [Cisco-IOS-XE-meraki-leds-actions-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-meraki-leds-actions-rpc.yang) | Meraki LEDs actions RPC | RPC | +3 / 8 | Meraki Devices | LED control operations for Meraki hardware devices | Added 3 new system LED state enumerations: alt-green-red, solid-red, and blink-red for enhanced LED status visibility. |
| 14 | [Cisco-IOS-XE-platform-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-platform-rpc.yang) | Platform RPC | RPC | +1 / 150 | All Platforms | Platform-level operational commands and system management | Added wireless-case branch and Cisco-IOS-XE-wireless-rpc include for wireless feature debug RPC support. |
| 15 | [Cisco-IOS-XE-rescue-config-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-rescue-config-rpc.yang) | Rescue config RPC | RPC | +1 / 11 | All Platforms | Configuration rescue and recovery operations | Added transaction tracking fields (to, comment) for configuration rescue and recovery operation auditing. |
| 16 | [Cisco-IOS-XE-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-rpc.yang) | RPC | RPC | 2 / 293 | All Platforms | General-purpose RPC operations and system commands | Modified 2 items: Added wireless-rpc include; modified filename-drop-node-name pattern to support stack members (bootflash-1, etc.) and standby nodes. |
| 17 | [Cisco-IOS-XE-tech-support-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-tech-support-rpc.yang) | Tech support RPC | RPC | +1 / 4 | All Platforms | Technical support file generation and diagnostic data collection | Added archive-wireless flag for wireless-specific technical support file generation with targeted diagnostic data. |
| 18 | [Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-access-point-cfg-rpc.yang) | Wireless access point cfg RPC | RPC | +42 / 225 | Wireless Controllers | Bulk AP UWB time-of-arrival config, 6GHz dual-band support, AP height/GNSS configuration | Added 43 new AP configuration RPCs for bulk UWB time-of-arrival config, 6GHz dual-band support, AP height/GNSS. |
| 19 | [Cisco-IOS-XE-wireless-tech-support-rpc.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-tech-support-rpc.yang) | Wireless tech support RPC | RPC | +2 / 5 | Wireless Controllers | Wireless client MAC filtering for targeted tech-support file generation | Added wireless-info-v2 and client-mac parameters for wireless client MAC filtering in targeted tech-support files. |

---

## UPDATED Native Models (76 models)
*Models that augment the ios:native tree*

### Critical Native Models 

| # | YANG Model | Module Name | Type | # XPaths (Updated/Total) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 1 | [Cisco-IOS-XE-native.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-native.yang) | Native | Configuration | +58 / 1318 | All Platforms | Root model for all IOS-XE configuration, 27 new model imports, two-stage commit, atomic config replace | Added 69 new configuration nodes with 27 new model imports; implemented two-stage commit (PREPARE/COMMIT) and atomic config replace. |
| 2 | [Cisco-IOS-XE-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-interfaces.yang) | Interfaces | Configuration | +23 / 1605 | All Platforms | Interface configuration for all types, QoS/security integration, atomic configuration support | Added 23 new interface configuration nodes for enhanced QoS/security integration across all interface types. |
| 3 | [Cisco-IOS-XE-crypto.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-crypto.yang) | Crypto | Configuration | +51 / 2809 | All Platforms | Comprehensive cryptographic configuration, IPsec, PKI, key management, encryption protocols | Added 64 new comprehensive cryptographic configuration nodes for IPsec, PKI, key management with enhanced validation. |
| 4 | [Cisco-IOS-XE-aaa.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-aaa.yang) | AAA | Configuration | +8 / 1202 | All Platforms | Authentication, authorization, accounting configuration updates and refinements | Added 9 new authentication/authorization/accounting configuration nodes for enhanced AAA server groups and policy. |
| 5 | [Cisco-IOS-XE-bgp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-bgp.yang) | BGP | Configuration | +1 / 2057 | All Platforms | BGP configuration with async CLI paths, link-local IPv6, advertisement-startup-delay, critical-delay | Added 9 new BGP configuration nodes including async CLI paths, link-local IPv6 support, advertisement-startup-delay. |
| 6 | [Cisco-IOS-XE-ospf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ospf.yang) | OSPF | Configuration | 25 / 602 | All Platforms | OSPF routing protocol configuration updates and refinements | Added 23 must constraints for passive-interface switchport validation across interface types; added 1 must constraint for auth-key type 0/6/7 validation; marked 1 node (maximum-paths) as obsolete. |
| 7 | [Cisco-IOS-XE-lisp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-lisp.yang) | LISP | Configuration | 6 / 1649 | All Platforms | Locator/ID Separation Protocol configuration, mobility and overlay networking support | Modified 6 status attributes: Changed 6 deprecated nodes to obsolete status: sgt-only, proxy, sgt, summary, ipv4-multicast, ipv6-multicast (deprecated in 17.12-17.14). |

### Additional Native Augmenting Models (6 models)

| # | YANG Model | Module Name | Type | # XPaths (Updated/Total) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 14 | [Cisco-IOS-XE-acl.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-acl.yang) | ACL | Configuration | 1 / 604 | All Platforms | Access control list refinements, protocol range expansion for IPv6 role-based ACL | Modified 1 constraint: IPv6 ACL other-protocol range expanded to include protocol 0 (was 1..5, now 0..5) for role-based access control. |
| 15 | [Cisco-IOS-XE-dhcp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-dhcp.yang) | DHCP | Configuration | +11 / 469 | All Platforms | DHCP server and client enhancements, new binding options, improved lease management | Added 16 new data nodes for enhanced relay options, binding parameters, and client/server configuration. |
| 16 | [Cisco-IOS-XE-nat.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-nat.yang) | NAT | Configuration | +1 / 677 | All Platforms | Network address translation policy updates, enhanced mapping options | Added 7 new configuration nodes for enhanced NAT pool management and policy-based translation rules. |
| 17 | [Cisco-IOS-XE-umbrella.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-umbrella.yang) | Umbrella | Configuration | +1 grouping / 32 | All Platforms | Cisco Umbrella cloud security integration updates | Added umbrella-dns-defense-global-grouping with 10+ new config leaves: local-domain, dnscrypt, public-key, udp-timeout, orgid, api-key, secret, registration-vrf, vrf list for DNS Defense. |
| 18 | [Cisco-IOS-XE-uplink-autoconfig.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-uplink-autoconfig.yang) | Uplink autoconfig | Configuration | +4 / 13 | Cat9K, Wireless | Uplink auto-provisioning enhancements, expanded configuration options | Added 13 new parameters for enhanced uplink auto-provisioning including trust and port configuration. |
| 19 | [Cisco-IOS-XE-utd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-utd.yang) | UTD | Configuration | +4 / 229 | ISR, ASR, Cat9K | Unified Threat Defense security feature updates, new threat detection parameters | Added 4 new threat detection parameters for Unified Threat Defense with enhanced signature validation. |

### Other Native Models (63 models)

| # | YANG Model | Module Name | Type | # XPaths (Updated) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 14 | [Cisco-IOS-XE-app-hosting.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-app-hosting.yang) | App hosting | Grouping/Type Definition | +27 | All Platforms | Application hosting groupings and interface type definitions |  |
| 15 | [Cisco-IOS-XE-bridge-domain.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-bridge-domain.yang) | Bridge domain | Configuration | Descriptions only | All Platforms | Bridge domain configuration for layer 2 networking | Updated bridge domain layer 2 networking configuration descriptions and refined VLAN mapping documentation. |
| 16 | [Cisco-IOS-XE-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-common-types.yang) | Common types | Type Definition | Descriptions only | All Platforms | Common type definitions used across multiple YANG models | Added new reusable type definitions used across multiple YANG models for standardized data structures. |
| 17 | [Cisco-IOS-XE-controller.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-controller.yang) | Controller | Configuration | +13 | All Platforms | Hardware controller configuration for various interface types | Added 13 new hardware controller configuration nodes for various interface types; deprecated 1 legacy controller option. |
| 18 | [Cisco-IOS-XE-cts.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-cts.yang) | CTS | Configuration | +21 | All Platforms | Cisco TrustSec configuration for identity-based networking | Added 21 new Cisco TrustSec configuration nodes for identity-based networking with enhanced security policy validation. |
| 19 | [Cisco-IOS-XE-device-sensor.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-device-sensor.yang) | Device sensor | Configuration | +38 | All Platforms | Device sensor configuration for endpoint profiling | Added 38 new device sensor configuration nodes for endpoint profiling with enhanced validation constraints. |
| 20 | [Cisco-IOS-XE-device-tracking.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-device-tracking.yang) | Device tracking | Configuration | +2 | All Platforms | Device tracking configuration for IPv6 SLAAC and ND | Added 2 new nodes: TDL container and dhcp-stats fields for enhanced IPv6 SLAAC and Neighbor Discovery device tracking. |
| 21 | [Cisco-IOS-XE-dot1x.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-dot1x.yang) | Dot1x | Configuration | +1 | All Platforms | 802.1X port-based authentication configuration | Added 1 new node: enable-macsec field to integrate 802.1X port-based authentication with MACsec layer 2 encryption. |
| 22 | [Cisco-IOS-XE-eem.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-eem.yang) | EEM | Configuration | +1 | All Platforms | Embedded Event Manager for automated actions | Added 1 new node: routername field for router identification in Embedded Event Manager automated action configurations. |
| 23 | [Cisco-IOS-XE-eigrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-eigrp.yang) | EIGRP | Configuration | Descriptions only | All Platforms | Enhanced Interior Gateway Routing Protocol configuration | Enhanced EIGRP routing protocol validation constraints for improved configuration policy enforcement. |
| 24 | [Cisco-IOS-XE-endpoint-tracker-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-endpoint-tracker-events.yang) | Endpoint tracker events | Event Notification | +1 | All Platforms | Endpoint tracking event notifications | Added 2 new fields: to and reason fields for enhanced endpoint tracking event notification details and troubleshooting. |
| 25 | [Cisco-IOS-XE-ethernet-cfm-efp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ethernet-cfm-efp.yang) | Ethernet CFM EFP | Configuration | +4 | All Platforms | Ethernet Connectivity Fault Management for EFP | Added 4 new Ethernet Connectivity Fault Management nodes for EFP service instances; deprecated 1 legacy CFM option. |
| 26 | [Cisco-IOS-XE-ethernet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ethernet.yang) | Ethernet | Configuration | Descriptions only | All Platforms | Ethernet interface and protocol configuration | Updated Ethernet interface and protocol configuration descriptions for enhanced layer 2 feature clarity. |
| 27 | [Cisco-IOS-XE-ezpm.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ezpm.yang) | EZPM | Configuration | +4 | All Platforms | EZ Policy Management configuration | Added 4 new EZ Policy Management configuration nodes for simplified policy deployment workflows. |
| 28 | [Cisco-IOS-XE-features.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-features.yang) | Features | Configuration | Descriptions only | All Platforms | Platform feature enablement and configuration | Updated platform feature enablement configuration descriptions and refined capability documentation. |
| 29 | [Cisco-IOS-XE-flow.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-flow.yang) | Flow | Configuration | +3 | All Platforms | NetFlow and traffic flow monitoring configuration | Added 3 new nodes: NAT container and inside field for NetFlow traffic flow monitoring of NAT translation events. |
| 30 | [Cisco-IOS-XE-hsrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-hsrp.yang) | HSRP | Configuration | +15 | All Platforms | Hot Standby Router Protocol configuration | Added 15 new Hot Standby Router Protocol configuration nodes with enhanced validation for redundancy policy. |
| 31 | [Cisco-IOS-XE-http.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-http.yang) | HTTP | Configuration | +3 | All Platforms | HTTP server and client configuration | Added 3 new HTTP server/client configuration nodes including authentication options; deprecated 1 legacy HTTP setting. |
| 32 | [Cisco-IOS-XE-ip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ip.yang) | IP | Configuration | ~60 / 791 | All Platforms | IP routing and addressing configuration | Added 24 default values (TCP MSS, ARP inspection, etc.); added 3 must conditions (VLAN routes, VRF validation); deprecated/obsoleted 35+ insecure protocol nodes (telnet, rcmd, ftp, tftp, source-route, finger); added MLKEM hybrid key exchange algorithms for SSH; added type-6 encryption support. |
| 33 | [Cisco-IOS-XE-isis.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-isis.yang) | ISIS | Configuration | +16 | All Platforms | IS-IS routing protocol configuration | Added 16 new IS-IS routing protocol configuration nodes for enhanced topology and metric management. |
| 34 | [Cisco-IOS-XE-l2vpn.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-l2vpn.yang) | L2VPN | Configuration | +13 | All Platforms | Layer 2 VPN configuration | Added 13 new Layer 2 VPN configuration nodes with enhanced validation constraints for VPLS and VPWS services. |
| 35 | [Cisco-IOS-XE-line.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-line.yang) | Line | Configuration | Descriptions only | All Platforms | Console, VTY, and AUX line configuration | Updated console, VTY, and AUX line configuration descriptions for improved management access clarity. |
| 36 | [Cisco-IOS-XE-logging.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-logging.yang) | Logging | Configuration | +8 | All Platforms | System logging and syslog configuration | Added 8 new system logging and syslog configuration nodes with enhanced validation for log filtering. |
| 37 | [Cisco-IOS-XE-mdt-common-defs.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-mdt-common-defs.yang) | MDT common defs | Type Definition | +11 | All Platforms | Model-driven telemetry common definitions | Added 11 new model-driven telemetry common type definitions for standardized subscription structures. |
| 38 | [Cisco-IOS-XE-mld.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-mld.yang) | MLD | Configuration | +1 | All Platforms | Multicast Listener Discovery configuration | Added 1 new node: interface list structures for enhanced Multicast Listener Discovery configuration and management. |
| 39 | [Cisco-IOS-XE-mpls.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-mpls.yang) | MPLS | Configuration | Descriptions only | All Platforms | MPLS protocol and label switching configuration | Updated MPLS protocol and label switching configuration descriptions for better feature documentation. |
| 40 | [Cisco-IOS-XE-mrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-mrp.yang) | MRP | Configuration | +2 | IE3x00 | Media Redundancy Protocol for industrial networks | Added 2 new nodes: enable and vlan fields for Media Redundancy Protocol configuration in industrial network deployments. |
| 41 | [Cisco-IOS-XE-multicast.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-multicast.yang) | Multicast | Configuration | +9 | All Platforms | IP multicast routing configuration | Added 9 new IP multicast routing configuration nodes including PIM enhancements; deprecated 3 legacy multicast options. |
| 42 | [Cisco-IOS-XE-nbar.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-nbar.yang) | NBAR | Configuration | Descriptions only | All Platforms | Network-Based Application Recognition configuration | Updated Network-Based Application Recognition configuration descriptions for application visibility and control. |
| 43 | [Cisco-IOS-XE-nd.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-nd.yang) | ND | Configuration | Descriptions only | All Platforms | IPv6 Neighbor Discovery configuration | Updated IPv6 Neighbor Discovery configuration descriptions for SLAAC and address resolution clarity. |
| 44 | [Cisco-IOS-XE-nhrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-nhrp.yang) | NHRP | Configuration | Descriptions only | All Platforms | Next Hop Resolution Protocol for dynamic tunneling | Updated Next Hop Resolution Protocol configuration descriptions for dynamic tunneling and spoke registration. |
| 45 | [Cisco-IOS-XE-ntp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ntp.yang) | NTP | Configuration | Descriptions only | All Platforms | Network Time Protocol configuration | Enhanced Network Time Protocol validation constraints for improved time synchronization policy enforcement. |
| 46 | [Cisco-IOS-XE-object-group.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-object-group.yang) | Object group | Configuration | +18 | All Platforms | Object grouping for ACLs and policies | Added 18 new object grouping nodes for ACLs and policies; deprecated 18 legacy object-group structures. |
| 47 | [Cisco-IOS-XE-ospfv3.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ospfv3.yang) | OSPFv3 | Configuration | +14 | All Platforms | OSPFv3 for IPv6 routing configuration | Added 14 new OSPFv3 IPv6 routing configuration nodes with enhanced validation constraints for routing policy. |
| 48 | [Cisco-IOS-XE-platform.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-platform.yang) | Platform | Configuration | +7 | All Platforms | Platform-specific configuration and hardware settings | Added 7 new platform-specific configuration nodes for hardware settings and resource management. |
| 49 | [Cisco-IOS-XE-policy.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-policy.yang) | Policy | Configuration | Descriptions only | All Platforms | QoS policy and service policy configuration | Updated QoS policy and service policy configuration descriptions for improved traffic management clarity. |
| 50 | [Cisco-IOS-XE-power.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-power.yang) | Power | Configuration | +3 | All Platforms | Power management and PoE configuration | Added 3 new nodes: wattage container and flexible-poe fields for power management and PoE budget configuration. |
| 51 | [Cisco-IOS-XE-pppoe.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-pppoe.yang) | PPPoE | Configuration | Descriptions only | All Platforms | PPP over Ethernet configuration | Updated PPP over Ethernet configuration descriptions for WAN connectivity feature clarity. |
| 52 | [Cisco-IOS-XE-prp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-prp.yang) | PRP | Configuration | +1 | IE3x00 | Parallel Redundancy Protocol (IEC 62439-3) | Added 1 new node: padding field for Parallel Redundancy Protocol (IEC 62439-3) industrial network configuration. |
| 53 | [Cisco-IOS-XE-ptp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ptp.yang) | PTP | Configuration | +23 | All Platforms | Precision Time Protocol (IEEE 1588) configuration | Added 23 new Precision Time Protocol configuration nodes for IEEE 1588 timing; deprecated 1 legacy PTP option. |
| 54 | [Cisco-IOS-XE-qfp-stats.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-qfp-stats.yang) | QFP stats | Configuration | +2 | All Platforms | Quantum Flow Processor statistics configuration | Added 2 new nodes: pkt-reorder-drop counters for Quantum Flow Processor packet reordering statistics configuration. |
| 55 | [Cisco-IOS-XE-rip.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-rip.yang) | RIP | Configuration | Descriptions only | All Platforms | Routing Information Protocol configuration | Updated Routing Information Protocol configuration descriptions for legacy network support clarity. |
| 56 | [Cisco-IOS-XE-route-map.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-route-map.yang) | Route map | Configuration | +13 | All Platforms | Route manipulation and policy routing configuration | Added 13 new route manipulation and policy routing configuration nodes for enhanced traffic engineering. |
| 57 | [Cisco-IOS-XE-sanet.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sanet.yang) | SANet | Configuration | +2, -1 | All Platforms | Service Advertisement Network configuration | Added 2 new nodes (pqc-type, tls-version) for post-quantum cryptography and TLS configuration; deprecated 1 legacy option. |
| 58 | [Cisco-IOS-XE-segment-routing.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-segment-routing.yang) | Segment routing | Configuration | Descriptions only | ASR, NCS | Segment routing for MPLS and SRv6 configuration | Updated segment routing configuration descriptions for MPLS and SRv6 traffic engineering clarity. |
| 59 | [Cisco-IOS-XE-sip-ua.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sip-ua.yang) | SIP UA | Configuration | Descriptions only | ISR, Voice Gateways | SIP user agent voice configuration | Added SIP user agent voice configuration field for enhanced VoIP call routing options. |
| 60 | [Cisco-IOS-XE-sisf.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-sisf.yang) | SISF | Configuration | Descriptions only | All Platforms | Source Identity Security Features configuration | Updated Source Identity Security Features configuration descriptions for access control clarity. |
| 61 | [Cisco-IOS-XE-site-manager.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-site-manager.yang) | Site manager | Configuration | Descriptions only | All Platforms | Site management and organization configuration | Updated site management and organization configuration descriptions for multi-site deployment clarity. |
| 62 | [Cisco-IOS-XE-snmp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-snmp.yang) | SNMP | Configuration | +12 | All Platforms | SNMP agent and trap configuration | Added 12 new SNMP agent and trap configuration nodes including v3 security enhancements; deprecated 2 legacy options. |
| 63 | [Cisco-IOS-XE-spanning-tree.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-spanning-tree.yang) | Spanning tree | Configuration | Descriptions only | All Platforms | Spanning Tree Protocol configuration | Updated Spanning Tree Protocol configuration descriptions for layer 2 loop prevention clarity. |
| 64 | [Cisco-IOS-XE-switch.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-switch.yang) | Switch | Configuration | +7 | All Platforms | Cat9K, IE3x00 | Added 7 new switch-specific configuration nodes for Catalyst features with enhanced validation constraints. |
| 65 | [Cisco-IOS-XE-template.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-template.yang) | Template | Configuration | +44 | All Platforms | Configuration template management | Added 44 new configuration template management nodes for streamlined device provisioning workflows. |
| 66 | [Cisco-IOS-XE-track.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-track.yang) | Track | Configuration | +2, -2 | All Platforms | Object tracking for high availability | Added 2 new nodes: tracked-object list and delay container; removed 2 legacy nodes for enhanced object tracking high availability configuration. |
| 67 | [Cisco-IOS-XE-tunnel.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-tunnel.yang) | Tunnel | Configuration | Descriptions only | All Platforms | Tunnel interface and encapsulation configuration | Added IPv4 container for enhanced tunnel interface and encapsulation configuration options. |
| 68 | [Cisco-IOS-XE-vlan.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-vlan.yang) | VLAN | Configuration | Descriptions only | All Platforms | VLAN configuration and management | Updated VLAN configuration and management descriptions for layer 2 network segmentation clarity. |
| 69 | [Cisco-IOS-XE-voice-class.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-voice-class.yang) | Voice class | Configuration | Descriptions only | ISR, Voice Gateways | Voice class configuration for call routing | Updated voice class configuration descriptions for call routing and dial-plan management clarity. |
| 70 | [Cisco-IOS-XE-voice-register.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-voice-register.yang) | Voice register | Configuration | Descriptions only | ISR, Voice Gateways | Voice registration and SIP endpoints | Updated voice registration and SIP endpoint configuration descriptions for VoIP deployment clarity. |
| 71 | [Cisco-IOS-XE-voice.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-voice.yang) | Voice | Configuration | +5 | ISR, Voice Gateways | Voice dial-peer and telephony configuration | Added 5 new voice dial-peer and telephony configuration nodes for enhanced call routing options. |
| 72 | [Cisco-IOS-XE-vrrp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-vrrp.yang) | VRRP | Configuration | +4 | All Platforms | Virtual Router Redundancy Protocol configuration | Added 4 new Virtual Router Redundancy Protocol configuration nodes with enhanced validation for FHRP policy. |
| 73 | [Cisco-IOS-XE-vtp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-vtp.yang) | VTP | Configuration | +2 | All Platforms | VLAN Trunking Protocol configuration | Added 2 new nodes: vtp field for VLAN Trunking Protocol configuration and inter-switch VLAN synchronization. |
| 74 | [Cisco-IOS-XE-wccp.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wccp.yang) | WCCP | Configuration | Descriptions only | All Platforms | Web Cache Communication Protocol configuration | Enhanced Web Cache Communication Protocol validation constraints for cache redirection policy enforcement. |
| 75 | [Cisco-IOS-XE-yang-interfaces-oper.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-yang-interfaces-oper.yang) | YANG interfaces oper | Operational Data | +6 | All Platforms | YANG interface operational data and schema visibility | Added 6 new YANG interface operational nodes for schema visibility and model discovery telemetry. |
| 76 | [Cisco-IOS-XE-xcopy-events.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-xcopy-events.yang) | Xcopy events | Event Notification | +1 | All Platforms | File copy event notifications | Added dwnld-err field for file copy event notifications with enhanced error tracking and troubleshooting. |

---

## UPDATED Wireless Models (11 additional models not in other sections)

| # | YANG Model | Module Name | Type | # XPaths | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|----------|---------------------|---------|--------------|
| 1 | [Cisco-IOS-XE-wireless-ap-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-ap-cfg.yang) | Wireless AP cfg | Configuration | +1 / 47 | Wireless Controllers | Added AP name field under static AP configuration for identification | Added ap-name field under static AP configuration for improved access point identification and management. |
| 2 | [Cisco-IOS-XE-wireless-general-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-general-cfg.yang) | Wireless general cfg | Configuration | +2 / 128 | Wireless Controllers | Client IP event notification interval, multicast-over-multicast IPv6 validation | Added client IP event notification interval and multicast-over-multicast IPv6 validation. |
| 3 | [Cisco-IOS-XE-wireless-rfid-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-rfid-cfg.yang) | Wireless RFID cfg | Configuration | +1 / 9 | Wireless Controllers | Call admission control drop allowance for RFID tracking | Added allow-cac-drop field for call admission control drop allowance in RFID tracking configurations. |
| 4 | [Cisco-IOS-XE-wireless-rlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-rlan-cfg.yang) | Wireless RLAN cfg | Configuration | 1 / 79 | Wireless Controllers | Default violation mode configuration for remote LAN policy | Modified 1 default value: Added default value "violation-mode-replace" for violation-mode leaf in remote LAN configuration. |
| 5 | [Cisco-IOS-XE-wireless-site-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-site-cfg.yang) | Wireless site cfg | Configuration | +2 / 193 | Wireless Controllers | AP MACsec security and console speed settings for site management | Added MACsec security and console speed settings containers for wireless site management and AP access control. |
| 6 | [Cisco-IOS-XE-wireless-wlan-cfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-wlan-cfg.yang) | Wireless WLAN cfg | Configuration | +3 / 383 | Wireless Controllers | AP hostname in beacons, minimum data rate, deprecated OSEN/load balance | Added AP hostname in beacons and minimum data rate fields; deprecated OSEN authentication and load balance options. |
| 7 | [Cisco-IOS-XE-wireless-ap-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-ap-types.yang) | Wireless AP types | Type Definition | +7 / 209 | Wireless Controllers | UWB way-finding types, AP MACsec types, WiFi-IOT coexistence types | Added 7 new type definitions for UWB way-finding, AP MACsec encryption, and WiFi-IOT coexistence features. |
| 14 | [Cisco-IOS-XE-wireless-enum-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-enum-types.yang) | Wireless enum types | Type Definition | +15+ enums | Wireless Controllers | UWB way-finding enums, data rate enums, client IP event frequency | Added 15+ new enum values: enm-ap-console-speed (3), rate-type (12 data rates: 1m-54m), plus UWB way-finding, client IP event frequency, URWB status, AP ciphersuite enums. |
| 15 | [Cisco-IOS-XE-wireless-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-types.yang) | Wireless types | Type Definition | +15+ enums / 101 | Wireless Controllers | Bulk UWB time-of-arrival types, AP reboot stats, UWB UCI parameters | Added 15+ new ap-reboot-reason enum values (59-73+): type-meraki, type-site-survey, country-changed, pnp-dot1x-config/failure/timeout, dual-5g-radio, etc.; added bulk UWB ToA support. |
| 16 | [Cisco-IOS-XE-wireless-urwb-common-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-wireless-urwb-common-types.yang) | Wireless URWB common types | Type Definition | +11 / 46 | Wireless Controllers | URWB mobility/reliability parameters, radio role enumeration | Added 11 new URWB mobility/reliability parameter types and radio role enumeration. |

---

## UPDATED Type Definitions (8 models - partial list)

| # | YANG Model | Module Name | Type | # XPaths (Updated) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 1 | [Cisco-IOS-XE-install-event-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-install-event-types.yang) | Install event types | Type Definition | Descriptions only | All Platforms | Software installation event type definitions | Updated software installation event type definitions for improved install/upgrade event notification clarity. |
| 2 | [Cisco-IOS-XE-alarm-profile.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-alarm-profile.yang) | Alarm profile | Type Definition | +10 | All Platforms | Alarm profiling type definitions and severity levels | Added 10 new alarm profiling nodes and imported features module for severity level definitions. |

---

## UPDATED Deviation Models (10 models)

| # | YANG Model | Module Name | Type | # XPaths (Updated) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 1 | [Cisco-IOS-XE-aaa-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-aaa-deviation.yang) | AAA deviation | Deviation | Descriptions only | Platform-specific | Platform-specific AAA feature restrictions and deviations | Updated platform-specific AAA feature restriction descriptions for accurate capability documentation. |
| 2 | [Cisco-IOS-XE-ethernet-mcp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-ethernet-mcp-deviation.yang) | Ethernet MCP deviation | Deviation | Descriptions only | Platform-specific | Ethernet MACsec Channel Protection deviations | Updated Ethernet MACsec Channel Protection deviation descriptions for platform encryption support clarity. |
| 3 | [Cisco-IOS-XE-interfaces-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-interfaces-deviation.yang) | Interfaces deviation | Deviation | Descriptions only | Platform-specific | Interface feature support variations across platforms | Updated interface feature support deviation descriptions for platform-specific capability accuracy. |
| 4 | [Cisco-IOS-XE-logging-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-logging-deviation.yang) | Logging deviation | Deviation | 24 | Platform-specific | Logging feature availability per platform | Modified 24 deviation statements: Minor refinements to platform-specific logging feature availability documentation. |
| 5 | [Cisco-IOS-XE-switch-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/Cisco-IOS-XE-switch-deviation.yang) | Switch deviation | Deviation | Descriptions only | Cat9K | Catalyst 9000 series switch-specific deviations | Added switch-specific imports with enhanced validation constraints for Catalyst 9000 series feature deviations. |

---

## UPDATED Open Standard (12 models)

| # | YANG Model | Module Name | Type | # XPaths (Updated) | Platforms Supported | Summary | What Changed |
|---|------------|-------------|------|--------------------------|---------------------|---------|--------------|
| 1 | [cisco-xe-openconfig-access-points-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/cisco-xe-openconfig-access-points-deviation.yang) | OC access points deviation | Deviation | -12 | All Platforms | OpenConfig wireless access point model deviations for IOS-XE | Removed 12 unsupported OpenConfig wireless access point model features for IOS-XE platform alignment. |
| 2 | [cisco-xe-openconfig-isis-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/cisco-xe-openconfig-isis-deviation.yang) | OC ISIS deviation | Deviation | ~31 | All Platforms | OpenConfig IS-IS routing deviations | Updated OpenConfig IS-IS routing protocol deviation descriptions for IOS-XE implementation alignment. |
| 3 | [cisco-xe-openconfig-network-instance-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/cisco-xe-openconfig-network-instance-deviation.yang) | OC network instance deviation | Deviation | ~9 | All Platforms | OpenConfig network instance (VRF) deviations | Updated OpenConfig network instance (VRF) deviation descriptions for IOS-XE VRF feature alignment. |
| 4 | [cisco-xe-routing-isr-openconfig-platform-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/cisco-xe-routing-isr-openconfig-platform-deviation.yang) | OC platform deviation | Deviation | -10 | ISR | OpenConfig platform model deviations for ISR routers | Removed 10 unsupported OpenConfig platform model features for ISR router hardware alignment. |
| 5 | [cisco-xe-switching-openconfig-lacp-deviation.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/cisco-xe-switching-openconfig-lacp-deviation.yang) | OC LACP deviation | Deviation | -4 | Cat9K, IE3x00 | OpenConfig LACP deviations for switching platforms | Removed 4 unsupported OpenConfig LACP features for IOS-XE switching platform alignment. |
| 6 | [openconfig-interfaces.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-interfaces.yang) | OC interfaces | Standard | +28 | All Platforms | OpenConfig interfaces standard model updates | Added 28 new interface configuration nodes and imported transport-types for enhanced OpenConfig standard support. |
| 7 | [openconfig-isis-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-isis-types.yang) | OC ISIS types | Standard | +3, -3 | All Platforms | OpenConfig IS-IS type definitions | Minor refinements with 3 additions and 3 removals for IS-IS type definition alignment with latest standard. |
| 8 | [openconfig-system.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-system.yang) | OC system | Standard | +34 | All Platforms | OpenConfig system management model | Added 34 new system management nodes and imported platform/network-instance modules for expanded OpenConfig coverage. |
| 9 | [openconfig-vlan-types.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/openconfig-vlan-types.yang) | OC VLAN types | Standard | +4, -4 | All Platforms | OpenConfig VLAN type definitions | Minor refinements with 4 additions and 4 removals for VLAN type definition alignment with latest standard. |
| 10 | [confd_dyncfg.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/confd_dyncfg.yang) | Confd dyncfg | Vendor Extension | Descriptions only | All Platforms | Confd dynamic configuration module | Updated Confd dynamic configuration module descriptions for runtime configuration management clarity. |
| 11 | [tailf-cli-extensions.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/tailf-cli-extensions.yang) | Tailf CLI extensions | Vendor Extension | +3 | All Platforms | Tailf CLI extension capabilities | Added 3 containers (should/will/is) for enhanced CLI extension capabilities; deprecated 3 legacy CLI extension options. |
| 12 | [tailf-common.yang](https://github.com/YangModels/yang/blob/main/vendor/cisco/xe/2611/tailf-common.yang) | Tailf common | Vendor Extension | Descriptions only | All Platforms | Tailf common definitions and extensions | Updated Tailf common definitions and extensions descriptions for NETCONF/YANG tool integration clarity. |

---

**Document Updated**: May 5, 2026  
**Source Comparison**: v17.18.1 → v26.11
