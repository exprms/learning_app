# -*- coding: utf-8 -*-

from pydantic import BaseModel

class Pair(BaseModel):
    left: str
    right: str
    info_left: str
    info_right: str
    tag_subject: str
    tags: list[str] 
    
    def display(self, hidden_side):
        if self.info_left != '':
            sep_left = ', '
        else:
            sep_left = ''
            
        if self.info_right != '':
            sep_right = ', '
        else:
            sep_right = ''
            
        if hidden_side == 'left':
            return ['', self.right + sep_right + self.info_right]
        if hidden_side == 'right':
            return [self.left + sep_left + self.info_left, '']
        if hidden_side == 'none':
            return [self.left + sep_left + self.info_left, self.right + sep_right + self.info_right]
        
    def solve(self):
        return self.display(hidden_side='none')
    