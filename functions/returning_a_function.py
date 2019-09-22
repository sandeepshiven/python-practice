from random import choice

def make_laugh_func(person=''):
    def get_laugh():
        l = choice(('HAHAHAHAHA','LOL','thehehehehe'))
        return f"{l} {person}"

    return get_laugh

laugh = make_laugh_func()
print(laugh())

#inner function can access outer functions scope

laugh_at = make_laugh_func("Sandeep")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
# inner