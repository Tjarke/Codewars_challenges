
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

    Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Courtesy of projecteuler.net


https://www.codewars.com/kata/514b92a657cdc65150000006

"""

def solution(number):
    a=set()
    
    for i in range(1,number):
        if i%3==0:
            a.add(i)
        elif i%5==0:
            a.add(i)
    return sum(a)