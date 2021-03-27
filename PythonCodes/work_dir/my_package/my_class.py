# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:55:14 2020

@author: User
"""

class ParentClass:
    def __init__(self):
        print("Parent")
    


class MyClass(ParentClass): 
   def __init__(self, my_string_list):
      super().__init__()
      self.my_string_list = my_string_list
      self.my_string = self.my_fun_string()
        
   def my_fun_string(self):
      return " ".join(self.my_string_list)
        
   print("MyClass")    