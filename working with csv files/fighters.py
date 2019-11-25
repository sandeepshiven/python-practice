from csv import reader
from csv import DictReader

with open('fighters.csv','r') as file:
    data = reader(file)
    for i in data:
        print(i)



with open('fighters.csv','r') as file:
    data = DictReader(file) # converts into Ordered dictionary
    print(data)
    for i in data:
        print(dict(i))
