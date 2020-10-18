
"""
Snail Sort

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]

For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

This image will illustrate things more clearly:
    
    see codewars site 

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].



https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1

"""

import numpy as np


def snail(arr):
    output = []
    mat =np.array(arr)
    direction = 1
    
    if arr == [[]]:
        return []
    
    while mat.shape != (0,0):
        if mat.shape[0] == mat.shape[1]:
            for i in range(mat.shape[1]):
                if direction == 1:
                    output.append(mat[0,i])                    
                else:
                    output.append(mat[-1,-i-1])
            if direction == 1:
                mat = mat[1:,:]
            else:
                mat = mat[:-1,:]
        else:
            for i in range(mat.shape[0]):
                if direction == 1:
                    output.append(mat[i,-1])
                else:
                    output.append(mat[-i-1,0])
            if direction == 1:
                mat = mat[:,:-1]
                direction = direction*(-1)
            else:
                mat = mat[:,1:]
                direction = direction*(-1)

    return output


array = [[1,2,3],
         [4,5,6],
         [7,8,9]]

array = [[1,2,3,6],
         [4,5,6,7],
         [7,8,9,8],
         [3,3,4,5]
         ]


snail(array)