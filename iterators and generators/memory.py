def fun_list(n):
    a,b = 0,1
    i = 0
    nums =[]
    while i < n:
        nums.append(b)
        a,b = b, b+a
        i += 1
    return nums

# num = fun_list(100000)
# print(num)

# the above process took more than 1.5 gb of memory and still didn't produced the result

def fun_gen(n):
    a,b = 0,1
    i = 0
    while i < n:
        yield b
        a,b = b,b+a
        i += 1

for _ in fun_gen(100000):  # this took around 34 mb and was printing every number still didn't produced result
    print(_)              # even after long time but hogged less ram


