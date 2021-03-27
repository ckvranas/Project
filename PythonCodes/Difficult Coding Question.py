# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 18:00:16 2020

@author: User
"""

def func(args):
    args = sorted(args)
    i = 0
    length = 1
    start = args[i]
    result = []
    position = []
    while i < len(args) - 1:
        if args[i] + 1 in args:
            length += 1 
        else: 
            if length > 1:
                position.append(length)
                result.append([start, args[i]])
                length = 1
                
            start = args[i] 
        i += 1
        
    indexx = position.index(max(position))
    return result[indexx]


print(func([1,11,3,0,6,5,2,4,10,7,12,8]))