"""
Task

You are looking for teammates for an oncoming intellectual game in which you will have to answer some questions.

It is known that each question belongs to one of the n categories. A team is called perfect if for each category there is at least one team member who knows it perfectly.

You don't know any category well enough, but you are going to build a perfect team. You consider several candidates, and you are aware of the categories each of them knows perfectly. There is no restriction on the team size, but smaller teams gain additional bonus points. Thus, you want to build a perfect team of minimal possible size. Find this size (and don't forget to count yourself!) or determine that it is impossible to form a perfect team from the candidates you have.
Input/Output

[input] integer n representing the number of categories

1 ≤ n ≤ 10.

[input] 2D integer array candidates

For each valid i, candidates[i] is an array of different integers representing indices of the categories which the ith candidate knows perfectly.

0 ≤ candidates.length ≤ 10,

0 ≤ candidates[i].length < n,

0 ≤ candidates[i][j] < n.

[output] an integer

The minimal possible size of the perfect team, or -1 ( or Nothing or a similar empty value ) if you can't build it.
Example

For n = 3 and

candidates = [[0, 2],
              [1, 2],
              [0, 1],
              [0]]
the output should be  3.

You can build a perfect team of size 3 in any of the following ways:

yourself, candidate number 1 (1-based) and candidate number 2 
[] + [0, 2] + [1, 2] = [0, 1, 2]
yourself, candidate number 1 and candidate number 3
[] + [0, 2] + [0, 1] = [0, 1, 2]
yourself, candidate number 2 and candidate number 3
[] + [1, 2] + [0, 1] = [0, 1, 2]
yourself, candidate number 2 and candidate number 4
[] + [1, 2] + [0] = [0, 1, 2]
"""
import itertools


def perfect_team_of_minimal_size(n, candidates):
    cats = [i for i in range(n)]
    for i in range(n):
        grps = list(itertools.combinations(candidates,i+1))
        for j in grps:
            cats_in_grp = []
            for k in j:
                cats_in_grp += k
            if set(cats_in_grp) == set(cats):
                return i+2
    return -1
