import random
import socket
from datetime import datetime

# the correct username and password for the security event logger
correct_username = "admin"
correct_password = "Password123!"

# get the local ip address of the pc your on 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip_address = s.getsockname()[0]
s.close()

# display the security event log heading 
print("security event log ")
print("-" * 18)

# keep asking for the username and password until the correct ones are entered
while True:
    # ask the user to enter the username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

# generate a random event id and get the current timestamp for the log
    event_id = random.randint(1000, 9999)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# check if the entered username and password match the correct ones
    if username == correct_username and password == correct_password:
        event = "suscessful login"

# display yhe log information for the successful login event
        print("event id:", event_id)
        print("username:", username)
        print("ip address:", ip_address)
        print("timestamp:", timestamp)
        print()

# display the access granted message when the correct username and password are entered
        print("access granted")
        break

    else:
        event = "failed login attempt"
# display the log information for the failed login attempt event
        print("event id:", event_id)
        print("username:", username)
        print("ip address:", ip_address)
        print("timestamp:", timestamp)
        print()
# display the access denied message and security alert for the failed login attempt
        print("access denied")
        print("security alert: failed login attempt detected from ip address", ip_address)
        print()

