def days_of_week():
    days = ['Monday','Tuesday','Wednesday','Friday','Saturday','Sunday']
    for day in days:
        yield day

for i in days_of_week():
    print(i)