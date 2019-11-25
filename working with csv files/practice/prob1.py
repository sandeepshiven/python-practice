'''For this exercise, you'll be working with a file called 
Each row of data consists of two columns  user's first name, and a user's last name.
Implement the following function
Takes in a first name and a last name and adds a new user to the
'''

from os import system
from csv import DictReader, DictWriter

def start():
    while True:
        system("clear")
        print("What do you want to do? \n1. Insert\n2. View\n3. Find\n4. Update User\n5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            first_name = input("Enter first name of user: ") 
            last_name = input("Enter last name of user: ")
            add_user(first_name,last_name)
            input()
        
        elif choice == 2:
            display()
            input()
        elif choice == 3:
            first = input("Enter first name: ")
            last = input("Enter last name: ")
            result = find_user(first,last)
            if result:
                print(f"User found at row: {result}")
                input()
            else:
                print("User not found")
                input()            
        elif choice == 4:
            old_first = input("Enter first name of old user: ")
            old_last = input("Enter last name of old user: ")
            new_first = input("Enter first name of new user: ")
            new_last = input("Enter last name of new user: ")
            result = update_user(old_first,old_last,new_first,new_last)
            print(f"Users Updated: {result}")
            input()
        
        else:
            print("Invalid Choice")
            input()


def add_user(first, last):
    with open('user.csv','r+') as file:
        read = DictReader(file)
        
        if read.fieldnames == None:
            header = ['firstName','lastName']
            data = DictWriter(file,fieldnames=header)
            data.writeheader()
            data.writerow({
                'firstName':first,
                'lastName' : last
            })
        else:
            header = ['firstName','lastName']
            data = DictWriter(file,fieldnames=header)
            data.writerow({
                'firstName':first,
                'lastName' : last
            })

def display():
    with open('user.csv','r') as file:
        read = DictReader(file)
        for i in read:
            print(i['firstName'],i['lastName'])

def find_user(first,last):
    with open('user.csv','r') as file:
        read = DictReader(file)
        count = 1
        for i in read:
            if i["firstName"] == first and i["lastName"] == last:
                return count 
            count += 1
        return 0


def update_user(f_old,l_old,f_new,l_new):
    with open('/media/sandeep/sandeep files1/github/python-practice/working with csv files/practice/user.csv','r') as file:
        read = DictReader(file)
        count = []
        flag = 0
        for i in read:
            if i["firstName"] == f_old and i["lastName"] == l_old:
                i["firstName"] = f_new
                i["lastName"] = l_new
                flag += 1
            count.append(i)
        
    with open('user.csv','w') as file:
        header = ['firstName','lastName']
        write = DictWriter(file,fieldnames=header)
        write.writeheader()
        for i in count:
            write.writerow(i)
        
    return flag
       
        






if __name__ == '__main__':
    start()


