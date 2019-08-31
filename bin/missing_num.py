test = int(input())
i=0
arr=[]
while test>0:
    
    arr.append(int(input()))
    arr[i]= arr[i]*2+arr[i]*3+arr[i]*6
    test -=1
    i += 1
for i in arr:
    print(i)