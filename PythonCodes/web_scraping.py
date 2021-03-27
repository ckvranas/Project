# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:50:11 2021

@author: User
"""

import requests

#r = requests.get('https://imgs.xkcd.com/comics/viral_vector_immunity.png')

#payload = {'username': 'corey', 'password': 'testing'}
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
print(r)





#r_dict = r.json()

#print(r_dict['form']) #200 means ok or r.ok
#r.headers

#with open('comic.png', 'wb') as f:
 #   f.write(r.content)
