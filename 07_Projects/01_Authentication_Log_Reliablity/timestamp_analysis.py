from datetime import datetime, timezone
timestamp = "2026-11-12T23:34:14.660923-05:00"
timestamp_2 = "2026-11-13T04:30:00+00:00"
parsed_timestamp_2 = datetime.fromisoformat(timestamp_2)
utc_timestamp_2 = parsed_timestamp_2.astimezone(timezone.utc)

parsed_timestamp = datetime.fromisoformat(timestamp)
time_difference = abs((parsed_timestamp_2 - parsed_timestamp).total_seconds())
print("Original timestamp:", timestamp)
print("Parsed timestamp:", parsed_timestamp)
print("UTC timestamp:", parsed_timestamp.astimezone(timezone.utc))
print("Second UTC timestamp:", utc_timestamp_2)
if parsed_timestamp < parsed_timestamp_2:
    print("The original event happened first.")
elif parsed_timestamp == parsed_timestamp_2:
    print("Both events happened at the same time.")
else:
    print("The second event happened first.")
print("Time difference in seconds:", time_difference)