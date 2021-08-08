"""
Your task is to write a higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions.

chained([a,b,c,d])(input)

Should yield the same result as

d(c(b(a(input))))


"""


def chained(functions):
    def h(*args):
        if len(functions) == 1:
            return functions[0](*args)
        else:
            return functions[-1](chained(functions[:-1])(*args))
    return h

"""
Easier:
def chained(functions):
    def f(x):
        for function in functions:
            x = function(x)
        return x
    return f
"""