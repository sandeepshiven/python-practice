from functools import wraps

def only_ints(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if any([i for i in args if type(i) != int]):
            print("Only ints are allowed")
            return
        return fn(*args, **kwargs)
    return wrapper

@only_ints
def add(*args):
    print( sum(args))

add(2,2,2,3)
add(2,2,'d',2,3)



def only_ints_2(*types):
    def info(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            for i in args:
                if type(i) != types[0]:
                    print("ver 2 only ints")
                    return
            return fn(*args,**kwargs)
        return wrapper
    return info

@only_ints_2(int)
def add2(*args):
    print(sum(args))

add2(1,3,6,4)
add2(1,3,6,'d',4)