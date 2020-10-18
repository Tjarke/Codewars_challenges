
"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.


https://www.codewars.com/kata/54da5a58ea159efa38000836
"""

def find_it(seq):
    cnt = 0
    
    for i in seq:
        for j in seq:
            if i == j:
                cnt +=1
        if cnt%2 ==1:
            return i
