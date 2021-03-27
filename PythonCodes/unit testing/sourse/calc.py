# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 15:28:29 2020

@author: User
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
