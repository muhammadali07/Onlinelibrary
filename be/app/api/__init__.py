from fastapi import APIRouter

from .users_api import *
from .book_api import *

api_router = APIRouter()

api_router.include_router(users_api.router, prefix='/users', tags=['Users'])
api_router.include_router(book_api.router, prefix='/books', tags=['Books'])

