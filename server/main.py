# -*- coding: utf-8 -*-
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

import uvicorn
#from fastapi import FastAPI


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

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


@app.post("/pairs/",response_model=schemas.Pair)
def post_pair(pair:schemas.PairCreate, db:Session=Depends(get_db)):
    # db_pair = crud.get_pair_per_topic(db, topic_name=pair.topic, chapter_name=pair.chapter)
    # if db_pair:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_pair(db=db,pair=pair)

@app.get("/pairs/", response_model=list[schemas.Pair])
def get_pair(db:Session=Depends(get_db)):
    pairs = crud.get_pairs(db)
    return pairs

@app.get("/pairs/topic/{topic_name}/chapter/{chapter_name}", response_model=list[schemas.Pair])
def get_pair_from_topic(topic_name: str, chapter_name: str, db:Session=Depends(get_db)):
    pairs = crud.get_pairs_from_topic(db, topic_name=topic_name, chapter_name=chapter_name)
    return pairs

@app.get("/pairs/{pair_id}/",response_model=schemas.Pair)
def get_pair(pair_id:int, db:Session=Depends(get_db)):
    db_pair = crud.get_pair(db, pair_id=pair_id )
    if db_pair is None:
        raise HTTPException(status_code=404, detail="Pair not found")
    return db_pair

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

