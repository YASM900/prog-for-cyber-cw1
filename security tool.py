from abc import ABC, abstractmethod




# creat an abstract class that defines the login and menu workflow for a security utility
class main_username(ABC):
    """Abstract security utility that defines a login and menu workflow."""

# store the correct username and password for the security utility
    def __init__(self, username: str = "admin", password: str = "P@$$word"):
        self.main_username = username
        self.main_password = password

# check if the supplied credentials match the stored ones
    @abstractmethod
    def validate_login(self, username: str, password: str) -> bool:
        """Return True when the supplied credentials match the stored ones."""
        
# count the number of failed password attempts and report the failure percentage
    @abstractmethod
    def security_event_counter(self) -> None:
        """Check a set of password attempts and report the failure percentage."""
        
# simulate a brute-force attack against a known password and report the result if the password is cracked or the maximum attempts are reached
    @abstractmethod
    def brute_force_simulator(self) -> None:
        """Simulate a brute-force attack against a known password."""
        
# authenticate a user account with limited failed attempts
    @abstractmethod
    def login_authentication(self) -> None:
        """Authenticate a second user account with limited failed attempts."""
        
# end the security tool cleanly
    @abstractmethod
    def exit_program(self) -> None:
        """End the security tool cleanly."""
        pass

# concrete class that implements the all seecurity functions 
class SecurityTool(main_username):
    """Concrete implementation of the abstract security methods."""
# verify the user login credentials 
    def validate_login(self, username: str, password: str) -> bool:
        return username == self.main_username and password == self.main_password

# track the number of failed password attempts and report the failure percentage
    def security_event_counter(self) -> None:
        correct_password = "password123"
        correct_count = 0
        incorrect_count = 0

        for i in range(1, 11):
            entered_password = input(f"enter password ({i}/10): ")
            if entered_password == correct_password:
                correct_count += 1
            else:
                incorrect_count += 1

        percentage = (incorrect_count / 10) * 100

        print("\nresults")
        print("correct password:", correct_count)
        print("incorrect password:", incorrect_count)
        print("incorrect percentage:", percentage, "%")

        if percentage > 50:
            print("try to remember your password")
# simulate a brute-force attack against a known password and report the result if the password is cracked or the maximum attempts are reached
    def brute_force_simulator(self) -> None:
        correct_password = "secret123"
        max_attempts = 5
        attempts = 0

        while attempts < max_attempts:
            guess = input("guess the password: ")
            attempts += 1

            if guess == correct_password:
                print("password cracked!")
                return
            print("incorrect guess")

        print("maximum attempts reached. account locked.")
# authenticate a user account with limited failed attempts
    def login_authentication(self) -> None:
        username = "user1"
        password = "pass123"
        failed_attempts = 0

        while failed_attempts < 3:
            enter_user = input("username: ")
            enter_pass = input("password: ")

            if enter_user == username and enter_pass == password:
                print("authentication succeeded")
                return

            failed_attempts += 1
            print("authentication failed")

        print("account id frozen for 24hrs")
# end the security tool cleanly
    def exit_program(self) -> None:
        print("thank you for using this tool")

    def show_menu(self) -> None:
        print("\n========== security menu ===============")
        print("1. security event counter")
        print("2. brute-force simulator")
        print("3. login authentication")
        print("4. exit program")
# run the security tool login and menu workflow
    def run(self) -> None:
        print("======security tool login =====")
        while True:
            username = input("enter your username: ")
            password = input("enter your password: ")

            if self.validate_login(username, password):
                print("you have entered the correct password and username!\n")
                while True:
                    self.show_menu()
                    choice = input("enter your number: ")

                    if choice == "1":
                        self.security_event_counter()
                    elif choice == "2":
                        self.brute_force_simulator()
                    elif choice == "3":
                        self.login_authentication()
                    elif choice == "4":
                        self.exit_program()
                        return
                    else:
                        print("plz press 1 to 4")
            else:
                print("wrong password plz try again!\n")

# run the security tool if this file is executed as the main program
if __name__ == "__main__":
    SecurityTool().run()