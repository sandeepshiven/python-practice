''' iterator = an object that can be iterated upon. An object which returns data,one element at a time when next() 
    is called on it

    iterable = an object which will return an iterator when iter() is called on it 
'''
string = 'lkjsflgaslg' # string is an iterable
try:
    print(next(string))
except:
    print("TypeError: 'str' object is not an iterator")
string = iter(string)
print(next(string))
print(next(string))
print(next(string))
print(next(string))

l = [1,4,6,2.3,4,1,6,3.2,4,87,8,63,3.4,4.6,4]
try:
    print(next(l))
except:
    print("TypeError: 'list' object is not an iterator")

l = iter(l)
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
print(next(l))
