"""
Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

Example:

solution(1000) # should return 'M'

Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000

Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

"""

dic = {1:"I",5:"V",10:"X",50:"L",100:"C",500:"D",1000:"M"}

def solution(n):
    s = str(n)
    ans = ""
    for i in range(1,len(s)+1):
        l = int(s[-i])
        pos = 10**(i-1)
        if l < 4:
            ans = l * dic[pos] + ans
        elif l == 4:
            ans = dic[pos] + dic[pos*5] + ans
        elif l >= 5 and l < 9:
            ans = dic[pos*5] + (l-5)*dic[pos] + ans
        else:
            ans = abs(l-10)*dic[pos] + dic[pos*10]+ans
    return ans