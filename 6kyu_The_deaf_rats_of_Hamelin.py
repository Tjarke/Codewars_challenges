"""
Story

The Pied Piper has been enlisted to play his magical tune and coax all the rats out of town.

But some of the rats are deaf and are going the wrong way!
Kata Task

How many deaf rats are there?
Legend

    P = The Pied Piper
    O~ = Rat going left
    ~O = Rat going right

Example

    ex1 ~O~O~O~O P has 0 deaf rats

    ex2 P O~ O~ ~O O~ has 1 deaf rat

    ex3 ~O~O~O~OP~O~OO~ has 2 deaf rats

 """


def count_deaf_rats(town):
    rats = town.replace(" ", "").split('P')
    return count_left_right(rats[0], left=True) + count_left_right(rats[1], left=False)


def count_left_right(s, left=True):
    counts = {'~O': 0, 'O~': 0}
    for i in range(0, len(s)-1, 2):
        counts[s[i:i+2]] += 1
    return counts['O~'] if left else counts['~O']
