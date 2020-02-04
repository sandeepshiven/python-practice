import re

def parse_name(input):
    name_pattern = re.compile(r"^(Mr.|Ms.|Mrs.) (?P<first>[a-zA-z]+) ([a-zA-z]+)$") # adding a lable with ?P<lable_name>
    res = name_pattern.search(input)
    print(f"Hello {res.group('first')}")



parse_name("Mrs. Tilda Winston")
































