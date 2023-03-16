from fastapi import FastAPI
from enum import Enum
from typing import Optional
app = FastAPI()


# example of path paramether
@app.get('/index/{id}')
def index(id:int):
    return {'message':f'the id is {id}'}




# example of predefined path
class DeliveryMethod(str,Enum):
    inside_dhaka = 'inside_dhaka'
    outside_dhaka = 'outside_dhaka'

@app.get('/delivery/{method}')
def delivery_method(method: DeliveryMethod):
     return {'message':f'{method} method is selected !'}


# example of query parameters 
@app.get('/all/products')
def get_all_products(page=1,page_size:Optional[int]=None):
    return {'message':f'total page {page} and page size {page_size}'}


# example of query parameter and path parameter same time
@app.get('/blog/{id}/liked/{like_id}')
def get_blog_like(id:int,like_id:int,username:Optional[str]=None):
    return {'message':f'Blog id {id}, like id {like_id} , user name {username}'}