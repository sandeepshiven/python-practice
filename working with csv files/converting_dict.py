from csv import DictReader , DictWriter


def cm_to_inch(height):
    if height == '':
        return None
    return int(height)*0.393701



with open('dict.csv') as file:
    read = DictReader(file)
    with open('new_dict.csv','w') as new:
        headers = ['Name','Surname','Age','Height(in inch)']
        write = DictWriter(new, fieldnames= headers)
        write.writeheader()
        for i in read:
            write.writerow({
                'Name' : i['Name'],
                'Surname' : i['Surname'],
                'Age' : i['Age'],
                'Height(in inch)' : cm_to_inch(i['Height(in cm)']),
            })



