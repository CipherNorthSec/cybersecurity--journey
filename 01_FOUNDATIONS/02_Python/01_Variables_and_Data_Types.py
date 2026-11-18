# Lesson 01: Variables and Data Types

# Variables store information that can be used later.

username = "CipherNorth"
age = 29
username = "CipherNorth"
age = 29

height = 5.75
is_learning_python = True
temperature = 21.5

print(username)
print(age)

print(type(username))
print(type(age))
print(type(username))
print(type(age))

print(type(height))
print(type(is_learning_python))
print(type(temperature))
print(f"My username is {username} and I am {age} years old.")
favorite_language = input("What is your favorite programming language? ")
print(f"Your favorite programming language is {favorite_language}.")
user_age = int(input("How old are you? "))
if user_age >= 18:
    print("You are an adult.")
else:
    print("You are under 18.")
print(user_age + 1)
user_height = float(input("Enter your height in metres: "))
print(f"Your height is {user_height} metres.")
print(29 == 29)
print(29 != 18)
print(29 > 18)
print(16 < 18)
count = 1

while count <= 5:
    print(count)
    count += 2
    for number in range(1, 6):
        print(number)
usernames = ["alice", "bob", "charlie", "diana", "eve"]

print(usernames)

print(usernames)
print(usernames[0])
print(usernames[2])
print(usernames[4])
usernames[1] = "frank"

print(usernames)
usernames.append("grace")

print(usernames)
usernames.remove("charlie")

print(usernames)   
print(len(usernames)) 
for username in usernames:
    print(username)   
for username in usernames:
    if username == "frank":
        print("Account found!")
print("frank" in usernames)
print("charlie" in usernames)
user_account = {
    "username": "frank",
    "ip_address": "192.0.2.15",
    "status": "active"
}

print(user_account)
print(user_account["username"])
print(user_account["ip_address"])
print(user_account["status"])
user_account["status"] = "disabled"

print(user_account)
user_account["last_login"] = "2026-11-16"

print(user_account)
del user_account["ip_address"]

print(user_account)
print(user_account.keys())
print(user_account.values())
print(user_account.items())
user_accounts = {
    "alice": {
        "ip_address": "192.0.2.10",
        "status": "active"
    },
    "frank": {
        "ip_address": "192.0.2.15",
        "status": "disabled"
    },
    "diana": {
        "ip_address": "192.0.2.20",
        "status": "active"
    }
}


print(user_accounts)
print(user_accounts["frank"])
print(user_accounts["frank"]["status"])

user_accounts["frank"]["status"] = "active"

print(user_accounts["frank"])

for username, details in user_accounts.items():
    if details["status"] == "active":
        print(username)

print("\n--- FRANK'S ACCOUNT INVESTIGATION ---")
print("Username:", "frank")
print("Account details:", user_accounts["frank"])
print("Account status:", user_accounts["frank"]["status"])
print("IP address:", user_accounts["frank"]["ip_address"])

print("\n--- FRANK'S AUDIT LOG ---")
from datetime import datetime
audit_log = [
    {
        "event": "Account created",
        "timestamp": "2026-11-10 09:00:00",
        "username": "frank",
        "status": "active"
    }
]
audit_log.append({
    "event": "Account disabled",
    "timestamp": "2026-11-10 09:15:00",
    "username": "frank",
    "status": "disabled"
})
audit_log.append({
    "event": "IP address removed",
   "timestamp": "2026-11-10 09:20:00", 
    "username": "frank",
    "ip_address": None
})

print(audit_log)

audit_log.append({
    "event": "Account restored",
  "timestamp": "2026-11-10 09:45:00",  
    "username": "frank",
    "status": "active",
    "ip_address": "192.0.2.15"
})
timeline = sorted(
    audit_log,
    key=lambda event: datetime.strptime(
        event["timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )
)

print()
print("FR-002: ACCOUNT ACTIVITY TIMELINE")
print("================================")
for event in timeline:
    print("Timestamp:", event["timestamp"])
    print("Event:", event["event"])
    print("Account:", event["username"])

    if "ip_address" in event:
        print("IP address:", event["ip_address"])
    else:
        print("IP address: Not recorded")

    print("--------------------------------")

print(audit_log)

print("\n--- INVESTIGATION RESULTS ---")

for event in audit_log:
    print("Event:", event["event"])
    print("Username:", event["username"])
    print("---")

expected_fields = {
    "Account created": [],
    "Account disabled": [],
    "IP address removed": ["ip_address"],
    "Account restored": ["ip_address"]
}  
print("\n--- MISSING IP INVESTIGATION ---")

for event in audit_log:
    if "ip_address" in expected_fields.get(event["event"], []) and event.get("ip_address") is None:  
        print("Missing IP detected!")
        print("Username:", event["username"])
        print("Event:", event["event"])   

print("\n===================================")
print("       INCIDENT REPORT FR-001")
print("  Frank's Disappearing IP Address")
print("===================================")
print("\n1. INCIDENT SUMMARY")
print("Account under investigation: frank")
print("Recorded events:", len(audit_log))
print("Investigation type: Account activity review")


missing_ip_count = 0
explicit_removal_count = 0

for event in audit_log:
    expected = expected_fields.get(event["event"], [])

    if "ip_address" in expected and event.get("ip_address") is None:
        missing_ip_count += 1

for event in audit_log:
    if event["event"] == "IP address removed":
        explicit_removal_count += 1

print("Explicit IP removal events:", explicit_removal_count)

for event in audit_log:
    expected = expected_fields.get(event["event"], [])

    if "ip_address" in expected and event.get("ip_address") is None:
        print("Missing expected IP address for:", event["username"])
        print("Event:", event["event"])
print()
print("2. FORENSIC FINDINGS")
print("--------------------")
for event in audit_log:
    expected = expected_fields.get(event["event"], [])

    if "ip_address" in expected and event.get("ip_address") is None:
        print("Finding: Missing expected IP address")
        print("Account:", event["username"])
    if "ip_address" in event:
        print("IP address:", event["ip_address"])
    else:
        print("IP address: Not recorded")    
        print("Event:", event["event"])
        print("Recorded IP address:", event.get("ip_address"))
        print("Assessment: The expected IP address was not recorded.")
        print()
print("Missing IP events:", missing_ip_count)
if explicit_removal_count == 0:
    print("No explicit IP removal events were recorded.")
elif explicit_removal_count == 1:
    print("One explicit IP removal event was recorded.")
else:
    print(f"{explicit_removal_count} explicit IP removal events were recorded.")
if missing_ip_count == 0:
    print("No missing expected IP addresses were identified.")
elif missing_ip_count == 1:
    print("One expected IP address was missing.")
else:
    print(f"{missing_ip_count} expected IP addresses were missing.")  
print()
print("3. INVESTIGATION LIMITATIONS")
print("----------------------------")
print("The audit log does not identify who performed the IP removal.")
print("The available records do not establish why the IP address was removed.")
print("The missing IP address limits attribution and further verification.")
print()
print("4. INVESTIGATION CONCLUSION")
print("---------------------------")

if explicit_removal_count > 0:
    print("An IP-removal event was recorded in the audit log.")
else:
    print("No IP-removal event was recorded in the audit log.")

if missing_ip_count > 0:
    print("At least one expected IP address was missing.")
else:
    print("No missing expected IP addresses were identified.")

print("The available audit records do not identify the responsible actor.")
print("Further evidence would be required to establish attribution or intent.")