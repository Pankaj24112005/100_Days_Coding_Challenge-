# Day 10: Encapsulation & Instance Methods in Python

class BankAccount:
    def __init__(self, account_holder, balance):
        # Public attribute
        self.account_holder = account_holder
        
        # Private attribute (encapsulation)
        self.__balance = balance

    # Instance method to get balance (getter)
    def get_balance(self):
        return self.__balance

    # Instance method to deposit money (setter-like behavior)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    # Instance method to withdraw money
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    # Instance method to display account details
    def display_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ₹{self.__balance}")


# Creating object of the class
account = BankAccount("Pankaj", 5000)

# Accessing instance methods
account.display_details()
account.deposit(2000)
account.withdraw(1000)

# Accessing balance using getter
print("Final Balance:", account.get_balance())

# Trying to access private variable directly (will cause error if uncommented)
# print(account.__balance)
