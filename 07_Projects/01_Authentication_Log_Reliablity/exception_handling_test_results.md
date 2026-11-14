# Exception Handling and Timestamp Validation — Test Results

## 1. Purpose

This experiment tests whether a Python script can distinguish between:

- Timestamps containing timezone information.
- Timestamps missing timezone information.
- Invalid timestamps that cannot be parsed.

The experiment supports the Authentication Log Reliability and Detection Research project.

## 2. Test Dataset

| Test case | Timestamp | Expected classification |
|---|---|---|
| 1 | `2026-11-12T23:34:14.660923-05:00` | Timezone-aware |
| 2 | `2026-11-13T04:40:00` | Missing timezone |
| 3 | `not-a-real-timestamp` | Invalid |

## 3. Results

| Classification | Expected count | Actual count |
|---|---:|---:|
| Timezone-aware timestamps | 1 | 1 |
| Missing timezone | 1 | 1 |
| Invalid timestamps | 1 | 1 |

**Overall result:** All three test cases were classified correctly.

## 4. Exception Handling

The script successfully caught the invalid timestamp and recorded the Python error:

`Invalid isoformat string: 'not-a-real-timestamp'`

The script continued processing instead of terminating when it encountered the invalid input.

## 5. Observations

- Python successfully parsed the timezone-aware timestamp.
- Python also parsed the timestamp without timezone information, but the script identified it as missing timezone metadata.
- The malformed timestamp raised a `ValueError`.
- The exception handler captured the error and allowed the remaining processing and summary counts to complete.

## 6. Limitations

This experiment uses only three controlled test cases.

It does not establish whether timestamps are authentic, whether their recorded times are accurate, or whether an authentication event actually occurred.

A timezone-aware timestamp is not automatically trustworthy. Further testing is needed to assess timestamp normalization, event ordering, and authentication-log reliability.

## 7. Conclusion

The exception-handling test successfully distinguished timezone-aware, timezone-naive, and invalid timestamps.

This provides a foundation for further testing of timestamp consistency and event reconstruction in authentication logs.