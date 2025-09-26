# Networking_Lab

This repository contains exercises, notes, and demonstrations for learning **Computer Networking** concepts. It is designed for beginners to understand networking step by step with practical examples.

---

## Topics Covered

1. **Introduction to Networking**
   - What is a network?
   - Types of networks: LAN, WAN, MAN, PAN
   - Networking devices: Router, Switch, Hub, Modem

2. **IP Addressing**
   - IPv4 and IPv6
   - Subnetting basics
   - Public vs Private IP addresses
   - Static and Dynamic IP

3. **Network Protocols**
   - TCP/IP model
   - OSI model
   - Common protocols: HTTP, HTTPS, FTP, SMTP, DNS, DHCP

4. **Subnetting and CIDR**
   - Calculating subnet masks
   - Number of hosts per subnet
   - CIDR notation examples

5. **Routing and Switching**
   - How routers and switches work
   - Routing vs Switching
   - Basic routing concepts: static and dynamic routing

6. **Network Tools**
   - `ping`, `tracert` / `traceroute`
   - `ipconfig` / `ifconfig`
   - `nslookup` / `dig`
   - Wireshark basics

7. **Wireless Networking**
   - Wi-Fi standards: 802.11a/b/g/n/ac/ax
   - Channels and frequencies
   - Security: WEP, WPA, WPA2, WPA3

8. **Network Troubleshooting**
   - Diagnosing connectivity issues
   - Common errors: IP conflict, DNS failure
   - Tools and methods for troubleshooting

---

## Practical Lab Exercises

1. **Ping Test**
   ```bash
   ping google.com
Check IP Address

ipconfig      # Windows
ifconfig      # Linux/Mac


Traceroute

tracert google.com   # Windows
traceroute google.com  # Linux/Mac


DNS Lookup

nslookup example.com
dig example.com


Subnet Calculation

Calculate the subnet mask, number of hosts, and broadcast address for a given network.
