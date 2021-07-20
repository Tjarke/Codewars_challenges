"""
In English and programming, groups can be made using symbols such as () and {} that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

({})
[[]()]
[{()}]

The next are done incorrectly:

{(})
([]
[])

A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols (), {} or [] to create groups.

It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.

"""
grps = {"(": ")", "[": "]", "{": "}"}


def group_check(s):
    last_open = []
    for i in s:
        if i in grps:
            last_open.append(i)
        else:
            if len(last_open) == 0:
                return False
            if i != grps[last_open.pop()]:
                return False
    return len(last_open) == 0
