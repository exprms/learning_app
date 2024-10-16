# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session

import models, schemas

def get_pair(db: Session, pair_id: int):
    return db.query(models.Pair).filter(models.Pair.id == pair_id).first()

def get_pairs_from_topic(
        db: Session, 
        topic_name: str, 
        chapter_name: str
        ):
    return db.query(models.Pair).filter(models.Pair.topic == topic_name, models.Pair.chapter == chapter_name).all()

def get_pairs(db: Session):
    return db.query(models.Pair).all()

def create_pair(db: Session, pair: schemas.PairCreate):
    db_pair = models.Pair(
        topic=pair.topic,
        chapter=pair.chapter,
        mode=pair.mode,
        left=pair.left,
        right=pair.right)
    
    db.add(db_pair)
    db.commit()
    db.refresh(db_pair)
    return db_pair

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip:int=0, limit:int=100):
#     # return db.query(models.User).offset(skip).limit(limit).all()
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user:schemas.UserCreate):
#     db_user = models.User(email=user.email,
#                           name=user.name)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user


# def get_todos(db: Session, skip:int=0, limit: int=100):
#     return db.query(models.Todo).offset(skip).limit(limit).all()


# def create_user_todo(db:Session, todo:schemas.TodoCreate, user_id : int):
#     db_todo = models.Todo(**todo.model_dump(),owner_id=user_id )
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo''

