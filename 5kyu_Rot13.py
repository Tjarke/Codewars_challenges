
"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.


https://www.codewars.com/kata/530e15517bc88ac656000716

"""

def rot13(message):
    alph = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
            "q","r","s","t","u","v","w","x","y","z"]
    
    encd = []
    
    for i in message:
        if i in alph:
            encd+=alph[(alph.index(i)-13)]
        elif i.lower() in alph:
            encd+=alph[(alph.index(i.lower())-13)].upper()
        else:
            encd += i
    
    return ''.join(encd)