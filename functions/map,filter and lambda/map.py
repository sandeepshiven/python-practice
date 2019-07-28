

def square(num):
	return num**2

mylist = [1,2,3,4,5,6,7,8,9]
# using map for iterating every element in mylist and operating square on each number

for item in map(square,mylist):
	print(item)
	
print(list(map(square,mylist)))

def splicer(word):
	if len(word)%2 == 0:
		return 'EVEN'
	else:
		return word[0]
		
		
mystring = ['Sandeep','Shiven','Ikshit','Unni']
print(list(map(splicer,mystring)))