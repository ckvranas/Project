# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:15:18 2020

@author: User
"""

import re

a = re.findall(r"#movies", "Love #movies! I had fun yesterday going to the #movies")
print(a)

b = re.split(r"!", "Nice Place to eat! I'll come back! Excellent meat!")
print(b)

c = re.sub(r"yellow", "nice", "I have a yellow car and a yellow house in a yellow neighborhood")
print(c)

d = re.findall(r"User\d", "The winners are: User9, UserN, User8")
print(d) 

e = re.findall(r"User\D", "The winners are: User9, UserN, User8")
print(e)

f = re.findall(r"User\w", "The winners are: User9, UserN, User8")
print(f)

g = re.findall(r"\W\d", "This skirt is on sale, only $5 today!")
print(g)

h = re.findall(r"Data\sScience", "I enjoy learning Data Science")
print(h)

i = re.sub(r"ice\Scream", "ice cream", "I really like ice-cream")
print(i)

j = re.findall(r"\d+-\d+", "Date of start: 4-3. Date of registration: 10-04.")
print(j) # + one or more 

k = re.findall(r"@\w+\W*\w+", "The concert was amazing! @ameli!a @joh&&n @mary90")
print(k) # zero or more

l = re.findall(r"colou?r", "The color of this image is amazing. However, the colour blue could be brighter.")
print(l) # zero or once

m = re.findall(r"\d{1,2}-\d{3}-\d{2,3}-\d{4, }", "John: 1-966-847-3131 Michelle: 54-908-42-42424")
print(m)







