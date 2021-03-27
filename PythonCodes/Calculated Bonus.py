# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 11:21:48 2020

@author: User
"""

def bonus(days):
    if days < 33:
        return 0
    elif days > 32 and days < 41:
        return (32*0 + (days - 32)*325)
    else:
        return (32*0 + 8*325 + (days - 48) * 550)


print(bonus(50))