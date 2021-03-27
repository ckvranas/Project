# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 17:36:01 2020

@author: User
"""

import pandas as pd

df = pd.read_csv("Automobile_data.csv")
#print(df.head())
#print(df.tail())

#df.replace(["?", "n.a"], value="NaN")

#a = df[["company", "price"]][df.price == df['price'].max()]
#print(a)

#b = df[df['company'] == 'toyota']
#print(b)

#c = df['company'].value_counts()
#print(c)

#e = df.groupby('company')['company', 'price'].max()
#print(e)

#f = df.groupby('company')["average-mileage"].mean()
#print(f)

#h = df.sort_values('price', ascending=False)
#print(h)

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}

g = pd.DataFrame(GermanCars, )

carsDf2 = pd.DataFrame.from_dict(japaneseCars)
final = pd.concat([g, carsDf2], keys=["Germany", "Japan"])
print(final)

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
carPriceDf = pd.DataFrame.from_dict(Car_Price)

car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
carsHorsepowerDf = pd.DataFrame.from_dict(car_Horsepower)

carsDf = pd.merge(carPriceDf, carsHorsepowerDf, on="Company")
carsDf