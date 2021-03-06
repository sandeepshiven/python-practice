import jsonpickle




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
        return f"Account owner : {self.owner}\nAccount Balance : {self.balance}"


''' making instance for pickling and dumping it into json file to access information or instances 

sa = Account("Sandeep",1000)
sa.deposit(500)
sa.withdraw(200)

an = Account("Ansh",6000)
an.deposit(500)
an.withdraw(2000)

with open('accounts.json','w') as file:

    acc1 = jsonpickle.encode(sa)
    acc2 = jsonpickle.encode(an)
    file.write(acc1)
    file.write('\n')
    file.write(acc2)

'''

# accesing the data again
with open('accounts.json','r') as file:
    data = file.readline()
    data1 = jsonpickle.decode(data)
    data = file.readline()
    data2 = jsonpickle.decode(data) 


print(data1)
print(data2)
data1.deposit(500)
data1.withdraw(200)
data2.deposit(500)
data2.withdraw(200)
print(data1)
print(data2)
