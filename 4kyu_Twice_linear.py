#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consider a sequence u where u is defined as follows:

    The number u(0) = 1 is the first one in u.
    For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
    There are no other numbers in u.

Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
Task:

Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
Example:

dbl_linear(10) should return 22
Note:

Focus attention on efficiency



https://www.codewars.com/kata/5672682212c8ecf83e000050
"""

def dbl_linear(n):
    u=[1]
    index = 0
    while len(u) < n*9:        #I have not quite figured out how many times i have to run this loop :/ n*9 was trial and error
        u.append(2*u[index]+1)
        u.append(3*u[index]+1)
        index+=1
    u.sort()

    
    result = []
    seen = set()
    for i in u:
        if i not in seen:
            result.append(i)
            seen.add(i)
    return result[n]