
"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
Examples

pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !


https://www.codewars.com/kata/520b9d2ad5c005041100000f
"""

def pig_it(text):
    words = text.split()
    pig_text = ""
    for i in words:
        char = i[0]
        if char.isalpha():
            pig_text += i[1:]+char+"ay "
        else:
            pig_text += i+" "
    
    
    return pig_text[:-1]
    



    