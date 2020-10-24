#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A format for expressing an ordered list of integers is to use a comma separated list of either

    individual integers
    or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"

Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"

Courtesy of rosettacode.org


https://www.codewars.com/kata/51ba717bb08c1cd60f00002f
"""

def solution(args):
    args = sorted(args)
    in_range = False
    output = ""
    
    for cnt,i in enumerate(args):
        prev = args[cnt-1]
        nex = args[cnt-len(args)+1]
        if prev == i-1 and nex == i+1:
            if not in_range:
                start = args[cnt-1]
                output = output[:(-1-len(str(start)))]
            in_range = True
        elif in_range:
            output += str(start)+"-"+str(i)+","
            in_range = False           
        else:
            output+=str(i)+","
    return output[:-1]
    
    
    
  

