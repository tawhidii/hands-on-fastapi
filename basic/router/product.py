from typing import Optional
from fastapi import APIRouter,Header,Cookie,Form
from fastapi.responses import Response


router = APIRouter(prefix='/product', tags=['product'])

products = ['product1', 'product2', 'product3']


@router.post('/create')
def create_product(product:str =  Form(...)):
    products.append(product)
    return products

@router.get('/with-header')
def get_product_with_header(
    response: Response,
    custom_header: Optional[str] = Header(None),
    response_cookie: Optional[str] = Cookie(None)
    ):
    response.headers['response-headers'] = ', '.join(custom_header)
    return {
        "data": products,
        "test_cookie": response_cookie
    }

@router.get('/get-all-products')
def get_all_products(response: Response):
    response.set_cookie(key='response_cookie', value='response-cookie-value')
    return products