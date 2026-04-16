class BankAccount:
    def __init__(self,name,balance,):
         self.name= name
         self.balance = balance

    def diposit(self,diposit):
          if diposit >= 0 :
              print(f"invalid diposit amount, Your account balance is {self.balance}")
          else:
              self.balance+=diposit

    def withdraw(self,withdraw):
          if withdraw >= self.balance:
              print(f"cant make this transaction, withdraw is more than you current balance {self.balance}!!")
          elif withdraw <= 0:
               print(f"withdraw amount cant be 0 or less than 0. Your balance is {self.balance}")
          else:
              self.balance-=withdraw

    def info(self):
         print(f"{self.name} have {self.balance} in their bank account")

people = BankAccount("sanket", 0)
people1= BankAccount('jon',0)

# people.name = 'sanket'
# people.balance= 19436
# print(people.info)
people.diposit(100)
people.withdraw(60)
people.info()

# people1.name = 'jon'
# people.balance = 12954
people1.diposit(100)
people1.withdraw(-50)
people1.info()
# print(people1.info)
