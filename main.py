import uvicorn
from fastapi import FastAPI,Body,Depends
from app.model import PostSchema,UserSchema, UserLoginSchema
from app.auth.auth_handler import signJWT
from app.auth.jwt_bearer import JWTBearer


#not using db so give some data here

posts = [
    {
        "id": 1,
        "title": "book ",
        "price": "200"
    },
    
    {
        "id": 2,
        "title": "book2 ",
        "price": "299"
    },
    {
        "id": 3,
        "title": "book3 ",
        "price": "100"
    },
    
    {
        "id": 2,
        "title": "book4 ",
        "price": "199"
    }
]

users = []

app = FastAPI()


# (tags is used for grouping)

# Get all Posts
@app.get("/posts", tags=["books"])
def get_posts():
    return { "data": posts }

# get a post by id..
@app.get("/posts/{id}",dependencies=[Depends(JWTBearer())], tags=["books"])
def get_single_post(id: int):
    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }



@app.post("/posts",dependencies=[Depends(JWTBearer())], tags=["books"])
def add_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }

@app.get("/user", tags=["user"])
def get_user():
    return {"data": users}
    
# for user signup

@app.post("/user/signup", tags=["user"])
def user_signup(user: UserSchema = Body(default=None)):
    users.append(user) 
    return signJWT(user.email)

def check_user(data: UserLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
        return False




@app.post("/user/login", tags=["user"])
def user_login(user: UserLoginSchema = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }