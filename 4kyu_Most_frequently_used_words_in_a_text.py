"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
Assumptions:

    A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII. (No need to handle fancy punctuation.)
    Matches should be case-insensitive, and the words in the result should be lowercased.
    Ties may be broken arbitrarily.
    If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.

Examples:

top_3_words("In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]

Bonus points (not really, but just for fun):

    Avoid creating an array whose memory footprint is roughly as big as the input text.
    Avoid sorting the entire array of unique words.


"""


def top_3_words(text):
    for i in text:
        if (not i.isalpha()) and (i != "'"):
            text = text.replace(i, " ")
    while " ''" in text:  text = text.replace(" ''", " ")
    if " ' " in text: text = text.replace(" ' ", " ")
    lst = text.lower().split()
    if not lst:
        return []
    most = max(set(lst), key=lst.count)
    if len(set(lst)) < 2:
        return [most]
    second = max(set(lst)-set([most]), key=lst.count)
    if len(set(lst)) < 3:
        return [most, second]
    third = max(set(lst)-set([most, second]), key=lst.count)
    return [most, second, third]
