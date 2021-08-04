"""
Implement a function that receives a string, and lets you extend it with repeated calls. When no argument is passed you should return a string consisting of space-separated words you've received earlier.

Note: there will always be at least 1 string; all inputs will be non-empty.

For example:

create_message("Hello")("World!")("how")("are")("you?")() == "Hello World! how are you

"""


class create_message():
    def __init__(self, s):
        self.string = s

    def __call__(self, s=""):
        if len(s) > 0:
            self.string += " "+s
        return self

    def __eq__(self, o):
        return self.string == o

    def __add__(self, s):
        return self.string+s
