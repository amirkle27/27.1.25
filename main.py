import BankAccounts
from BankAccounts import *

if __name__ == "__main__":

    try:
        amir = BankAccount('Amir','amirkle@gmail.com',2.2)
        gefen = BankAccount('Gefen','gefen@wall.co.il', 29.1)
        gideon = BankAccount('Gideon','gideon12@gmail.com', 450020.9)
        shaul = BankAccount('Shaul','Shaul51@gmail.com',89.4)
        rika = BankAccount('Rika','RikaIsCool12@wall.co.il', 900000.1)
        tuvia = BankAccount('Tuvia','NotZafir@gmail.com', 4020.3)
        amir.deposit(200000.0)
    except Exception as e:
        print(e)

    try:
        print(BankAccount.last_operation_time)
        print(BankAccounts.BankAccount.min_balance)  # Access property without parentheses
        print(BankAccount.number_of_accounts)  # Access property without parentheses
        print(BankAccount.last_operation_time)
        print(BankAccount.number_of_accounts)  # Access property without parentheses
        print(BankAccount.balance_all_accounts)  # Access property without parentheses
        amir.close_account()
        print(amir)
        amir.deposit(500.0)
        print(BankAccount.max_balance)  # Access property without parentheses
        print(BankAccount.min_balance)  # Access property without parentheses
        print(BankAccount.balance_all_accounts)  # Access property without parentheses
        print(BankAccount.last_operation_time)
        print(BankAccount.number_of_accounts)

    except Exception as e:
        print(e)



