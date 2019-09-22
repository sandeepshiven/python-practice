def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper


@shout
def welcome():
    return 'Welcome to the world of decorators'

@shout
def name(person):
    return f"Hi! My name is {person}"

@shout
def full_name(first,last):
    return f"My full name is {first} {last}"

print(welcome())
print(name('Sandeep'))
print(full_name('Sandeep','Shiven'))