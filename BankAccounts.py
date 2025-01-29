from error_messages import *
from datetime import datetime

class BankAccount:

    max_balance: float = 0
    max_balance_name = ""
    min_balance: float = None
    min_balance_name = ""
    balance_all_accounts: float = 0
    last_operation_time: datetime
    number_of_accounts = 0

    def __init__(self, name: str, email: str, start_balance: float):
        self.__active = True
        self.name = name
        self.email = email
        self.start_balance = start_balance
        self.balance = start_balance
        if start_balance > BankAccount.max_balance:
            BankAccount.max_balance = start_balance
            BankAccount.min_balance_name = name
        if BankAccount.min_balance is None:
            BankAccount.min_balance = start_balance
            BankAccount.min_balance_name = name
        if not BankAccount.min_balance is None and start_balance < BankAccount.min_balance:
            BankAccount.min_balance = start_balance
            BankAccount.min_balance_name = name
        if BankAccount.number_of_accounts == 10:
            raise MaxNumberOfAccountsError(f"{[self.name]} - - Max number of accounts is 10, cannot create a new account and exceed the Max Number")
        BankAccount.balance_all_accounts += start_balance
        print(f"Account created successfully {[self.name]}")
        BankAccount.number_of_accounts += 1
        BankAccount.last_operation_time = datetime.now()


    @property
    def name (self):
        return self.__name

    @name.setter
    def name(self, name):
        if not name:
            raise EmptyValueError(f"Name cannot be left empty!")
        if not isinstance(name,str):
            raise TypeError(f"{[self.name]} - - Name must be string, cannot be of type {type(name)}")
        if not name:
            raise EmptyNameError("Name cannot be empty!")
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not email:
            raise EmptyValueError("Email cannot be left empty!")
        if not isinstance(email,str):
            raise NameNotStrError(f"{[self.email]} - - Email must be of type str, cannot be {type(email)}!")
        if not email:
            raise EmptyNameError("Email cannot be empty!")
        if not "@" in email or not "." in email:
            raise ImproperEmailError(f"Error with email {email}:\n Email must contain '@' and '.'")
        self.__email = email

    @property
    def start_balance(self):
        return self.__start_balance

    @start_balance.setter

    def start_balance(self, start_balance):
        if start_balance == None:
            raise EmptyValueError(f"{[self.start_balance]} - - Start Balance cannot be left empty!")
        if not isinstance(start_balance, float):
            raise BalanceNotFloatError(f"{[self.start_balance]} - - Balance must be of type 'float', cannot be {type(start_balance)}")
        if start_balance < 0:
            raise DepositBelowZeroError(f"{[self.start_balance]} - - Start balance cannot be lower than 0")
        if not self.__active:
            raise NonActiveAccountError(f"{[self.start_balance]} - - Attention! Account not active!")
        self.__start_balance = start_balance
        BankAccount.last_operation_time = datetime.now()

    @property
    def last_operation_time(self):
        return BankAccount.last_operation_time

    def __str__(self):
        return f"{self.name}'s Bank Account details:\n\
Name: {self.__name}\nEmail: {self.__email}\nStart Balance: {self.__start_balance}\nBalance Status: {self.__active}"

    def deposit (self, amount: float):
        if not isinstance(amount,float):
            raise BalanceNotFloatError(f"{[amount]} - - Deposit amount must be of type 'float', cannot be {type(amount)}")
        if amount < 0:
            raise DepositBelowZeroError(f"{[amount]} - - Deposit amount cannot be lower than 0")
        if not self.__active:
            raise NonActiveAccountError(f"{self.name} - - Attention! Account not active! Cannot deposit new amount")
        self.balance += amount
        if self.balance > BankAccount.max_balance:
            BankAccount.max_balance = self.balance
        BankAccount.balance_all_accounts += self.balance
        BankAccount.last_operation_time = datetime.now()

    def withdraw(self, amount: float):
        if not isinstance(amount, float):
            raise BalanceNotFloatError(f"{[amount]} - - Withdraw amount must be of type 'float', cannot be {type(amount)}")
        if amount < 0:
            raise DepositBelowZeroError(f"{[amount]} - - Withdraw amount cannot be lower than 0")
        if not self.__active:
            raise NonActiveAccountError(f"{self.name} - - Attention! Account not active!")
        if self.balance < BankAccount.min_balance:
            BankAccount.min_balance = self.balance
        self.balance -= amount
        BankAccount.balance_all_accounts -= amount
        BankAccount.last_operation_time = datetime.now()

    def close_account(self):
        if not self.__active:
            raise NonActiveAccountError(f"{self.name} - - Account already closed")
        BankAccount.balance_all_accounts -= self.balance
        self.balance = 0
        self.__active = False
        print(f"{self.name}'s account has been closed successfully")
        BankAccount.number_of_accounts -= 1
        BankAccount.last_operation_time = datetime.now()
