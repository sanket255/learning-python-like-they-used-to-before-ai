# Day 17 Task: Build Your First Class
# Build a Bank Account Class:
# Class BankAccount:
# - Attributes: account_holder, balance
# - Methods:
#   - __init__(name, initial_balance)
#   - deposit(amount)
#   - withdraw(amount)
#   - check_balance()
# Create objects and test them.
# 
# Before You Code
# Real Questions:
# 
# What goes in __init__? (Data that every account needs)
# What's the difference between a method and a function? (Methods use self)
# Why use a class instead of just functions? (Organization + multiple objects)



class BankAccount:
    def __init__(self,name,balance):
         self.name= name
         self.balance = balance

    def diposit(self,amt):
         self.amount=amt

    def withdraw(self,withd):
         self.amount=withd

    def info(self):
         print(f"{self.name} have {self.balance} in their bank account")

people = BankAccount("sanket", 19042)
people1= BankAccount('jon',14234)

# people.name = 'sanket'
# people.balance= 19436
# print(people.info)

people.diposit(10978)
people.withdraw(436)

people.info()

# people1.name = 'jon'
# people.balance = 12954



people1.info()
# print(people1.info)
