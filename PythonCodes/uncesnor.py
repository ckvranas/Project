# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 10:02:57 2020

@author: User
"""

def uncensor(my_string, vowels):
    k = 0
    if len(vowels) == 0:
        print(my_string)
        return
    else:
        for letter, i in enumerate(my_string):
            if letter == "*":
                my_string[i] = vowels[k]
                k += 1
    
    print(my_string)
    return


uncensor("*PP*RC*S*", "UEAE")