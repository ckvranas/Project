# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 17:15:16 2021

@author: User
"""

class Parent:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
        #print(f"Parent's name is {self.name} at the age of {self.age}")
    
    def Salary(self):
        self.balance += 200 

        
class Child(Parent):
    def __init__(self, name, age, school, balance):
        super().__init__(name, age, balance)     # OR Parent__init__(self, name, age)
        self.school = school
        print(f"Child's name is {self.name} at teh age of {self.age} and {self.school}")
    
    def Salary(self):
        super().Salary()
        self.balance += 100 
        return self.balance
        
        
    
    #@classmethod -----> returns an object
    #def child2(obj, self, name, age):
     #  self.name = "marina"
     #  self.age = 33
     #  return obj(name, age)
     
    
dad = Parent("kostas", 61, 1000000000)
print(dad)
child = Child("chris", 24, "graduate", 100)
print(isinstance(child, Parent))


Balance = child.Salary()
print(Balance)