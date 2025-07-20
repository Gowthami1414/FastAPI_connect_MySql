from fastapi import FastAPI
from pydantic import BaseModel, constr           #Pydantic is the most widely used data validation library for Python.
from typing import Optional,List

app=FastAPI()

class User_Input(BaseModel):
    title:str
    body:str
    name:Optional[str]=None
    

@app.post('/')
def create(title,Body):
    return {'title':'response successfully submitted','Body':'Thanks For Visiting'}

@app.post('/userinput')
def create(request_u:User_Input):
    return request_u   