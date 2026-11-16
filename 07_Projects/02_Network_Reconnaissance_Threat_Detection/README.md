# Network Reconnaissance & Threat Detection

## Project Overview

This project explores network reconnaissance and basic threat detection through practical, controlled experiments.

It focuses on identifying active hosts, examining TCP port states, understanding exposed network services, and interpreting scan results from both offensive and defensive security perspectives.

All experiments are conducted in authorised environments.

## Research Objectives

- Understand fundamental network reconnaissance techniques.
- Identify active hosts and discover open, closed, and filtered ports.
- Learn how to identify network services and interpret their exposure.
- Examine potential security risks associated with exposed services.
- Explore basic defensive techniques for identifying suspicious network activitytivity.
- Develop practical scripts and repeatable experiments to support network analysis.

## Project Areas

### Offensive Security

- Host discovery and network reconnaissance.
- TCP port scanning and service enumeration.
- Identification of potentially exposed services.
- Analysis of network attack surfaces.

### Defensive Security

- Interpretation of network scan results.
- Identification of unexpected or unnecessary exposed services.
- Basic investigation of suspicious network activitytivity.
- Development of introductory detection and analysis methods.

## Tools and Environment

- Operating System: Ubuntu running under WSL2
- Network Scanning: Nmap 7.98
- Programming: Python
- Development Environment: Visual Studio Code
- Version Control: Git and GitHub.

## Experiments

| Experiment | Description | Status |
|---|---|---|
| 01 - Localhost TCP Port Scan | Initial Nmap scan examining TCP port states on the local system. | Completed |

## Ethics and Authorisation

All testing is conducted on systems and networks that we own or have explicit permission to assess.

No unauthorised scanning, access attempts, exploitation, or disruption of third-party systems is permitted.

Experiments are documented with their scope, methodology, findings, and limitations.

## Project Structure

```text
02_Network_Reconnaissance_Threat_Detection/
├── README.md
└── 01_Localhost_TCP_Port_Scan.md
...

## Planned Future Work

- Perform additional TCP port scanning experiments.
- Investigate open ports and identify associated services.
- Explore service and version detection using Nmap.
- Compare scan results under different network conditions.
- Develop Python scripts to assist with network analysis.
- Explore basic methods for identifying suspicious network activity.
- Document findings, limitations, and defensive recommendations.