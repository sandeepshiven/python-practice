original_path = input("Enter the file name with path and extension: ")
copy_path = input("Enter the path and file name with extension you want to copy: ")

with open(original_path,'rb') as original:
    with open(copy_path,'wb') as copy:
        while True:
            temp = original.read(1)
            if not temp:
                break
            copy.write(temp)



