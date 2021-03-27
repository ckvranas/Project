# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 13:02:05 2020

@author: User
"""
from .token_utils import tokenize

class Document:
    def __init__(self, text, token_regex=r'[a-zA-Z]+'):
        self.text = text
        self.tokens = self._tokenize()
        
    def _tokenize(self):
        return tokenize(self.text)