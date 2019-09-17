class Human():

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self._age = age


    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,num):
        if num >= 0:
            self._age = num
        else:
            raise ValueError("Age cannot be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self,new_name):
        self.first ,self.last = new_name.split(" ")







sandy = Human("Sandeep","Shiven",20)
print(sandy.age) # we don't have to call the age as a function
sandy.age = 21 # we don't have to pass the new age as parameter in function instead we can change it
                # like regular variable
print(sandy.age)
print(sandy.full_name)
sandy.full_name = "Ansh Shrivastava"
print(sandy.full_name)

print(sandy.__dict__)