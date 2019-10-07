class Robot():
    def __init__(self,name,battery = 100, skills = []):
        self.name = name
        self.battery = battery
        self.skills = skills

    def charge(self):
        self.battery = 100
        return self

    def say_name(self):
        if self.battery > 0:
            self.battery -= 1
            return f"BEEP BOP! I am {self.name}"
        return "Low power! Charge Immediately!"

    def learn_skill(self, new_skill, cost_of_learning):
        if self.battery >= cost_of_learning:
            self.battery -= cost_of_learning
            self.skills.append(new_skill)
            return f"1,2,3.... and {self.name} learned {new_skill}"
        return f"Insufficient battery Charge and Try again"
