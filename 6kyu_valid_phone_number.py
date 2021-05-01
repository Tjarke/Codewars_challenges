"""
Write a function that accepts a string, and returns true if it is in the form of a phone number.
Assume that any integer from 0-9 in any of the spots will produce a valid phone number.

Only worry about the following format:
(123) 456-7890 (don't forget the space after the close parentheses)

Examples:

validPhoneNumber("(123) 456-7890")  =>  returns true
validPhoneNumber("(1111)555 2345")  => returns false
validPhoneNumber("(098) 123 4567")  => returns false

"""

def validPhoneNumber(phoneNumber):
    # s = phoneNumber.split()
    if phoneNumber[0] != "(" or phoneNumber[4] != ")" or phoneNumber[5] != " " or phoneNumber[9] != "-":
        print("hre")
        return False
    if phoneNumber[1:3].isnumeric() and phoneNumber[6:9].isnumeric() and phoneNumber[10:].isnumeric():
        return True
    else:
        return False
    
"""
re version:
import re

def validPhoneNumber(phoneNumber):
    return bool(re.match(r"^(\([0-9]+\))? [0-9]+-[0-9]+$", phoneNumber))
"""
    
    
    
    