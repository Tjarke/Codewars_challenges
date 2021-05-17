"""
In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula
(nk)=n!k!(n−k)!\lparen {n \atop k} \rparen = \frac {n!} {k!(n-k)!}(kn​)=k!(n−k)!n!​

where n denotes a row of the triangle, and k is a position of a term in the row.

Pascal's Triangle

You can read Wikipedia article on Pascal's Triangle for more information.
Task

Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional list/array.
Example:

n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]




"""

from math import factorial as f

def pascals_triangle(n):
    ans = []
    for i in range(n):
        for j in range(i+1):
            ans.append(int(f(i)/(f(j)*f(i-j))))
    return ans

"""
This only works for smaller n because of precision
alternative: 
from scipy.special import comb
def pascals_triangle(n):
    return [comb(a, b, exact=True) for a in range(n) for b in range(a + 1)] 
"""