from functools import wraps

def not_allowed(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        print(args)
        if kwargs:
            raise ValueError("Sorry! No keyword arguments allowed :(")
        return fn(*args,**kwargs)
    return wrapper

@not_allowed
def welcome(name):
    print(f"Welcome! {name}")

welcome("Sandeep")
