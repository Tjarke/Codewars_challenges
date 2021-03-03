"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

This is the second kata in series:

    Find the unique number
    Find the unique string (this kata)
    Find The Unique



"""


def find_uniq(arr):
    
    setlist = []
    
    for i in arr:
        setlist.append(set(i.lower()))
        
    wrong = set()
    for i in arr:
        
        if wrong != set(i.lower()):
            if setlist.count(set(i.lower())) != 1:
                wrong = set(i.lower())
            else:
                if len(i) != 0:
                    return i

