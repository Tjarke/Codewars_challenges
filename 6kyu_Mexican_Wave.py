"""
Task

In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return that string in an array where an uppercase letter is a person standing up. 

Rules

 1.  The input string will always be lower case but maybe empty.

 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

Example

wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
"""


def wave(people):
    ans = []
    if len(people) == 0:
        return ans
    for i in range(len(people)-1):
        if people[i] != " ":
            word = people[:i] + people[i].upper() + people[i+1:]
            ans.append(word)
    if people[-1] != " ":
        word = people[:-1] + people[-1].upper()
        ans.append(word)
    return ans
