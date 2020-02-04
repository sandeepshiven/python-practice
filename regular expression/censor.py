import re

def censor(input):
    pattern = re.compile(r"frack[a-z]*", re.IGNORECASE)
    res = pattern.sub("CENSORED", input)
    return res


print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))




































