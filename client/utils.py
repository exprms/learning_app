# -*- coding: utf-8 -*-

class WordList:
    
    def __init__(self, left_word, right_word, hidden_side):
        self.left = left_word
        self.right = right_word
        self.hidden_side = hidden_side
        
    def display(self):
        if self.hidden_side == 'left':
            return ['', self.right]
        if self.hidden_side == 'right':
            return [self.left, '']

