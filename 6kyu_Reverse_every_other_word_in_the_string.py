"""
Reverse every other word in a given string, then return the string.
Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word.
Punctuation marks should be treated as if they are a part of the word in this kata.

"""


def reverse_alternate(string):
    string = string.strip()
    s = string.split()
    for i in range(1, len(s), 2):
        s[i] = s[i][::-1]
    return " ".join(s)
