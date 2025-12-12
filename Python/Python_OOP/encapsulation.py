# encapsulation
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited: {amount}. New balance: {self.__balance}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew: {amount}. New balance: {self.__balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

    def get_balance(self):
        return f"Account balance for {self.__account_holder}: {self.__balance}"


# Demonstration of Encapsulation
account = BankAccount("John Doe", 1000)
print(account.get_balance())  # Accessing balance via public method
print(account.deposit(500))   # Depositing money
print(account.withdraw(200))  # Withdrawing money
# Accessing balance via public method after transactions
print(account.get_balance())
# Attempting to access private attributes directly will raise an AttributeError
# print(account.__balance)  # Uncommenting this line will cause an error

# Encapsulation is the concept of restricting direct access to some of an object's components,
# which is a fundamental principle of OOP. It helps in protecting the internal state of the object
# and only allows modification through well-defined interfaces (methods).
# This ensures that the object's data remains valid and consistent.
# In this example, the BankAccount class encapsulates the account holder's name and balance,
# providing public methods to interact with these private attributes safely.
