class Character():
    def __init__(self,name,hp,level):
        self.name = name
        self.hp = hp
        self.level = level

class NPC(Character):
    def __init__(self,name,hp,level):
        Character.__init__(self,name,hp,level)

    def speak(self):
        print("I heard there were monsters running around last night")


villager = NPC("Bob",100,12)
print (villager.name)
print (villager.hp)
print (villager.level)
villager.speak()



















