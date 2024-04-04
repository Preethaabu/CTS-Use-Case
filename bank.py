class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_deposit):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = {'name': name, 'balance': initial_deposit, 'transactions': []}
            print("Account created successfully!")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            self.accounts[account_number]['transactions'].append(f"Deposited ${amount}")
            print("Deposit successful. Current balance:", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount > self.accounts[account_number]['balance']:
                print("Insufficient funds!")
            else:
                self.accounts[account_number]['balance'] -= amount
                self.accounts[account_number]['transactions'].append(f"Withdrew ${amount}")
                print("Withdrawal successful. Current balance:", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist!")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            print("Current balance for account", account_number, ":", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist!")

    def check_transaction_history(self, account_number):
        if account_number in self.accounts:
            print(f"Transaction History for Account Number {account_number}:")
            for transaction in self.accounts[account_number]['transactions']:
                print(transaction)
        else:
            print("Account does not exist!")


# Example usage
bank = Bank()

# Get account details from the user
account_number = input("Enter account number: ")
name = input("Enter account holder's name: ")
initial_deposit = float(input("Enter initial deposit amount: "))

# Creating an account
bank.create_account(account_number, name, initial_deposit)

# Get deposit amount from the user
deposit_amount = float(input("Enter deposit amount: "))

# Depositing money
bank.deposit(account_number, deposit_amount)


# Get withdrawal amount from the user
withdrawal_amount = float(input("Enter withdrawal amount: "))

# Withdrawing money
bank.withdraw(account_number, withdrawal_amount)


# Displaying balance
bank.display_balance(account_number)

# Checking transaction history
bank.check_transaction_history(account_number)
