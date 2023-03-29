from .database import Base
from sqlalchemy import Column, Integer, String,Text,Boolean
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


class DbUser(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, index=True)
  username = Column(String)
  email = Column(String)
  password = Column(String)
  articles = relationship('DbArticle',back_populates='user')

class DbArticle(Base):
  __tablename__ = 'articles'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(Text)
  is_published = Column(Boolean)
  user_id = Column(Integer,ForeignKey('users.id'))
  user = relationship('DbUser',back_populates='articles') 


