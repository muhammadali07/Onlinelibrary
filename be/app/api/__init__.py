from fastapi import APIRouter

from .users_api import *
from .book_api import *
from .transaction_api import *
from .login_api import *

api_router = APIRouter()

api_router.include_router(login_api.router, prefix='/access', tags=['Access'])
api_router.include_router(users_api.router, prefix='/users', tags=['Users'])
api_router.include_router(book_api.router, prefix='/books', tags=['Books'])
api_router.include_router(transaction_api.router, prefix='/transactions', tags=['Transactions'])

