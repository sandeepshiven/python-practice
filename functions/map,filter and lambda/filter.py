def even(num):
	return num%2 == 0
	
	
mylist = [1,2,3,4,5,6,7,8,9]


print(list(filter(even,mylist))) # filters out the false value for the elements in mylist

for item in filter(even,mylist):
	print(item)