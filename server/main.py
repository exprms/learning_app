# -*- coding: utf-8 -*-
import uvicorn
import logging
import json

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import server.crud as crud
import server.schemas as schemas
from server.database import SessionLocal, engine, Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)
logger.info("API is starting up")
logger.info(uvicorn.Config.asgi_version)

@app.get("/")
async def index():
   return {"message": "Hello World"}


#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()


@app.get("/pair/{pair_id}", response_model=list[schemas.Pair])
def get_pair(pair_id: int, db:Session=Depends(get_db)):
    sql_stmt = crud.query_maker(q_type='pair_by_where', where_clause=f" where id = {pair_id}")
    logger.debug(sql_stmt)
    #pairs = crud.get_pair(db=db, where_clause=f" where id = {pair_id}")
    pairs = crud.get_pair(db=db, sql_stmt=sql_stmt)
    return pairs

@app.post("/pair/pair_by_tags/", response_model=list[schemas.Pair])
def get_pair_by_tags(tag_list: schemas.TagList, db:Session=Depends(get_db)):
    if len(tag_list.tags)>0:
        sql_stmt = crud.query_maker(q_type='pair_by_tags', tag_list=tag_list.tags)
        logger.debug(sql_stmt)
        pairs = crud.get_pair(db=db, sql_stmt=sql_stmt)
    else:
        pairs = crud.get_pair(db=db)
    return pairs

@app.get("/tags/", response_model=list[str])
def get_tags(db:Session=Depends(get_db)):
    return crud.get_tags(db=db)
# @app.post("/pair", response_model=schemas.Pair)
# def post_pair(pair:schemas.PairCreate, db:Session=Depends(get_db)):
#     # db_pair = crud.get_pair_per_topic(db, topic_name=pair.topic, chapter_name=pair.chapter)
#     # if db_pair:
#     #     raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_pair(db=db,pair=pair)

# @app.get("/pair/pair_by_word/{left}", response_model=schemas.Pair)
# def get_pair(left: str, db:Session=Depends(get_db)):
#     pairs = crud.get_pair(db=db, left=left)
#     return pairs

# @app.post("/tag",response_model=schemas.Tag)
# def post_tag(tag:schemas.TagCreate, db:Session=Depends(get_db)):
#     # db_pair = crud.get_pair_per_topic(db, topic_name=pair.topic, chapter_name=pair.chapter)
#     # if db_pair:
#     #     raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_tag(db=db,tag=tag)


# @app.get("/tag/by_id/{tag_id}", response_model=schemas.Tag)
# def get_tag(tag_id: int, db:Session=Depends(get_db)):
#     tags = crud.get_tag(db=db, tag_id=tag_id)
#     return tags

# @app.get("/tag/by_name/{tag}", response_model=schemas.Tag)
# def get_tag(tag: str, db:Session=Depends(get_db)):
#     tags = crud.get_tag(db=db, tag=tag)
#     return tags

# @app.get("/pairs/topic/{topic_name}/chapter/{chapter_name}", response_model=list[schemas.Pair])
# def get_pair_from_topic(topic_name: str, chapter_name: str, db:Session=Depends(get_db)):
#     pairs = crud.get_pairs_from_topic(db, topic_name=topic_name, chapter_name=chapter_name)
#     return pairs

# @app.get("/chapters/{topic_name}", response_model=list[schemas.Chapter])
# def get_chapters_from_topic(topic_name: str, db:Session=Depends(get_db)):
#     chapters = crud.get_chapters_from_topic(db, topic_name=topic_name)
#     return chapters




# @app.get("/pairs/{pair_id}/",response_model=schemas.Pair)
# def get_pair(pair_id:int, db:Session=Depends(get_db)):
#     db_pair = crud.get_pair(db, pair_id=pair_id )
#     if db_pair is None:
#         raise HTTPException(status_code=404, detail="Pair not found")
#     return db_pair

# @app.post("/users/",response_model=schemas.User)
# def post_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db,user=user)


# @app.get("/users/", response_model=list[schemas.User])
# def get_users(skip:int=0, limit:int=0, db:Session=Depends(get_db)):
#     users = crud.get_users(db,skip=skip,limit=limit)
#     return users


# @app.get("/users/{user_id}/",response_model=schemas.User)
# def get_user(user_id:int, db:Session=Depends(get_db)):
#     db_user = crud.get_user(db,user_id =user_id )
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user


# @app.post("/users/{user_id}/todos/",response_model=schemas.Todo)
# def post_todo_for_user(user_id:int, todo:schemas.TodoCreate, db:Session=Depends(get_db)):
#     return crud.create_user_todo(db=db,user_id=user_id, todo=todo)


# @app.get("/todos/", response_model=list[schemas.Todo])
# def get_todos(skip:int=0,limit:int=100,db:Session=Depends(get_db)):
#     todos = crud.get_todos(db,skip=skip,limit=limit)
#     return todos



if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

