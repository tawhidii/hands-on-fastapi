from sqlalchemy.orm import Session

from schemas import ArticleBase, ArticleDisplay,UserResopnse
from fastapi import APIRouter, Depends
from db import db_article
from db.database import get_db
from auth.oauth2 import get_current_user


router = APIRouter(prefix='/article', tags=['article'])

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
  return db_article.create_article(db, request)

#get article by id
@router.get('/{id}')
def get_article_by_id(id: int, db: Session = Depends(get_db),current_user: UserResopnse = Depends(get_current_user)):
  return{
    'article': db_article.get_article_by_id(db, id),
    'user': current_user
  } 