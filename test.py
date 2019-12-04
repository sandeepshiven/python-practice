

import itertools

def possibleWords(a,N):
    ##Your code jkldefhere
    keypad = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    l = [keypad[i] for i in a]
    l1 = itertools.product(*l)
    for i in l1:
        print(*i,sep='',end=' ')




possibleWords([2,3,4],3)