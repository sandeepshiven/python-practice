import time

gen_start = time.time()
print(sum(n for n in range(100000000))) # adding at every iteration
gen_time = time.time() - gen_start

list_start = time.time()
print(sum([n for n in range(100000000)]))  # first making list and then adding
list_time = time.time() - gen_start

print(f"time for sum(n for n in range(100000000)): {gen_time}")
print(f"time for sum([n for n in range(100000000)]): {list_time}")

'''
time for sum(n for n in range(1000000)): 5.862866163253784
time for sum([n for n in range(1000000)]): 12.892170906066895
'''

