import re

pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) [a-z]+", re.IGNORECASE)

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

result = pattern.sub("REDACTED", text)

print(result)

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

result = pattern.sub(r"\g<1>REDACTED", text)

print(result)


pattern = re.compile(r"(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+", re.IGNORECASE)

text = "Last night Mrs. Daisy and Mr. White murdered Ms. Chow"

result = pattern.sub(r"\g<1>\g<2>", text)

print(result)





































