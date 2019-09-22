def gen_yes_no():
    ans = ['yes','no']
    while True:
        yield ans[0]
        yield ans[1]


gen = gen_yes_no()
print(next(gen)) # 'yes'
print(next(gen)) # 'no'
print(next(gen)) # 'yes'
print(next(gen)) #