# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 19:55:56 2020

@author: User
"""
import re

my_links = "Just check out this link: www.amazingpics.com. It has amazing photos!"
a = re.findall(r"www.+com", my_links)
print(a)


my_string = "the 80s music was much better that the 90s"
b = re.findall(r"the\s\d+s", my_string)
b2 = re.findall(r"^the\s\d+s", my_string) #^ means start of the string
print(b)
print(b2)

c = re.findall(r"the\s\d+s$", my_string)
print(c)# $ means start of the string

my_string = "I love the music of Mr.Go. However, the sound was too loud."
d = re.split(r"\.\s", my_string)
print(d) # \ means escape characters

my_string = "Elephants are the world's largest land animal! I would love to see an elephant one day"
e = re.findall(r"Elephant|elephant", my_string)
print(e)

my_string = "Yesterday I spent my afternoon with my friends: MaryJohn2 Clary3"
f = re.findall(r"[a-zA-Z]+\d", my_string) #OR operator
print(f)

my_string = "My&name&is#John Smith. I%live$in#London."
g = re.sub(r"[&#%$]", " ", my_string)
print(g)





