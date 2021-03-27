# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 14:36:22 2021

@author: User
"""

import requests
import json
import webbrowser
import timeit

start = timeit.timeit()

r = requests.get('https://live.24media.gr/service/sections/1/?accept=json').text
r = json.loads(r)
teams = ()
array = []
Final = []
index = 0

urls = [matches["links"][0]["url"] for matches in r[0]["events"]]
for match in urls:
    array = match.split("-")
    if len(array) > 3:
        teams = (array[1], array[3].split(".")[0], match)
    else:
        teams = (array[1], array[2].split(".")[0], match)
    
    Final.append(
        {
           str(index):
                [ 
                  {   
                    "home": teams[0],
                    "away": teams[1],
                    "url": teams[2]
                  }
                ]  
         }        
    )
    index += 1
    

#Save results in sport.txt!

r_text = json.dumps(Final, indent=3)
with open("sport24.csv", 'w') as file:
    file.write(r_text)

webbrowser.open(Final[0][str(0)][0]['url'], new=1)
        
end = timeit.timeit()

print(f"Elapsed time {end - start}s")
