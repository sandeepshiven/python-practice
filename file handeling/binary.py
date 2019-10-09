file = open('test.txt','rb')
file2 = open('test1.txt','wb')
while True:
    temp = file.read(1)
    if not temp :
        break
    print(bytearray(temp))
    file2.write(temp+b'-21')


