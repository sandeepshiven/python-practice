from csv import reader,writer


# method 1 
with open("fighters.csv") as file:
    read = reader(file)
    content = [[s.upper() for s in row] for row in read]

with open("upper_fighter.csv",'w') as file1:
    write = writer(file1)
    for i in content:
        write.writerow(i)


# method 2
with open("fighters.csv") as file:
    read = reader(file)
    with open("upper_fighter2.csv",'w') as file1:
        write = writer(file1)
        for fighter in read:
            write.writerow([s.upper() for s in fighter])


