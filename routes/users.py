#users.py
from fastapi import Depends, HTTPException
from models import User

from sqlalchemy.orm import Session
from schemas import(
    UserCreate,
    UserResponse,
    UserUpdate
)
from utils import hash_password


from database import get_db

from fastapi import APIRouter

router= APIRouter(
    prefix = "/users",
    tags=["Users"]
)

#======GET USERS==================
@router.get('')
def get_users(db:Session = Depends(get_db)):

    users = db.query(User).all()

    return users

#------------POST USERS----------------------------
@router.post('', response_model=UserResponse)
def create_user(user:UserCreate,
                db:Session = Depends(get_db)):
    
    hashed_password = hash_password(user.password)
    
    new_user = User(
        name=user.name,
        email=user.email,
        password = hashed_password
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return new_user

#============get user by id===============
@router.get("/{id}",response_model=UserResponse)
def get_user_by_id(id:int, db:Session=Depends(get_db)):
    
    
    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return user

#=========UPDATE [PUT]===============
@router.put('/{id}',response_model= UserResponse)
def update_user(id:int,user_update:UserUpdate ,db:Session= Depends(get_db)):

    user = db.query(User).filter(User.id == id).first()


    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if user_update.name is not None:
        user.name = user_update.name
    
    if user_update.email is not None:
        user.email = user_update.email
    
    
    db.commit()
    db.refresh(user)
    
    return user
        
#=========DELETE==================
@router.delete('/{id}')
def delete_user(id:int,db:Session= Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail= 'User not found'
        )
    
    db.delete(user)
    db.commit()
    return {'message':'User deleted successfully'}

#===========================================
#===========GET POSTS BY USER id================
@router.get('/{id}/posts')
def get_user_posts(id:int, db:Session= Depends(get_db)):


    user = db.query(User).filter(User.id == id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail='User not found'
        )
    
    return user.posts