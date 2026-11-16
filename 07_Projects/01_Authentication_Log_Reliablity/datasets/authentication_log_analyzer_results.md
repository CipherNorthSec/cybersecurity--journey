
# Authentication Log Analyzer — Test Results

**Project ID:** CN-001

## 1. Purpose

This document records the initial testing of the Python authentication log analyzer.

The tests evaluate whether the analyzer can:
- Read synthetic Linux-style authentication log records.
- Count successful and failed login attempts.
- Identify usernames associated with failed login attempts.
- Count failed login attempts by username.
- Identify source IP addresses associated with failed attempts.
- Count failed login attempts by source IP address.
- Generate alerts when an IP address reaches a defined failure threshold.

## 2. Test Dataset

The analyzer was tested using a synthetic authentication log containing four records.

The dataset includes:
- One successful SSH public-key login.
- One failed login attempt involving an invalid username (`admin`).
- Two failed password attempts involving the username `alice`.
- Three failed login attempts originating from the same source IP address (`198.51.100.25`).

The dataset uses documentation/example IP address ranges and does not represent real authentication activity.

## 3. Initial Counting Results

The analyzer successfully processed all four authentication log records.

| Measurement | Result |
|---|---:|
| Total log records | 4 |
| Successful logins | 1 |
| Failed logins | 3 |
| Failed attempts against `admin` | 1 |
| Failed attempts against `alice` | 2 |
| Failed attempts from `198.51.100.25` | 3 |

The results demonstrate that the analyzer can distinguish successful and failed authentication events and maintain separate failure counts by username and source IP address.

## 4. Detection Threshold Testing

A configurable threshold of three failed login attempts per source IP address was introduced.

### Test A: Below Threshold

**Input:** Two failed login attempts from `198.51.100.25`.

**Expected result:** No alert should be generated.

**Actual result:** No alert was generated.

**Status:** Passed.

### Test B: Threshold Reached

**Input:** Three failed login attempts from `198.51.100.25`.

**Expected result:** An alert should be generated.

**Actual result:**

`ALERT: IP address exceeded failure threshold: 198.51.100.25`

**Status:** Passed.

### Test C: Dataset Restoration

The fourth log record was restored after Test A.

**Expected result:** The analyzer should again detect three failed attempts and generate an alert.

**Actual result:** The alert was generated successfully.

**Status:** Passed.

## 5. Limitations

The current analyzer is an initial prototype and has several limitations:

- It has only been tested against a small synthetic dataset.
- It currently relies on specific log message formats and field positions.
- It uses a fixed threshold rather than a configurable detection policy.
- It does not establish whether an IP address represents a malicious actor.
- It does not yet correlate events across multiple log sources.
- It does not yet evaluate detection precision, recall, or false-positive rates.

The successful tests demonstrate basic parsing, counting, and threshold-alert functionality. They do not establish reliability across different Linux authentication log formats or real-world environments.

## 6. Conclusion

The initial authentication log analyzer successfully demonstrated basic authentication event processing.

It correctly:
- Counted successful and failed login attempts.
- Extracted usernames from the tested failed-login formats.
- Grouped failed attempts by username.
- Extracted and grouped source IP addresses.
- Generated alerts when a source IP reached the defined threshold.
- Avoided generating alerts when the threshold was not reached.

These results establish a working foundation for further development and controlled testing under Project CN-001.

Future work will focus on improving parser reliability, handling variations in authentication log formats, and evaluating detection accuracy using larger and more varied datasets.
