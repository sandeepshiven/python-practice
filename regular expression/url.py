import re

url_pattern = re.compile(r"(https?)://(www\.?[A-Za-z0-9-]{2,256}\.[a-z]{2,4})(/[-a-zA-Z0-9_//?&!@#:+.//=#~]*)*")

res = url_pattern.search("https://www.site-my.com/bio?data=blah&dog=yes")

print(url_pattern.fullmatch("https://www.site-my.com"))


print(f"Protocol: {res.group(1)}")
print(f"Domain: {res.group(2)}")
print(f"Everything else: {res.group(3)}")






























