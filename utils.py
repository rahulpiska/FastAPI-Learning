
from passlib.context import CryptContext
from jose import jwt, JWTError

from models import User
from database import get_db
from sqlalchemy.orm import Session

from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer

from datetime import datetime, timedelta

import os
from dotenv import load_dotenv

#=====password hashing =====we should import cryptcontext from passlib.context======
pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated = 'auto'
)

def hash_password(password:str):
    return pwd_context.hash(password)

def verify_password(
        plain_password: str,
        hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
#=========JWT===we do import from jose import jwt,jwterror===============

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")


def create_access_token(data:dict):

    to_encode = data.copy()

    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update(
         {"exp": expire}
    )

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm= ALGORITHM
    )

    return token

def verify_access_token(token:str):

    try:
        playload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        user_id = playload.get('user_id')

        return user_id

    except JWTError:
        return None


#--------------get_current_user---we should import------------
# from models import User
# from database import get_db
# from sqlalchemy.orm import Session

# from fastapi import Depends,HTTPException
# from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(
        token: str = Depends(oauth2_scheme),
        db:Session = Depends(get_db)
    ):

        user_id = verify_access_token(token)

        if user_id is None:
             raise HTTPException(
                  status_code=401,
                  detail='Invalid token'
             )

        user = db.query(User).filter(User.id == user_id).first()

        return user



