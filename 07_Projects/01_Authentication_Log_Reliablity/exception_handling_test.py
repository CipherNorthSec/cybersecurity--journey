from datetime import datetime, timezone

timestamps = [
    "2026-11-12T23:34:14.660923-05:00",
    "2026-11-13T04:40:00",
    "not-a-real-timestamp",
]

timezone_aware_count = 0
invalid_count = 0
missing_timezone_count = 0
errors_found = []

for timestamp in timestamps:
    try:
        parsed_timestamp = datetime.fromisoformat(timestamp)

        if parsed_timestamp.tzinfo is None:
            print("Warning: Timestamp has no timezone information:", timestamp)
            missing_timezone_count += 1
        else:
            timezone_aware_count += 1

        print("Parsed timestamp:", parsed_timestamp)

    except ValueError as errors:
        invalid_count += 1
        print("Invalid timestamp detected:", timestamp)
        print("Reason:", errors)
        errors_found.append((timestamp, str(errors)))

print("Timezone-aware timestamps:", timezone_aware_count)
print("Invalid timestamps:", invalid_count)
print("Missing timezone:", missing_timezone_count)
print("Error report:", errors_found)