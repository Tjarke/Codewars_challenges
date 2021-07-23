"""
Modify the kebabize function so that it converts a camel case string into a kebab case.

kebabize('camelsHaveThreeHumps') // camels-have-three-humps
kebabize('camelsHave3Humps') // camels-have-humps

Notes:

    the returned string should only contain lowercase letters


"""


def kebabize(string):
    if string.isnumeric():
        return ""
    ans = ""
    for i in string:
        if not i.isalpha():
            continue
        if i.isupper():
            ans += "-" + i.lower()
        else:
            ans += i
    return ans if ans[0] != "-" else ans[1:]
