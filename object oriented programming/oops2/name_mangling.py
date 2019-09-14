''' 
_name // just a convention that tells this variable is meant for use inside the class don't acces it outside
__name // does something behind the scenes adds the class name and __name together so it can be only
accesed like this object._Class__name
___name__ // is used to ovewirte some built in methods like __len__, __str__ etc.
'''


class Person:
    def __init__(self):
        self.name = "Sandeep Shiven"
        self._secret = "Only for use in class"
        self.__msg = "Behind the scenes"
        self.__lol = "HAHAHAHAHA"

p = Person()

print(dir(p))

print(p.name)
print(p._secret)
print(p._Person__lol)
print(p.__msg)


