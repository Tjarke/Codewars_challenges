"""
Your job is to write a function which increments a string, to create a new string.

    If the string already ends with a number, the number should be incremented by 1.
    If the string does not end with a number. the number 1 should be appended to the new string.

Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.


"""


def increment_string(strng):
    n = ""
    pre_fix = ""
    for i in range(len(strng)):
        if strng[-i-1].isnumeric():
            n = strng[-i-1] + n
        else:
            pre_fix = strng[:-i]
            break
    if len(n) > 0:
        while n[0] == "0" and len(n) > 1:
            pre_fix += "0"
            n = n[1:]
        if pre_fix[-1] == "0" and n == len(n) * n[0] and n[0] == "9":
            return pre_fix[:-1] + str(int(n)+1)
        return pre_fix + str(int(n)+1)
    else:
        return strng + "1"
