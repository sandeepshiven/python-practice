def sum(n,func):
    total = 0
    for i in range(1,n+1):
        total += func(i)
    return total

def square(x):
    return x*x

def cube(x):
    return x**3

squ = sum(3,square)  # passing function as argument don't use paranthesis while passing function as argument
cu = sum(3,cube)
print(squ)
print(cu)