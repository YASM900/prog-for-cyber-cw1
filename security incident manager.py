
# Get user input
username = input("Enter username: ")
ip_address = input("Enter IP address: ")

# Check IP address
parts = ip_address.split(".")

if len(parts) != 4:
    print("Invalid IP")
else:
    valid = True

    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            valid = False

    if valid:

        # Create dictionary
        incident = {
            "username": username,
            "ip_address": ip_address,
            "event_type": "Failed Login",
            "risk_level": "High"
        }

        # Display the username and IP address
        print("Username:", incident["username"])
        print("IP Address:", incident["ip_address"])

        # Add a new field called status
        incident["status"] = "Under Investigation"

        # Update the risk level
        incident["risk_level"] = "Critical"

        # Remove one field from the dictionary
        del incident["event_type"]

        # Display all remaining keys and values
        print("\nRemaining Keys and Values:")
        for key, value in incident.items():
            print(key, ":", value)

        # Display the total number of key-value pairs
        print("\nTotal Number of Key-Value Pairs:", len(incident))

    else:
        print("Invalid IP")
