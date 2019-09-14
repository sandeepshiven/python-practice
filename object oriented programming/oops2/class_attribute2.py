class Pet():
    allowed = ['cat','dog','rat']  # if we do it in any method it's scope will be limitted we do this
    def __init__(self,name,species): # because we are using allowed more than once
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} as a pet.")
        self.name = name
        self.species = species

    def set_species(self,species): # adding a method for setting the species
        if species not in Pet.allowed:
            raise ValueError(f"You can't change the species to {species}")
        self.species = species


cat = Pet("Tom","cat")
dog = Pet("Spike","dog")
rat = Pet("Jerry","rat")
# croc = Pet("Crocky","corocodile")  # this will raise an error
# dog.species = "tiger" # no one is preventing this
#dog.set_species('tiger')  # now this will raise an error
#print(dog.species)
print(Pet.allowed)

# we can change the pet.allowed
Pet.allowed.append('pig')  # now we can change the species of cat to pig
print(Pet.allowed)
print(dog.allowed) # each instance can also use the class attribute
print(cat.allowed)

# showing that .allowed is same
print(id(dog.allowed))
print(id(cat.allowed))
print(id(Pet.allowed))

# we can change the allowed attribute of object
cat.allowed = ['tiger','lion']
print(Pet.allowed)
print(dog.allowed) # each instance can also use the class attribute
print(cat.allowed)

print(id(dog.allowed))
print(id(cat.allowed))  # Now the id of the allowed in cat is been changed
print(id(Pet.allowed))



