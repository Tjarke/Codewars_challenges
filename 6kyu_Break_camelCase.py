"""

Complete the solution so that the function will break up camel casing, using a space between words.
Example

solution("camelCasing")  ==  "camel Casing"


 
 """
import re 
 
def solution(s):
    first_word = re.findall('[^A-Z]*[A-Z]',s)
    words = re.findall('[A-Z][^A-Z]*',s)
    words.insert(0,first_word[0][:-1])
    return " ".join(words)


'''better : 
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
'''