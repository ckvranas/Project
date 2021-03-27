# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 08:00:59 2020

@author: User
"""

import re

pets = re.findall('([A-Za-z]+)\s\w+\s(\d+)\s(\w+)', "Clary has 2 dogs but John has 3 cats")
print(pets[0][0])


a = my_string = "My lucky numbers are 8755 and 33"
re.findall(r"(\d)+", my_string)
print(a)


b = re.findall(r"(\d+)", my_string)
print(b)

my_string = "I want to have a pet. But I don't know if I want 2 cats, 1 dog or a bird."
c = re.findall(r"\d+\s(cat|dog|bird)", my_string)
print(c)

my_string = "I want to have a pet. But I don't know if I want 2 cats, 1 dog or a bird."
d = re.findall(r"(\d+)\s(cat|dog|bird)", my_string)
print(d)


my_string = "John Smith: 34-34-34-042-980, Rebeca Smith: 10-10-10-434-425"
e = re.findall(r"(?:\d{2}-){3}(\d{3}-\d{3})", my_string)
print(e)

my_date = "Today is 23rd May 2019. Tomorrow is 24th May 19."
f = re.findall(r"(\d+)(?:th|rd)", my_date)
print(f)


text = "Python 3.0 was released on 12-03-2008."
information = re.search("(\d{1,2})-(\d{2})-(\d{4})", text)
print(information.group(0))
print(information.group(3))


text = "Austin, 78701"
cities = re.search(r"(?P<city>[A-Za-z]+).*?(?P<zipcode>\d{5})", text)
cities.group("zipcode")


my_text = "tweets.txt transferred, mypass.txt transferred, keywords.txt error"
re.findall(r"\w+\.txt(?=\stransferred)", my_text)# ?= menas look ahead positive, ?! negative


my_text = "Member: Angus Young, Member: Chris Slade, Past: Malcolm Young, Past: Cliff Williams."
re.findall(r"(?<=Member:\s)\w+\s\w+", my_text)





