class Animal():

    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self,sound):
        return f"{self.name} says {sound}!"

    def __repr__(self):
        return f"{self.name} is a {self.species}"

class Cat(Animal):

    def __init__(self,name,breed,toy):
        super().__init__(name,species = "cat") # super is used in place of
        self.breed = breed           # Animal.__init__(self,name,species)
        self.toy = toy

    def plays(self):
        return f"{self.name} plays with {self.toy}"


tom = Cat("Tom","normal","yarn")
print(tom)
print(tom.species)
print(tom.breed)
print(tom.toy)
print(tom.make_sound("Meow"))
print(tom.plays())
















