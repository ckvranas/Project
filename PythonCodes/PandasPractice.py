# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 17:49:21 2020

@author: User
"""

import numpy as np

a = np.array([[64392, 31655],
              [32579, 0],
              [49248, 462],
              [0, 0]])
a = np.empty([4, 2], dtype = np.uint16)

print(a.shape)
print(a.ndim)
print(a.itemsize)

b = np.linspace(100, 190, 10).reshape(5,2)
print(b)


sampleArray = np.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]])
print(sampleArray[:,1])


sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
[27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

print(sampleArray[::2,1::2])