
import unittest

from security_log_analyzer import (
    process_logs,
    analyze_events
)


class TestCipherNorth(unittest.TestCase):

    def test_valid_log_records(self):
        lines = [
            "2026-11-18 08:00:00|user=alice|event=login_success|ip=192.0.2.10",
            "2026-11-18 08:01:00|user=bob|event=login_failed|ip=192.0.2.20"
        ]

        valid, invalid = process_logs_from_lines(lines)

        self.assertEqual(len(valid), 2)
        self.assertEqual(len(invalid), 0)

    def test_incorrect_field_count(self):
        lines = [
            "2026-11-18 08:00:00|user=alice|event=login_success"
        ]

        valid, invalid = process_logs_from_lines(lines)

        self.assertEqual(len(valid), 0)
        self.assertEqual(len(invalid), 1)

    def test_invalid_username_field(self):
        lines = [
            "2026-11-18 08:00:00|username=alice|event=login_success|ip=192.0.2.10"
        ]

        valid, invalid = process_logs_from_lines(lines)

        self.assertEqual(len(valid), 0)
        self.assertEqual(len(invalid), 1)

    def test_invalid_timestamp(self):
        lines = [
            "not-a-timestamp|user=alice|event=login_success|ip=192.0.2.10"
        ]

        valid, invalid = process_logs_from_lines(lines)

        self.assertEqual(len(valid), 0)
        self.assertEqual(len(invalid), 1)

    def test_invalid_ip_address(self):
        lines = [
            "2026-11-18 08:00:00|user=alice|event=login_success|ip=not-an-ip"
        ]

        valid, invalid = process_logs_from_lines(lines)

        self.assertEqual(len(valid), 0)
        self.assertEqual(len(invalid), 1)

    def test_unsupported_event(self):
        lines = [
            "2026-11-18 08:00:00|user=alice|event=unknown_event|ip=192.0.2.10"
        ]

        valid, invalid = process_logs_from_lines(lines)

        self.assertEqual(len(valid), 0)
        self.assertEqual(len(invalid), 1)

    def test_repeated_failed_logins(self):
        events = [
            make_event("alice", "login_failed", "192.0.2.10"),
            make_event("alice", "login_failed", "192.0.2.10"),
            make_event("alice", "login_failed", "192.0.2.10")
        ]

        results = analyze_events(events, [])

        self.assertEqual(
            results["failed_attempts_by_user"]["alice"],
            3
        )

        self.assertEqual(
            results["failed_attempts_by_ip"]["192.0.2.10"],
            3
        )

    def test_success_after_repeated_failures(self):
        events = [
            make_event("bob", "login_failed", "192.0.2.20"),
            make_event("bob", "login_failed", "192.0.2.20"),
            make_event("bob", "login_failed", "192.0.2.20"),
            make_event("bob", "login_success", "192.0.2.20")
        ]

        results = analyze_events(events, [])

        self.assertIn(
            "bob",
            results["successful_after_failures"]
        )

    def test_multiple_accounts_targeted_by_one_ip(self):
        events = [
            make_event("alice", "login_failed", "192.0.2.99"),
            make_event("bob", "login_failed", "192.0.2.99"),
            make_event("charlie", "login_failed", "192.0.2.99")
        ]

        results = analyze_events(events, [])

        self.assertEqual(
            len(results["accounts_targeted_by_ip"]["192.0.2.99"]),
            3
        )

    def test_blank_lines_are_ignored(self):
        lines = [
            "",
            "   ",
            "2026-11-18 08:00:00|user=alice|event=login_success|ip=192.0.2.10"
        ]

        valid, invalid = process_logs_from_lines(lines)

        self.assertEqual(len(valid), 1)
        self.assertEqual(len(invalid), 0)


def process_logs_from_lines(lines):
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        delete=False
    ) as temporary_file:

        temporary_file.write("\n".join(lines))
        temporary_path = temporary_file.name

    try:
        return process_logs(temporary_path)
    finally:
        os.unlink(temporary_path)


def make_event(username, event, ip_address):
    return {
        "timestamp": "2026-11-18 08:00:00",
        "username": username,
        "event": event,
        "ip": ip_address
    }


if __name__ == "__main__":
    unittest.main(verbosity=2)
