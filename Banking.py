import random

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, initial_balance):
        account_number = random.randint(100000, 999999)
        while account_number in self.accounts:
            account_number = random.randint(100000, 999999)

        self.accounts[account_number] = {"name": name, "balance": initial_balance}
        print(f"Account created successfully. Account Number: {account_number}")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            balance = self.accounts[account_number]["balance"]
            print(f"Account Balance for Account Number {account_number}: ${balance}")
        else:
            print("Invalid account number. Please enter a valid account number.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            self.accounts[account_number]["balance"] += amount
            print(f"Deposit successful. New balance: ${self.accounts[account_number]['balance']}")
        else:
            print("Invalid account number or deposit amount.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and 0 < amount <= self.accounts[account_number]["balance"]:
            self.accounts[account_number]["balance"] -= amount
            print(f"Withdrawal successful. New balance: ${self.accounts[account_number]['balance']}")
        else:
            print("Invalid account number, withdrawal amount, or insufficient funds.")

# Example usage
def banking():
    bank = Bank()

    while True:
        print("\nBanking System")
        print("1. Create Account")
        print("2. Display Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            name = input("Enter your name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(name, initial_balance)
        elif choice == "2":
            account_number = int(input("Enter account number: "))
            bank.display_balance(account_number)
        elif choice == "3":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == "4":
            account_number = int(input("Enter account number: "))
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == "5":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

banking()


