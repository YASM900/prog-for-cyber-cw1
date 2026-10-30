import random
import string

# checks if the password meets the security requirements
def validate_password(password):
    """
    checks whether a password:
    is at least 8 characters long
    contains at least one uppercase letter
    contains at least one digit
    contains at least one special character
    """
    # password must be at least 8 characters long
    if len(password) < 8:
        return False
    has_uppercase = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    return has_uppercase and has_digit and has_special

# checks whether the ip address follows the correct format and is valid
def validate_ip(ip_address):
    """
    checks whether an IP address is valid
    contains exactly 4 octets separated by dots
    uses three dots
    each octet is a number between 0 and 255
    """
    # check if the IP address contains exactly three dots
    parts = ip_address.split('.')

# check if the IP address has exactly 4 parts
    if len(parts) != 4:
        return False

# check each part of the IP address
    for part in parts:
        # each part of the IP address must contain only numbers
        if not part.isdigit():
            return False

# convert the part to an integer
        num = int(part)

        if num < 0 or num > 255:
            return False    

    return True
# generate a strong password suggestion
def generate_strong_password():
    """
    Generates a strong password:
    - Random length between 10 and 16 characters
    - Includes uppercase, lowercase, digits, and symbols
    """
    length = random.randint(10, 16)

    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    symbol = random.choice("!@#$%&?")

    remaining = ''.join(
        random.choice(
            string.ascii_letters +
            string.digits +
            "!@#$%&?"
        )
        for _ in range(length - 4)
    )

    password = uppercase + lowercase + digit + symbol + remaining

    # Shuffle characters to make the password more random
    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)
 