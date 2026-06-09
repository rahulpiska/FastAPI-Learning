#posts.py

from fastapi import Depends,HTTPException

from schemas import(
    PostCreate,
    PostResponse,
    PostUpdate,
    PostWithOwnerResponse,
)
from sqlalchemy.orm import Session
from utils import get_current_user
from models import User, Post

from database import get_db

from fastapi import APIRouter
router = APIRouter(
    prefix = "/posts",
    tags=["Posts"]
)

#=============================POSTS===============================================
#=============POSTCREATE FOR POSTS==================
@router.post('',response_model=PostResponse)
def create_post(post:PostCreate, 
                current_user:User = Depends(get_current_user),
                db:Session=Depends(get_db)):

    
    new_post = Post(
        title = post.title,
        content = post.content,
        user_id = current_user.id
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post



#==================post with owner response================
@router.get('/{id}',response_model=PostWithOwnerResponse)
def get_post_with_owner_response(id:int,db:Session=Depends(get_db)):

    post = db.query(Post).filter(Post.id == id).first()

    return post


#-============POST DELETE========================
@router.delete("/{id}")
def delete_posts(
    id: int,
    current_user:User = Depends(get_current_user),
    db:Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
    )
    
    if current_user.id != post.user_id:
        raise HTTPException(
            status_code=403,
            detail="forbidden"
    )
    db.delete(post)
    db.commit()
    return{
        'Message':"Post Deleted successfully"
    }

#===========UPDATE POST =====================================
@router.put('/{id}',response_model=PostResponse)
def update_post(id:int,
                update_post:PostUpdate,
                current_user:User = Depends(get_current_user),
                db:Session = Depends(get_db)):
    
    post = db.query(Post).filter(Post.id == id ).first()

    if not post:
        raise HTTPException(
            status_code=404,
            detail="Post not found"
    )
    
    if current_user.id != post.user_id:
        raise HTTPException(
            status_code=403,
            detail="Forbidden"
    )
    
    if update_post.title is not None:
        post.title = update_post.title
    if update_post.content is not None:
        post.content = update_post.content

    db.commit()
    db.refresh(post)

    return post