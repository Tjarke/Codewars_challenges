
"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
Examples

"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"""

def to_camel_case(text):
    ans = ""
    switch = False
    for i in text:
        if switch:
            ans += i.upper()
            switch = False
        else:
            ans += i
        if i == "-" or i =="_":
            switch = True
            ans = ans[:-1]
    return ans