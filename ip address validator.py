# to cheack if an ip address is valid 
def validate_ip(ip):

    # The ip must contain dots 
    if "." not in ip:
        return False

# split the ip address into sections
    parts = ip.split(".")

# it cheacks if the ip address have exacly 4 part 
    if len(parts) != 4:
        return False

# check each part of the uip address 
    for part in parts:
        #each part of the ip must contain only numbers 
        if not part.isdigit():
            return False
# convert the part to an integer 
        num = int(part)
# the number must be between 0 and 255 if it pass thos number it faile
        if num < 0 or num > 255:
            return False
# if all the cecks are true then the ip is valid 
    return True

 # ask the user to enter a ip address 
ip = input("Enter an IP address: ")
# dosplay the validation result 
if validate_ip(ip):
    print("Valid IP address")
else:
    print("Invalid IP address")
