import re

byte_pattern = re.compile(r"\b[10]{8}\b")

print(byte_pattern.findall("11010101 101 323"))

print(byte_pattern.findall("my data is: 10101010 11100010"))

print(byte_pattern.findall("asdsa"))



































