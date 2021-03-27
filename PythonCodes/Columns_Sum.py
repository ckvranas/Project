# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:07:13 2020

@author: User
"""

"""
A city skyline can be represented as a 2-D list with 1s representing buildings. 
In the example below, the height of the tallest building is 4 (second-most right column).
"""

import numpy as np

def tallest_skyscraper(array2):
    array2 = np.array(array2)
    
    print(max(array2.sum(axis = 0)))
    return


tallest_skyscraper([[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]])
