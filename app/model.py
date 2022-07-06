
from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id:      int = Field(default=None)
    title:   str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_demo = {
                "demo"    : {
                "title"   : "give a title.",
                "content" : "give some content"
            }
        }
    
class UserSchema(BaseModel):
    fullname:   str = Field(default=None)
    email:      EmailStr = Field(default=None)
    password:   str = Field(default=None)

    class Config:   #for formate

        schema_demo1 = {
            "example": {
                "fullname"  : "sam",
                "email"     : "sam@gmail.com",
                "password"  : "password"
            }
        }

class UserLoginSchema(BaseModel):
    email:      EmailStr = Field(default=None)
    password:   str = Field(default=None)

    class Config:
        schema_demo2 = {
            "example"       : {
                "email"     : "sam@gmail.com",
                "password"  : "password"
            }
        }
