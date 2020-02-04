import re


# normal way (difficult to read)
#email_pattern = re.compile(r"^([a-z0-9-_.]+)@([0-9a-z-_.\\]+)\.([a-z\.]{2,6})$")

new_pattern = re.compile(r"""
                        ^([a-z0-9-_.]+) # username
                        @([0-9a-z0-9-_.]+) # service
                        \.([a-z\.]{2,6})$ # .com .in etc.
                        """, re.VERBOSE | re.IGNORECASE)


# res = email_pattern.search(r"SandeepshvieN0@g\mail.com")
# print(res.group())
# print(res.groups())


res = new_pattern.search("SandeepshvieN0@gmail.com")
print(res.group())
print(res.groups())






















































