# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 17:20:45 2021

@author: User
"""

import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)


# print(json.dumps(data, indent=2))