from csv import writer,DictReader

with open('writing.csv','w') as file:
    csv_reader = writer(file)
    csv_reader.writerow(['Name','Surname','Age'])
    csv_reader.writerow(['Sandeep','Shiven',20])
    csv_reader.writerow(['Yash','',19])
    csv_reader.writerow(['Ansh','Shrivastava',18])


with open('writing.csv','r') as file:
    read = DictReader(file)
    for i in read:
        print(i['Surname'])