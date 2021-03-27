# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:24:20 2020

@author: User
"""

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sampleSet.update(sampleList)
print(sampleSet)

set1 = {10, 20, 30}
set2 = {20, 40, 50}

print(set2.union(set1))

set1.difference_update(set2)
print(set1)

set4 = {10, 20, 30, 40, 50}
set4.difference_update({10, 20, 30})
print(set4)

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference(set2)
print(set2)

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

if not set1.isdisjoint(set2):
    print("Common")
    print(set1.intersection(set2))
    