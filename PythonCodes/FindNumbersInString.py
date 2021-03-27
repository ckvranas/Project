# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:20:43 2020

@author: User
"""
import numpy as np
import re

str1 = "English = 78 Science = 83 Math = 68 History = 65"
list1 = []

list1 = [int(num) for num in re.findall(r'\b\d+\b', str1)]   
list1 = np.array([list1])

print(list1.sum(), list1.mean())