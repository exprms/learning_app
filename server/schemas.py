# -*- coding: utf-8 -*-
from pydantic import BaseModel
from typing import List, Optional

# data laoding: ==============================

class FieldMapper(BaseModel):
    name: str
    columns: list[str]
    
class CSVFileMapper(FieldMapper):
    json_columns: FieldMapper
     
    @property
    def source_column_names(self) -> list[str]:
        return self.columns + self.json_columns.columns
    
    @property
    def target_column_names(self) -> list[str]:
        return self.columns + [self.json_columns.name]    

# database: ++++++++++++++++++
class Pair(BaseModel):
    id: int
    left: str
    right: str
    info_left: str=""
    info_right: str=""
    tag_subject: str=""
    tags: list=[]
        
    class Config:
        orm_mode = True
               
    
class PairCreate(Pair):
    pass
    

# TAG ==========================================================
class TagList(BaseModel):
    tags: list[str]
    
    class Config:
        orm_mode = True
        
        
# class TagCreate(Tag):
#     pass

# assoziation tabkle for many to many relationship: ==========    
class PairTag(BaseModel):
    pair_id: int
    tag_id: int
    
    class Config:
        orm_mode = True

class PairTagCreate(PairTag):
    pass

# class Chapter(BaseModel):
#     chapter: str
    

    
# class TodoBase(BaseModel):
#     title : str
#     description : str | None = None


# class TodoCreate(TodoBase):
#     pass


# class Todo(TodoBase):
#     id : int
#     owner_id  : int

#     class Config:
#         orm_mode = True


# class UserBase(BaseModel):
#     email: str
#     name: str


# class UserCreate(UserBase):
#     pass 


# class User(UserBase):
#     id : int
#     is_active : bool
#     todos : list[Todo] = []

#     class Config:
#         orm_model = True

