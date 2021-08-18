
"""
Complete the function/method so that it takes a CamelCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
Examples

"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"



"""


def to_underscore(string):
    ans = string[0].lower()
    for i in string[1:]:
        if i.isupper():
            ans += "_" + i.lower()
        else:
            ans += i
    return ans
