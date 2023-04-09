from pydantic import BaseModel
from typing import Text,List

class Airticle(BaseModel):
  id: int
  title : str
  content: Text
  is_published: bool

  class Config():
    orm_mode = True
    

class UserBase(BaseModel):
  username: str
  email: str
  password: str



class UserDisplay(BaseModel):
  username: str
  email: str
  articles: List[Airticle] = []

  class Config():
    orm_mode = True

  
class ArticleBase(BaseModel):
  title: str
  content: Text
  is_published: bool
  creator_id: int


class User(BaseModel):
  username: str
  email: str

  class Config():
    orm_mode = True

class ArticleDisplay(BaseModel):
  title: str
  content: Text
  is_published: bool
  user: User

  class Config():
    orm_mode = True