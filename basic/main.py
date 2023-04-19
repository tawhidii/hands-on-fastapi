from typing import Optional
from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from router import blog_get
from router import blog_post
from router import user
from router import article
from router import product
from auth import authenticate
from db.database import engine
from db import models
from exceptions import StoryError


app = FastAPI()
app.include_router(authenticate.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(product.router)

@app.get('/hello')
def index():
  return {'message': 'Hello world!'}

@app.exception_handler(StoryError)
def story_error_handler(request: Request, exc: StoryError):
    return JSONResponse(
        status_code=418,
        content={"message": f"{exc.name}"},
    )

models.Base.metadata.create_all(engine)

