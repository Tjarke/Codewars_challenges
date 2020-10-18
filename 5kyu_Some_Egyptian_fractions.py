
"""
Given a rational number n

n >= 0, with denominator strictly positive

    as a string (example: "2/3" in Ruby, Python, Clojure, JS, CS, Go)
    or as two strings (example: "2" "3" in Haskell, Java, CSharp, C++, Swift)
    or as a rational or decimal number (example: 3/4, 0.67 in R)
    or two integers (Fortran)

decompose this number as a sum of rationals with numerators equal to one and without repetitions (2/3 = 1/2 + 1/6 is correct but not 2/3 = 1/3 + 1/3, 1/3 is repeated).

The algorithm must be "greedy", so at each stage the new rational obtained in the decomposition must have a denominator as small as possible. In this manner the sum of a few fractions in the decomposition gives a rather good approximation of the rational to decompose.

2/3 = 1/3 + 1/3 doesn't fit because of the repetition but also because the first 1/3 has a denominator bigger than the one in 1/2 in the decomposition 2/3 = 1/2 + 1/6.
Example:

(You can see other examples in "Sample Tests:")

decompose("21/23") or "21" "23" or 21/23 should return 

["1/2", "1/3", "1/13", "1/359", "1/644046"] in Ruby, Python, Clojure, JS, CS, Haskell, Go

"[1/2, 1/3, 1/13, 1/359, 1/644046]" in Java, CSharp, C++

"1/2,1/3,1/13,1/359,1/644046" in C, Swift, R

Notes

1) The decomposition of 21/23 as

21/23 = 1/2 + 1/3 + 1/13 + 1/598 + 1/897

is exact but don't fulfill our requirement because 598 is bigger than 359. Same for

21/23 = 1/2 + 1/3 + 1/23 + 1/46 + 1/69 (23 is bigger than 13)
or 
21/23 = 1/2 + 1/3 + 1/15 + 1/110 + 1/253 (15 is bigger than 13).

2) The rational given to decompose could be greater than one or equal to one, in which case the first "fraction" will be an integer (with an implicit denominator of 1).

3) If the numerator parses to zero the function "decompose" returns [] (or "".

4) The number could also be a decimal which can be expressed as a rational.

examples:

0.6 in Ruby, Python, Clojure,JS, CS, Julia, Go

"66" "100" in Haskell, Java, CSharp, C++, C, Swift, Scala, Kotlin

0.67 in R.

Ref: http://en.wikipedia.org/wiki/Egyptian_fraction


https://www.codewars.com/kata/54f8693ea58bce689100065f

"""

import math

def decompose(n):
        
    if "/" in n:
        a = n.split("/")
        x = int(a[0])
        y = int(a[1])
    elif "." in n:
        a = n.split(".")
        y = 10**len(a[1])
        x = int(a[0]+a[1])
    else:
        x = int(n)
        y = 1
    
    outpt_txt = []
    
    if x % y == 0 and x != 0:
        outpt_txt.append(str(int(x/y)))
        x = 0
    
    
    while x!= 0:
        outpt_txt.append("1/"+str(math.ceil(y/x)))
        x_new = -y % x
        y_new = y *math.ceil(y/x)
        x = x_new
        y = y_new
        if outpt_txt[0] == "1/1":        #not a nice way to do it but no motivation to do it better atm
            outpt_txt[0] = "1"
        
    return outpt_txt

