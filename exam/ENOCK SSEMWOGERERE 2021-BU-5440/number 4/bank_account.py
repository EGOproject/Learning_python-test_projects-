# -*- coding: utf-8 -*-
"""
Created on Wed May 10 23:57:47 2023

@author: lab
"""

#back account


class BankAccount():
    def __init__(self, account_number, account_balance,deposit_cash):
        self.account_number = account_number
        self.account_balance = account_balance
        self.deposit_cash = deposit_cash
        
   
    def deposit (account_balance,deposit_ammount):
        account_balance = account_balance + deposit_ammount
        print("Your new balance is: ", account_balance)
        
    def withdraw (account_balance,withdraw_ammount):
        account_balance = account_balance - withdraw_ammount
        print("Your new balance is: ", account_balance)
        
        
#interface
def usage():
    account_number = input("What is your account number?: ")
    #assume we already have money on the account
    account_balance = 20000
    print(account_number)
    
    choice = input("How may we help you? deposit or withdraw? type here: ")
    if choice == "deposit" or "withdraw":
        if choice == "deposit":
            deposit_ammount = int(input("How much do you want to deposit?: "))
            BankAccount.deposit(account_balance, deposit_ammount)
        elif choice == "withdraw":
            withdraw_ammount = int(input("How much do you want to Withdraw?: "))
            BankAccount.withdraw(account_balance, withdraw_ammount)
    elif choice != "deposit" or "withdraw":
        print("Try Again Later!!")
usage()



























