"""
At a job interview, you are challenged to write an algorithm to check if a given string, s, can be formed from two other strings, part1 and part2.

The restriction is that the characters in part1 and part2 should be in the same order as in s.

The interviewer gives you the following example and tells you to figure out the rest from the given test cases.

For example:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""


def is_merge(s, part1, part2):
    if len(s) == 0:
        return False if (len(part1) != 0) or (len(part2) != 0) else True

    cur1 = []
    cur2 = []
    cnt1 = 0
    cnt2 = 0
    p1_complete = False
    p2_complete = False
    
    if len(part1) == 0:
        p1_complete = True
        part1 = [1]
    if len(part2) == 0:
        p2_complete = True
        part2 = [1]

    for i in s:
       
        if (i !=  part1[cnt1]) & (i !=  part2[cnt2]) & (len(cur1) > 0) & (len(cur2) > 0):
            if (i == cur1[-1]) & (i == cur2[-1]):
                cnt2 -= len(cur2)
                cur2 = []
                cur1 = []
        
        if (i == part1[cnt1]) & (not p1_complete):
            cur1.append(i)
            cnt1 += 1
        if (i == part2[cnt2]) & (not p2_complete):
            cur2.append(i)
            cnt2 += 1
            
        if cur1 != cur2:
            if cur1 > cur2:
                cnt2 -= len(cur2)
                cur2 = []
                cur1 = []
            else:
                cnt1 -= len(cur1)
                cur1 = []
                cur2 = []
        if cnt1 == len(part1):
            p1_complete = True
            cnt1 = 0
            if cnt2 == len(part2):
                return False
        elif cnt2 == len(part2):
            p2_complete = True
            cnt2 = 0
    if part1[0] == 1:
        part1 = []
    if part2[0] == 1:
        part2 = []
    
    if p1_complete & p2_complete & (len(part1) + len(part2) == len(s)):
        return True
    else:
        return False
