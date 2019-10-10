from csv import DictWriter

with open("dict.csv",'w') as file:
    headers = ['Name','Surname','Age','Height(in cm)']
    dict_writer = DictWriter(file,fieldnames=headers)
    dict_writer.writeheader()
    dict_writer.writerow({
        "Name": "Sandeep",
        "Surname":"Shiven",
        "Age" : 20,
        "Height(in cm)" : 154,
    })
    dict_writer.writerow({
        "Name": "Sandeep",
        "Surname":"",
        "Age" : 20,
        "Height(in cm)" : 164,
    })
    dict_writer.writerow({
        "Name": "Sandeep",
        "Surname":"Shiven",
        "Age" : '',
        "Height(in cm)" : 184,
    })
    dict_writer.writerow({
        "Name": "Sandeep",
        "Surname":"Shiven",
        "Age" : 20,
        "Height(in cm)" : '',
    })
    dict_writer.writerow({
        "Name": "",
        "Surname":"Shiven",
        "Age" : 20,
        "Height(in cm)" : 194,
    })