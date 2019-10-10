from csv import reader
from csv import DictReader

with open('fighters.csv','r') as file:
    data = reader(file)
    for i in data:
        print(i)



with open('fighters.csv','r') as file:
    data = DictReader(file) # converts into Ordered dictionary
    for i in data:
        print(i['Name'])
