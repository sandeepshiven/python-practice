mylist = [1,2,3,4,5,6,7,8,9]

square = lambda num: num**2   # basically same as writing a function to return square of number


#using lambda with map
print(list(map(lambda num: num**2,mylist)))  # taking num as a parameter and returning the value after :

print(list(filter(lambda num: num%2 == 0,mylist)))



