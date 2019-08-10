#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 02:29:06 2019

@author: sandeep
"""

  # polymorphism refers to the way in which different object classes can share the same method name, and those methods can be called from the same place even though a variety of different objects might be passed in
class Dog():
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):   
        return self.name + " says woof!"
        
        
class Cat():
    
    
    def __init__(self,name):
        self.name  = name
        
    def speak(self):     # same method name as Dog class
        return self.name + " says meow!"
    
    
spike = Dog("Spike")
print(spike.speak())

tom = Cat("Tom")


print(tom.speak()) 
        

# another way to demonstrate polymorphism by using loop

for pet in [spike,tom]:
    print(type(pet))
    print(pet.speak())
        
    
# polymorphism can also be demonstrated by using function
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(spike)
pet_speak(tom)


# A more common practice is to use abstract classes and inheritance

# An abstract class is one that never expects to be instantiated
        
class Animal1():  # Constructor of the class
    
    def __init__(self,name):
        self.name = name
        
    def speak(self):    # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
    
class Dog1(Animal1):
    def speak(self):
        print(self.name + " says woof! again")
        
        
class Cat1(Animal1):
    def speak(self):
        print(self.name + " says meow! again")
        
        
anim = Animal1("abc")
#anim.speak()

spike1 = Dog1("Spike")
tom1 = Cat1("Tom")

spike1.speak()
tom1.speak()












