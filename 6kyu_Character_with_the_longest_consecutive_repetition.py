"""
For a given string s find the character c (or C) with longest consecutive repetition and return:

(c, l)

where l (or L) is the length of the repetition. If there are two or more characters with the same l return the first in order of appearance.

For empty string return:

('', 0)
"""


def longest_repetition(chars):
    cur = ""
    cnt = 0
    ans = (cur, cnt)
    for i in chars:
        if i == cur:
            cnt += 1
        else:
            if cnt > ans[-1]:
                ans = (cur, cnt)
            cur = i
            cnt = 1
    if cnt > ans[-1]:
        ans = (cur, cnt)
    return ans
