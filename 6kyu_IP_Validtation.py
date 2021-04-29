"""
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Input to the function is guaranteed to be a single string.
Examples

Valid inputs:

1.2.3.4
123.45.67.89

Invalid inputs:

1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089

Note that leading zeros (e.g. 01.02.03.04) are considered invalid.

"""
def is_valid_IP(strng):
    n = strng.split(".")
    if len(n) != 4:
        return False
    else:
        for i in n:
            if i.isnumeric():
                if len(i)>1 and i[0] == "0" or int(i)>255 or int(i)<0:
                    return False
            else:
                return False
    return True




"""
as regular expression: 
import re
def is_valid_IP(strng):
    return bool(re.match(r'^((\d{1,2}|1\d{2}|2[0-4]\d|25[0-5])(\.(?!$)|$)){4}(?=$)',strng))
"""