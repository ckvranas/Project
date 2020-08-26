# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:37:23 2020

@author: User
"""

def encrypt(word):
    new_word = " "
    
    word = word[::-1]
    for i in word:
        if i == 'a':
           new_word += '0'
        elif i == 'e':
            new_word += '1'
        elif i == 'i' or i == 'o':
            new_word += '2'
        elif i == 'u':
            new_word += '3'
        else:
            new_word += i
            
    print(new_word + "aca")


encrypt("karaca")