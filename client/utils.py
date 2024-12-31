# -*- coding: utf-8 -*-

from pydantic import BaseModel
import streamlit as st

class WordPair:
    
    def __init__(self, left_word, right_word, hidden_side):
        self.left = left_word
        self.right = right_word
        self.hidden_side = hidden_side
        
    def display(self):
        if self.hidden_side == 'left':
            return ['', self.right]
        if self.hidden_side == 'right':
            return [self.left, '']
        if self.hidden_side == 'none':
            return [self.left, self.right]
        
    def solve(self):
        return [self.left, self.right]

#class DebugSession(BaseModel):
    # index: int
    # _pairs: list[str]
    # _tags: list[str]

    # @property
    # def pairs(self):
    #     return len(self._pairs)
    
    # @property
    # def tags(self):
    #     return len(self._tags)
    
    # def __str__(self):
    #     return f"index: {self.index}, pairs: {self.pairs}, tags: {self.tags}"