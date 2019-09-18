class User:
    active_users = 0 
    
    @classmethod 
    def display_active_users(cls):  
        print( f"There are currently {cls.active_users} active users") 


    @classmethod
    def from_string(cls,data_string):
        first,last,age = data_string.split(',') 
        return cls(first,last,int(age))  
    
    def __init__(self,first,last,age): 
        self.first = first             
        self.last = last              
        self.age = age             
        User.active_users += 1   

    def logout(self):
        User.active_users -= 1
        print (f"{self.first} has logged out")

    def full_name(self):
        print (f"My name is {self.first} {self.last}")
    
    def initials(self):
        print (f"Initials : {self.first[0].upper()}.{self.last[0].upper()}.")

    def likes(self,thing):
        print (f"{self.first} likes {thing}")

    def is_senior(self):
        return self.age>=65

    def birthday(self):
        self.age += 1
        print( f"Happy {self.age}th birthday {self.first}") 

class Moderator(User):
    active_mods = 0

    def __init__(self,first,last,age,community):
        super().__init__(first,last,age)
        self.community = community
        Moderator.active_mods += 1

    @classmethod
    def display_active_mods(cls):
        print(f"There are currently {cls.active_mods} active mods")

    def remove_post(self):
        print(f"{self.full_name()} removed a post from the {self.community} community ")




User.display_active_users()
user1 = User("Ansh","Shrivastava",19)
User.display_active_users()
mod1 = Moderator("Sandeep","Shiven",20,"Coders")
User.display_active_users()
mod1.full_name()
print(mod1.community)
print("\n\n")

user2 = User("Ansh","Shrivastava",19)
user3 = User("Ansh","Shrivastava",19)
user4 = User("Ansh","Shrivastava",19)
mod2 = Moderator("Sandeep","Shiven",20,"Coders")
mod3 = Moderator("Sandeep","Shiven",20,"Coders")
mod4 = Moderator("Sandeep","Shiven",20,"Coders")
User.display_active_users()
Moderator.display_active_mods()







