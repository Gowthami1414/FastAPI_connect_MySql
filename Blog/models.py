from sqlalchemy import Boolean,Column,Integer,String
from Blog.database import Base

class User(Base):
    __tablename__='users'
    
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,nullable=False)
class Post(Base):
    __tablename__='posts'
    
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(50),nullable=False)
    content=Column(String(100),nullable=False)
    user_id=Column(Integer)