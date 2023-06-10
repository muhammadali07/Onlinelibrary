from schema import Users, UsersUpdate
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from service import get_async_session, ResponseOutCustom, utils, verify_token
from crud import users_crud

router = APIRouter()



@router.post("/create-new-users", )
async def create_new_user(
    data: Users, 
    db: AsyncSession = Depends(get_async_session)
    ):
    try:
        data.email = utils.validate_email(data.email)
        data.password = utils.validate_password(data.password)
        out_resp = await users_crud.create_new_user(data, db)
        return out_resp

    except ValueError as e:
        return ResponseOutCustom(
            message_id = "03",
            status = f'{e}',
            list_data = []
        )
    
@router.get("/get-list-users", )
async def get_list_users(
    user_info : dict = Depends(verify_token),
    db: AsyncSession = Depends(get_async_session),
    limit : int = 10,
    page : int = 0,
    keyword : str = ''
    ):
    out_resp = await users_crud.get_list_users(limit, page, keyword, db)
    return out_resp

@router.get("/get-user-by-email", )
async def get_user_by_email(
    email: str,
    user_info : dict = Depends(verify_token),
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.get_users_by_email(email, db)
    return out_resp

@router.put("/update-user-by-email", )
async def update_user_by_email(
    data: UsersUpdate, 
    user_info : dict = Depends(verify_token),
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.update_user_by_email(data, db)
    return out_resp


@router.delete("/delete-data-users", )
async def delete_data_uses(
    email:str,
    user_info : dict = Depends(verify_token),
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.delete_user_by_email(email,db)
    return out_resp

