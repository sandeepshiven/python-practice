import re


def parse_date(input):
    date_pattern = re.compile(r"^(\d\d)[,./](\d\d)[,./](\d{4})$")
    res = date_pattern.search(input)
    return {"d":res.group(1), "m":res.group(2), "y":res.group(3)}

print(parse_date("01/22/1999"))
print(parse_date("12,04,2003"))
print(parse_date("01.22.1999"))
print(parse_date("01.22.1999453"))






























































