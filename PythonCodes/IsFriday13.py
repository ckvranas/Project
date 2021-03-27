# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:09:36 2020

@author: User
"""
import calendar
from datetime import datetime

def has_friday_13(month, year):
    string = str(year) + '-' + str(month) + '-' + '13'
    my_date = datetime.strptime(string, "%Y-%m-%d")
    print(calendar.day_name[my_date.weekday()] == 'Friday')


has_friday_13(1, 1985)

