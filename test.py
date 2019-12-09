from itertools import permutations
from collections import Counter

def main():
    test = int(input())
    for i in range(test):
        a = input()
        b = input()
        a=set(permutations(a,len(a)))
        b=set(permutations(b,len(b)))
        a = set(map(str_to_dec,a))
        b = set(map(str_to_dec,b))
        l = [i^j for i in a for j in b]
        print(len(set(l)))

def str_to_dec(l):
    two = 0
    num = 0
    for i in l:
        num += int(i)*(2**two)
        two += 1
    return num

if __name__=="__main__":
    main()



    