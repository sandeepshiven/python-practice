class Animal():
    cool = True
    
    def make_sound(self,sound):
        return(f"This animal says {sound}")



class Cat(Animal):
    pass

amy = Cat()
print(amy.make_sound("Meow"))
print(amy.cool)
print(Cat.cool)
print(Animal.cool)

print(isinstance(amy,Cat))   # isinstance checks if the object is made of the same class