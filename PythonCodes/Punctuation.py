# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:00:38 2020

@author: User
"""
from string import punctuation

str1 = '/*Jon is @developer & musician!!'

for char in punctuation:
    str1 = str1.replace(char, '#')
    
print(str1)    
