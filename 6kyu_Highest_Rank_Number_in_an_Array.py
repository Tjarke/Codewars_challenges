"""
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

Note: no empty arrays will be given.
Examples

[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3




"""

def highest_rank(arr):
    highest_ranks = []
    max_n = 0
    for i in set(arr):
        cnt = arr.count(i)
        if cnt > max_n:
            highest_ranks = [i]
            max_n = cnt
        elif cnt == max_n:
            highest_ranks.append(i)
    
    return max(highest_ranks)
