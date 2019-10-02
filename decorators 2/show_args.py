from functools import wraps

def show_args(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        print(f"Here are the args:{result[0]}")
        print(f"Here are the kargs:{result[1]}")
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    return [tuple(args),dict(kwargs)]
    

do_nothing(1, 2, 3,a="hi",b="bye")