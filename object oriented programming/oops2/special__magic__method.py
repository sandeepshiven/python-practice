from copy import copy


class Human():

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __add__(self,other):
        if isinstance(other,Human):
            return Human("Newborn", self.last,0)
        return "YOU CAN'T ADD THOSE TWO"

    def __mul__(self,other):
        if isinstance(other,int):
            return [copy(self) for i in range(other)]
        return "CAN'T MULTIPLY THOSE"

j = Human("Ansh","Shrivastava",30)
k = Human("Camila","Cabello",25)

print(j)

print(j+k)
print(j+3)
triplets = k*3
print(triplets)
triplets[0].first = 'Sandeep'
print(triplets) # [Human named Sandeep Cabello aged 25, Human named Sandeep Cabello aged 25, Human named Sandeep Cabello aged 25]
# because all three are identical and pointing at same thing they are not copies
print(k) # Human named Sandeep Cabello aged 25
# for this to not happen we use copy module

triplets = (j+k)*5
print(triplets)

