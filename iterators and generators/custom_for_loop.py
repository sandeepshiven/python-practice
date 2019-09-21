def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            ans = next(iterator)
        except:
            print("STOP ITERATION!")
            break
        else:
            func(ans)


def square(x):
    print(x**2)

my_for('sandeep',print)

my_for([1,2,3,4,5],square)