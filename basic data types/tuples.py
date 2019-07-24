t = (1,2,3,3,'sandeep',3.32)
print(f"{len(t)}") # checking length just like a list

print(f"Your tuple : {t}")

print(f"{t[3]}") # indexing just like list

print(f"{t[1:3]}") #slicing just like string

# some methods
print(f"{t.index(3)}")  # returns the index of the value given as argument

print(f"{t.count(3)}") # counts the number of times a value appears in the tuple