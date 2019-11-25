import pickle

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


''' making instance for pickling and dumping it into file to access information or instances

sa = Account("Sandeep",1000)
sa.deposit(500)
sa.withdraw(200)

an = Account("Ansh",6000)
an.deposit(500)
an.withdraw(2000)

with open('accounts.pickle','wb') as file:
    pickle.dump(sa,file)
    pickle.dump(an,file)

'''

# accesing the data again

with open('accounts.pickle','rb') as file:
    data1 = pickle.load(file)
    data2 = pickle.load(file)
    
print(data1.owner)
print(data2.owner)
print(data1.balance)
print(data2.balance)

data1.deposit(500)
data1.withdraw(200)

data2.deposit(500)
data2.withdraw(200)

