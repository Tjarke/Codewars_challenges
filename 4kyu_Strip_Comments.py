"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples

The output expected would be:

apples, pears
grapes
bananas

The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"

"""

def solution(string,markers):
    text = ""
    com = False
    for i in string:
        if i in markers and not com:
            com = True
            if text != "":
                if text[-1] == " ":
                    text = text[:-1]
        if i == "\n":
            com = False
        if not com:
            text += i
    return text
  

