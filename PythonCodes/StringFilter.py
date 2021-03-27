# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 15:45:54 2020

@author: User
"""

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

new_str_list = list(filter(None, str_list))

print(new_str_list)