from enum import unique
from operator import index
from sqlalchemy import  Column, Integer, String,true
from db import Base
from sqlalchemy.orm import relationship
from pydantic import BaseModel, Field, EmailStr



class book(Base):
    __tablename__ ="book_table"
    id           = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    title        =   Column(String(255), index=True, nullable=False)
    price        = Column(String(255), index=True, nullable=False)

    
class User(Base):
    
    __tablename__ = "user_table"
    id            = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    name          = Column(String(255), index=True, nullable=False)
    email         = Column(String(100), index=True, nullable=False,unique=True)


class UserLogin(Base):
    __tablename__="userlogin_table"
    id            = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    email        = Column(String(100), index=True, nullable=False,unique=True)
    password     = Column(String(255), index=True, nullable=False)