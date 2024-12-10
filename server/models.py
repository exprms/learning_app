#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 21:44:35 2024

@author: bernd
"""

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Pair(Base):
    __tablename__ = "pairs"
    id = Column(Integer,primary_key=True,index=True)
    topic = Column(String(255),index=True)
    chapter = Column(String(255), index=True)
    mode = Column(String(255), index=False)
    left = Column(String(255), index=False)
    right = Column(String(255), index=False)
    
class Vocab(Base):
    __tablename__ = "vocab"
    id = Column(Integer,primary_key=True,index=True)
    topic = Column(String(255),index=True)
    left = Column(String(255), index=False)
    right = Column(String(255), index=False)
    info_left = Column(String(255), index=True)
    info_right = Column(String(255), index=False)

class Tags(Base):
    __tablename__ = "tags"
    id = Column(Integer,primary_key=True,index=True)
    tag = Column(String(255),index=True)
    
class VocabTags(Base):
    __tablename__ = "vocabtags"
    id = Column(Integer,primary_key=True,index=True)
    vocab_id = Column(Integer,ForeignKey("vocab.id"))
    tag_id = Column(Integer,ForeignKey("tags.id"))


# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer,primary_key=True,index=True)
#     name = Column(String(255),index=True)
#     email = Column(String(255), unique=True, index=True)
#     todos = relationship("Todo",back_populates="owner")
#     is_active = Column(Boolean,default=False)



# class Todo(Base):
#     __tablename__ = "todos"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(255), index=True)
#     description = Column(String(255), index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User",back_populates="todos")