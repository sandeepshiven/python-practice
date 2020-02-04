import re

def extract_number(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    res = phone_regex.search(input)
    if res:
        return res.group()
    return None


def extract_all_number(input):
    phone_regex = re.compile(r"\b\d{3} \d{3}-\d{4}\b")
    return phone_regex.findall(input)
   

print("Extract only one")
print(extract_number("my number is 654 546-3574")) 
print(extract_number("my number is 654 546-35746756dsf")) 
print(extract_number("654 546-3574 dasfagb  ad"))
print(extract_number("654 546-3574"),"\n\n")

print("Extract all")
print(extract_all_number("my number is 654 546-3574 654 546-3574")) 
print(extract_all_number("my number is 654 546-35746756dsf")) 
print(extract_all_number("654 546-3574 654 546-3574 dasfagb  ad"))
print(extract_all_number("654 546-3574 654 546-3574"),"\n\n")


def is_valid_phone(input):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    res = phone_regex.search(input)
    if res:
        return True
    return False

def is_valid_phone2(input):
    phone_regex = re.compile(r"^\d{3} \d{3}-\d{4}$")
    res = phone_regex.fullmatch(input)
    if res:
        return True
    return False

print(is_valid_phone("my number is 654 546-3574 654 546-3574"))
print(is_valid_phone("654 546-3574"))
print(is_valid_phone("a654 546-3574"))
print(is_valid_phone("654 546-3574b"))
print(is_valid_phone("a654 546-3574s"),"\n\n")

print(is_valid_phone2("my number is 654 546-3574 654 546-3574"))
print(is_valid_phone2("654 546-3574"))
print(is_valid_phone2("a654 546-3574"))
print(is_valid_phone2("654 546-3574b"))
print(is_valid_phone2("a654 546-3574s"))
























