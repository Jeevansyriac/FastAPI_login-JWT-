import uvicorn
import app.db
import app.schema
import app.models
from app.db import Base

from sqlalchemy.orm import Session
from fastapi import FastAPI,Body,Depends

from app.auth.auth_handler import signJWT
from app.auth.jwt_bearer import JWTBearer

from app.db import SessionLocal, engine


Base.metadata.create_all(bind=engine)

db = SessionLocal()



users = []

app = FastAPI()


# (tags is used for grouping)

# Get all Posts
# @app.get("/posts", tags=["books"])
# def get_posts():
#     return { "data": posts }

# get a post by id..
@app.get("/posts/{id}",dependencies=[Depends(JWTBearer())], tags=["books"])
def  get_user(id:str):
    receive_book = db.query(models.book).filter(models.book.id==id).first()
    return receive_book





# @app.post("/posts",dependencies=[Depends(JWTBearer())], tags=["books"])
# def add_post(post: PostSchema):
#     post.id = len(posts) + 1
#     posts.append(post.dict())
#     return {
#         "data": "post added."
#     }

# @app.get("/user", tags=["user"])
# def get_user():
#     return {"data": users}
    
# # for user signup

# @app.post("/user/signup", tags=["user"])
# def user_signup(user: UserSchema = Body(default=None)):
#     users.append(user) 
#     return signJWT(user.email)

# def check_user(data: UserLoginSchema):
#     for user in users:
#         if user.email == data.email and user.password == data.password:
#             return True
#         return False




# @app.post("/user/login", tags=["user"])
# def user_login(user: UserLoginSchema = Body(default=None)):
#     if check_user(user):
#         return signJWT(user.email)
#     return {
#         "error": "Wrong login details!"
#     }