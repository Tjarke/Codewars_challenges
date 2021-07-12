"""
Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.
Example:

"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0

"""

def longest_palindrome (s):
    current = ""
    max_len = 0
    
    for i in range(len(s)):
        for j in range(len(s)-i):
            current = s[i:i+j+1]
            if current == current[::-1]:
                max_len = max(max_len,len(current))
        current = ""

    return max_len
