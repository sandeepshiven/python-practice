from random import choice

def eat(food,isHealthy):
    if not isinstance(isHealthy,bool):
        raise ValueError("isHealthy must be boolean")
    ending = 'YOLO!'
    if isHealthy:
        ending = "my body is a temple"
    return f"I'm eating {food}, because {ending}"

def nap(hours):
    if hours >= 2:
        return "Ugh I overslept"
    return "I'm feeling refreshed"

def is_funny(person):
    if person == 'tim':
        return False
    return True

def laugh():
    return choice(('haha','lol','tehehe','HAHAHAHA'))