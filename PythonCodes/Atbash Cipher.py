# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:39:33 2020

@author: User
"""

"""
The Atbash cipher is an encryption method in which each letter of a word is replaced
with its "mirror" letter in the alphabet:
A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

"""

import string as str

def atbash(my_string):
    new_string = ""
    for i, letter in enumerate(my_string):      
        if letter.isupper(): 
            index = str.ascii_uppercase.index(letter)
            new_string += str.ascii_uppercase[-index-1]
        elif letter.islower():
            index = str.ascii_lowercase.index(letter)
            new_string += str.ascii_lowercase[-index-1]
        else:
            new_string += my_string[i]               
    return new_string


print(atbash("Christmas is the 25th of December"))