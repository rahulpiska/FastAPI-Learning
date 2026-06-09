from pydantic import BaseModel
from datetime import datetime


class UserCreate(BaseModel):
    name: str
    email : str
    password: str


class UserUpdate(BaseModel):#for PATCH & PUT
    name: str | None = None
    email: str | None = None

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

    class Config:
        from_attributes = True

#--------------------------------
class PostCreate(BaseModel):
    title :str
    content:str
    

class PostResponse(BaseModel):
    id : int
    title : str
    content: str
    user_id : int
    created_at:datetime
    updated_at:datetime

    class Config:
        from_attributes = True


class PostWithOwnerResponse(BaseModel):

    id: int
    title: str
    content: str

    owner: UserResponse

    class Config:
        from_attributes = True

#=============================================
class UserLogin(BaseModel):
    email: str
    password: str

class PostUpdate(BaseModel):
    title :str |None = None
    content:str | None = None
    