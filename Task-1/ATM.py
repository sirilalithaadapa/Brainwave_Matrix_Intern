import os
import time
from datetime import datetime, timedelta

class ATM:
    def __init__(self):
        self.users = {
            '1234': {'balance': 1000.0, 'pin': '1111', 'name': 'John Doe', 'daily_withdrawal_limit': 500.0, 'withdrawn_today': 0.0},
            '5678': {'balance': 1500.0, 'pin': '2222', 'name': 'Jane Smith', 'daily_withdrawal_limit': 500.0, 'withdrawn_today': 0.0},
        }
        self.current_user = None
        self.admin_pin = "0000"
        self.max_pin_attempts = 3
        self.daily_reset_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)

    def clear_console(self):
        """Clear the console for a cleaner interface."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def authenticate(self):
        """Authenticate user by card number and PIN."""
        card_number = input("Insert card (Enter card number): ")
        if card_number in self.users:
            tries = 0
            while tries < self.max_pin_attempts:
                entered_pin = input("Enter your 4-digit PIN: ")
                if entered_pin == self.users[card_number]['pin']:
                    print(f"Welcome, {self.users[card_number]['name']}!")
                    self.current_user = self.users[card_number]
                    return True
                elif entered_pin == self.admin_pin:
                    self.admin_panel()
                    return False
                else:
                    tries += 1
                    print(f"Incorrect PIN. {self.max_pin_attempts - tries} attempts left.")
            print("Too many incorrect attempts. Account is locked.")
            return False
        else:
            print("Invalid card number.")
            return False

    def check_daily_reset(self):
        """Reset daily withdrawal limit if the day has changed."""
        if datetime.now() >= self.daily_reset_time:
            self.daily_reset_time += timedelta(days=1)
            for user in self.users.values():
                user['withdrawn_today'] = 0.0

    def check_balance(self):
        """Check account balance."""
        print(f"Your current balance is: ${self.current_user['balance']:.2f}")

    def deposit(self):
        """Deposit money into the account."""
        while True:
            try:
                amount = float(input("Enter amount to deposit: $"))
                if amount > 0:
                    self.current_user['balance'] += amount
                    print(f"${amount:.2f} deposited successfully.")
                    break
                else:
                    print("Enter a positive amount.")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

    def withdraw(self):
        """Withdraw money from the account, enforcing the daily limit."""
        self.check_daily_reset()
        while True:
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount > 0:
                    if self.current_user['withdrawn_today'] + amount > self.current_user['daily_withdrawal_limit']:
                        print(f"Exceeded daily withdrawal limit of ${self.current_user['daily_withdrawal_limit']:.2f}.")
                    elif amount <= self.current_user['balance']:
                        self.current_user['balance'] -= amount
                        self.current_user['withdrawn_today'] += amount
                        print(f"${amount:.2f} withdrawn successfully.")
                        break
                    else:
                        print("Insufficient funds.")
                else:
                    print("Enter a positive amount.")
            except ValueError:
                print("Invalid amount. Please enter a valid number.")

    def show_transaction_options(self):
        """Show transaction options for the user."""
        while True:
            print("\n1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == '1':
                self.clear_console()
                self.check_balance()
            elif choice == '2':
                self.clear_console()
                self.deposit()
            elif choice == '3':
                self.clear_console()
                self.withdraw()
            elif choice == '4':
                print("Thank you for using our ATM! Please remove your card.")
                time.sleep(1)
                self.clear_console()
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def admin_panel(self):
        """Admin panel to view all users or reset PINs."""
        while True:
            print("\n--- Admin Panel ---")
            print("1. View User Data")
            print("2. Reset User PIN")
            print("3. Exit Admin Panel")

            choice = input("Choose an option (1-3): ")

            if choice == '1':
                for card_number, user_data in self.users.items():
                    print(f"Card: {card_number} | Name: {user_data['name']} | Balance: ${user_data['balance']:.2f}")
            elif choice == '2':
                card_number = input("Enter card number to reset PIN: ")
                if card_number in self.users:
                    new_pin = input(f"Enter new PIN for {self.users[card_number]['name']}: ")
                    if new_pin.isdigit() and len(new_pin) == 4:
                        self.users[card_number]['pin'] = new_pin
                        print(f"PIN reset successfully for {self.users[card_number]['name']}.")
                    else:
                        print("Invalid PIN. Must be a 4-digit number.")
                else:
                    print("Card number not found.")
            elif choice == '3':
                print("Exiting Admin Panel.")
                break
            else:
                print("Invalid choice. Please choose a valid option.")

    def start(self):
        """Start ATM interface."""
        self.clear_console()
        print("Welcome to the ATM")

        while True:
            if self.authenticate():
                self.show_transaction_options()
            else:
                print("Authentication failed. Restarting ATM system.")
                time.sleep(2)
                self.clear_console()

if __name__ == "__main__":
    atm = ATM()
    atm.start()
