from schema import UsersInLogIn , RefreshInLogIn
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from service import get_async_session, verify_token
from crud import login_crud

router = APIRouter()

@router.post("/login", )
async def login(
    data: UsersInLogIn, 
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await login_crud.login(
        data, db
    )
    return out_resp

@router.post("/refresh-token", )
async def refresh_token(
    user_info : dict = Depends(verify_token),
    ):
    
    out_resp = await login_crud.create_refresh_token(
        user_info
    )
    return out_resp

