class User:
    def __init__(self,first,last,age): # this init method is always called first on 
        self.first = first             # instantiating a class
        self.last = last
        self.age = age


user1 = User('Sandeep','Shiven',20)
user2 = User('Ansh','Shrivastava',19)

print(user2.first,user2.last)
print(user1.first,user1.last)
             