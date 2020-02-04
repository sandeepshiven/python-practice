import re

#defining our match pattern for phone number
pattern = re.compile(r"\d{3} \d{3}-\d{3}")

#finding the pattern
res1 = pattern.search("Call me at 546 645-9874 or 809 780-6789") # search only gives first match
res2 = pattern.findall("Call me at 546 645-9874 or 809 780-6789")
print(res1.group())
print(res2)











