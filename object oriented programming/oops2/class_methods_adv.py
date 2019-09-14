class User:
    active_users = 0  # class attribute it defined once and shared between all instances of the same class
    
    @classmethod # decorator  (similar to class attribute)
    def display_active_users(cls):  # in class methods automatically the class is going to be passed in
        return f"There are currently {cls.active_users} active users" # in the method


    @classmethod
    def from_string(cls,data_string):
        first,last,age = data_string.split(',') # class itself is passed in this method
        return cls(first,last,int(age))  # creates a new instance
    
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




# user1 = User('Sandeep','Shiven',20)
# user2 = User('Ansh','Shrivastava',68)

# print(User.display_active_users())

# print(user2.logout())
# del user2 #deleting user2 instance
# print(User.display_active_users())
# print(user2.first)

sandy = User.from_string("Sandeep,Shiven,20")
print(sandy.full_name())
print(sandy.birthday())


