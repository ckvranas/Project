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


arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

array = (arrayOne + arrayTwo) ** 2

print(array)

g = np.arange(10,34,1).reshape(8,3)
g = np.split(g, 4)
print(g)


import numpy

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (sampleArray)


minOfAxisOne = numpy.amin(sampleArray, 1) 
print("Printing amin Of Axis 1")
print(minOfAxisOne)

maxOfAxisOne = numpy.amax(sampleArray, 0) 
print("Printing amax Of Axis 0")
print(maxOfAxisOne)

print("Printing Original array")
sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
print (sampleArray)

print("Array after deleting column 2 on axis 1")
sampleArray = numpy.delete(sampleArray , 1, axis = 1) 
print (sampleArray)

arr = numpy.array([[10,10,10]])

print("Array after inserting column 2 on axis 1")
sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1) 
print (sampleArray)

from matplotlib import pyplot as plt
gg = np.array([[1, 1],
               [2, 2]])
plt.plot(gg[:,0], gg[:,1])
plt.show()
