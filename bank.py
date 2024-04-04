class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_deposit):
        if account_number in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[account_number] = {'name': name, 'balance': initial_deposit}
            print("Account created successfully!")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number]['balance'] += amount
            print("Deposit successful. Current balance:", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist!")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount > self.accounts[account_number]['balance']:
                print("Insufficient funds!")
            else:
                self.accounts[account_number]['balance'] -= amount
                print("Withdrawal successful. Current balance:", self.accounts[account_number]['balance'])
        else:
            print("Account does not exist!")

    def display_balance(self, account_number):
        if account_number in self.accounts:
            print("Current balance:", self.accounts[account_number]['balance'])
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

#message
