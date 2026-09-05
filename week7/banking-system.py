# Week 7 Lab session
# ------------------------------------------------
# Activity 1: Case study of Simple Banking System
# ------------------------------------------------

# Step 1: Define the classes

# Account class stores account details and provides basic banking functions such as deposits, withdrawals, and balance display.
class Account:
    def __init__(self, account_number, balance=0):
        # Set up account number and starting balance
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        # Add money to the account
        self.balance += amount
        print(f"${amount} deposited. New balance: ${self.balance}")

    def withdraw(self, amount):
        # Withdraw money if enough is available
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn. New balance: ${self.balance}")

    def display_balance(self):
        # Show the current balance
        print(f"Account {self.account_number} balance: ${self.balance}")


# Customer class stores customer name and account reference.
class Customer:
    def __init__(self, name, account):
        # Establish customer name and associated account
        self.name = name
        self.account = account

    def display_customer_info(self):
        # Display customer name and their account balance
        print(f"Customer Name: {self.name}")
        self.account.display_balance()


# Transaction class stores transaction details and carries out the action.
class Transaction:
    def __init__(self, account, amount, transaction_type):
        # Store the account, amount, and transaction type
        self.account = account
        self.amount = amount
        self.transaction_type = transaction_type
        # Carry out the transaction
        self.process_transaction()

    def process_transaction(self):
        # Perform the correct action based on transaction type   
        if self.transaction_type == "deposit":
            self.account.deposit(self.amount)
        elif self.transaction_type == "withdraw":
            self.account.withdraw(self.amount)
        else:
            print("Invalid transaction type!")


# Step 2: Test the functionality

# Create an account for a customer
account1 = Account(account_number=101, balance=100)
customer1 = Customer(name="Alice", account=account1)

# Display customer details
customer1.display_customer_info()

# Performing transactions
transaction1 = Transaction(account1, 50, "deposit")
transaction2 = Transaction(account1, 200, "transfer")

# Final account balance
customer1.display_customer_info()



