'''
# NOT WORKING CODE!
# JUST FOR DEMO PURPOSES!

# When we write:
@decorator
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator(func)


# When we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator_with_args(arg)(func)
'''

from functools import wraps

def ensure_no_arg(rest_argu):
    def info(fun):
        @wraps(fun)
        def wrapper(*args,**kwargs):
            if args and args[0] != rest_argu:
                return f"The first argument should be {rest_argu}"
            return fun(*args, **kwargs)
        return wrapper
    return info

@ensure_no_arg("Sandeep")
def name_print(*name):
    print(f"Sandeep {name[1]}")

print(name_print("Sandeep","Shiven")) 
print(name_print("Shiven","Sandeep"))

@ensure_no_arg(10)
def add(*nums):
    return sum(nums)

print(add(10,9))
print(add(9,10))




