# -*- coding: utf-8 -*-
from pydantic import BaseModel
    
class Pair(BaseModel):
    id: int
    topic: str
    chapter: str
    mode: str
    left: str
    right: str
    
    class Config:
        orm_mode = True

class PairCreate(Pair):
    pass

class Chapter(BaseModel):
    chapter: str
    
class Topic(BaseModel):
    topic: str
    
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

