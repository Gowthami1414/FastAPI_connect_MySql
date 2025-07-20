from fastapi import FastAPI,HTTPException,Depends,status
from pydantic import BaseModel
from typing import Annotated
from Blog import models
from Blog.database import engine,sessionlocal
from sqlalchemy.orm import Session

myapp=FastAPI()
models.Base.metadata.create_all(bind=engine)    # it creates tables automatically in mysql database based on the models

class PostBase(BaseModel):
    title:str
    content:str
    user_id:int
class UserBase(BaseModel):
    username:str
    
def get_db():
    db=sessionlocal()
    try:
        yield db 
    finally:
        db.close()
#PostTable      
@myapp.post("/posts/", status_code=status.HTTP_200_OK)
async def create_postm(post: PostBase, db: Annotated[Session, Depends(get_db)]):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    return {"message": "Content added successfully"}
@myapp.get("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def read_postm(post_id:int, db: Annotated[Session, Depends(get_db)]):
    post=db.query(models.Post).filter(models.Post.id==post_id).first()
    if post is None:
        raise HTTPException(status_code=404,detail='Post was not found')
    return post
#delete data from Post table by id

@myapp.delete("/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_postm(post_id:int, db: Annotated[Session, Depends(get_db)]):
    db_post=db.query(models.Post).filter(models.Post.id==post_id).first()
    if db_post is None:
        raise HTTPException(status_code=404,detail='Post was not found')
    db.delete(db_post)
    db.commit()
    

#USERTable

@myapp.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db: Annotated[Session, Depends(get_db)]):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    return {"message": "User created successfully"}
@myapp.get("/users/{user_id}", status_code=status.HTTP_201_CREATED)
async def read_user(user_id:int, db: Annotated[Session, Depends(get_db)]):
    user=db.query(models.User).filter(models.User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail='User not found')
    return user
    
    
    