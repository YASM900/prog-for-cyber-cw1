# imports the security_tools module 
import security_tools

# ask the user to enter a password 
password = input("Enter a password: ")

# ask the user to enter a an ip address
ip_address = input("Enter an IP address: ")

# cheaks if the password meets the security requirements
if security_tools.validate_password(password):
    print("Password is strong")
else:
    print("Password is weak")

# generate a strong password suggestion if the password is weak
    strong_password = security_tools.generate_strong_password()
    print(f"Suggested strong password: {strong_password}")

# checks if the ip address is valid
    if security_tools.validate_ip(ip_address):
        print("IP address is valid")
    else:
        print("IP address is invalid")  

# display an example of a strong password
print("\n example of a strong password: ")
print(security_tools.generate_strong_password())