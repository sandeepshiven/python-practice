class Aquatic():
    def __init__(self,name):
        self.name = name
    
    def swim(self):
        print(f"{self.name} is swimming")

    def greet(self):
        print(f"I am {self.name} of the sea!")

class Ambulatory():
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f"{self.name} is walking")
    
    def greet(self):
        print(f"I am {self.name} of the land!")

class Penguin(Ambulatory,Aquatic):
    def __init__(self,name):
        #super().__init__(name)  # it inherits the first class passed in the class 
      # so the greet method of the Ambulatory is passed in the penguin class
      # for preventing this
        Ambulatory.__init__(self,name)
        Aquatic.__init__(self,name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

captain_cook.swim()
captain_cook.walk()

captain_cook.greet()

print(f"Captain_cook is instance of Penguin:{isinstance(captain_cook,Penguin)}")
print(f"Captain_cook is instance of Ambulatory:{isinstance(captain_cook,Ambulatory)}")
print(f"Captain_cook is instance of Aquatic:{isinstance(captain_cook,Aquatic)}")








