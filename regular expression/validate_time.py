import re


def is_valid_time(input):
    time_regex = re.compile(r"^\d{1,2}:\d{1,3}$")
    res = time_regex.search(input)
    if res:
        return True
    return False

print(is_valid_time("10:45"))
print(is_valid_time("1:23"))
print(is_valid_time("10.45"))
print(is_valid_time("1999"))
print(is_valid_time("145:23"))
print(is_valid_time("it is 12:15"))
print(is_valid_time("12:15"))
print(is_valid_time("34:55"))





