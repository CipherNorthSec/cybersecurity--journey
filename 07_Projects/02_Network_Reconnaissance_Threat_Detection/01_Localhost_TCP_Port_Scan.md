# Experiment 01: Localhost TCP Port Scan

## 1. Objective

The objective of this experiment was to perform an initial network reconnaissance scan using Nmap and examine the TCP port states reported by the tool.

## 2. Testing Environment

- Operating system: Ubuntu running under WSL2
- Tool: Nmap 7.98
- Target: Localhost (`127.0.0.1`)
- Scan type: Default Nmap TCP port scan

## 3. Command Used

```bash
nmap 127.0.0.1
```

The target address `127.0.0.1` is the loopback address, which refers to the local system.

## 4. Results

Nmap reported:

- Host status: Up
- Response latency: 0.00015 seconds
- Ports scanned: 1,000 TCP ports
- Closed ports: 1,000
- Open ports: 0

No open TCP ports were identified among the 1,000 ports scanned.

## 5. Technical Analysis

The scan successfully identified the local host as active.

All 1,000 scanned TCP ports were reported as closed. This indicates that the host responded to the scan but no services were listening on those ports at the time of testing.

A closed port does not indicate that a host is offline. Host availability and port state are separate observations.

## 6. Security Relevance

Network reconnaissance can help identify services exposed on a system.

From an offensive security perspective, identifying open ports is an initial step toward understanding a system's externally accessible services.

From a defensive security perspective, understanding which services are listening helps administrators assess network exposure and reduce unnecessary attack surface.

## 7. Limitations

- The experiment examined only the local system.
- The scan covered Nmap's default 1,000