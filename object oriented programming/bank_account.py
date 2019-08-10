#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 12:48:31 2019

@author: sandeep
"""

class Account:
    
    
    def __init__ (self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
        
    def deposit(self,amount):
        self.balance = self.balance + amount
        print("Deposite Accepted")
        print(f"Current amount in account : {self.balance}")
        
    def withdraw(self,amount):
        if (amount > self.balance):
            print("Funds Unavailable!")
            print(f"Current amount in account : {self.balance}")
        else :
            self.balance = self.balance - amount
            print("Withdrawal Accepted")
            print(f"Current amount in account : {self.balance}")
            
            
    def __str__(self):
        return f" Account owner : {self.owner}\nAccount Balance : {self.balance}"
            
        
        
        
        
        
        
        
        
        
        
        

# 1. Instantiate the class
acct1 = Account('Jose',100)


# 2. Print the object
print(acct1)

# 3. Show the account owner attribute
#print(acct1.owner)

# 4. Show the account balance attribute
#print(acct1.balance)

# 5. Make a series of deposits and withdrawals
acct1.deposit(50)

acct1.withdraw(75)

# 6. Make a withdrawal that exceeds the available balance
acct1.withdraw(500)


#print(acct1.balance)


acct1.deposit(80)

#print(acct1.balance)

acct1.withdraw(5)

#print(acct1.balance)


acct1.withdraw(200)

print(acct1)

