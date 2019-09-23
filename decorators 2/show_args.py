from itertools import wraps

def show_args(fun):
    @wraps(fun)
    def wrapper(*args,**kwargs):
        result = fun(*args,**kwargs)
        print(f"Here are the args:{result[0]}")
        print(f"Here are the kargs:{result[1]}")


@show_args
def do_nothing(*args, **kwargs):
    

do_nothing(1, 2, 3,a="hi",b="bye")