from sqlalchemy import Column, Integer,String,ForeignKey

from database import Base

from sqlalchemy.orm import relationship


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer,primary_key= True, index=True)

    name = Column(String(100))

    email = Column(String(100),unique=True,nullable=False)

    password = Column(String(225))

    phone = Column(String(20))

    posts = relationship(
        'Post',
        back_populates='owner'
    )


#----------------------------------------------------
from sqlalchemy import DateTime
from datetime import datetime

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index = True)

    title = Column(String(200))

    content = Column(String(500))

    user_id = Column(
        Integer,
        ForeignKey('users.id')
    )
    created_at = Column(DateTime,default=datetime.utcnow)

    updated_at = Column(DateTime,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow
    )

    owner = relationship(
        'User',
        back_populates= 'posts'
    )