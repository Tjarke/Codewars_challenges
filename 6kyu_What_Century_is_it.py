"""
Return the century of the input year. The input will always be a 4 digit string, so there is no need for validation.
Examples

"1999" --> "20th"
"2011" --> "21st"
"2154" --> "22nd"
"2259" --> "23rd"
"1124" --> "12th"
"2000" --> "20th"
"""


def what_century(year):
    if year[2:] == "00":
        cent = year[:2]
    else:
        cent = str(int(year[:2]) + 1)
    if cent[1] == "1" and cent[0] != "1":
        return cent + "st"
    elif cent[1] == "2" and cent[0] != "1":
        return cent + "nd"
    elif cent[1] == "3" and cent[0] != "1":
        return cent + "rd"
    else:
        return cent + "th"
