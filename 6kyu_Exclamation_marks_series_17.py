"""
Description:

Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".
Examples

balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
"""


def balance(left, right):
    l = left.count('!') * 2 + left.count('?') * 3
    r = right.count('!') * 2 + right.count('?') * 3
    if l == r:
        return 'Balance'
    elif l > r:
        return 'Left'
    else:
        return 'Right'
