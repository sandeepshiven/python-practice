class User:
    def __init__(self,first,last,age): # this init method is always called first on 
        self.first = first             # instantiating a class
        self.last = last              # self is used to create a seperate variable
        self.age = age                #or method for each instance 
    
    def full_name(self):
        return f"My name is {self.first} {self.last}"
    
    def initials(self):
        return f"Initials : {self.first[0].upper()}.{self.last[0].upper()}."

    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age>=65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th birthday {self.first}" 




user1 = User('Sandeep','Shiven',20)
user2 = User('Ansh','Shrivastava',68)

print(user1.full_name())
print(user2.full_name())
print(user1.initials())
print(user2.initials())
print(user1.likes('coding'))
print(user2.likes('chatting'))
print(user1.is_senior())
print(user2.is_senior())
print(user1.age)
print(user1.birthday())
print(user1.age)

print(user2.age)
print(user2.birthday())
print(user2.age)









