# DDoS Defense Tool

A comprehensive and lightweight toolkit designed to help detect, mitigate, and understand Distributed Denial of Service (DDoS) attacks. This tool integrates optional proxy features like SOCKS and Cloudflare bypassing techniques.

---

## 📘 What is a DDoS Attack?

A **Distributed Denial of Service (DDoS)** attack is an attempt to disrupt the normal traffic of a targeted server, service, or network by overwhelming it with a flood of Internet traffic coming from multiple sources (often bots or infected machines).

These attacks usually aim to:

- Exhaust server resources (RAM, CPU, bandwidth).
- Block legitimate users from accessing the service.
- Cause service disruption or force downtime.
- In some cases, extort ransom to stop the attack.

---

## 🧠 How DDoS Works

All network infrastructure has a limit to the number of requests it can handle. DDoS attackers exploit these limits by:

1. Infecting devices with malware (creating a botnet).
2. Sending massive traffic or requests to a target server.
3. Overwhelming its bandwidth, CPU, or memory resources.
4. Causing the server to slow down, crash, or deny service.

---

## 🔍 DDoS Attack Types

### 1. Application Layer Attacks (Layer 7)
- **HTTP Flood**: High volume of legitimate-looking HTTP requests to overload servers.
- **Slowloris**: Keeps connections open as long as possible to exhaust server threads.

### 2. Protocol Attacks (Layer 3 & 4)
- **SYN Flood**: Exploits TCP handshake, sending multiple SYN packets with fake IPs.
- **Ping of Death / Smurf**: Malformed or amplified ICMP packets.

### 3. Volumetric Attacks
- **UDP Flood**: Sends high-volume UDP packets to random ports.
- **DNS Amplification**: Reflective attack using open DNS resolvers with spoofed IPs.

---

## 🔐 Proxy Integration

This tool supports proxy-based redirection for masking your traffic or testing DDoS protection systems.

### SOCKS Proxy
- Route requests through **SOCKS5** proxy for anonymized traffic.
- Useful for stress-testing or analysis without revealing source IP.

```bash
python3 tool.py --target example.com --proxy socks5://127.0.0.1:9050
