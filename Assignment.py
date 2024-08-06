class BankingDetail:
    def __init__(self):
        self.accounts = {}

    def add_account(self, acc_number, initial_balance):
        """Add a new account with initial balance"""
        if acc_number in self.accounts:
            raise ValueError("Account already exists.")
        self.accounts[acc_number] = initial_balance

    def deposit(self, acc_number, amount):
        """Deposit amount into an account"""
        if acc_number not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Deposit amount should be greater than zero.")
        self.accounts[acc_number] += amount
        print(
            f"Deposit of {amount} successful. New balance: {self.accounts[acc_number]}"
        )

    def withdraw(self, acc_number, amount):
        """Withdraw amount from an account"""
        if acc_number not in self.accounts:
            raise ValueError("Account does not exist.")
        if amount <= 0:
            raise ValueError("Withdraw amount should be greater than zero.")
        if self.accounts[acc_number] < amount:
            raise ValueError("Insufficient balance.")
        self.accounts[acc_number] -= amount
        print(
            f"Withdrawal of {amount} successful. New balance: {self.accounts[acc_number]}"
        )

    def display_balance(self, acc_number):
        """Display available balance"""
        if acc_number not in self.accounts:
            raise ValueError("Account does not exist.")
        print(f"Account Balance: {self.accounts[acc_number]}")

    def update_information(self, acc_number):
        """Update information if balance gets withdrawn"""
        if acc_number not in self.accounts:
            raise ValueError("Account does not exist.")
        print(
            f"Account {acc_number} details updated. Current Balance: {self.accounts[acc_number]}"
        )


bank = BankingDetail()

bank.add_account(1001, 5000)
bank.add_account(1002, 3000)


bank.deposit(1001, 1000)


bank.withdraw(1002, 500)


bank.display_balance(1001)


bank.update_information(1002)
