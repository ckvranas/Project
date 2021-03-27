# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 18:26:14 2021

@author: User
"""

class Customer:
    
    def __init__(self, name, id, balance):
        self.name, self.id, self.balance = name, id, balance
        
    def __str__(self):
        cust_str = f"Customer: {self.name} and {self.balance}"
        return cust_str
     
    def __eq__(self, other):
        return(self.name == other.name) and (self.id == other.id)

Cust1 = Customer("Chris", 1, 1e+6)
Cust2 = Customer("Chris", 1, 1e+7)
print(Cust1)
print(Cust1 == Cust2)