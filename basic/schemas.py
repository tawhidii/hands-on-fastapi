from pydantic import BaseModel
from typing import Text

class Airticle(BaseModel):
  id: int
  title : str
  content: Text
  is_published: bool

  class Config:
    orm_mode = True



class UserBase(BaseModel):
  username: str
  email: str
  password: str

class UserDisplay(BaseModel):
  username: str
  email: str
  

  class Config():
    orm_mode = True