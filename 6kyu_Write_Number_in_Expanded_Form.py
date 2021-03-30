"""
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.
"""

def expanded_form(num):
    ans = ""
    for i in range(1,len(str(num))+1):
        if str(num)[-i] != "0":
            ans = " + " + str(num)[-i] + (i-1)*"0" + ans       
    return ans[3:]