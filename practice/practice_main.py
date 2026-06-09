from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

class User(BaseModel):
    name:str
    email:str
    password:str

class UserCreate(BaseModel):
    name:str
    email:str
    password:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str

class UserUpdate(BaseModel):
    name:str |None=None
    email:str |None=None
    password:str|None=None


app = FastAPI()

users = []


@app.get("/hello")
def say_hello():
    return {"message": "Hello Rahul"}

# @app.get('/users/{user_id}')
# def get_user(user_id: int):
#     return {'user_id':user_id}

@app.get("/search")
def search_product(name:str):
    return {"product": name}

@app.get("/products")
def get_products(
    category: str= None,
    brand: str= None
):
    return{
        'category':category,
        "brand": brand
    }

@app.post("/signup")
def signup(user:User):
    return{
        "name": user.name,
        "email":user.email
    }
#----------------------------------------


@app.post('/user_signup',response_model=UserResponse)
def new_signup(user: UserCreate):
    return user


@app.post('/users',response_model=UserResponse)
def create_user(user:UserCreate):

    new_user={
        'id': len(users)+1,
        "name":user.name,
        "email":user.email,
        "password":user.password
   }
    
    users.append(new_user)

    return new_user

@app.get('/users',response_model=list[UserResponse])
def get_users():
    return users

@app.get('/users/{id}',response_model=UserResponse)
def get_user_by_id(id:int):

    for user in users:

        if user["id"] == id:
            return user
    
    raise HTTPException(
        status_code=404,
        detail='User not found'
    )

@app.put('/users/{id}',response_model=UserResponse)
def Update_user(id:int,user_update:UserUpdate):
    
    for user in users:

        if user['id']== id:

            if user_update.name:
                user['name']= user_update.name
            if user_update.email:
                user['email'] = user_update.email
            if user_update.password:
                user['password']= user_update.password

            return user
        
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@app.delete('/users{id}')
def dalete_user(id:int):

    for user in users:

        if user['id']==id:
            users.remove(user)

            return{
                'message':'User deleted succussfully'
            }
        
    raise HTTPException(
        status_code=404,
        detail='User not found'
    )



