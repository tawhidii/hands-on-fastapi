from sqlalchemy.orm import Session

from schemas import ArticleBase, ArticleDisplay
from fastapi import APIRouter, Depends
from db import db_article
from db.database import get_db


router = APIRouter(prefix='/article', tags=['article'])

# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
  return db_article.create_article(db, request)

#get article by id
@router.get('/{id}', response_model=ArticleDisplay)
def get_article_by_id(id: int, db: Session = Depends(get_db)):
  return db_article.get_article_by_id(db, id)