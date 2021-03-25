"""
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071

nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071

If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1

nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
"""

from itertools import permutations
    
    
def next_bigger(n):
    n = str(n)
    
    if len(n) == 1 or sorted(n,reverse = True) == list(n):
        return -1
    
    if len(n) == 2:
        return int(n[-1]+n[0])
    
    for i in range(1,len(n)):
        ans = n[:-i-1]
        a = sorted(list(permutations(n[-i-1:])))
        for j in a:
            b = "".join(j)
            if ans + b > n:
                return int(ans+b)


    