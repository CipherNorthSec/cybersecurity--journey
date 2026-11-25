
from datetime import datetime
import ipaddress
import sys


# ==================================================
# CIPHERNORTH SECURITY LOG ANALYZER
# ==================================================

DEFAULT_LOG_FILE = "malformed_logs_test.txt"

FAILED_LOGIN_THRESHOLD = 3
TARGETED_ACCOUNT_THRESHOLD = 3


# ==================================================
# FUNCTION 1: PROCESS AND VALIDATE LOGS
# ==================================================

def process_logs(log_file_path):

    valid_events = []
    invalid_records = []

    try:
        with open(log_file_path, "r") as log_file:

            for line_number, line in enumerate(log_file, start=1):

                if not line.strip():
                    continue

                fields = line.strip().split("|")

                if len(fields) != 4:
                    invalid_records.append(
                        (line_number, "Incorrect number of fields")
                    )
                    continue

                timestamp_field = fields[0].strip()
                username_field = fields[1].strip()
                event_field = fields[2].strip()
                ip_field = fields[3].strip()

                if not username_field.startswith("user="):
                    invalid_records.append(
                        (line_number, "Invalid username field")
                    )
                    continue

                if not event_field.startswith("event="):
                    invalid_records.append(
                        (line_number, "Invalid event field")
                    )
                    continue

                if not ip_field.startswith("ip="):
                    invalid_records.append(
                        (line_number, "Invalid IP field")
                    )
                    continue

                timestamp = timestamp_field
                username = username_field.split("=", 1)[1].strip()
                event = event_field.split("=", 1)[1].strip()
                ip_address = ip_field.split("=", 1)[1].strip()

                if not timestamp or not username or not event or not ip_address:
                    invalid_records.append(
                        (line_number, "Empty field")
                    )
                    continue

                try:
                    datetime.strptime(
                        timestamp,
                        "%Y-%m-%d %H:%M:%S"
                    )
                except ValueError:
                    invalid_records.append(
                        (line_number, "Invalid timestamp")
                    )
                    continue

                if event not in ("login_success", "login_failed"):
                    invalid_records.append(
                        (line_number, "Unsupported event type")
                    )
                    continue

                try:
                    ipaddress.ip_address(ip_address)
                except ValueError:
                    invalid_records.append(
                        (line_number, "Invalid IP address")
                    )
                    continue

                valid_events.append({
                    "timestamp": timestamp,
                    "username": username,
                    "event": event,
                    "ip": ip_address
                })

    except FileNotFoundError:
        raise FileNotFoundError(
            f"Log file '{log_file_path}' was not found."
        )

    return valid_events, invalid_records


# ==================================================
# FUNCTION 2: ANALYZE AUTHENTICATION EVENTS
# ==================================================

def analyze_events(valid_events, invalid_records):

    successful_logins = 0
    failed_logins = 0

    failed_attempts_by_user = {}
    failed_attempts_by_ip = {}
    successful_after_failures = {}
    accounts_targeted_by_ip = {}

    for record in valid_events:

        username = record["username"]
        event = record["event"]
        ip_address = record["ip"]
        timestamp = record["timestamp"]

        if event == "login_success":

            successful_logins += 1

            previous_failures = failed_attempts_by_user.get(
                username, 0
            )

            if previous_failures >= FAILED_LOGIN_THRESHOLD:

                successful_after_failures[username] = {
                    "timestamp": timestamp,
                    "ip": ip_address,
                    "failures": previous_failures
                }

        elif event == "login_failed":

            failed_logins += 1

            failed_attempts_by_user[username] = (
                failed_attempts_by_user.get(username, 0) + 1
            )

            failed_attempts_by_ip[ip_address] = (
                failed_attempts_by_ip.get(ip_address, 0) + 1
            )

            if ip_address not in accounts_targeted_by_ip:
                accounts_targeted_by_ip[ip_address] = set()

            accounts_targeted_by_ip[ip_address].add(username)

    return {
        "total_events": len(valid_events),
        "successful_logins": successful_logins,
        "failed_logins": failed_logins,
        "invalid_records": len(invalid_records),
        "failed_attempts_by_user": failed_attempts_by_user,
        "failed_attempts_by_ip": failed_attempts_by_ip,
        "successful_after_failures": successful_after_failures,
        "accounts_targeted_by_ip": accounts_targeted_by_ip,
        "invalid_record_details": invalid_records
    }


# ==================================================
# FUNCTION 3: GENERATE INVESTIGATION REPORT
# ==================================================

def generate_report(results):

    print("CipherNorth Security Log Analyzer")
    print("=" * 40)
    print("Authentication Log Investigation")
    print("=" * 40)

    print("\nLOG VALIDATION")
    print("-" * 40)

    for line_number, reason in results["invalid_record_details"]:
        print(
            f"INVALID RECORD: Line {line_number} - {reason}."
        )

    print("\nINVESTIGATION SUMMARY")
    print("-" * 40)

    print(f"Total valid events: {results['total_events']}")
    print(f"Successful logins: {results['successful_logins']}")
    print(f"Failed logins: {results['failed_logins']}")
    print(f"Invalid records: {results['invalid_records']}")

    # ----------------------------------------------
    # DETECTION RULE 001
    # ----------------------------------------------

    print("\nDETECTION RULE 001: REPEATED FAILED LOGINS BY USER")
    print("-" * 40)

    suspicious_accounts = 0

    for username, attempts in results["failed_attempts_by_user"].items():

        if attempts >= FAILED_LOGIN_THRESHOLD:

            print(
                f"WARNING: {username} had {attempts} "
                "failed attempts!"
            )

            suspicious_accounts += 1

    if suspicious_accounts == 0:
        print("No suspicious accounts detected.")

    print(f"Accounts flagged: {suspicious_accounts}")

    # ----------------------------------------------
    # DETECTION RULE 002
    # ----------------------------------------------

    print("\nDETECTION RULE 002: REPEATED FAILED LOGINS BY IP")
    print("-" * 40)

    suspicious_ips = 0

    for ip_address, attempts in results["failed_attempts_by_ip"].items():

        if attempts >= FAILED_LOGIN_THRESHOLD:

            print(
                f"WARNING: {ip_address} generated {attempts} "
                "failed attempts!"
            )

            suspicious_ips += 1

    if suspicious_ips == 0:
        print("No suspicious IP addresses detected.")

    print(f"IP addresses flagged: {suspicious_ips}")

    # ----------------------------------------------
    # DETECTION RULE 003
    # ----------------------------------------------

    print("\nDETECTION RULE 003: SUCCESS AFTER REPEATED FAILURES")
    print("-" * 40)

    for username, details in results["successful_after_failures"].items():

        print(
            f"WARNING: {username} logged in "
            "after repeated failures!"
        )

        print(f"Failed attempts: {details['failures']}")
        print(f"Successful login time: {details['timestamp']}")
        print(f"Successful login IP: {details['ip']}")

    if not results["successful_after_failures"]:
        print("No matching activity detected.")

    print(
        f"Accounts flagged: "
        f"{len(results['successful_after_failures'])}"
    )

    # ----------------------------------------------
    # DETECTION RULE 004
    # ----------------------------------------------

    print("\nDETECTION RULE 004: MULTIPLE ACCOUNTS TARGETED BY ONE IP")
    print("-" * 40)

    password_spraying_alerts = 0

    for ip_address, usernames in results["accounts_targeted_by_ip"].items():

        if len(usernames) >= TARGETED_ACCOUNT_THRESHOLD:

            print(
                f"WARNING: {ip_address} targeted "
                f"{len(usernames)} accounts!"
            )

            print(f"Accounts: {', '.join(sorted(usernames))}")

            password_spraying_alerts += 1

    if password_spraying_alerts == 0:
        print(
            "No IP addresses targeted enough accounts "
            "to trigger an alert."
        )

    print(f"IP addresses flagged: {password_spraying_alerts}")

    print("\n" + "=" * 40)
    print("CIPHERNORTH INVESTIGATION COMPLETE")
    print("=" * 40)


# ==================================================
# FUNCTION 4: RUN THE INVESTIGATION
# ==================================================

def run_investigation(log_file_path):

    valid_events, invalid_records = process_logs(log_file_path)

    results = analyze_events(valid_events, invalid_records)

    generate_report(results)

    return results


# ==================================================
# PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":

    log_file = (
        sys.argv[1]
        if len(sys.argv) > 1
        else DEFAULT_LOG_FILE
    )

    try:
        run_investigation(log_file)

    except FileNotFoundError as error:
        print(f"ERROR: {error}")
        sys.exit(1)
