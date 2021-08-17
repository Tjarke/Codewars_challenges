"""
There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.

A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".

As a simplification, you may assume that no letter occurs more than once in the secret string.

You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.


"""


def recoverSecret(triplets):
    ans = ""
    all_leters = set()
    for i in triplets:
        all_leters = all_leters | set(i)

    while len(all_leters) > 0:
        for letter in all_leters:
            looking_for = True
            for triplet in triplets:
                if letter in triplet:
                    if triplet[-1] != letter:
                        looking_for = False
            if looking_for:
                ans = letter + ans
                for triplet in triplets:
                    if letter in triplet:
                        triplet.pop(-1)
                all_leters = all_leters - set(letter)
    return ans
