#auth.py

from fastapi import Depends,HTTPException

from models import User
from sqlalchemy.orm import Session

from schemas import(
    UserLogin,
    UserResponse,
)

from utils import verify_password, create_access_token, get_current_user
from database import get_db

from fastapi import APIRouter
router = APIRouter(
    tags=["Auth"]
)
#----------------------LOGIN------------------------------------------
@router.post('/login')
def login(
    user_data:UserLogin,
    db:Session=Depends(get_db)
):
    
    user= db.query(User).filter(User.email== user_data.email).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Invalid credintials"
        )
    
    is_valid = verify_password(
        user_data.password,
        user.password
    )


    if not is_valid:
        raise HTTPException(
            status_code=401,
            detail='Invalid password'
        )
    
    token = create_access_token(
        {'user_id':user.id}
    )
    return {
        'access_token':token
    }

#---------------from learning purpose------------------------------
@router.get('/me', response_model=UserResponse)
def get_me(
    current_user = Depends(
        get_current_user
    )
):
    
    return current_user
