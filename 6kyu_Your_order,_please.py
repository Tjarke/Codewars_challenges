"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.
Examples

"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""

"""


def order(sentence):
    words = sentence.split()
    one, two, three, four, five, six, seven, eight, nine = "","","","","","","","",""
  
    for i in words:
          if "1" in i:
              one = i
          elif "2" in i:
              two = i
          elif "3" in i:
              three = i
          elif "4" in i:
              four = i
          elif "5" in i:
              five = i
          elif "6" in i:
              six = i
          elif "7" in i:
              seven = i
          elif "8" in i:
              eight = i
          elif "9" in i:
              nine = i
    ans = [one, two, three, four, five, six, seven, eight, nine]
    ans = " ".join(ans)
    ans = " ".join(ans.split())
    return ans



print(order("is2 Thi1s T4est 3a"))