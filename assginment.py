# Shopping Cart Question

# ————————————————

# Create a Python application for below functionalities.

# a. Items — to store and access the list of items.

# b. Add functionality

# c. Remove Functionality.

# e. View All items.


# Apply using Object Oriented Programming.

# Handle the Exceptions appropriately.

# Make it a Dynamic Application.


class Duplicate(Exception):
    pass


class NotInCart(Exception):
    pass


class Items:
    def __init__(self):
        self.items_cart = []

        try:
            number = int(input("Number of items: "))
            for i in range(number):
                add = input(f"Item number {i+1}: ")
                if add in self.items_cart:
                    raise Duplicate(f"{add} is a duplicate value")
                self.items_cart.append(add)
        except Duplicate as e:
            print(f"Duplicate Value: {e}")

    def add_functionality(self):
        try:
            new_cart = input("Add to cart: ")
            if new_cart in self.items_cart:
                raise Duplicate(f"{new_cart} is a duplicate value")
            self.items_cart.append(new_cart)
            print(f"{new_cart} added to cart successfully.")
        except Duplicate as e:
            print(f"Duplicate Value: {e}")

    def remove_functionality(self):
        try:
            delete = input("Delete item: ")
            if delete not in self.items_cart:
                raise NotInCart(f"{delete} is not in the cart")
            self.items_cart.remove(delete)
            print(f"{delete} removed from cart successfully.")
        except NotInCart as e:
            print(f"Not in Cart: {e}")

    def view_items(self):
        if self.items_cart:
            print("Items in Cart:")
            for item in self.items_cart:
                print(item)
        else:
            print("No items in cart.")


def main():
    try:
        cart = Items()
        while True:
            print("1. Add")
            print("2. Remove")
            print("3. View")

            choice = input("Enter your choice: ")

            if choice == "1":
                cart.add_functionality()
            elif choice == "2":
                cart.remove_functionality()
            elif choice == "3":
                cart.view_items()
            else:
                print("Invalid choice. Please enter a number from 1 to 3.")

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()


# 2. Bank Application

# Create a python application for Banking Sector which includes below details.

# a. Account Numbers

# b. Deposit

# c. Withdraw.

# d. Available Balance.

# e. Update the Information if the Balance gets withdrawn with details.

# Apply using Object Oriented Programming.

# Handle the Exceptions appropriately.


# Make it a Dynamic Application.
class BankAccount:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number, initial_deposit):
        if acc_number in self.accounts:
            raise ValueError(f"Account {acc_number} already exists!")
        if initial_deposit < 0:
            raise ValueError("Initial deposit must be non-negative.")

        self.accounts[acc_number] = initial_deposit
        print(f"Account {acc_number} created with initial deposit {initial_deposit}")

    def deposit(self, acc_number, amount):
        if acc_number not in self.accounts:
            raise ValueError(f"Account {acc_number} does not exist!")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.accounts[acc_number] += amount
        print(
            f"Deposited {amount} into account {acc_number}. New balance: {self.accounts[acc_number]}"
        )

    def withdraw(self, acc_number, amount):
        if acc_number not in self.accounts:
            raise ValueError(f"Account {acc_number} does not exist!")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.accounts[acc_number]:
            raise ValueError("Insufficient balance.")

        self.accounts[acc_number] -= amount
        print(
            f"Withdrew {amount} from account {acc_number}. New balance: {self.accounts[acc_number]}"
        )

    def display_balance(self, acc_number):
        if acc_number not in self.accounts:
            raise ValueError(f"Account {acc_number} does not exist!")

        print(f"Balance in account {acc_number}: {self.accounts[acc_number]}")

    def update_account_info(self, acc_number):
        if acc_number not in self.accounts:
            raise ValueError(f"Account {acc_number} does not exist!")

        print(
            f"Account {acc_number} details updated. Current balance: {self.accounts[acc_number]}"
        )

    def show_all_accounts(self):
        print("All Accounts:")
        for acc_number, balance in self.accounts.items():
            print(f"Account Number: {acc_number}, Balance: {balance}")


bank = BankAccount()

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Update Account Info")
    print("6. Show All Accounts")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        try:
            acc_number = int(input("Enter Account Number: "))
            initial_deposit = float(input("Enter Initial Deposit: "))
            bank.create_account(acc_number, initial_deposit)
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "2":
        try:
            acc_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Deposit Amount: "))
            bank.deposit(acc_number, amount)
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "3":
        try:
            acc_number = int(input("Enter Account Number: "))
            amount = float(input("Enter Withdrawal Amount: "))
            bank.withdraw(acc_number, amount)
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "4":
        try:
            acc_number = int(input("Enter Account Number: "))
            bank.display_balance(acc_number)
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "5":
        try:
            acc_number = int(input("Enter Account Number: "))
            bank.update_account_info(acc_number)
        except ValueError as e:
            print(f"Error: {e}")

    elif choice == "6":
        bank.show_all_accounts()

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
