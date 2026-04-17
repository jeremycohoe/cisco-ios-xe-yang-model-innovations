# IOS-XE YANG Model Innovation: 16.3.1 → 26.1.1

> **32 releases analyzed** spanning IOS-XE 16.3.1 through 26.1.1
>
> **Key Numbers:**
> - Model count: **83 → 887** (+969% growth)
> - Total new model introductions across releases: **965**
> - Models present since 16.3.1: **35**

---

## 1. YANG Model Growth Over Time

Total `.yang` files per IOS-XE release, broken down by origin.

| Release | Total | Cisco Native | OpenConfig | IETF | Tailf | Other |
|---------|------:|-------------:|-----------:|-----:|------:|------:|
| 16.3.1 | 83 | 0 | 0 | 16 | 15 | 52 |
| 16.3.2 | 74 | 0 | 0 | 15 | 8 | 51 |
| 16.4.1 | 74 | 0 | 0 | 15 | 8 | 51 |
| 16.5.1 | 170 | 111 | 0 | 25 | 10 | 24 |
| 16.6.1 | 235 | 122 | 30 | 24 | 13 | 46 |
| 16.6.2 | 227 | 122 | 25 | 24 | 13 | 43 |
| 16.7.1 | 218 | 118 | 21 | 24 | 13 | 42 |
| 16.8.1 | 290 | 146 | 52 | 25 | 13 | 54 |
| 16.9.1 | 315 | 162 | 57 | 27 | 13 | 56 |
| 16.9.3 | 311 | 162 | 54 | 26 | 13 | 56 |
| 16.10.1 | 368 | 215 | 57 | 26 | 13 | 57 |
| 16.11.1 | 404 | 235 | 56 | 26 | 13 | 74 |
| 16.12.1 | 472 | 272 | 84 | 26 | 13 | 77 |
| 17.1.1 | 486 | 282 | 84 | 26 | 13 | 81 |
| 17.2.1 | 510 | 306 | 84 | 26 | 13 | 81 |
| 17.3.1 | 549 | 341 | 86 | 28 | 13 | 81 |
| 17.4.1 | 571 | 362 | 84 | 28 | 13 | 84 |
| 17.5.1 | 599 | 388 | 84 | 28 | 14 | 85 |
| 17.6.1 | 629 | 416 | 84 | 29 | 14 | 86 |
| 17.7.1 | 637 | 420 | 86 | 29 | 14 | 88 |
| 17.8.1 | 678 | 441 | 108 | 29 | 14 | 86 |
| 17.9.1 | 701 | 461 | 110 | 29 | 14 | 87 |
| 17.10.1 | 700 | 463 | 110 | 28 | 14 | 85 |
| 17.11.1 | 712 | 470 | 110 | 29 | 17 | 86 |
| 17.12.1 | 719 | 475 | 110 | 30 | 18 | 86 |
| 17.13.1 | 731 | 487 | 110 | 30 | 18 | 86 |
| 17.14.1 | 771 | 506 | 128 | 30 | 20 | 87 |
| 17.15.1 | 799 | 534 | 128 | 30 | 20 | 87 |
| 17.16.1 | 819 | 554 | 128 | 30 | 20 | 87 |
| 17.17.1 | 829 | 564 | 128 | 30 | 20 | 87 |
| 17.18.1 | 848 | 581 | 129 | 34 | 20 | 84 |
| 26.1.1 | 887 | 613 | 134 | 34 | 21 | 85 |

## 2. New & Removed Models Per Release

| Release | Total | New | Removed | Net Change |
|---------|------:|----:|--------:|-----------:|
| 16.3.1 | 83 | +83 | -0 | +83 |
| 16.3.2 | 74 | +2 | -11 | -9 |
| 16.4.1 | 74 | +0 | -0 | +0 |
| 16.5.1 | 170 | +126 | -30 | +96 |
| 16.6.1 | 235 | +74 | -9 | +65 |
| 16.6.2 | 227 | +4 | -12 | -8 |
| 16.7.1 | 218 | +4 | -13 | -9 |
| 16.8.1 | 290 | +73 | -1 | +72 |
| 16.9.1 | 315 | +27 | -2 | +25 |
| 16.9.3 | 311 | +1 | -5 | -4 |
| 16.10.1 | 368 | +59 | -2 | +57 |
| 16.11.1 | 404 | +44 | -8 | +36 |
| 16.12.1 | 472 | +70 | -2 | +68 |
| 17.1.1 | 486 | +20 | -6 | +14 |
| 17.2.1 | 510 | +24 | -0 | +24 |
| 17.3.1 | 549 | +39 | -0 | +39 |
| 17.4.1 | 571 | +28 | -6 | +22 |
| 17.5.1 | 599 | +31 | -3 | +28 |
| 17.6.1 | 629 | +31 | -1 | +30 |
| 17.7.1 | 637 | +9 | -1 | +8 |
| 17.8.1 | 678 | +45 | -4 | +41 |
| 17.9.1 | 701 | +26 | -3 | +23 |
| 17.10.1 | 700 | +11 | -12 | -1 |
| 17.11.1 | 712 | +14 | -2 | +12 |
| 17.12.1 | 719 | +9 | -2 | +7 |
| 17.13.1 | 731 | +16 | -4 | +12 |
| 17.14.1 | 771 | +43 | -3 | +40 |
| 17.15.1 | 799 | +30 | -2 | +28 |
| 17.16.1 | 819 | +21 | -1 | +20 |
| 17.17.1 | 829 | +11 | -1 | +10 |
| 17.18.1 | 848 | +34 | -15 | +19 |
| 26.1.1 | 887 | +39 | -0 | +39 |

## 3. Top 10 Releases by New Model Count

| Rank | Release | New Models Introduced |
|------|---------|----------------------:|
| 1 | 16.5.1 | +126 |
| 2 | 16.3.1 | +83 |
| 3 | 16.6.1 | +74 |
| 4 | 16.8.1 | +73 |
| 5 | 16.12.1 | +70 |
| 6 | 16.10.1 | +59 |
| 7 | 17.8.1 | +45 |
| 8 | 16.11.1 | +44 |
| 9 | 17.14.1 | +43 |
| 10 | 17.3.1 | +39 |

## 4. Notable New Cisco-Native Models Per Release

New `Cisco-IOS-XE-*` models per release (excluding deviations and type definitions).

### 16.5.1 (+109 new models)

- `Cisco-IOS-XE-aaa`
- `Cisco-IOS-XE-acl-oper`
- `Cisco-IOS-XE-acl`
- `Cisco-IOS-XE-ap`
- `Cisco-IOS-XE-atm`
- `Cisco-IOS-XE-bba-group`
- `Cisco-IOS-XE-bfd-oper`
- `Cisco-IOS-XE-bfd`
- `Cisco-IOS-XE-bgp-oper`
- `Cisco-IOS-XE-bgp`
- `Cisco-IOS-XE-bridge-domain`
- `Cisco-IOS-XE-call-home`
- `Cisco-IOS-XE-card`
- `Cisco-IOS-XE-cdp`
- `Cisco-IOS-XE-cef`
- `Cisco-IOS-XE-cfm-oper`
- `Cisco-IOS-XE-checkpoint-archive-oper`
- `Cisco-IOS-XE-coap`
- `Cisco-IOS-XE-controller`
- `Cisco-IOS-XE-crypto`
- `Cisco-IOS-XE-cts`
- `Cisco-IOS-XE-device-sensor`
- `Cisco-IOS-XE-device-tracking`
- `Cisco-IOS-XE-dhcp`
- `Cisco-IOS-XE-diagnostics`
- `Cisco-IOS-XE-diffserv-target-oper`
- `Cisco-IOS-XE-dot1x`
- `Cisco-IOS-XE-eem`
- `Cisco-IOS-XE-efp-oper`
- `Cisco-IOS-XE-eigrp`
- `Cisco-IOS-XE-environment-oper`
- `Cisco-IOS-XE-ethernet`
- `Cisco-IOS-XE-ezpm`
- `Cisco-IOS-XE-features`
- `Cisco-IOS-XE-flow-monitor-oper`
- `Cisco-IOS-XE-flow`
- `Cisco-IOS-XE-http`
- `Cisco-IOS-XE-icmp`
- `Cisco-IOS-XE-igmp`
- `Cisco-IOS-XE-interface-common`
- `Cisco-IOS-XE-interfaces`
- `Cisco-IOS-XE-ip-sla-oper`
- `Cisco-IOS-XE-ip`
- `Cisco-IOS-XE-ipv6`
- `Cisco-IOS-XE-isis`
- `Cisco-IOS-XE-l2vpn`
- `Cisco-IOS-XE-l3vpn`
- `Cisco-IOS-XE-license`
- `Cisco-IOS-XE-line`
- `Cisco-IOS-XE-lisp`
- `Cisco-IOS-XE-lldp-oper`
- `Cisco-IOS-XE-lldp`
- `Cisco-IOS-XE-logging`
- `Cisco-IOS-XE-memory-oper`
- `Cisco-IOS-XE-mka`
- `Cisco-IOS-XE-mld`
- `Cisco-IOS-XE-mpls-fwd-oper`
- `Cisco-IOS-XE-mpls-ldp`
- `Cisco-IOS-XE-mpls`
- `Cisco-IOS-XE-multicast`
- `Cisco-IOS-XE-nat`
- `Cisco-IOS-XE-native`
- `Cisco-IOS-XE-nbar`
- `Cisco-IOS-XE-nd`
- `Cisco-IOS-XE-nhrp`
- `Cisco-IOS-XE-ntp`
- `Cisco-IOS-XE-object-group`
- `Cisco-IOS-XE-ospf`
- `Cisco-IOS-XE-ospfv3`
- `Cisco-IOS-XE-otv`
- `Cisco-IOS-XE-parser`
- `Cisco-IOS-XE-pathmgr`
- `Cisco-IOS-XE-pfr`
- `Cisco-IOS-XE-platform-software-oper`
- `Cisco-IOS-XE-platform`
- `Cisco-IOS-XE-policy`
- `Cisco-IOS-XE-power`
- `Cisco-IOS-XE-ppp`
- `Cisco-IOS-XE-process-cpu-oper`
- `Cisco-IOS-XE-process-memory-oper`
- `Cisco-IOS-XE-qos`
- `Cisco-IOS-XE-rip`
- `Cisco-IOS-XE-route-map`
- `Cisco-IOS-XE-rpc`
- `Cisco-IOS-XE-sanet`
- `Cisco-IOS-XE-segment-routing`
- `Cisco-IOS-XE-service-chain`
- `Cisco-IOS-XE-service-discovery`
- `Cisco-IOS-XE-service-insertion`
- `Cisco-IOS-XE-service-routing`
- `Cisco-IOS-XE-sla`
- `Cisco-IOS-XE-snmp`
- `Cisco-IOS-XE-spanning-tree`
- `Cisco-IOS-XE-switch`
- `Cisco-IOS-XE-track`
- `Cisco-IOS-XE-trustsec-oper`
- `Cisco-IOS-XE-tunnel`
- `Cisco-IOS-XE-udld`
- `Cisco-IOS-XE-utd`
- `Cisco-IOS-XE-virtual-service-oper`
- `Cisco-IOS-XE-vlan`
- `Cisco-IOS-XE-voice`
- `Cisco-IOS-XE-vpdn`
- `Cisco-IOS-XE-vservice`
- `Cisco-IOS-XE-vstack`
- `Cisco-IOS-XE-vtp`
- `Cisco-IOS-XE-wccp`
- `Cisco-IOS-XE-wsma`
- `Cisco-IOS-XE-zone`

### 16.6.1 (+11 new models)

- `Cisco-IOS-XE-arp`
- `Cisco-IOS-XE-bgp-common-oper`
- `Cisco-IOS-XE-bgp-route-oper`
- `Cisco-IOS-XE-cdp-oper`
- `Cisco-IOS-XE-mdt-cfg`
- `Cisco-IOS-XE-mdt-common-defs`
- `Cisco-IOS-XE-mdt-oper`
- `Cisco-IOS-XE-mmode`
- `Cisco-IOS-XE-platform-oper`
- `Cisco-IOS-XE-rsvp`
- `Cisco-IOS-XE-template`

### 16.6.2 (+1 new models)

- `Cisco-IOS-XE-umbrella`

### 16.7.1 (+2 new models)

- `Cisco-IOS-XE-iwanfabric`
- `Cisco-IOS-XE-lisp-oper`

### 16.8.1 (+27 new models)

- `Cisco-IOS-XE-aaa-oper`
- `Cisco-IOS-XE-avb`
- `Cisco-IOS-XE-cellular`
- `Cisco-IOS-XE-cellwan-oper`
- `Cisco-IOS-XE-coap`
- `Cisco-IOS-XE-device-hardware-oper`
- `Cisco-IOS-XE-device-sensor`
- `Cisco-IOS-XE-dhcp-oper`
- `Cisco-IOS-XE-eta`
- `Cisco-IOS-XE-fib-oper`
- `Cisco-IOS-XE-interfaces-oper`
- `Cisco-IOS-XE-ipv6-oper`
- `Cisco-IOS-XE-mmode`
- `Cisco-IOS-XE-mvrp`
- `Cisco-IOS-XE-nat-oper`
- `Cisco-IOS-XE-ntp-oper`
- `Cisco-IOS-XE-ospf-oper`
- `Cisco-IOS-XE-ppp-oper`
- `Cisco-IOS-XE-ptp`
- `Cisco-IOS-XE-spanning-tree-oper`
- `Cisco-IOS-XE-stackwise-virtual`
- `Cisco-IOS-XE-switch`
- `Cisco-IOS-XE-tcam-oper`
- `Cisco-IOS-XE-udld`
- `Cisco-IOS-XE-vlan-oper`
- `Cisco-IOS-XE-vrrp-oper`
- `Cisco-IOS-XE-vstack`

### 16.9.1 (+17 new models)

- `Cisco-IOS-XE-arp-oper`
- `Cisco-IOS-XE-boot-integrity-oper`
- `Cisco-IOS-XE-breakout-port-oper`
- `Cisco-IOS-XE-bridge-oper`
- `Cisco-IOS-XE-controller-vdsl-oper`
- `Cisco-IOS-XE-fw-oper`
- `Cisco-IOS-XE-ios-common-oper`
- `Cisco-IOS-XE-ios-events-oper`
- `Cisco-IOS-XE-linecard-oper`
- `Cisco-IOS-XE-mpls-forwarding-oper`
- `Cisco-IOS-XE-nam`
- `Cisco-IOS-XE-poe-oper`
- `Cisco-IOS-XE-transceiver-oper`
- `Cisco-IOS-XE-utd-common-oper`
- `Cisco-IOS-XE-utd-oper`
- `Cisco-IOS-XE-virtual-service-cfg`
- `Cisco-IOS-XE-vrrp`

### 16.9.3 (+1 new models)

- `Cisco-IOS-XE-pnp`

### 16.10.1 (+47 new models)

- `Cisco-IOS-XE-app-hosting-cfg`
- `Cisco-IOS-XE-app-hosting-oper`
- `Cisco-IOS-XE-dialer`
- `Cisco-IOS-XE-gir-oper`
- `Cisco-IOS-XE-ha-oper`
- `Cisco-IOS-XE-im-events-oper`
- `Cisco-IOS-XE-ios-events-oper`
- `Cisco-IOS-XE-mlppp-oper`
- `Cisco-IOS-XE-pppoe`
- `Cisco-IOS-XE-serial`
- `Cisco-IOS-XE-stack-oper`
- `Cisco-IOS-XE-voice-oper`
- `Cisco-IOS-XE-wireless-access-point-oper`
- `Cisco-IOS-XE-wireless-ap-cfg`
- `Cisco-IOS-XE-wireless-apf-cfg`
- `Cisco-IOS-XE-wireless-client-oper`
- `Cisco-IOS-XE-wireless-cts-sxp-cfg`
- `Cisco-IOS-XE-wireless-cts-sxp-oper`
- `Cisco-IOS-XE-wireless-dot11-cfg`
- `Cisco-IOS-XE-wireless-events-oper`
- `Cisco-IOS-XE-wireless-fabric-cfg`
- `Cisco-IOS-XE-wireless-flex-cfg`
- `Cisco-IOS-XE-wireless-fqdn-cfg`
- `Cisco-IOS-XE-wireless-fqdn-oper`
- `Cisco-IOS-XE-wireless-general-cfg`
- `Cisco-IOS-XE-wireless-hyperlocation-oper`
- `Cisco-IOS-XE-wireless-lisp-agent-oper`
- `Cisco-IOS-XE-wireless-location-cfg`
- `Cisco-IOS-XE-wireless-location-oper`
- `Cisco-IOS-XE-wireless-mcast-oper`
- `Cisco-IOS-XE-wireless-mesh-cfg`
- `Cisco-IOS-XE-wireless-mesh-oper`
- `Cisco-IOS-XE-wireless-mobility-cfg`
- `Cisco-IOS-XE-wireless-mobility-oper`
- `Cisco-IOS-XE-wireless-mstream-cfg`
- `Cisco-IOS-XE-wireless-nmsp-oper`
- `Cisco-IOS-XE-wireless-rf-cfg`
- `Cisco-IOS-XE-wireless-rf-profile-oper`
- `Cisco-IOS-XE-wireless-rfid-cfg`
- `Cisco-IOS-XE-wireless-rfid-oper`
- `Cisco-IOS-XE-wireless-rogue-cfg`
- `Cisco-IOS-XE-wireless-rogue-oper`
- `Cisco-IOS-XE-wireless-rrm-cfg`
- `Cisco-IOS-XE-wireless-rrm-oper`
- `Cisco-IOS-XE-wireless-security-cfg`
- `Cisco-IOS-XE-wireless-site-cfg`
- `Cisco-IOS-XE-wireless-wlan-cfg`

### 16.11.1 (+20 new models)

- `Cisco-IOS-XE-cable-diag-oper`
- `Cisco-IOS-XE-crypto-oper`
- `Cisco-IOS-XE-crypto-pki-oper`
- `Cisco-IOS-XE-dapr`
- `Cisco-IOS-XE-eigrp-oper`
- `Cisco-IOS-XE-mdns-gateway`
- `Cisco-IOS-XE-qfp-stats`
- `Cisco-IOS-XE-site-manager`
- `Cisco-IOS-XE-stacking-oper`
- `Cisco-IOS-XE-tunnel-oper`
- `Cisco-IOS-XE-umbrella-oper-dp`
- `Cisco-IOS-XE-umbrella-oper`
- `Cisco-IOS-XE-vrf-oper`
- `Cisco-IOS-XE-vxlan`
- `Cisco-IOS-XE-wireless-ble-mgmt-oper`
- `Cisco-IOS-XE-wireless-general-oper`
- `Cisco-IOS-XE-wireless-mdns-oper`
- `Cisco-IOS-XE-wireless-rlan-cfg`
- `Cisco-IOS-XE-wireless-tunnel-cfg`
- `Cisco-IOS-XE-yang-interfaces-cfg`

### 16.12.1 (+37 new models)

- `Cisco-IOS-XE-aaa-rpc`
- `Cisco-IOS-XE-arp-rpc`
- `Cisco-IOS-XE-bgp-rpc`
- `Cisco-IOS-XE-cable-diag-rpc`
- `Cisco-IOS-XE-cellular-rpc`
- `Cisco-IOS-XE-crypto-rpc`
- `Cisco-IOS-XE-cts-rpc`
- `Cisco-IOS-XE-dhcp-rpc`
- `Cisco-IOS-XE-docsis-oper`
- `Cisco-IOS-XE-eigrp-obsolete`
- `Cisco-IOS-XE-ethernet-cfm-efp`
- `Cisco-IOS-XE-ethernet-oam`
- `Cisco-IOS-XE-factory-reset-secure-rpc`
- `Cisco-IOS-XE-flow-rpc`
- `Cisco-IOS-XE-g8032`
- `Cisco-IOS-XE-matm-oper`
- `Cisco-IOS-XE-mka-oper`
- `Cisco-IOS-XE-ospf-obsolete`
- `Cisco-IOS-XE-ospf-rpc`
- `Cisco-IOS-XE-platform-rpc`
- `Cisco-IOS-XE-ptp-pi`
- `Cisco-IOS-XE-scada-gw-oper`
- `Cisco-IOS-XE-stack-mgr-events-oper`
- `Cisco-IOS-XE-switch-rpc`
- `Cisco-IOS-XE-ucse-oper`
- `Cisco-IOS-XE-ucse-rpc`
- `Cisco-IOS-XE-ucse`
- `Cisco-IOS-XE-umbrella-rpc`
- `Cisco-IOS-XE-utd-rpc`
- `Cisco-IOS-XE-voice-register`
- `Cisco-IOS-XE-wireless-access-point-cmd-rpc`
- `Cisco-IOS-XE-wireless-file-transfer-cfg`
- `Cisco-IOS-XE-wireless-hotspot-cfg`
- `Cisco-IOS-XE-wireless-image-download-cfg`
- `Cisco-IOS-XE-wireless-mobility-express-rpc`
- `Cisco-IOS-XE-wireless-radio-cfg`
- `Cisco-IOS-XE-zone-rpc`

### 17.1.1 (+11 new models)

- `Cisco-IOS-XE-controller-t1e1-oper`
- `Cisco-IOS-XE-crypto-pki-events`
- `Cisco-IOS-XE-identity-oper`
- `Cisco-IOS-XE-isdn-oper`
- `Cisco-IOS-XE-perf-measure`
- `Cisco-IOS-XE-platform-common-oper`
- `Cisco-IOS-XE-platform-events-oper`
- `Cisco-IOS-XE-rmi-dad`
- `Cisco-IOS-XE-scada-gw`
- `Cisco-IOS-XE-sm-events-oper`
- `Cisco-IOS-XE-wireless-awips-oper`

### 17.2.1 (+23 new models)

- `Cisco-IOS-XE-controller-shdsl-common`
- `Cisco-IOS-XE-controller-shdsl-events`
- `Cisco-IOS-XE-controller-shdsl-oper`
- `Cisco-IOS-XE-g8032`
- `Cisco-IOS-XE-gnss-oper`
- `Cisco-IOS-XE-install-events`
- `Cisco-IOS-XE-install-rpc`
- `Cisco-IOS-XE-ip-sla-events`
- `Cisco-IOS-XE-ipmux`
- `Cisco-IOS-XE-isg`
- `Cisco-IOS-XE-l2tp-oper`
- `Cisco-IOS-XE-lacp-oper`
- `Cisco-IOS-XE-mpls-ldp-oper`
- `Cisco-IOS-XE-ptp-synce-oper`
- `Cisco-IOS-XE-qfp-classification-oper`
- `Cisco-IOS-XE-qfp-stats-oper`
- `Cisco-IOS-XE-rawsocket-oper`
- `Cisco-IOS-XE-rawsocket`
- `Cisco-IOS-XE-sd-vxlan-oper`
- `Cisco-IOS-XE-synce`
- `Cisco-IOS-XE-voice-port`
- `Cisco-IOS-XE-wireless-access-point-cfg-rpc`
- `Cisco-IOS-XE-wireless-access-point-cmd-rpc`

### 17.3.1 (+30 new models)

- `Cisco-IOS-XE-banner-internal`
- `Cisco-IOS-XE-digital-io-oper`
- `Cisco-IOS-XE-digitalio`
- `Cisco-IOS-XE-eogre-tunnel-oper`
- `Cisco-IOS-XE-frame-relay`
- `Cisco-IOS-XE-install-oper`
- `Cisco-IOS-XE-isdn`
- `Cisco-IOS-XE-macsec-oper`
- `Cisco-IOS-XE-mdt-oper-v2`
- `Cisco-IOS-XE-mobileip`
- `Cisco-IOS-XE-mroute-oper`
- `Cisco-IOS-XE-multicast-rpc`
- `Cisco-IOS-XE-ncch-cfg`
- `Cisco-IOS-XE-ncch-oper`
- `Cisco-IOS-XE-ospf-common`
- `Cisco-IOS-XE-ospf-events`
- `Cisco-IOS-XE-perf-measure-events`
- `Cisco-IOS-XE-perf-measure-oper`
- `Cisco-IOS-XE-pim-oper`
- `Cisco-IOS-XE-qfp-resource-utilization-oper`
- `Cisco-IOS-XE-switch-dp-mac-learning-oper`
- `Cisco-IOS-XE-switch-dp-punt-inject-oper`
- `Cisco-IOS-XE-switch-dp-resources-oper`
- `Cisco-IOS-XE-voice-class`
- `Cisco-IOS-XE-voice-dspfarm`
- `Cisco-IOS-XE-wireless-ble-ltx-oper`
- `Cisco-IOS-XE-wireless-ble-mgmt-cmd-rpc`
- `Cisco-IOS-XE-wireless-dot15-cfg`
- `Cisco-IOS-XE-wireless-rule-cfg`
- `Cisco-IOS-XE-wireless-rule-mdns-oper`

### 17.4.1 (+18 new models)

- `Cisco-IOS-XE-app-hosting`
- `Cisco-IOS-XE-appqoe-events`
- `Cisco-IOS-XE-appqoe-oper`
- `Cisco-IOS-XE-dhcp-security-track-server-oper`
- `Cisco-IOS-XE-endpoint-tracker-oper`
- `Cisco-IOS-XE-ethinternal-subslot`
- `Cisco-IOS-XE-hsrp-events`
- `Cisco-IOS-XE-hsrp-oper`
- `Cisco-IOS-XE-isis-oper`
- `Cisco-IOS-XE-nwpi-oper`
- `Cisco-IOS-XE-nwpi-rpc`
- `Cisco-IOS-XE-service-insertion-oper`
- `Cisco-IOS-XE-stack-member-oper`
- `Cisco-IOS-XE-wireless-file-transfer-cfg`
- `Cisco-IOS-XE-wireless-image-download-cfg`
- `Cisco-IOS-XE-wireless-me-general-cfg`
- `Cisco-IOS-XE-wireless-mobility-express-rpc`
- `Cisco-IOS-XE-wireless-rrm-rpc`

### 17.5.1 (+23 new models)

- `Cisco-IOS-XE-adsl`
- `Cisco-IOS-XE-crypto-actions-rpc`
- `Cisco-IOS-XE-dca-events`
- `Cisco-IOS-XE-docsis-oper`
- `Cisco-IOS-XE-dre-cp-oper`
- `Cisco-IOS-XE-dre-oper`
- `Cisco-IOS-XE-fqdn`
- `Cisco-IOS-XE-geo-events`
- `Cisco-IOS-XE-geo-oper`
- `Cisco-IOS-XE-geo-rpc`
- `Cisco-IOS-XE-geo`
- `Cisco-IOS-XE-gnss-dr-oper`
- `Cisco-IOS-XE-l2vpn-pw-events`
- `Cisco-IOS-XE-netconf-diag-oper`
- `Cisco-IOS-XE-netconf-diag-rpc`
- `Cisco-IOS-XE-platform-software-events`
- `Cisco-IOS-XE-psecure-oper`
- `Cisco-IOS-XE-sip-ua`
- `Cisco-IOS-XE-switch-cp-svl-oper`
- `Cisco-IOS-XE-vrrp-events`
- `Cisco-IOS-XE-wireless-ap-global-oper`
- `Cisco-IOS-XE-xcopy-events`
- `Cisco-IOS-XE-xcopy-rpc`

### 17.6.1 (+24 new models)

- `Cisco-IOS-XE-aaa-actions-rpc`
- `Cisco-IOS-XE-aaa-events`
- `Cisco-IOS-XE-alarm-profile`
- `Cisco-IOS-XE-appqoe-serv-oper`
- `Cisco-IOS-XE-appqoe-sslproxy-oper`
- `Cisco-IOS-XE-appqoe-tcpproxy-oper`
- `Cisco-IOS-XE-bridge`
- `Cisco-IOS-XE-embedded-ap-oper`
- `Cisco-IOS-XE-ethernet-rpc`
- `Cisco-IOS-XE-gnmi-cfg`
- `Cisco-IOS-XE-group-policy`
- `Cisco-IOS-XE-ignition-oper`
- `Cisco-IOS-XE-mdt-capabilities-oper`
- `Cisco-IOS-XE-mpls-te-oper`
- `Cisco-IOS-XE-sisf`
- `Cisco-IOS-XE-teyes-oper`
- `Cisco-IOS-XE-trace-events`
- `Cisco-IOS-XE-trace-rpc`
- `Cisco-IOS-XE-verify-events`
- `Cisco-IOS-XE-verify-rpc`
- `Cisco-IOS-XE-wireless-actions-rpc`
- `Cisco-IOS-XE-wireless-client-global-oper`
- `Cisco-IOS-XE-wireless-mesh-rpc`
- `Cisco-IOS-XE-yang-interfaces-oper`

### 17.7.1 (+2 new models)

- `Cisco-IOS-XE-endpoint-tracker-events`
- `Cisco-IOS-XE-wireless-sdavc-oper`

### 17.8.1 (+18 new models)

- `Cisco-IOS-XE-bbu-oper`
- `Cisco-IOS-XE-chassis-rpc`
- `Cisco-IOS-XE-fib-events`
- `Cisco-IOS-XE-hsrp`
- `Cisco-IOS-XE-mdt-stats-oper`
- `Cisco-IOS-XE-nat-events`
- `Cisco-IOS-XE-packet-core-5gc-cfg`
- `Cisco-IOS-XE-packet-core-gtpu-cfg`
- `Cisco-IOS-XE-packet-core-plmn-cfg`
- `Cisco-IOS-XE-packet-core-policy-cfg`
- `Cisco-IOS-XE-packet-core-sctp-cfg`
- `Cisco-IOS-XE-packet-core-timer-cfg`
- `Cisco-IOS-XE-packet-core-upf-cfg`
- `Cisco-IOS-XE-port-security-rpc`
- `Cisco-IOS-XE-qfp-crypto-dp-oper`
- `Cisco-IOS-XE-wireless-mesh-global-oper`
- `Cisco-IOS-XE-wireless-power-cfg`
- `Cisco-IOS-XE-wpan-oper`

### 17.9.1 (+20 new models)

- `Cisco-IOS-XE-appqoe-http-oper`
- `Cisco-IOS-XE-banner-internal`
- `Cisco-IOS-XE-bgp-actions-rpc`
- `Cisco-IOS-XE-cli-rpc`
- `Cisco-IOS-XE-location`
- `Cisco-IOS-XE-loop-detect`
- `Cisco-IOS-XE-mrp`
- `Cisco-IOS-XE-poe-health-oper`
- `Cisco-IOS-XE-prp-oper`
- `Cisco-IOS-XE-prp`
- `Cisco-IOS-XE-qfp-appqoe-dp-oper`
- `Cisco-IOS-XE-system-integrity-oper`
- `Cisco-IOS-XE-transceiver-monitor`
- `Cisco-IOS-XE-uidp-oper`
- `Cisco-IOS-XE-voice-rpc`
- `Cisco-IOS-XE-wireless-client-rpc`
- `Cisco-IOS-XE-wireless-rfid-global-oper`
- `Cisco-IOS-XE-wireless-rrm-emul-oper`
- `Cisco-IOS-XE-wireless-rrm-global-oper`
- `Cisco-IOS-XE-wireless-sisf-global-oper`

### 17.10.1 (+9 new models)

- `Cisco-IOS-XE-app-cflowd-oper`
- `Cisco-IOS-XE-hsr-oper`
- `Cisco-IOS-XE-l2vpn-oper`
- `Cisco-IOS-XE-lorawan-oper`
- `Cisco-IOS-XE-lorawan`
- `Cisco-IOS-XE-pae`
- `Cisco-IOS-XE-utd-actions-rpc`
- `Cisco-IOS-XE-wireless-geolocation-oper`
- `Cisco-IOS-XE-wireless-wlan-global-oper`

### 17.11.1 (+8 new models)

- `Cisco-IOS-XE-cloud-services-cfg`
- `Cisco-IOS-XE-cloud-services-rpc`
- `Cisco-IOS-XE-grpc-tunnel-cfg`
- `Cisco-IOS-XE-logging-ios-actions-rpc`
- `Cisco-IOS-XE-sdwan-rpc`
- `Cisco-IOS-XE-switch-ptp-dp-oper`
- `Cisco-IOS-XE-switch-ptp-oper`
- `Cisco-IOS-XE-webauth-banner-internal`

### 17.12.1 (+5 new models)

- `Cisco-IOS-XE-ctrl-mng-cfg`
- `Cisco-IOS-XE-dying-gasp`
- `Cisco-IOS-XE-lte450`
- `Cisco-IOS-XE-msdp-oper`
- `Cisco-IOS-XE-spanning-tree-events`

### 17.13.1 (+12 new models)

- `Cisco-IOS-XE-cli-preview-rpc`
- `Cisco-IOS-XE-dlr-oper`
- `Cisco-IOS-XE-dlr`
- `Cisco-IOS-XE-dns-oper`
- `Cisco-IOS-XE-eem-oper`
- `Cisco-IOS-XE-meraki-connect-oper`
- `Cisco-IOS-XE-stack-power-rpc`
- `Cisco-IOS-XE-tech-support-events`
- `Cisco-IOS-XE-tech-support-rpc`
- `Cisco-IOS-XE-wireless-afc-cloud-oper`
- `Cisco-IOS-XE-wireless-afc-oper`
- `Cisco-IOS-XE-wireless-tunnel-oper`

### 17.14.1 (+17 new models)

- `Cisco-IOS-XE-banner-internal`
- `Cisco-IOS-XE-cwan-fw-rpc`
- `Cisco-IOS-XE-embedded-ap-actions-rpc`
- `Cisco-IOS-XE-ida`
- `Cisco-IOS-XE-l2nat`
- `Cisco-IOS-XE-l3nat-iox`
- `Cisco-IOS-XE-loop-detect-events`
- `Cisco-IOS-XE-matm-events`
- `Cisco-IOS-XE-meraki-leds-actions-rpc`
- `Cisco-IOS-XE-mrp-oper`
- `Cisco-IOS-XE-service-chain`
- `Cisco-IOS-XE-sslproxy-cfg`
- `Cisco-IOS-XE-sslproxy-rpc`
- `Cisco-IOS-XE-switchport-oper`
- `Cisco-IOS-XE-udld-events`
- `Cisco-IOS-XE-udld-oper`
- `Cisco-IOS-XE-utd-events`

### 17.15.1 (+22 new models)

- `Cisco-IOS-XE-buffers`
- `Cisco-IOS-XE-clns`
- `Cisco-IOS-XE-cloud-services-oper`
- `Cisco-IOS-XE-cwmp`
- `Cisco-IOS-XE-gnss`
- `Cisco-IOS-XE-ipc`
- `Cisco-IOS-XE-irig`
- `Cisco-IOS-XE-l2nat-oper`
- `Cisco-IOS-XE-livetools-actions-rpc`
- `Cisco-IOS-XE-livetools-oper`
- `Cisco-IOS-XE-mcast-events`
- `Cisco-IOS-XE-nve-oper`
- `Cisco-IOS-XE-omp-oper`
- `Cisco-IOS-XE-omp-rpc`
- `Cisco-IOS-XE-port-bounce-events`
- `Cisco-IOS-XE-port-bounce-rpc`
- `Cisco-IOS-XE-red-app-events`
- `Cisco-IOS-XE-rg-oper`
- `Cisco-IOS-XE-uplink-autoconfig-oper`
- `Cisco-IOS-XE-uplink-autoconfig`
- `Cisco-IOS-XE-wireless-cisco-spaces-oper`
- `Cisco-IOS-XE-wireless-tech-support-rpc`

### 17.16.1 (+12 new models)

- `Cisco-IOS-XE-banner-internal`
- `Cisco-IOS-XE-crypto-events`
- `Cisco-IOS-XE-interface-bw-events`
- `Cisco-IOS-XE-kron`
- `Cisco-IOS-XE-line-actions-rpc`
- `Cisco-IOS-XE-line-events`
- `Cisco-IOS-XE-line-oper`
- `Cisco-IOS-XE-power-supply-rpc`
- `Cisco-IOS-XE-qfp-dp-cmn-stats-oper`
- `Cisco-IOS-XE-qfp-resource-events`
- `Cisco-IOS-XE-service-chain-oper`
- `Cisco-IOS-XE-transport`

### 17.17.1 (+7 new models)

- `Cisco-IOS-XE-evpn-oper`
- `Cisco-IOS-XE-group-policy-oper`
- `Cisco-IOS-XE-ngfw-events`
- `Cisco-IOS-XE-sdwan-aaa-oper`
- `Cisco-IOS-XE-steering-policy-oper`
- `Cisco-IOS-XE-vdsp-oper`
- `Cisco-IOS-XE-wireless-rogue-authz-rpc`

### 17.18.1 (+22 new models)

- `Cisco-IOS-XE-aws-common-cfg`
- `Cisco-IOS-XE-aws-common-oper`
- `Cisco-IOS-XE-aws-cw-cfg`
- `Cisco-IOS-XE-aws-cw-oper`
- `Cisco-IOS-XE-aws-s3-cfg`
- `Cisco-IOS-XE-aws-s3-oper`
- `Cisco-IOS-XE-bgp-nbr-oper`
- `Cisco-IOS-XE-bgp-rib-oper`
- `Cisco-IOS-XE-cwan-actions-rpc`
- `Cisco-IOS-XE-fwd-oper`
- `Cisco-IOS-XE-ip-arp-oper`
- `Cisco-IOS-XE-ipv6-nd-oper`
- `Cisco-IOS-XE-isis-intf-oper`
- `Cisco-IOS-XE-lte450-oper`
- `Cisco-IOS-XE-policymap-target-oper`
- `Cisco-IOS-XE-rescue-config-rpc`
- `Cisco-IOS-XE-rif-oper`
- `Cisco-IOS-XE-sdwan-oper`
- `Cisco-IOS-XE-uac-actions-rpc`
- `Cisco-IOS-XE-wireless-urwb-cfg`
- `Cisco-IOS-XE-wireless-urwbnet-oper`
- `Cisco-IOS-XE-wireless-wat-cfg`

### 26.1.1 (+26 new models)

- `Cisco-IOS-XE-alarm`
- `Cisco-IOS-XE-autovpn-events`
- `Cisco-IOS-XE-banner-internal`
- `Cisco-IOS-XE-cip`
- `Cisco-IOS-XE-dns-defense-oper`
- `Cisco-IOS-XE-dns-defense`
- `Cisco-IOS-XE-dpi-events`
- `Cisco-IOS-XE-hsr`
- `Cisco-IOS-XE-iad-oper`
- `Cisco-IOS-XE-matm-state-oper`
- `Cisco-IOS-XE-rib-oper`
- `Cisco-IOS-XE-rollback-rpc`
- `Cisco-IOS-XE-scada`
- `Cisco-IOS-XE-sdwan-ipsec-oper`
- `Cisco-IOS-XE-service-chain`
- `Cisco-IOS-XE-sr-oper`
- `Cisco-IOS-XE-sse-actions-rpc`
- `Cisco-IOS-XE-sse-events`
- `Cisco-IOS-XE-sse-oper`
- `Cisco-IOS-XE-stack-info-oper`
- `Cisco-IOS-XE-statistics`
- `Cisco-IOS-XE-system-security-events`
- `Cisco-IOS-XE-system-security-oper`
- `Cisco-IOS-XE-wireless-cisco-spaces-rpc`
- `Cisco-IOS-XE-wireless-rpc`
- `Cisco-IOS-XE-wireless-urwb-oper`

## 5. Feature Category Breakdown (Latest vs First)

| Category | 16.3.1 | 26.1.1 | Growth |
|----------|------:|------:|-------:|
| AAA | 0 | 7 | NEW |
| ACL | 1 | 3 | +200% |
| App Hosting | 1 | 4 | +300% |
| Cloud | 0 | 11 | NEW |
| DHCP | 0 | 5 | NEW |
| DNS | 0 | 2 | NEW |
| DPI/AppVis | 1 | 9 | +800% |
| Geo/Location | 0 | 5 | NEW |
| High Availability | 0 | 5 | NEW |
| IETF Deviation | 0 | 9 | NEW |
| IETF Standard | 16 | 36 | +125% |
| Interfaces | 2 | 46 | +2200% |
| IoT/Industrial | 0 | 32 | NEW |
| NAT | 0 | 6 | NEW |
| OC Deviation | 2 | 47 | +2250% |
| OpenConfig | 0 | 134 | NEW |
| Platform | 5 | 44 | +780% |
| QoS | 10 | 14 | +40% |
| Routing | 9 | 89 | +889% |
| SD-WAN | 0 | 27 | NEW |
| Security | 0 | 54 | NEW |
| Switching | 6 | 64 | +967% |
| System | 12 | 76 | +533% |
| Tailf/NSO | 15 | 22 | +47% |
| Telemetry | 0 | 17 | NEW |
| Timing | 0 | 4 | NEW |
| VPN/Tunnel | 3 | 14 | +367% |
| Voice/UC | 0 | 13 | NEW |
| Wireless | 0 | 88 | NEW |

## 6. Feature Category Trend Over Time

| Category | 16.3.1 | 16.6.1 | 16.9.1 | 16.12.1 | 17.4.1 | 17.8.1 | 17.12.1 | 17.16.1 | 26.1.1 |
|----------|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| AAA | 0 | 1 | 2 | 3 | 4 | 6 | 6 | 7 | 7 |
| ACL | 1 | 4 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| App Hosting | 1 | 2 | 3 | 3 | 4 | 4 | 4 | 4 | 4 |
| Cloud | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 5 | 11 |
| DHCP | 0 | 1 | 2 | 3 | 4 | 4 | 5 | 5 | 5 |
| DNS | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 2 | 2 |
| DPI/AppVis | 1 | 4 | 5 | 6 | 6 | 7 | 7 | 8 | 9 |
| Geo/Location | 0 | 0 | 0 | 0 | 0 | 4 | 5 | 5 | 5 |
| High Availability | 0 | 0 | 0 | 2 | 2 | 2 | 2 | 5 | 5 |
| IETF Deviation | 0 | 7 | 8 | 8 | 8 | 8 | 8 | 9 | 9 |
| IETF Standard | 16 | 26 | 29 | 28 | 30 | 31 | 32 | 32 | 36 |
| Interfaces | 2 | 10 | 15 | 23 | 31 | 33 | 33 | 43 | 46 |
| IoT/Industrial | 0 | 1 | 1 | 3 | 9 | 13 | 21 | 26 | 32 |
| NAT | 0 | 1 | 2 | 2 | 2 | 3 | 3 | 6 | 6 |
| OC Deviation | 2 | 13 | 23 | 43 | 46 | 50 | 50 | 50 | 47 |
| OpenConfig | 0 | 30 | 57 | 84 | 84 | 108 | 110 | 128 | 134 |
| Platform | 5 | 10 | 17 | 19 | 31 | 37 | 40 | 44 | 44 |
| QoS | 10 | 9 | 8 | 8 | 10 | 10 | 10 | 11 | 14 |
| Routing | 9 | 38 | 44 | 51 | 68 | 85 | 79 | 83 | 89 |
| SD-WAN | 0 | 2 | 3 | 4 | 10 | 14 | 16 | 21 | 27 |
| Security | 0 | 9 | 13 | 23 | 27 | 34 | 39 | 42 | 54 |
| Switching | 6 | 17 | 23 | 31 | 38 | 44 | 47 | 62 | 64 |
| System | 12 | 24 | 30 | 39 | 46 | 51 | 54 | 70 | 76 |
| Tailf/NSO | 15 | 14 | 14 | 14 | 14 | 15 | 19 | 21 | 22 |
| Telemetry | 0 | 3 | 4 | 4 | 8 | 15 | 16 | 16 | 17 |
| Timing | 0 | 0 | 1 | 2 | 4 | 4 | 6 | 6 | 4 |
| VPN/Tunnel | 3 | 7 | 7 | 10 | 12 | 12 | 12 | 13 | 14 |
| Voice/UC | 0 | 1 | 1 | 3 | 8 | 11 | 12 | 12 | 13 |
| Wireless | 0 | 1 | 0 | 52 | 61 | 69 | 77 | 80 | 88 |

## 7. Model Type Breakdown (Latest vs First)

How the mix of Configuration, Operational, Events, and RPC models has evolved.

| Type | 16.3.1 | 26.1.1 | Growth |
|------|------:|------:|-------:|
| Configuration | 76 | 407 | +436% |
| Deviation | 2 | 92 | +4500% |
| Events | 0 | 36 | NEW |
| Operational | 2 | 222 | +11000% |
| RPC | 0 | 66 | NEW |
| Types | 3 | 64 | +2033% |

## 8. OpenConfig Adoption Timeline

**140** OpenConfig models adopted:

| Release | New OpenConfig Models | Count |
|---------|----------------------|------:|
| 16.6.1 | openconfig-acl, openconfig-extensions, openconfig-if-aggregate, openconfig-if-ethernet, openconfig-if-ip... | 30 |
| 16.6.2 | openconfig-inet-types, openconfig-yang-types | 2 |
| 16.8.1 | openconfig-aaa, openconfig-aaa-radius, openconfig-aaa-tacacs, openconfig-aaa-types, openconfig-bgp... | 24 |
| 16.9.1 | openconfig-alarms, openconfig-if-poe, openconfig-platform-linecard, openconfig-platform-port | 4 |
| 16.12.1 | openconfig-access-points, openconfig-aft, openconfig-aft-network-instance, openconfig-aft-types, openconfig-alarm-types... | 28 |
| 17.1.1 | openconfig-system-management | 1 |
| 17.3.1 | openconfig-macsec, openconfig-macsec-types | 2 |
| 17.7.1 | openconfig-bfd | 1 |
| 17.8.1 | openconfig-evpn, openconfig-evpn-types, openconfig-if-types, openconfig-igmp, openconfig-igmp-types... | 22 |
| 17.9.1 | openconfig-license, openconfig-messages, openconfig-system-grpc | 3 |
| 17.14.1 | openconfig-aft-common, openconfig-aft-ethernet, openconfig-aft-ipv4, openconfig-aft-ipv6, openconfig-aft-mpls... | 17 |
| 17.18.1 | openconfig-ethernet-segments | 1 |
| 26.1.1 | openconfig-qos, openconfig-qos-elements, openconfig-qos-interfaces, openconfig-qos-mem-mgmt, openconfig-qos-types | 5 |

<details>
<summary>Full OpenConfig model list with first-seen release</summary>

| OpenConfig Model | First Appeared |
|-----------------|---------------|
| `openconfig-aaa-radius` | 16.8.1 |
| `openconfig-aaa-tacacs` | 16.8.1 |
| `openconfig-aaa-types` | 16.8.1 |
| `openconfig-aaa` | 16.8.1 |
| `openconfig-access-points` | 16.12.1 |
| `openconfig-acl` | 16.6.1 |
| `openconfig-aft-common` | 17.14.1 |
| `openconfig-aft-ethernet` | 17.14.1 |
| `openconfig-aft-ipv4` | 17.14.1 |
| `openconfig-aft-ipv6` | 17.14.1 |
| `openconfig-aft-mpls` | 17.14.1 |
| `openconfig-aft-network-instance` | 16.12.1 |
| `openconfig-aft-pf` | 17.14.1 |
| `openconfig-aft-state-synced` | 17.14.1 |
| `openconfig-aft-types` | 16.12.1 |
| `openconfig-aft` | 16.12.1 |
| `openconfig-alarm-types` | 16.12.1 |
| `openconfig-alarms` | 16.9.1 |
| `openconfig-ap-manager` | 16.12.1 |
| `openconfig-bfd` | 17.7.1 |
| `openconfig-bgp-common-multiprotocol` | 16.8.1 |
| `openconfig-bgp-common-structure` | 16.8.1 |
| `openconfig-bgp-common` | 16.8.1 |
| `openconfig-bgp-errors` | 17.14.1 |
| `openconfig-bgp-global` | 16.8.1 |
| `openconfig-bgp-neighbor` | 16.8.1 |
| `openconfig-bgp-peer-group` | 16.8.1 |
| `openconfig-bgp-policy` | 16.8.1 |
| `openconfig-bgp-types` | 16.8.1 |
| `openconfig-bgp` | 16.8.1 |
| `openconfig-ethernet-segments` | 17.18.1 |
| `openconfig-evpn-types` | 17.8.1 |
| `openconfig-evpn` | 17.8.1 |
| `openconfig-extensions` | 16.6.1 |
| `openconfig-if-aggregate` | 16.6.1 |
| `openconfig-if-ethernet` | 16.6.1 |
| `openconfig-if-ip-ext` | 16.6.1 |
| `openconfig-if-ip` | 16.6.1 |
| `openconfig-if-poe` | 16.9.1 |
| `openconfig-if-types` | 17.8.1 |
| `openconfig-igmp-types` | 17.8.1 |
| `openconfig-igmp` | 17.8.1 |
| `openconfig-inet-types` | 16.6.2 |
| `openconfig-interfaces` | 16.6.1 |
| `openconfig-isis-lsdb-types` | 16.12.1 |
| `openconfig-isis-lsp` | 16.12.1 |
| `openconfig-isis-policy` | 16.12.1 |
| `openconfig-isis-routing` | 16.12.1 |
| `openconfig-isis-types` | 16.12.1 |
| `openconfig-isis` | 16.12.1 |
| `openconfig-keychain-types` | 17.14.1 |
| `openconfig-keychain` | 17.14.1 |
| `openconfig-lacp` | 16.6.1 |
| `openconfig-license` | 17.9.1 |
| `openconfig-lldp-types` | 16.6.1 |
| `openconfig-lldp` | 16.6.1 |
| `openconfig-local-routing` | 16.6.1 |
| `openconfig-macsec-types` | 17.3.1 |
| `openconfig-macsec` | 17.3.1 |
| `openconfig-messages` | 17.9.1 |
| `openconfig-mpls-igp` | 16.12.1 |
| `openconfig-mpls-ldp` | 16.12.1 |
| `openconfig-mpls-rsvp` | 16.12.1 |
| `openconfig-mpls-sr` | 16.12.1 |
| `openconfig-mpls-static` | 16.12.1 |
| `openconfig-mpls-te` | 16.12.1 |
| `openconfig-mpls-types` | 16.12.1 |
| `openconfig-mpls` | 16.12.1 |
| `openconfig-network-instance-l2` | 16.6.1 |
| `openconfig-network-instance-l3` | 16.6.1 |
| `openconfig-network-instance-policy` | 17.8.1 |
| `openconfig-network-instance-types` | 16.6.1 |
| `openconfig-network-instance` | 16.6.1 |
| `openconfig-openflow-types` | 16.8.1 |
| `openconfig-openflow` | 16.8.1 |
| `openconfig-optical-amplifier` | 16.6.1 |
| `openconfig-ospf-policy` | 17.8.1 |
| `openconfig-ospf-types` | 17.8.1 |
| `openconfig-ospfv2-area-interface` | 17.8.1 |
| `openconfig-ospfv2-area` | 17.8.1 |
| `openconfig-ospfv2-common` | 17.8.1 |
| `openconfig-ospfv2-global` | 17.8.1 |
| `openconfig-ospfv2-lsdb` | 17.8.1 |
| `openconfig-ospfv2` | 17.8.1 |
| `openconfig-packet-match-types` | 16.6.1 |
| `openconfig-packet-match` | 16.6.1 |
| `openconfig-pcep` | 17.14.1 |
| `openconfig-pf-forwarding-policies` | 17.8.1 |
| `openconfig-pf-interfaces` | 17.8.1 |
| `openconfig-pf-path-groups` | 17.8.1 |
| `openconfig-pf-srte` | 17.8.1 |
| `openconfig-pim-types` | 17.8.1 |
| `openconfig-pim` | 17.8.1 |
| `openconfig-platform-cpu` | 16.12.1 |
| `openconfig-platform-fan` | 16.12.1 |
| `openconfig-platform-linecard` | 16.9.1 |
| `openconfig-platform-port` | 16.9.1 |
| `openconfig-platform-psu` | 16.12.1 |
| `openconfig-platform-transceiver` | 16.6.1 |
| `openconfig-platform-types` | 16.6.1 |
| `openconfig-platform` | 16.6.1 |
| `openconfig-policy-forwarding` | 17.8.1 |
| `openconfig-policy-types` | 16.6.1 |
| `openconfig-procmon` | 16.8.1 |
| `openconfig-programming-errors` | 17.14.1 |
| `openconfig-qos-elements` | 26.1.1 |
| `openconfig-qos-interfaces` | 26.1.1 |
| `openconfig-qos-mem-mgmt` | 26.1.1 |
| `openconfig-qos-types` | 26.1.1 |
| `openconfig-qos` | 26.1.1 |
| `openconfig-rib-bgp-attributes` | 17.14.1 |
| `openconfig-rib-bgp-ext` | 16.8.1 |
| `openconfig-rib-bgp-shared-attributes` | 17.14.1 |
| `openconfig-rib-bgp-table-attributes` | 17.14.1 |
| `openconfig-rib-bgp-tables` | 17.14.1 |
| `openconfig-rib-bgp-types` | 16.8.1 |
| `openconfig-rib-bgp` | 16.8.1 |
| `openconfig-route-summary` | 17.14.1 |
| `openconfig-routing-policy` | 16.6.1 |
| `openconfig-segment-routing-types` | 17.8.1 |
| `openconfig-segment-routing` | 16.12.1 |
| `openconfig-spanning-tree-types` | 16.8.1 |
| `openconfig-spanning-tree` | 16.8.1 |
| `openconfig-system-grpc` | 17.9.1 |
| `openconfig-system-logging` | 16.8.1 |
| `openconfig-system-management` | 17.1.1 |
| `openconfig-system-terminal` | 16.8.1 |
| `openconfig-system-wifi-ext` | 16.12.1 |
| `openconfig-system` | 16.8.1 |
| `openconfig-terminal-device` | 16.6.1 |
| `openconfig-transport-line-common` | 16.6.1 |
| `openconfig-transport-types` | 16.6.1 |
| `openconfig-types` | 16.6.1 |
| `openconfig-vlan-types` | 16.6.1 |
| `openconfig-vlan` | 16.6.1 |
| `openconfig-wavelength-router` | 16.6.1 |
| `openconfig-wifi-mac` | 16.12.1 |
| `openconfig-wifi-phy` | 16.12.1 |
| `openconfig-wifi-types` | 16.12.1 |
| `openconfig-yang-types` | 16.6.2 |

</details>

## 9. Foundation Models (Present in All Releases)

**35** models present in every release from 16.3.1 to 26.1.1:

**IETF Standard** (10): ietf-diffserv-action, ietf-diffserv-classifier, ietf-diffserv-policy, ietf-diffserv-target, ietf-interfaces-ext, ietf-ipv4-unicast-routing, ietf-ipv6-unicast-routing, ietf-key-chain...

**Interfaces** (1): cisco-ethernet

**QoS** (5): cisco-policy, cisco-policy-filters, cisco-policy-target, policy-attr, policy-types

**Routing** (6): cisco-ospf, cisco-routing-ext, common-mpls-static, common-mpls-static-devs, common-mpls-types, pim

**Switching** (3): cisco-bridge-common, cisco-bridge-domain, cisco-storm-control

**System** (2): cisco-ia, cisco-self-mgmt

**Tailf/NSO** (5): tailf-cli-extensions, tailf-common, tailf-confd-monitoring, tailf-meta-extensions, tailf-netconf-monitoring

**VPN/Tunnel** (3): cisco-pw, nvo, nvo-devs


---

## 10. Platform Support Dimension

Platform data from NETCONF yang-library and capability XML files across **23 releases**
(16.9.3 → 26.1.1). All YANG models included (MIBs excluded).

> **Platform ordering:** Switching (Cat 9K → Cat 9200) | WLC | Routers (C8500 → ASR → ISR) | IoT/Industrial (IR → IE → ESS)

> **Note:** Cat 9200 and Cat 9K are **separate platforms** with different model support.
> Cat 9200 has 406 YANG models vs Cat 9K with 684 in 26.1.1.
> Earlier releases tracked Cat 9300/9400/9500/9600 individually; later consolidated to "Cat 9K."

### 10a. Platform Availability Per Release

✓ = platform data available. **22 distinct platforms** tracked.

| Release | Cat 9K | Cat 9200 | Cat 9300 | Cat 9400 | Cat 9500 | Cat 9600 | Cat 3K | WLC | C8500 | C8000v | C8200 | C8300 | C8500L | ASR 1K | ISR 1K | ISR 4K | CSR 1Kv | ASR 900 | IR 1101 | IE 3x00 | ESS 3x00 | cBR |
|---------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 16.9.3 |  |  | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  | ✓ |
| 16.10.1 |  |  | ✓ | ✓ | ✓ |  |  | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ |
| 16.11.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 16.12.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17.1.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17.2.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17.3.1 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17.4.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| 17.5.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ |  | ✓ |  |  |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17.6.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17.7.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
| 17.8.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.9.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.10.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.11.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.12.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.13.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.14.1 |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.15.1 | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.16.1 | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.17.1 | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ |  |  |  | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  |
| 17.18.1 | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ |  |  |  | ✓ | ✓ |  |  |  | ✓ | ✓ | ✓ |  |
| 26.1.1 | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ |  |  |  | ✓ | ✓ |  |  |  | ✓ | ✓ | ✓ |  |

### 10b. YANG Model Count Per Platform (26.1.1)

All YANG models (no MIBs).

| Platform | Total YANG | Cisco-IOS-XE | OpenConfig | IETF | Tailf | Other |
|----------|----------:|-------------:|-----------:|-----:|------:|------:|
| Cat 9K | 684 | 428 | 128 | 39 | 21 | 68 |
| Cat 9200 | 406 | 156 | 125 | 39 | 21 | 65 |
| WLC | 607 | 361 | 124 | 38 | 21 | 63 |
| C8500 | 583 | 345 | 119 | 38 | 21 | 60 |
| C8000v | 587 | 356 | 112 | 38 | 21 | 60 |
| ASR 1K | 583 | 345 | 119 | 38 | 21 | 60 |
| ISR 1K | 621 | 381 | 119 | 38 | 21 | 62 |
| IR 1101 | 646 | 406 | 119 | 38 | 21 | 62 |
| IE 3x00 | 525 | 292 | 112 | 38 | 21 | 62 |
| ESS 3x00 | 525 | 292 | 112 | 38 | 21 | 62 |

### 10c. Platform Support Matrix — All YANG Models (26.1.1)

**890** YANG models across **10** platforms (MIBs excluded).
✓ = model in platform yang-library. Grouped by origin.

| Origin | Module | Cat 9K | Cat 9200 | WLC | C8500 | C8000v | ASR 1K | ISR 1K | IR 1101 | IE 3x00 | ESS 3x00 |
|--------|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Cisco-IOS-XE | `Cisco-IOS-XE-aaa` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-aaa-actions-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-aaa-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-aaa-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-aaa-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-aaa-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-aaa-types` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-acl` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-acl-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-adsl` |  |  |  |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-aging-time-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-alarm` |  | ✓ |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-alarm-profile` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-app-cflowd-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-app-hosting` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-app-hosting-cfg` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-app-hosting-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-appqoe-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-appqoe-http-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-appqoe-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-appqoe-serv-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-appqoe-sslproxy-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-appqoe-tcpproxy-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-appqoe-types` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-arp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-arp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-arp-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-atm` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-autovpn-events` |  |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-avb` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-aws-common-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-aws-common-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-aws-cw-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-aws-cw-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-aws-s3-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-aws-s3-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-bba-group` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bbu-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-bfd` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bfd-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bgp` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bgp-actions-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bgp-common-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bgp-nbr-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bgp-oper` | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-bgp-rib-oper` | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-bgp-route-oper` | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-bgp-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-boot-integrity-oper` | ✓ |  | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-breakout-port-oper` | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-bridge` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-bridge-domain` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-bridge-oper` |  |  |  |  |  |  | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-buffers` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cable-diag-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-cable-diag-rpc` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-call-home` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-card` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cdp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cdp-deviation` |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-cdp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cef` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cef-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cellular` |  |  |  |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cellular-rpc` |  |  |  |  | ✓ |  | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cellwan-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cfm-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-chassis-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-checkpoint-archive-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cip` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-cli-preview-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-cli-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-clns` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-cloud-services-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-cloud-services-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-cloud-services-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-coap` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-common-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-controller` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-controller-shdsl-common` |  |  |  |  | ✓ |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-controller-shdsl-events` |  |  |  |  | ✓ |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-controller-shdsl-oper` |  |  |  |  | ✓ |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-controller-t1e1-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-controller-vdsl-oper` |  |  |  |  | ✓ |  | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-crypto` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-crypto-actions-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-crypto-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-crypto-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-crypto-pki-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-crypto-pki-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-crypto-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-crypto-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ctrl-mng-cfg` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-cts` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cts-routing-deviation` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-cts-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-cts-switching-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-cwan-actions-rpc` |  |  |  |  | ✓ |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-cwan-fw-rpc` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-cwmp` |  |  |  |  | ✓ |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-dapr` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-dca-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-device-hardware-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-device-sensor` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-device-sensor-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-device-tracking` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-device-tracking-cat9k-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-dhcp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dhcp-deviation` |  |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-dhcp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dhcp-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dhcp-security-track-server-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-diagnostics` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dialer` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dialer-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-digital-io-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-digitalio` |  |  |  |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-dlr` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-dlr-oper` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-dmi-common-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dns-defense` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dns-defense-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-dns-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dot1x` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-dpi-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-dre-cp-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-dre-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-dying-gasp` |  | ✓ |  |  |  |  |  | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-eem` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-eem-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-efp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-eigrp` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-eigrp-obsolete` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-eigrp-oper` | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-embedded-ap-actions-rpc` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-embedded-ap-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-endpoint-tracker-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-endpoint-tracker-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-environment-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-eogre-tunnel-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-eta` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ethernet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ethernet-cat9k-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-ethernet-cfm-efp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ethernet-cfm-efp-deviation` |  | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-ethernet-deviation` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-ethernet-mcp-deviation` |  |  |  | ✓ |  | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-ethernet-oam` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ethernet-radium-deviation` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-ethernet-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ethinternal-subslot` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-event-history-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-evpn-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-ezpm` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-factory-reset-secure-rpc` |  |  | ✓ |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-features` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-fib-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-fib-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-flow` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-flow-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-flow-monitor-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-flow-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-fqdn` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-frame-relay` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-fw-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-fwd-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-geo` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-geo-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-geo-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-geo-rpc` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-gir-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-gnmi-cfg` | ✓ |  | ✓ | ✓ |  | ✓ |  | ✓ |  |  |
|  | `Cisco-IOS-XE-gnss` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-gnss-dr-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-gnss-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-group-policy` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-group-policy-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-grpc-tunnel-cfg` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-ha-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-hsr` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-hsr-oper` |  |  |  |  |  |  | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-hsrp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-hsrp-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-hsrp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-http` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-iad-oper` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-icmp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ida` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-identity-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-igmp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ignition-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-im-events-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-install-event-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-install-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-install-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-install-oper-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-install-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-interface-bw-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-interface-common` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-interfaces` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-interfaces-cat9k-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-interfaces-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-interfaces-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-interfaces-wlc-deviation` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-ios-common-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ios-events-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ip` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ip-arp-oper` | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-ip-sla-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ip-sla-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ipc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ipmux` |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ipv6` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ipv6-nd-oper` | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-ipv6-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-irig` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-isdn` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-isdn-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-isg` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-isis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-isis-intf-oper` | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-isis-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-iwanfabric` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-kron` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-l2nat` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-l2nat-oper` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-l2tp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-l2vpn` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-l2vpn-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-l3nat-iox` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-l3vpn` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-lacp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-license` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-line` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-line-actions-rpc` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-line-common-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-line-deviation` |  |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-line-events` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-line-nonquake-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-line-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-line-quake-deviation` |  | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-linecard-oper` | ✓ |  | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-lisp` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-lisp-deviation` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-lisp-oper` | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-livetools-actions-rpc` | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-livetools-common-types` | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-livetools-oper` | ✓ |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-lldp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-lldp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-location` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-logging` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-logging-deviation` | ✓ | ✓ |  |  | ✓ |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-logging-ios-actions-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-loop-detect` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-loop-detect-events` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-lorawan` |  |  |  |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-lorawan-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-lte450` |  |  |  |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-lte450-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-macsec-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-matm-events` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-matm-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-matm-state-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-mcast-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mdns-gateway` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mdt-capabilities-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mdt-cfg` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mdt-common-defs` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mdt-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mdt-oper-v2` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mdt-stats-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-memory-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-meraki-connect-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-meraki-leds-actions-rpc` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-mka` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mka-oper` | ✓ |  |  | ✓ |  | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-mld` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mlppp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mmode` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-mobileip` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-mpls` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mpls-forwarding-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mpls-ldp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mpls-te-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mroute-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mrp` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-mrp-oper` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-msdp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-multicast` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-multicast-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-mvrp` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-nam` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-nat` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-nat-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-nat-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-native` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-nbar` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ncch-cfg` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ncch-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-nd` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-nd-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-netconf-diag-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-netconf-diag-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ngfw-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-nhrp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ntp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ntp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-nve-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-nwpi-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-nwpi-rpc` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-nwpi-types` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-object-group` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-omp-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-omp-rpc` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-ospf` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospf-common` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospf-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospf-events` | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospf-obsolete` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospf-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospf-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospfv3` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ospfv3-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-otv` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-pae` | ✓ | ✓ | ✓ |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-parser` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-pathmgr` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-perf-measure` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-perf-measure-deviation` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-perf-measure-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-perf-measure-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-pfr` |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-pim-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-platform` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-platform-common-oper` | ✓ |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-platform-events-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-platform-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-platform-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-platform-software-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-platform-software-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-pnp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-pnp-deviation` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-poch-lb-switch-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-poe-health-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-poe-oper` | ✓ |  |  |  |  |  | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-policy-cat9k-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-policy-deviation` |  |  |  |  | ✓ |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-policy-mcp-deviation` |  |  |  | ✓ |  | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-policy-vxe-deviation` |  |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-policy-wlc-deviation` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-policymap-target-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-port-bounce-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-port-bounce-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-port-channel-crankshaft-deviation` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-port-channel-deviation` |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-port-channel-quake-deviation` |  | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-port-channel-unsupported-deviation` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-port-security-rpc` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-power` | ✓ | ✓ |  |  |  |  | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-power-deviation` |  | ✓ |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-power-supply-rpc` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-ppp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-ppp-mcp-deviation` |  |  |  | ✓ |  | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-ppp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-pppoe` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-process-cpu-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-process-memory-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-prp` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-prp-oper` |  |  |  |  |  |  | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-psecure-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-ptp` | ✓ | ✓ |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-qfp-appqoe-dp-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-qfp-classification-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-qfp-crypto-dp-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-qfp-dp-cmn-stats-oper` |  |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-qfp-resource-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-qfp-resource-utilization-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-qfp-stats` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-qfp-stats-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-qos` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-rawsocket` |  |  |  |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-rawsocket-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-red-app-common-types` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-red-app-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-rep` |  | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-rescue-config-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-rg-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-rib-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-rif-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-rip` | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-rmi-dad` |  |  | ✓ | ✓ |  | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-rollback-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-route-map` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-rsvp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-sanet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-sanet-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-scada` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-scada-gw` |  |  |  |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-scada-gw-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-sd-vxlan-oper` |  |  |  | ✓ | ✓ | ✓ |  |  |  |  |
|  | `Cisco-IOS-XE-sdwan-aaa-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-sdwan-ipsec-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-sdwan-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-sdwan-rpc` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-sdwan-types` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-segment-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-serial` |  |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-service-chain-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-service-discovery` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-service-insertion` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-service-insertion-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-service-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-sip-ua` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-sisf` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-site-manager` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-sla` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-sm-enum-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-sm-events-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-snmp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-snmp-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-spanning-tree` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-spanning-tree-events` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-spanning-tree-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-sr-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-sslproxy-cfg` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-sslproxy-rpc` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-stack-info-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-stack-member-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-stack-mgr-events-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-stack-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-stack-power-rpc` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-stacking-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-stackwise-virtual` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-statistics` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-steering-policy-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-stp-quake-deviation` |  | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-swc` |  | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-switch-cp-svl-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch-dp-mac-learning-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch-dp-punt-inject-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch-dp-resources-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch-ptp-dp-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch-ptp-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switch-rpc` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switchport-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switchport-ewlc-deviation` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-switchport-oper` | ✓ |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-synce` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-system-integrity-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-system-security-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-system-security-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-system-security-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-tcam-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-tech-support-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-tech-support-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-template` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-teyes-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-trace-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-trace-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-track` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-transceiver-monitor` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-transceiver-oper` | ✓ |  | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-transport` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-trustsec-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-tunnel` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-tunnel-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-tunnel-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-uac-actions-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-ucse` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-ucse-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-ucse-rpc` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-udld` | ✓ | ✓ |  | ✓ |  | ✓ |  | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-udld-events` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-udld-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-uidp-oper` |  |  |  | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-umbrella` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-umbrella-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-umbrella-oper-dp` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-umbrella-rpc` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-uplink-autoconfig` | ✓ | ✓ |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-uplink-autoconfig-oper` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-utd` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-utd-actions-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-utd-common-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-utd-events` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-utd-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-utd-rpc` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vdsp-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-verify-events` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-verify-rpc` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-vlan` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vlan-ewlc-deviation` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-vlan-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-vlan-quake-deviation` |  | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-vlan-vxe-deviation` |  |  |  |  | ✓ |  |  |  |  |  |
|  | `Cisco-IOS-XE-voice` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-voice-class` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-voice-dspfarm` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-voice-oper` |  |  |  |  | ✓ |  | ✓ |  | ✓ | ✓ |
|  | `Cisco-IOS-XE-voice-port` |  |  |  |  |  |  | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-voice-register` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-voice-rpc` |  |  |  | ✓ | ✓ | ✓ | ✓ |  |  |  |
|  | `Cisco-IOS-XE-vpdn` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vrf-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vrrp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vrrp-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-vrrp-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vrrp-types` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vservice` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `Cisco-IOS-XE-vstack` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `Cisco-IOS-XE-vtp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-vxlan` |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-wccp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-wireless-access-point-cfg-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-access-point-cmd-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-access-point-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-actions-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-afc-cloud-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-afc-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-afc-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-ap-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-ap-global-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-ap-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-apf-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-awips-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-ble-ltx-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-ble-mgmt-cmd-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-ble-mgmt-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-cisco-spaces-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-cisco-spaces-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-client-global-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-client-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-client-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-client-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-cts-sxp-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-cts-sxp-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-dot11-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-dot15-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-enum-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-events-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-fabric-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-flex-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-fqdn-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-general-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-general-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-geolocation-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-geolocation-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-hotspot-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-hyperlocation-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-lisp-agent-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-location-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-location-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mcast-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mdns-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mesh-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mesh-global-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mesh-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mesh-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mobility-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mobility-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mobility-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-mstream-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-nmsp-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-power-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-radio-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rf-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rfid-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rfid-global-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rfid-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rlan-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rogue-authz-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rogue-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rogue-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rogue-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rpc` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-wireless-rrm-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rrm-emul-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rrm-global-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rrm-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rrm-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rrm-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rule-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-rule-mdns-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-sdavc-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-security-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-sisf-global-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-site-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-tech-support-rpc` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-tunnel-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-tunnel-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-tunnel-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-urwb-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-urwb-common-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-urwb-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-urwbnet-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-wat-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-wlan-cfg` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wireless-wlan-global-oper` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wpan-oper` |  |  |  |  |  |  | ✓ |  |  |  |
|  | `Cisco-IOS-XE-wsa-types` | ✓ |  | ✓ |  |  |  |  | ✓ |  |  |
|  | `Cisco-IOS-XE-wsma` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-xcopy-events` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-xcopy-rpc` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-yang-interfaces-cfg` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-yang-interfaces-oper` | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-zone` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `Cisco-IOS-XE-zone-rpc` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| IETF | `ietf-datastores` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-diffserv-action` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-diffserv-classifier` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-diffserv-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-diffserv-target` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-event-notifications` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-inet-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-interfaces` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-interfaces-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-ip` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-ipv4-unicast-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-ipv6-unicast-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-key-chain` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf-monitoring` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf-nmda` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf-notifications` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf-otlp-context` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf-otlp-context-traceparent-version-1.0` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf-otlp-context-tracestate-version-1.0` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-netconf-with-defaults` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-network-instance` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-origin` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-ospf` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-restconf` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-restconf-monitoring` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-routing-types` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `ietf-subscribed-notifications` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-subscribed-notifications-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-x509-cert-to-name` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-library` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-metadata` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-patch` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-push` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-schema-mount` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-smiv2` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-structure-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `ietf-yang-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| OpenConfig | `openconfig-aaa` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aaa-radius` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aaa-tacacs` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aaa-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-access-points` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `openconfig-acl` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-common` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-ethernet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-ipv4` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-ipv6` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-mpls` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-network-instance` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-pf` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-state-synced` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-aft-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-alarm-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-alarms` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ap-manager` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `openconfig-bfd` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-common` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-common-multiprotocol` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-common-structure` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-errors` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-global` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-neighbor` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-peer-group` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-bgp-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ethernet-segments` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `openconfig-evpn` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-evpn-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-extensions` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-if-aggregate` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-if-ethernet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-if-ip` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-if-ip-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-if-poe` | ✓ | ✓ |  | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `openconfig-if-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-igmp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-igmp-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-inet-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-interfaces` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-isis` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-isis-lsdb-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-isis-lsp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-isis-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-isis-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-isis-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-keychain` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-keychain-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-lacp` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `openconfig-license` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-lldp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-lldp-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-local-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-macsec` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `openconfig-macsec-types` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `openconfig-messages` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls-igp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls-ldp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls-rsvp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls-sr` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls-static` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls-te` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-mpls-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-network-instance` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-network-instance-l2` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-network-instance-l3` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-network-instance-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-network-instance-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-openflow` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `openconfig-openflow-types` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `openconfig-ospf-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ospf-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ospfv2` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ospfv2-area` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ospfv2-area-interface` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ospfv2-common` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ospfv2-global` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-ospfv2-lsdb` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-packet-match` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-packet-match-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-pcep` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-pf-forwarding-policies` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-pf-interfaces` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-pf-path-groups` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-pim` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-pim-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-platform` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-platform-cpu` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `openconfig-platform-fan` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `openconfig-platform-linecard` | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |
|  | `openconfig-platform-port` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `openconfig-platform-psu` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `openconfig-platform-transceiver` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `openconfig-platform-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-policy-forwarding` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-policy-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-procmon` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-programming-errors` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |  |
|  | `openconfig-qos` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-qos-elements` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-qos-interfaces` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-qos-mem-mgmt` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-qos-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-rib-bgp` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-rib-bgp-attributes` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-rib-bgp-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-rib-bgp-shared-attributes` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-rib-bgp-table-attributes` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-rib-bgp-tables` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-rib-bgp-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-route-summary` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-routing-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-segment-routing` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-segment-routing-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-spanning-tree` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `openconfig-spanning-tree-types` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `openconfig-system` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-system-grpc` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-system-logging` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-system-terminal` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-transport-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-vlan` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-vlan-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `openconfig-wifi-mac` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `openconfig-wifi-phy` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `openconfig-wifi-types` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `openconfig-yang-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Other | `cisco-bridge-common` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-bridge-domain` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-ethernet` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-evpn-service` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-extensions` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-ia` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-ospf` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-policy` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-policy-filters` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-policy-target` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-pw` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-routing-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-self-mgmt` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-semver` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-smart-license` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-smart-license-errors` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-storm-control` |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-event-notifications-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-ip-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-ipv4-unicast-routing-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-ipv6-unicast-routing-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-ospf-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-routing-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-routing-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-yang-push-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-ietf-yang-push-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-access-points-deviation` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `cisco-xe-openconfig-acl-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-acl-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-aft-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-bgp-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-bgp-policy-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-ethernet-segments-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `cisco-xe-openconfig-evpn-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-if-ethernet-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-if-ip-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-if-poe-deviation` | ✓ | ✓ |  |  |  |  | ✓ | ✓ |  |  |
|  | `cisco-xe-openconfig-interfaces-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-interfaces-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-isis-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-isis-policy-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-lldp-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-local-routing-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-mpls-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-network-instance-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-network-instance-l2-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-openflow-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `cisco-xe-openconfig-platform-ext` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `cisco-xe-openconfig-qos-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-rib-bgp-ext` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-routing-policy-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-segment-routing-deviation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-openconfig-spanning-tree-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-xe-openconfig-spanning-tree-ext` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-xe-openconfig-system-ext` | ✓ | ✓ | ✓ | ✓ |  | ✓ | ✓ | ✓ |  |  |
|  | `cisco-xe-openconfig-system-grpc-deviation` | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |
|  | `cisco-xe-openconfig-vlan-ext` | ✓ | ✓ | ✓ |  |  |  |  |  |  |  |
|  | `cisco-xe-routing-asr-openconfig-if-ethernet-deviation` |  |  |  | ✓ |  | ✓ |  |  |  |  |
|  | `cisco-xe-routing-csr-openconfig-platform-deviation` |  |  |  |  | ✓ |  |  |  |  |  |
|  | `cisco-xe-routing-isr-openconfig-if-ethernet-deviation` |  |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-routing-isr-openconfig-platform-deviation` |  |  |  |  |  |  |  |  | ✓ | ✓ |
|  | `cisco-xe-routing-openconfig-system-deviation` |  |  |  |  | ✓ |  |  |  | ✓ | ✓ |
|  | `cisco-xe-routing-openconfig-system-ext` |  |  |  |  | ✓ |  |  |  | ✓ | ✓ |
|  | `cisco-xe-routing-openconfig-system-grpc-deviation` |  |  |  |  |  |  | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-routing-openconfig-vlan-deviation` |  |  |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `cisco-xe-switching-cat9k-openconfig-system-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-xe-switching-openconfig-if-ethernet-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-xe-switching-openconfig-interfaces-deviation` | ✓ |  |  |  |  |  |  |  |  |  |
|  | `cisco-xe-switching-openconfig-lacp-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-xe-switching-openconfig-platform-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-xe-switching-openconfig-vlan-deviation` | ✓ | ✓ |  |  |  |  |  |  |  |  |
|  | `cisco-xe-wireless-openconfig-if-ethernet-deviation` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `cisco-xe-wireless-openconfig-vlan-deviation` |  |  | ✓ |  |  |  |  |  |  |  |
|  | `common-mpls-static` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `common-mpls-static-devs` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `common-mpls-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `iana-crypt-hash` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `iana-if-type` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `nvo` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `nvo-devs` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `pim` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `policy-attr` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `policy-types` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tailf | `tailf-cli-extensions` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-common` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-common-monitoring2` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-common-query` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-confd-monitoring` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-confd-monitoring2` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-confd-progress` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-key-rotation` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-last-login` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-meta-extensions` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-extensions` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-forward` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-inactive` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-monitoring` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-rollback` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-transactions` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-with-rollback-id` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-netconf-with-transaction-id` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-rollback` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-tls` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
|  | `tailf-yang-patch` | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

### 10d. Platform-Exclusive Models (26.1.1)

YANG models supported on only **one** platform (all origins, MIBs excluded).

**103** platform-exclusive YANG models total:

#### Cat 9K — 53 exclusive models

| # | Module | Origin | Category |
|--:|--------|--------|----------|
| 1 | `Cisco-IOS-XE-aaa-types` | Cisco-IOS-XE | AAA |
| 2 | `Cisco-IOS-XE-cable-diag-oper` | Cisco-IOS-XE | Switching |
| 3 | `Cisco-IOS-XE-device-tracking-cat9k-deviation` | Cisco-IOS-XE | Security |
| 4 | `Cisco-IOS-XE-dhcp-security-track-server-oper` | Cisco-IOS-XE | DHCP |
| 5 | `Cisco-IOS-XE-ethernet-cat9k-deviation` | Cisco-IOS-XE | Interfaces |
| 6 | `Cisco-IOS-XE-evpn-oper` | Cisco-IOS-XE | Switching |
| 7 | `Cisco-IOS-XE-fwd-oper` | Cisco-IOS-XE | Routing |
| 8 | `Cisco-IOS-XE-group-policy-oper` | Cisco-IOS-XE | Security |
| 9 | `Cisco-IOS-XE-grpc-tunnel-cfg` | Cisco-IOS-XE | Telemetry |
| 10 | `Cisco-IOS-XE-identity-oper` | Cisco-IOS-XE | Security |
| 11 | `Cisco-IOS-XE-interfaces-cat9k-deviation` | Cisco-IOS-XE | Interfaces |
| 12 | `Cisco-IOS-XE-line-nonquake-deviation` | Cisco-IOS-XE | Interfaces |
| 13 | `Cisco-IOS-XE-loop-detect-events` | Cisco-IOS-XE | Switching |
| 14 | `Cisco-IOS-XE-macsec-oper` | Cisco-IOS-XE | Security |
| 15 | `Cisco-IOS-XE-matm-events` | Cisco-IOS-XE | Switching |
| 16 | `Cisco-IOS-XE-matm-oper` | Cisco-IOS-XE | Switching |
| 17 | `Cisco-IOS-XE-matm-state-oper` | Cisco-IOS-XE | Switching |
| 18 | `Cisco-IOS-XE-meraki-leds-actions-rpc` | Cisco-IOS-XE | Cloud |
| 19 | `Cisco-IOS-XE-nve-oper` | Cisco-IOS-XE | VPN/Tunnel |
| 20 | `Cisco-IOS-XE-platform-events-oper` | Cisco-IOS-XE | Platform |
| 21 | `Cisco-IOS-XE-poch-lb-switch-deviation` | Cisco-IOS-XE | Switching |
| 22 | `Cisco-IOS-XE-poe-health-oper` | Cisco-IOS-XE | Platform |
| 23 | `Cisco-IOS-XE-policy-cat9k-deviation` | Cisco-IOS-XE | QoS |
| 24 | `Cisco-IOS-XE-port-security-rpc` | Cisco-IOS-XE | Security |
| 25 | `Cisco-IOS-XE-power-supply-rpc` | Cisco-IOS-XE | Platform |
| 26 | `Cisco-IOS-XE-psecure-oper` | Cisco-IOS-XE | Security |
| 27 | `Cisco-IOS-XE-rib-oper` | Cisco-IOS-XE | Routing |
| 28 | `Cisco-IOS-XE-spanning-tree-events` | Cisco-IOS-XE | Switching |
| 29 | `Cisco-IOS-XE-spanning-tree-oper` | Cisco-IOS-XE | Switching |
| 30 | `Cisco-IOS-XE-stack-info-oper` | Cisco-IOS-XE | Switching |
| 31 | `Cisco-IOS-XE-stack-member-oper` | Cisco-IOS-XE | Switching |
| 32 | `Cisco-IOS-XE-stack-mgr-events-oper` | Cisco-IOS-XE | Switching |
| 33 | `Cisco-IOS-XE-stack-power-rpc` | Cisco-IOS-XE | Switching |
| 34 | `Cisco-IOS-XE-stacking-oper` | Cisco-IOS-XE | Switching |
| 35 | `Cisco-IOS-XE-steering-policy-oper` | Cisco-IOS-XE | SD-WAN |
| 36 | `Cisco-IOS-XE-switch-cp-svl-oper` | Cisco-IOS-XE | Switching |
| 37 | `Cisco-IOS-XE-switch-dp-mac-learning-oper` | Cisco-IOS-XE | Switching |
| 38 | `Cisco-IOS-XE-switch-dp-punt-inject-oper` | Cisco-IOS-XE | Switching |
| 39 | `Cisco-IOS-XE-switch-dp-resources-oper` | Cisco-IOS-XE | Switching |
| 40 | `Cisco-IOS-XE-switch-ptp-dp-oper` | Cisco-IOS-XE | Timing |
| 41 | `Cisco-IOS-XE-switch-ptp-oper` | Cisco-IOS-XE | Timing |
| 42 | `Cisco-IOS-XE-tcam-oper` | Cisco-IOS-XE | Platform |
| 43 | `Cisco-IOS-XE-udld-events` | Cisco-IOS-XE | Switching |
| 44 | `Cisco-IOS-XE-udld-oper` | Cisco-IOS-XE | Switching |
| 45 | `Cisco-IOS-XE-uplink-autoconfig-oper` | Cisco-IOS-XE | Switching |
| 46 | `Cisco-IOS-XE-verify-events` | Cisco-IOS-XE | System |
| 47 | `Cisco-IOS-XE-verify-rpc` | Cisco-IOS-XE | System |
| 48 | `openconfig-ethernet-segments` | OpenConfig | OpenConfig |
| 49 | `openconfig-openflow` | OpenConfig | OpenConfig |
| 50 | `openconfig-openflow-types` | OpenConfig | OpenConfig |
| 51 | `cisco-xe-openconfig-ethernet-segments-deviation` | Other | OC Deviation |
| 52 | `cisco-xe-openconfig-openflow-deviation` | Other | OC Deviation |
| 53 | `cisco-xe-switching-openconfig-interfaces-deviation` | Other | OC Deviation |

#### Cat 9200 — 7 exclusive models

| # | Module | Origin | Category |
|--:|--------|--------|----------|
| 1 | `Cisco-IOS-XE-ethernet-cfm-efp-deviation` | Cisco-IOS-XE | Interfaces |
| 2 | `Cisco-IOS-XE-line-quake-deviation` | Cisco-IOS-XE | Interfaces |
| 3 | `Cisco-IOS-XE-port-channel-quake-deviation` | Cisco-IOS-XE | Switching |
| 4 | `Cisco-IOS-XE-rep` | Cisco-IOS-XE | Switching |
| 5 | `Cisco-IOS-XE-stp-quake-deviation` | Cisco-IOS-XE | Switching |
| 6 | `Cisco-IOS-XE-swc` | Cisco-IOS-XE | Switching |
| 7 | `Cisco-IOS-XE-vlan-quake-deviation` | Cisco-IOS-XE | Switching |

#### WLC — 12 exclusive models

| # | Module | Origin | Category |
|--:|--------|--------|----------|
| 1 | `Cisco-IOS-XE-interfaces-wlc-deviation` | Cisco-IOS-XE | Interfaces |
| 2 | `Cisco-IOS-XE-policy-wlc-deviation` | Cisco-IOS-XE | QoS |
| 3 | `Cisco-IOS-XE-switchport-ewlc-deviation` | Cisco-IOS-XE | Switching |
| 4 | `Cisco-IOS-XE-vlan-ewlc-deviation` | Cisco-IOS-XE | Switching |
| 5 | `openconfig-access-points` | OpenConfig | OpenConfig |
| 6 | `openconfig-ap-manager` | OpenConfig | OpenConfig |
| 7 | `openconfig-wifi-mac` | OpenConfig | OpenConfig |
| 8 | `openconfig-wifi-phy` | OpenConfig | OpenConfig |
| 9 | `openconfig-wifi-types` | OpenConfig | OpenConfig |
| 10 | `cisco-xe-openconfig-access-points-deviation` | Other | OC Deviation |
| 11 | `cisco-xe-wireless-openconfig-if-ethernet-deviation` | Other | OC Deviation |
| 12 | `cisco-xe-wireless-openconfig-vlan-deviation` | Other | OC Deviation |

#### C8000v — 6 exclusive models

| # | Module | Origin | Category |
|--:|--------|--------|----------|
| 1 | `Cisco-IOS-XE-autovpn-events` | Cisco-IOS-XE | VPN/Tunnel |
| 2 | `Cisco-IOS-XE-dhcp-deviation` | Cisco-IOS-XE | DHCP |
| 3 | `Cisco-IOS-XE-line-deviation` | Cisco-IOS-XE | Interfaces |
| 4 | `Cisco-IOS-XE-policy-vxe-deviation` | Cisco-IOS-XE | QoS |
| 5 | `Cisco-IOS-XE-vlan-vxe-deviation` | Cisco-IOS-XE | Switching |
| 6 | `cisco-xe-routing-csr-openconfig-platform-deviation` | Other | OC Deviation |

#### ISR 1K — 19 exclusive models

| # | Module | Origin | Category |
|--:|--------|--------|----------|
| 1 | `Cisco-IOS-XE-bbu-oper` | Cisco-IOS-XE | Platform |
| 2 | `Cisco-IOS-XE-controller-t1e1-oper` | Cisco-IOS-XE | Interfaces |
| 3 | `Cisco-IOS-XE-cwan-fw-rpc` | Cisco-IOS-XE | SD-WAN |
| 4 | `Cisco-IOS-XE-digital-io-oper` | Cisco-IOS-XE | IoT/Industrial |
| 5 | `Cisco-IOS-XE-embedded-ap-actions-rpc` | Cisco-IOS-XE | Wireless |
| 6 | `Cisco-IOS-XE-embedded-ap-oper` | Cisco-IOS-XE | Wireless |
| 7 | `Cisco-IOS-XE-gnss-dr-oper` | Cisco-IOS-XE | IoT/Industrial |
| 8 | `Cisco-IOS-XE-ignition-oper` | Cisco-IOS-XE | IoT/Industrial |
| 9 | `Cisco-IOS-XE-isdn-oper` | Cisco-IOS-XE | Voice/UC |
| 10 | `Cisco-IOS-XE-line-actions-rpc` | Cisco-IOS-XE | Interfaces |
| 11 | `Cisco-IOS-XE-line-events` | Cisco-IOS-XE | Interfaces |
| 12 | `Cisco-IOS-XE-line-oper` | Cisco-IOS-XE | Interfaces |
| 13 | `Cisco-IOS-XE-lorawan-oper` | Cisco-IOS-XE | IoT/Industrial |
| 14 | `Cisco-IOS-XE-lte450-oper` | Cisco-IOS-XE | IoT/Industrial |
| 15 | `Cisco-IOS-XE-rawsocket-oper` | Cisco-IOS-XE | IoT/Industrial |
| 16 | `Cisco-IOS-XE-scada-gw-oper` | Cisco-IOS-XE | IoT/Industrial |
| 17 | `Cisco-IOS-XE-ucse-oper` | Cisco-IOS-XE | System |
| 18 | `Cisco-IOS-XE-vdsp-oper` | Cisco-IOS-XE | Voice/UC |
| 19 | `Cisco-IOS-XE-wpan-oper` | Cisco-IOS-XE | IoT/Industrial |

#### IR 1101 — 6 exclusive models

| # | Module | Origin | Category |
|--:|--------|--------|----------|
| 1 | `Cisco-IOS-XE-adsl` | Cisco-IOS-XE | Interfaces |
| 2 | `Cisco-IOS-XE-digitalio` | Cisco-IOS-XE | IoT/Industrial |
| 3 | `Cisco-IOS-XE-lorawan` | Cisco-IOS-XE | IoT/Industrial |
| 4 | `Cisco-IOS-XE-lte450` | Cisco-IOS-XE | IoT/Industrial |
| 5 | `Cisco-IOS-XE-rawsocket` | Cisco-IOS-XE | IoT/Industrial |
| 6 | `Cisco-IOS-XE-scada-gw` | Cisco-IOS-XE | IoT/Industrial |

#### Shared by Exactly 2 Platforms (26.1.1)

YANG models on only two platforms — highlights platform-pair feature overlap.

| Module | Origin | Platform 1 | Platform 2 |
|--------|--------|-----------|-----------|
| `Cisco-IOS-XE-aging-time-deviation` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-alarm-profile` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-app-hosting` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-avb` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-bgp-rib-oper` | Cisco-IOS-XE | Cat 9K | C8000v |
| `Cisco-IOS-XE-cable-diag-rpc` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-cip` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-coap` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-controller-shdsl-common` | Cisco-IOS-XE | C8000v | ISR 1K |
| `Cisco-IOS-XE-controller-shdsl-events` | Cisco-IOS-XE | C8000v | ISR 1K |
| `Cisco-IOS-XE-controller-shdsl-oper` | Cisco-IOS-XE | C8000v | ISR 1K |
| `Cisco-IOS-XE-cts-switching-deviation` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-cwan-actions-rpc` | Cisco-IOS-XE | C8000v | ISR 1K |
| `Cisco-IOS-XE-device-sensor` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-device-sensor-deviation` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-dlr` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-dlr-oper` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-ethernet-deviation` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-ethernet-mcp-deviation` | Cisco-IOS-XE | C8500 | ASR 1K |
| `Cisco-IOS-XE-ethernet-radium-deviation` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-ethinternal-subslot` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-gnss` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-group-policy` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-hsr` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-iad-oper` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-ida` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-ip-arp-oper` | Cisco-IOS-XE | Cat 9K | C8000v |
| `Cisco-IOS-XE-ipv6-nd-oper` | Cisco-IOS-XE | Cat 9K | C8000v |
| `Cisco-IOS-XE-irig` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-isdn` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-isis-intf-oper` | Cisco-IOS-XE | Cat 9K | C8000v |
| `Cisco-IOS-XE-l2nat` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-l2nat-oper` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-l3nat-iox` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-livetools-actions-rpc` | Cisco-IOS-XE | Cat 9K | C8000v |
| `Cisco-IOS-XE-livetools-common-types` | Cisco-IOS-XE | Cat 9K | C8000v |
| `Cisco-IOS-XE-livetools-oper` | Cisco-IOS-XE | Cat 9K | C8000v |
| `Cisco-IOS-XE-loop-detect` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-mmode` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-mrp` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-mrp-oper` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-mvrp` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-policy-mcp-deviation` | Cisco-IOS-XE | C8500 | ASR 1K |
| `Cisco-IOS-XE-port-channel-crankshaft-deviation` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-ppp-mcp-deviation` | Cisco-IOS-XE | C8500 | ASR 1K |
| `Cisco-IOS-XE-prp` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-qfp-dp-cmn-stats-oper` | Cisco-IOS-XE | WLC | IR 1101 |
| `Cisco-IOS-XE-scada` | Cisco-IOS-XE | IE 3x00 | ESS 3x00 |
| `Cisco-IOS-XE-stackwise-virtual` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-switch-deviation` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-switch-rpc` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-switchport-deviation` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-switchport-oper` | Cisco-IOS-XE | Cat 9K | ISR 1K |
| `Cisco-IOS-XE-synce` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-ucse` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-ucse-rpc` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-voice-port` | Cisco-IOS-XE | ISR 1K | IR 1101 |
| `Cisco-IOS-XE-vrrp-deviation` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `Cisco-IOS-XE-vstack` | Cisco-IOS-XE | Cat 9K | Cat 9200 |
| `ietf-routing-types` | IETF | Cat 9K | Cat 9200 |
| `openconfig-lacp` | OpenConfig | Cat 9K | Cat 9200 |
| `openconfig-macsec` | OpenConfig | Cat 9K | Cat 9200 |
| `openconfig-macsec-types` | OpenConfig | Cat 9K | Cat 9200 |
| `openconfig-spanning-tree` | OpenConfig | Cat 9K | Cat 9200 |
| `openconfig-spanning-tree-types` | OpenConfig | Cat 9K | Cat 9200 |
| `cisco-evpn-service` | Other | Cat 9K | Cat 9200 |
| `cisco-xe-openconfig-spanning-tree-deviation` | Other | Cat 9K | Cat 9200 |
| `cisco-xe-openconfig-spanning-tree-ext` | Other | Cat 9K | Cat 9200 |
| `cisco-xe-routing-asr-openconfig-if-ethernet-deviation` | Other | C8500 | ASR 1K |
| `cisco-xe-routing-isr-openconfig-platform-deviation` | Other | IE 3x00 | ESS 3x00 |
| `cisco-xe-switching-cat9k-openconfig-system-deviation` | Other | Cat 9K | Cat 9200 |
| `cisco-xe-switching-openconfig-if-ethernet-deviation` | Other | Cat 9K | Cat 9200 |
| `cisco-xe-switching-openconfig-lacp-deviation` | Other | Cat 9K | Cat 9200 |
| `cisco-xe-switching-openconfig-platform-deviation` | Other | Cat 9K | Cat 9200 |
| `cisco-xe-switching-openconfig-vlan-deviation` | Other | Cat 9K | Cat 9200 |

### 10e. Universal YANG Models — All 10 Platforms (26.1.1)

**330** YANG models supported on **every** platform:

**Cisco-IOS-XE** (108 models):

- AAA (2): `Cisco-IOS-XE-aaa`, `Cisco-IOS-XE-aaa-rpc`
- ACL (2): `Cisco-IOS-XE-acl`, `Cisco-IOS-XE-object-group`
- DHCP (2): `Cisco-IOS-XE-dhcp`, `Cisco-IOS-XE-dhcp-rpc`
- DNS (1): `Cisco-IOS-XE-mdns-gateway`
- DPI/AppVis (5): `Cisco-IOS-XE-eta`, `Cisco-IOS-XE-flow`, `Cisco-IOS-XE-flow-deviation`, `Cisco-IOS-XE-flow-rpc`, `Cisco-IOS-XE-nbar`
- Geo/Location (1): `Cisco-IOS-XE-location`
- Interfaces (13): `Cisco-IOS-XE-atm`, `Cisco-IOS-XE-dialer`, `Cisco-IOS-XE-dialer-deviation`, `Cisco-IOS-XE-ethernet`, `Cisco-IOS-XE-ethernet-cfm-efp`, `Cisco-IOS-XE-ethernet-oam`, `Cisco-IOS-XE-interface-common`, `Cisco-IOS-XE-interfaces`, `Cisco-IOS-XE-interfaces-deviation`, `Cisco-IOS-XE-line`, `Cisco-IOS-XE-line-common-deviation`, `Cisco-IOS-XE-ppp`, `Cisco-IOS-XE-pppoe`
- Platform (5): `Cisco-IOS-XE-buffers`, `Cisco-IOS-XE-diagnostics`, `Cisco-IOS-XE-platform`, `Cisco-IOS-XE-platform-rpc`, `Cisco-IOS-XE-transceiver-monitor`
- QoS (2): `Cisco-IOS-XE-policy`, `Cisco-IOS-XE-qos`
- Routing (31): `Cisco-IOS-XE-arp`, `Cisco-IOS-XE-arp-rpc`, `Cisco-IOS-XE-bfd`, `Cisco-IOS-XE-bgp-rpc`, `Cisco-IOS-XE-cef`, `Cisco-IOS-XE-cef-deviation`, `Cisco-IOS-XE-hsrp`, `Cisco-IOS-XE-icmp`, `Cisco-IOS-XE-igmp`, `Cisco-IOS-XE-ip`, `Cisco-IOS-XE-ipv6`, `Cisco-IOS-XE-isis`, `Cisco-IOS-XE-mld`, `Cisco-IOS-XE-mpls`, `Cisco-IOS-XE-multicast`, `Cisco-IOS-XE-multicast-rpc`, `Cisco-IOS-XE-nd`, `Cisco-IOS-XE-nd-deviation`, `Cisco-IOS-XE-nhrp`, `Cisco-IOS-XE-ospf`, `Cisco-IOS-XE-ospf-deviation`, `Cisco-IOS-XE-ospf-obsolete`, `Cisco-IOS-XE-ospf-rpc`, `Cisco-IOS-XE-ospfv3`, `Cisco-IOS-XE-ospfv3-deviation`, `Cisco-IOS-XE-route-map`, `Cisco-IOS-XE-rsvp`, `Cisco-IOS-XE-segment-routing`, `Cisco-IOS-XE-service-routing`, `Cisco-IOS-XE-vrrp`, `Cisco-IOS-XE-wccp`
- SD-WAN (1): `Cisco-IOS-XE-service-insertion`
- Security (9): `Cisco-IOS-XE-crypto`, `Cisco-IOS-XE-crypto-rpc`, `Cisco-IOS-XE-cts`, `Cisco-IOS-XE-cts-rpc`, `Cisco-IOS-XE-device-tracking`, `Cisco-IOS-XE-dot1x`, `Cisco-IOS-XE-sanet`, `Cisco-IOS-XE-sanet-deviation`, `Cisco-IOS-XE-sisf`
- Switching (7): `Cisco-IOS-XE-cdp`, `Cisco-IOS-XE-l2vpn`, `Cisco-IOS-XE-lldp`, `Cisco-IOS-XE-spanning-tree`, `Cisco-IOS-XE-switch`, `Cisco-IOS-XE-vlan`, `Cisco-IOS-XE-vtp`
- System (25): `Cisco-IOS-XE-call-home`, `Cisco-IOS-XE-cli-rpc`, `Cisco-IOS-XE-eem`, `Cisco-IOS-XE-features`, `Cisco-IOS-XE-http`, `Cisco-IOS-XE-ipc`, `Cisco-IOS-XE-kron`, `Cisco-IOS-XE-license`, `Cisco-IOS-XE-logging`, `Cisco-IOS-XE-native`, `Cisco-IOS-XE-ntp`, `Cisco-IOS-XE-parser`, `Cisco-IOS-XE-pnp`, `Cisco-IOS-XE-rescue-config-rpc`, `Cisco-IOS-XE-rollback-rpc`, `Cisco-IOS-XE-rpc`, `Cisco-IOS-XE-service-discovery`, `Cisco-IOS-XE-sla`, `Cisco-IOS-XE-snmp`, `Cisco-IOS-XE-snmp-deviation`, `Cisco-IOS-XE-template`, `Cisco-IOS-XE-track`, `Cisco-IOS-XE-transport`, `Cisco-IOS-XE-types`, `Cisco-IOS-XE-wsma`
- VPN/Tunnel (1): `Cisco-IOS-XE-tunnel`
- Wireless (1): `Cisco-IOS-XE-wireless-rpc`

**OpenConfig** (111 models):

- OpenConfig (111): `openconfig-aaa`, `openconfig-aaa-radius`, `openconfig-aaa-tacacs`, `openconfig-aaa-types`, `openconfig-acl`, `openconfig-aft`, `openconfig-aft-common`, `openconfig-aft-ethernet`, `openconfig-aft-ipv4`, `openconfig-aft-ipv6`, `openconfig-aft-mpls`, `openconfig-aft-network-instance`, `openconfig-aft-pf`, `openconfig-aft-state-synced`, `openconfig-aft-types`, `openconfig-alarm-types`, `openconfig-alarms`, `openconfig-bfd`, `openconfig-bgp`, `openconfig-bgp-common`, `openconfig-bgp-common-multiprotocol`, `openconfig-bgp-common-structure`, `openconfig-bgp-errors`, `openconfig-bgp-global`, `openconfig-bgp-neighbor`, `openconfig-bgp-peer-group`, `openconfig-bgp-policy`, `openconfig-bgp-types`, `openconfig-evpn`, `openconfig-evpn-types`, `openconfig-extensions`, `openconfig-if-aggregate`, `openconfig-if-ethernet`, `openconfig-if-ip`, `openconfig-if-ip-ext`, `openconfig-if-types`, `openconfig-igmp`, `openconfig-igmp-types`, `openconfig-inet-types`, `openconfig-interfaces`, `openconfig-isis`, `openconfig-isis-lsdb-types`, `openconfig-isis-lsp`, `openconfig-isis-policy`, `openconfig-isis-routing`, `openconfig-isis-types`, `openconfig-keychain`, `openconfig-keychain-types`, `openconfig-license`, `openconfig-lldp`, `openconfig-lldp-types`, `openconfig-local-routing`, `openconfig-messages`, `openconfig-mpls`, `openconfig-mpls-igp`, `openconfig-mpls-ldp`, `openconfig-mpls-rsvp`, `openconfig-mpls-sr`, `openconfig-mpls-static`, `openconfig-mpls-te`, `openconfig-mpls-types`, `openconfig-network-instance`, `openconfig-network-instance-l2`, `openconfig-network-instance-l3`, `openconfig-network-instance-policy`, `openconfig-network-instance-types`, `openconfig-ospf-policy`, `openconfig-ospf-types`, `openconfig-ospfv2`, `openconfig-ospfv2-area`, `openconfig-ospfv2-area-interface`, `openconfig-ospfv2-common`, `openconfig-ospfv2-global`, `openconfig-ospfv2-lsdb`, `openconfig-packet-match`, `openconfig-packet-match-types`, `openconfig-pcep`, `openconfig-pf-forwarding-policies`, `openconfig-pf-interfaces`, `openconfig-pf-path-groups`, `openconfig-pim`, `openconfig-pim-types`, `openconfig-platform`, `openconfig-platform-types`, `openconfig-policy-forwarding`, `openconfig-policy-types`, `openconfig-procmon`, `openconfig-qos`, `openconfig-qos-elements`, `openconfig-qos-interfaces`, `openconfig-qos-mem-mgmt`, `openconfig-qos-types`, `openconfig-rib-bgp`, `openconfig-rib-bgp-attributes`, `openconfig-rib-bgp-ext`, `openconfig-rib-bgp-shared-attributes`, `openconfig-rib-bgp-table-attributes`, `openconfig-rib-bgp-tables`, `openconfig-rib-bgp-types`, `openconfig-route-summary`, `openconfig-routing-policy`, `openconfig-segment-routing`, `openconfig-segment-routing-types`, `openconfig-system`, `openconfig-system-logging`, `openconfig-system-terminal`, `openconfig-transport-types`, `openconfig-types`, `openconfig-vlan`, `openconfig-vlan-types`, `openconfig-yang-types`

**IETF** (38 models):

- IETF Standard (38): `ietf-datastores`, `ietf-diffserv-action`, `ietf-diffserv-classifier`, `ietf-diffserv-policy`, `ietf-diffserv-target`, `ietf-event-notifications`, `ietf-inet-types`, `ietf-interfaces`, `ietf-interfaces-ext`, `ietf-ip`, `ietf-ipv4-unicast-routing`, `ietf-ipv6-unicast-routing`, `ietf-key-chain`, `ietf-netconf`, `ietf-netconf-monitoring`, `ietf-netconf-nmda`, `ietf-netconf-notifications`, `ietf-netconf-otlp-context`, `ietf-netconf-otlp-context-traceparent-version-1.0`, `ietf-netconf-otlp-context-tracestate-version-1.0`, `ietf-netconf-with-defaults`, `ietf-network-instance`, `ietf-origin`, `ietf-ospf`, `ietf-restconf`, `ietf-restconf-monitoring`, `ietf-routing`, `ietf-subscribed-notifications`, `ietf-subscribed-notifications-deviation`, `ietf-x509-cert-to-name`, `ietf-yang-library`, `ietf-yang-metadata`, `ietf-yang-patch`, `ietf-yang-push`, `ietf-yang-schema-mount`, `ietf-yang-smiv2`, `ietf-yang-structure-ext`, `ietf-yang-types`

**Tailf** (21 models):

- Tailf/NSO (21): `tailf-cli-extensions`, `tailf-common`, `tailf-common-monitoring2`, `tailf-common-query`, `tailf-confd-monitoring`, `tailf-confd-monitoring2`, `tailf-confd-progress`, `tailf-key-rotation`, `tailf-last-login`, `tailf-meta-extensions`, `tailf-netconf-extensions`, `tailf-netconf-forward`, `tailf-netconf-inactive`, `tailf-netconf-monitoring`, `tailf-netconf-rollback`, `tailf-netconf-transactions`, `tailf-netconf-with-rollback-id`, `tailf-netconf-with-transaction-id`, `tailf-rollback`, `tailf-tls`, `tailf-yang-patch`

**Other** (52 models):

- IETF Deviation (9): `cisco-xe-ietf-event-notifications-deviation`, `cisco-xe-ietf-ip-deviation`, `cisco-xe-ietf-ipv4-unicast-routing-deviation`, `cisco-xe-ietf-ipv6-unicast-routing-deviation`, `cisco-xe-ietf-ospf-deviation`, `cisco-xe-ietf-routing-deviation`, `cisco-xe-ietf-routing-ext`, `cisco-xe-ietf-yang-push-deviation`, `cisco-xe-ietf-yang-push-ext`
- IETF Standard (2): `iana-crypt-hash`, `iana-if-type`
- Interfaces (1): `cisco-ethernet`
- OC Deviation (21): `cisco-xe-openconfig-acl-deviation`, `cisco-xe-openconfig-acl-ext`, `cisco-xe-openconfig-aft-deviation`, `cisco-xe-openconfig-bgp-deviation`, `cisco-xe-openconfig-bgp-policy-deviation`, `cisco-xe-openconfig-evpn-deviation`, `cisco-xe-openconfig-if-ethernet-ext`, `cisco-xe-openconfig-if-ip-deviation`, `cisco-xe-openconfig-interfaces-deviation`, `cisco-xe-openconfig-interfaces-ext`, `cisco-xe-openconfig-isis-deviation`, `cisco-xe-openconfig-isis-policy-deviation`, `cisco-xe-openconfig-lldp-deviation`, `cisco-xe-openconfig-local-routing-deviation`, `cisco-xe-openconfig-mpls-deviation`, `cisco-xe-openconfig-network-instance-deviation`, `cisco-xe-openconfig-network-instance-l2-deviation`, `cisco-xe-openconfig-qos-deviation`, `cisco-xe-openconfig-rib-bgp-ext`, `cisco-xe-openconfig-routing-policy-deviation`, `cisco-xe-openconfig-segment-routing-deviation`
- QoS (5): `cisco-policy`, `cisco-policy-filters`, `cisco-policy-target`, `policy-attr`, `policy-types`
- Routing (6): `cisco-ospf`, `cisco-routing-ext`, `common-mpls-static`, `common-mpls-static-devs`, `common-mpls-types`, `pim`
- System (6): `cisco-extensions`, `cisco-ia`, `cisco-self-mgmt`, `cisco-semver`, `cisco-smart-license`, `cisco-smart-license-errors`
- VPN/Tunnel (2): `nvo`, `nvo-devs`

### 10f. Platform Model Count Growth Over Time

YANG model counts (MIBs excluded).

| Platform | 16.9.3 | 16.12.1 | 17.3.1 | 17.6.1 | 17.9.1 | 17.12.1 | 17.15.1 | 17.18.1 | 26.1.1 |
|----------|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| Cat 9K | — | — | 336 | — | — | — | 546 | 663 | 684 |
| Cat 9200 | — | 299 | 336 | 438 | 480 | 566 | 383 | 397 | 406 |
| WLC | — | 350 | 382 | 403 | 438 | 518 | 559 | 589 | 607 |
| C8500 | — | — | — | 380 | 423 | 495 | 543 | 565 | 583 |
| C8000v | — | — | — | 376 | 416 | 488 | 536 | 564 | 587 |
| ASR 1K | 253 | 297 | 329 | 380 | 423 | 495 | 543 | 565 | 583 |
| ISR 1K | 256 | 310 | 348 | 404 | 439 | 524 | 572 | 599 | 621 |
| IR 1101 | — | 307 | 265 | 408 | 443 | 530 | 579 | 628 | 646 |
| IE 3x00 | — | 290 | 314 | 342 | 373 | 452 | 494 | 506 | 525 |
| ESS 3x00 | — | 290 | 314 | 342 | 373 | 452 | 494 | 506 | 525 |

### 10g. Feature Category by Platform (26.1.1)

Number of YANG models per feature category per platform (all origins, no MIBs).

| Category | Cat 9K | Cat 9200 | WLC | C8500 | C8000v | ASR 1K | ISR 1K | IR 1101 | IE 3x00 | ESS 3x00 |
|----------|------:|------:|------:|------:|------:|------:|------:|------:|------:|------:|
| AAA | 7 | 3 | 6 | 6 | 6 | 6 | 5 | 5 | 6 | 6 |
| ACL | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| App Hosting | 2 | — | 3 | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| Cloud | 11 | — | 10 | — | — | — | — | 10 | — | — |
| DHCP | 4 | 2 | 3 | 3 | 4 | 3 | 3 | 3 | 3 | 3 |
| DNS | 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| DPI/AppVis | 7 | 6 | 7 | 9 | 9 | 9 | 9 | 7 | 6 | 6 |
| Geo/Location | 1 | 1 | 1 | 5 | 5 | 5 | 5 | 2 | 2 | 2 |
| High Availability | 2 | — | 2 | 4 | 4 | 4 | 4 | 2 | 1 | 1 |
| IETF Deviation | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 9 |
| IETF Standard | 41 | 41 | 40 | 40 | 40 | 40 | 40 | 40 | 40 | 40 |
| Interfaces | 23 | 17 | 23 | 27 | 32 | 27 | 38 | 30 | 27 | 27 |
| IoT/Industrial | 2 | 3 | 1 | 2 | 2 | 2 | 14 | 10 | 15 | 15 |
| NAT | 1 | — | 2 | 3 | 3 | 3 | 3 | 2 | 4 | 4 |
| OC Deviation | 36 | 33 | 28 | 25 | 25 | 25 | 27 | 27 | 27 | 27 |
| OpenConfig | 128 | 125 | 124 | 119 | 112 | 119 | 119 | 119 | 112 | 112 |
| Platform | 32 | 7 | 27 | 32 | 28 | 32 | 36 | 30 | 27 | 27 |
| QoS | 8 | 7 | 8 | 9 | 10 | 9 | 9 | 8 | 7 | 7 |
| Routing | 82 | 46 | 67 | 82 | 86 | 82 | 80 | 74 | 78 | 78 |
| SD-WAN | 2 | 1 | 2 | 23 | 24 | 23 | 24 | 3 | 2 | 2 |
| Security | 34 | 13 | 30 | 42 | 40 | 42 | 41 | 33 | 34 | 34 |
| Switching | 52 | 26 | 22 | 23 | 23 | 23 | 24 | 25 | 19 | 19 |
| System | 63 | 35 | 56 | 55 | 59 | 55 | 59 | 59 | 54 | 54 |
| Tailf/NSO | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 | 21 |
| Telemetry | 13 | — | 12 | 16 | 15 | 16 | 15 | 13 | 11 | 11 |
| Timing | 3 | 1 | — | — | — | — | 2 | 2 | — | — |
| VPN/Tunnel | 9 | 5 | 12 | 11 | 12 | 11 | 10 | 11 | 10 | 10 |
| Voice/UC | — | — | — | 8 | 9 | 8 | 13 | 7 | 1 | 1 |
| Wireless | 86 | 1 | 86 | 1 | 1 | 1 | 3 | 86 | 1 | 1 |

### Platform Key Takeaways

- **Broadest coverage:** Cat 9K with **684** YANG models
- **Most focused:** Cat 9200 with **406** YANG models
- **Cat 9200 vs Cat 9K:** 406 vs 684 YANG models — Cat 9K is the campus feature leader
- **Universal core:** **330** YANG models work on every platform
- **Platform-specific:** **103** YANG models exclusive to a single platform
- **Cat 9K depth:** **53** exclusive models (stacking, switching, PoE, MACsec, etc.)
- **IoT/Industrial edge:** **6** models exclusive to IE/IR/ESS platforms

---

## Key Takeaways for Technical Marketing

1. **Sustained Innovation:** 969% model growth from 16.3.1 to 26.1.1 (83 → 887 models)
2. **Biggest Release:** 16.5.1 introduced **126** new models
3. **Operational Visibility Explosion:** Operational data models grew from **2** to **222** — enabling deep telemetry and monitoring
4. **Event-Driven Automation:** Event notification models are **entirely new** — 36 event models enable reactive automation
5. **OpenConfig Standards:** **140** OpenConfig models adopted, demonstrating commitment to multi-vendor interoperability
6. **Foundation Stability:** **35** models present in every release — stable APIs operators can rely on
7. **SD-WAN:** Entirely new category — programmable overlay management didn't exist in 16.3.1

> **Generated:** April 2026 | **Source:** Filename + yang-library analysis of 32 IOS-XE releases, all YANG models, MIBs excluded