
# CipherNorth Security Log Analyzer

A Python-based security tool that parses authentication logs, validates records, and identifies potentially suspicious login activity.

## Features

- Authentication log parsing and validation
- Detection of repeated failed login attempts by user
- Detection of repeated failed login attempts by IP address
- Detection of successful logins following repeated failures
- Detection of one IP address targeting multiple accounts
- Automated unit testing

## Requirements

- Python 3.10 or later
- No external dependencies

## Usage

Run the analyzer using the default test log:

```bash
python3 security_log_analyzer.py
```

Specify a log file:

```bash
python3 security_log_analyzer.py sample.logs.txt
```

Run the automated tests:

```bash
python3 -m unittest -v
```

## Log Format

Each record must contain four pipe-separated fields:

```text
YYYY-MM-DD HH:MM:SS|user=username|event=login_failed|ip=192.0.2.10
```

Supported events:

- `login_success`
- `login_failed`

## Detection Rules

| Rule | Description |
|---|---|
| 001 | Repeated failed logins by user |
| 002 | Repeated failed logins by IP |
| 003 | Successful login after repeated failures |
| 004 | Multiple accounts targeted by one IP |

## Testing

The project includes 10 automated tests covering:

- Valid and malformed records
- Timestamp and IP validation
- Unsupported event types
- Blank lines
- Repeated login failures
- Successful login after repeated failures
- Multiple accounts targeted by one IP

## Limitations

- Detection thresholds are configurable in the source code.
- Detection results are indicators of potentially suspicious activity, not proof of an attack.
- Rule 003 currently evaluates accumulated failed attempts within the supplied log.
- The analyzer does not currently implement time-window analysis or persistent storage.

## Project Purpose

CipherNorth demonstrates practical Python programming, input validation, log analysis, automated testing, and foundational cybersecurity investigation techniques.

**Author:** CipherNorthSec
