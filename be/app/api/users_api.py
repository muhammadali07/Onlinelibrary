from schema import Users
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from service import get_async_session
from crud import users_crud

router = APIRouter()

@router.post("/create-new-users", )
async def create_new_user(
    data: Users, 
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.create_new_user(
        data, db
    )
    return out_resp
    
@router.get("/get-list-users", )
async def get_list_users(
    db: AsyncSession = Depends(get_async_session),
    limit : int = 10,
    page : int = 0,
    keyword : str = ''
    ):
    out_resp = await users_crud.get_list_users(limit, page, keyword, db)
    return out_resp



@router.get("/get-user-by-email", )
async def get_user_by_email(
    db: AsyncSession = Depends(get_async_session),
    email=str
    ):
    out_resp = await users_crud.get_users_by_email(email, db)
    return out_resp

@router.put("/update-user-by-email", )
async def update_user_by_email(
    data: Users, 
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.update_user_by_email(data, db)
    return out_resp


# @router.put("/update_data_cucu", )
# async def update_data_cucu(
#     data: UpdateCucuBudi,
#     db: AsyncSession = Depends(get_async_session)
#     ):
#     out_resp = await users_crud.update_data_cucu(data,db)
#     return out_resp


@router.delete("/delete-data-users", )
async def delete_data_uses(
    email = str,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.delete_data_cucu(email,db)
    return out_resp

