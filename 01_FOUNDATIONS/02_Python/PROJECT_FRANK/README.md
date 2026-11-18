# Project Frank
## Python-Based Account Activity Investigation & Forensic Timeline

**Project Status:** Functional Educational Prototype  
**Category:** Cybersecurity / Python Development / Digital Forensics Foundations  
**Language:** Python 3  
**Dependencies:** Python Standard Library only

---

## 1. Project Overview

Project Frank is a Python-based cybersecurity investigation prototype designed to examine account activity records, identify missing expected information, and generate structured incident reporting.

The project uses a synthetic account activity dataset to demonstrate foundational digital investigation concepts, including chronological event reconstruction, data validation, anomaly identification, and evidence-based reporting.

The central investigation examines an account named `frank` and an event in which an expected IP address was not recorded.

## 2. Project Objectives

The project was developed to demonstrate the ability to:

- Structure and examine account activity data.
- Reconstruct an event timeline using timestamps.
- Identify missing expected information.
- Distinguish between information that was not required and information that was expected but missing.
- Generate structured investigation findings.
- Communicate technical limitations and conclusions accurately.

## 3. Investigation Scenario

The prototype examines four synthetic account activity events.

| Timestamp | Event | Account | IP Address |
|---|---|---|---|
| 09:00 | Account created | frank | Not recorded |
| 09:15 | Account disabled | frank | Not recorded |
| 09:20 | IP address removed | frank | None |
| 09:45 | Account restored | frank | 192.0.2.15 |

**Important:** All records are synthetic training data. The IP address is documentation-only example data, not an actual account address.

## 4. Investigation Components

### FR-001 — Account Activity Investigation

The first investigation component examines expected data fields and identifies missing information.

Its functionality includes:

- Counting recorded events.
- Identifying explicit IP-removal events.
- Checking whether expected IP information is present.
- Reporting missing expected information.
- Producing an investigation summary.
- Documenting limitations and conclusions.

The validation rules are defined specifically for this demonstration dataset.

### FR-002 — Account Activity Timeline

The second component reconstructs the account activity timeline.

It uses Python's `datetime` functionality to parse timestamps and sort events chronologically.

The resulting timeline provides a readable sequence of account activity and associated IP-address information.

## 5. Technical Implementation

The project demonstrates the following Python concepts:

| Concept | Application |
|---|---|
| Dictionaries | Represent individual audit events |
| Lists | Store the audit log |
| Conditional statements | Evaluate investigation findings |
| Loops | Process recorded events |
| Functions and methods | Access and process data |
| `datetime` | Parse and compare timestamps |
| `sorted()` | Reconstruct chronological event order |
| Lambda expressions | Define the timestamp sorting key |
| F-strings | Format investigation output |

The prototype uses Python's standard library and requires no third-party packages.

## 6. Running the Project

### Requirements

- Python 3
- A terminal or command-line interface

### Execution

From the `PROJECT_FRANK` directory, run:

```bash
python3 project_frank.py
```

The program generates the account activity timeline and investigation report in the terminal.

## 7. Investigation Findings

The synthetic dataset contains:

- Four recorded account activity events.
- One explicit IP-removal event.
- One missing expected IP address.
- One subsequent account restoration event.

The available records establish that an IP-removal event was recorded and that an expected IP address was missing.

However, the records do not establish who performed the removal or why it occurred.

## 8. Limitations

Project Frank is an educational prototype, not a production-grade digital forensics platform.

Current limitations include:

- Synthetic rather than independently acquired evidence.
- No authenticated external log source.
- No identification of the individual responsible for an event.
- No determination of intent or motive.
- Manually defined validation expectations.
- No evidence-preservation or chain-of-custody mechanism.
- No automated integrity verification.
- No persistent database or evidence repository.

The investigation therefore demonstrates data analysis and reporting techniques rather than proving malicious activity or attributing responsibility.

## 9. Potential Future Development

Possible enhancements include:

- Importing audit records from CSV and JSON files.
- Supporting multiple accounts.
- Expanding event validation rules.
- Adding automated integrity checks.
- Implementing unit tests.
- Generating downloadable investigation reports.
- Recording evidence-processing history.
- Improving anomaly detection and reporting.

These are proposed enhancements and are not represented as existing functionality.

## 10. Project Purpose

Project Frank demonstrates the practical application of Python programming to a cybersecurity investigation scenario.

It focuses on structured data analysis, chronological reconstruction, validation logic, and responsible technical reporting.

The project forms part of an ongoing cybersecurity and programming portfolio intended to demonstrate practical development skills and continued technical progression.