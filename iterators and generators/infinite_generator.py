def count_infy():
    nums = (1,2,3,4) # we will get a infinite sequence but only one integer at a time
    i =0             # so  no need to store the value and the iterate over it
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1

i = 17
j = count_infy()
while i:
    print(next(j))
    i -= 1
 