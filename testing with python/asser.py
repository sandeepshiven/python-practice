def add_positive(x,y):
    assert x>0 and y>0, "Both no. must be +ve"
    return x+y

print(add_positive(1,1)) # 2
try:
    print(add_positive(-1,1)) # assertion error
except:
    print("There was an assertion error")

def eat_food(food):
    assert food in [
        'pizza','ice cream','burger','coffee','fries','hotdog'
    ],'food must be junk food'
    return f"NOM NOM! I am eating {food}."

print(eat_food('burger'))
try:
    print(eat_food("Juice")) # assertion error
except:
    print("There was an assertion error")
