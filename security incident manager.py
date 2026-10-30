
# Create a dictionary containing a username,
#    IP address, event type, and risk level
incident = {
    "username": "john_doe",
    "ip_address": "192.168.1.100",
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