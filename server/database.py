# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from server.constants import DATABASE_FILEPATH, DATABASE_NAME

# 3 slashes for relative path
# 4 slashes for absolute path
# DB_URL = "sqlite:///learning_app.db"
DB_URL = "sqlite:///" + DATABASE_FILEPATH + DATABASE_NAME
engine = create_engine(DB_URL,echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

#print(Base.metadata)

