"""
Given an array of integers of any length, return an array that has 1 added to the value represented by the array.

    the array can't be empty
    only non-negative, single digit integers are allowed

Return nil (or your language's equivalent) for invalid inputs.
Examples

For example the array [2, 3, 9] equals 239, adding one would return the array [2, 4, 0].

[4, 3, 2, 5] would return [4, 3, 2, 6]

"""


def up_array(arr):
    if type(arr) != list:
        return None
    if len(arr) == 0:
        return None
    for i in arr:
        if type(i) != int:
            return None
        elif i < 0 or i > 9:
            return None
    if arr[-1] != 9:
        arr[-1] = arr[-1]+1
        return arr
    else:
        end = []
        while arr[-1] == 9:
            if len(arr) == 1:
                return [1, 0]+end
            end.append(0)
            arr = arr[:-1]
        end.insert(0, arr[-1]+1)
        return arr[:-1]+end
