
def my_sort(arr):
    new_arr = []
    for i in arr:
        if i[1].split('@')[1] == 'gmail.com':
            new_arr.append(i[0])
    return(sorted(new_arr))


fptr = open('input08.txt','r')
test = int(fptr.readline())
arr = []
for i in range(test):
    arr.append(tuple(map(str ,fptr.readline().split())))
#print(arr)
arr = my_sort(arr)
for i in arr:
    print(i)