def count_upto(n):
    count = 1
    while count<n:
        yield count # the function immedietly returns the count and stops there until it is called again
        count += 1

c = count_upto(4)
print(c)
print(next(c))
print(next(c))
print(next(c))
try:
    print(next(c)) # the loop is ended and automatically stop iteration message is followed 
except:
    print("StopIteration")

d = count_upto(5)
for i in d:
    print(i)

