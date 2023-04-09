from db.hash import Hash
from sqlalchemy.orm.session import Session
from schemas import ArticleBase
from db.models import DbArticle
from fastapi import HTTPException, status
from exceptions import StoryError

def create_article(db: Session, request: ArticleBase):
    if request.content.startswith('hello'):
        raise StoryError('Hello is not allowed')
    
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        is_published = request.is_published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article


def get_article_by_id(db:Session,id:int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    if article is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Article with id {id} not found')
    return article