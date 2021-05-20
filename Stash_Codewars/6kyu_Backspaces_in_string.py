"""
Assume "#" is like a backspace in string. This means that string "a#bc#d" actually is "bd"

Your task is to process a string with "#" symbols.
Examples

"abc#d##c"      ==>  "ac"
"abc##d######"  ==>  ""
"#######"       ==>  ""
""              ==>  ""



"""

def clean_string(s):
    ans = ""
    for i in s:
        ans += i
        if i == "#" and len(ans)>1:
            ans = ans[:-2]
        elif i == "#":
            ans = ans[:-1]
    return ans