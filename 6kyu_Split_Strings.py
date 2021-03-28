"""
Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']



"""


def solution(s):
    ele = int(len(s)/2)
    ans = []
    for i in range(ele):
        ans.append(s[i*2:i*2+2])
    if len(s)%2 == 1:
        ans.append(s[-1]+"_")
    return ans