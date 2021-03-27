# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:50:35 2020

@author: User
"""

#1
import re
str1 = "bdjb9959"
a = re.search("r [^a-zA-Z0-9.]", str1)
print(a)

#2
str2 = "ab"
if re.search("ab{2,3}", str2):
    print("FOUND")
else:
    print("NOT FOUND")
    
    
#3
str3 = "Assd"
d = re.findall("r ^[A-Z]+[a-z]+$", str3)
print(d)

