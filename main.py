import uvicorn

import db
import model
import schema
from fastapi import FastAPI,Body,Depends

from auth_handler import signJWT
from jwt_bearer import JWTBearer

from db import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)
db = SessionLocal()

app = FastAPI(title="user registration")


users = []

app = FastAPI()


# (tags is used for grouping)

# Get all Posts
@app.get("/posts", tags=["books"])
def get_posts():
    get_post = db.query(model.book).all()
    return get_post


# get a post by id..
@app.get("/posts/{id}",dependencies=[Depends(JWTBearer())], tags=["books"])
def  get_user(id:str):
    receive_book = db.query(model.book).filter(model.book.id==id).first()
    return receive_book



@app.post("/posts",dependencies=[Depends(JWTBearer())], tags=["books"])
def add_post(data:schema.Base):
    try:
        add_posts= model.book(**data.dict())
        db.add( add_posts)
        db.commit()
        
         
        
    except:
         return{'db error'}
    return data,add_posts

@app.get("/user", tags=["user"])
def get_user():
    gert_users = db.query(model.book).all()
    return gert_users
    
# # for user signup

@app.post("/user/signup", tags=["user"])
def user_signup(user: schema.user = Body(default=None)):
    users.append(user) 
    return signJWT(user.email)

def check_user(data: schema.user):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False




@app.post("/user/login", tags=["user"])
def user_login(user: schema.userlogin = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }