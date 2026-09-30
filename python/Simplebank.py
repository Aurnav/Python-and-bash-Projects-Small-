
class User:
    def __init__(self, name, age):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")       
        self.name = name
        self.age = age


class Bank:
    def __init__(self,account_number, name , balance):
        Accounts = []
        if not isinstance(account_number, int):
            raise TypeError("Account number must be an integer")
        self.account_number = account_number
        if not isinstance(name,str):
            raise TypeError("Name must be a string")
        self.name = name
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number")
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount}. New balance is {self.balance}")
        else:
            print("Insufficient funds")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive")
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}")
        
