from fastapi import APIRouter

from .users_api import *

api_router = APIRouter()

api_router.include_router(users_api.router, prefix='/users', tags=['Users'])

