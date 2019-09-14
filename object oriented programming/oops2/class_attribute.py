class User:
    active_users = 0  # class attribute it defined once and shared between all instances of the same class
    def __init__(self,first,last,age): 
        self.first = first             # self variabels are only restricted to particular class instance
        self.last = last              # and cannot be used without object.variable
        self.age = age             
        User.active_users += 1   # syntax for using class attribute

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"

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

print(User.active_users)

print(user2.logout())
del user2 #deleting user2 instance
print(User.active_users)
print(user2.first)

# print(user1.full_name())
# print(user2.full_name())
# print(user1.initials())
# print(user2.initials())
# print(user1.likes('coding'))
# print(user2.likes('chatting'))
# print(user1.is_senior())
# print(user2.is_senior())
# print(user1.age)
# print(user1.birthday())
# print(user1.age)

# print(user2.age)
# print(user2.birthday())
# print(user2.age)









