from pathlib import Path

log_file = Path(__file__).parent / "authentication_sample.log"

with log_file.open("r", encoding="utf-8") as file:
    log_entries = file.readlines()

successful_logins = 0
failed_logins = 0
failed_users = []
failed_attempts_by_user = {}
failed_attempts_by_ip = {}
ip_failure_threshold = 3

print("Total log entries:", len(log_entries))

for entry in log_entries:
    if "Accepted" in entry:
        successful_logins += 1

    elif "Failed" in entry:
        failed_logins += 1
        failed_users.append(entry)

        parts = entry.split()

        if "invalid" in parts:
            username = parts[8]
            ip_address = parts[10]
        else:
            username = parts[6]
            ip_address = parts[8]     
        if username in failed_attempts_by_user:
            failed_attempts_by_user[username] += 1
        else:
            failed_attempts_by_user[username] = 1
        if ip_address in failed_attempts_by_ip:
            failed_attempts_by_ip[ip_address] += 1
        else:
            failed_attempts_by_ip[ip_address] = 1   

        print("Failed username:", username)
        print("Examining failed record:", entry.strip())

    print(entry)

print("Successful logins:", successful_logins)
print("Failed logins:", failed_logins)
print("Failed login records:", failed_users)
print("Failed attempts by username:", failed_attempts_by_user)
print("Failed attempts by IP:", failed_attempts_by_ip)
for ip_address, attempts in failed_attempts_by_ip.items():
    if attempts >= ip_failure_threshold:
        print("ALERT: IP address exceeded failure threshold:", ip_address)
