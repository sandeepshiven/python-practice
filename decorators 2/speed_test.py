from time import time
from functools import wraps
time1 = time()

def speed_test(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"Executing the {fn.__name__} function")
        start_time = time()
        result = fn(*args, **kwargs)
        end_time = time()
        print(f"Execution took : {end_time - start_time} seconds")
        return result

    return wrapper


@speed_test
def sum_gen():
    return( sum(x for x in range(90000000)))

@speed_test
def sum_list():
    return(sum([x for x in range(90000000)]))


sum_gen()

sum_list()

time2 = time()
print(f"Whole process took {time2-time1}")