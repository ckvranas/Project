# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 14:39:12 2021

@author: User
"""

from bs4 import BeautifulSoup
import requests 

"""
with open('simple.txt') as html_file:
    soup = BeautifulSoup(html_file, 'lxml') #lxml parser

#print(soup.prettify())    
#match = soup.title.text
#article = soup.find('div', class_='article')
for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    summary = article.p.text
    
    print(headline)
    print(summary)
    
"""

source = requests.get('https://coreyms.com/?s=regex').text

soup = BeautifulSoup(source, 'lxml')

article = soup.find('article')
#print(article)

# headline = article.h2.a.text
# print(headline)

#summary = article.find('div', class_="entry-content").p.text
#print(summary)

vid_src = article.find('iframe', class_='youtube-player')['src']
print(vid_src)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]

#print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
