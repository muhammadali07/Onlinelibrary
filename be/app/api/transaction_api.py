from schema import Transactions
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from service import get_async_session, verify_token
from crud import transaction_crud

router = APIRouter()

@router.post("/create-new-pinjaman-buku", )
async def create_new_user(
    data: Transactions, 
    db: AsyncSession = Depends(get_async_session),
    user_info : dict = Depends(verify_token)
    ):
    out_resp = await transaction_crud.create_new_trasancation(
        data,user_info, db
    )
    return out_resp
    
@router.get("/get-list-pinjman-buku", )
async def get_list_pinjman_buku(
    user_info : dict = Depends(verify_token),
    db: AsyncSession = Depends(get_async_session),
    limit : int = 10,
    page : int = 0,
    keyword : str = ''
    ):
    out_resp = await transaction_crud.get_list_pinjman_buku(limit, page, keyword, user_info,db)
    return out_resp

@router.get("/get-list-data-buku", )
async def get_list_buku(
    user_info : dict = Depends(verify_token),
    db: AsyncSession = Depends(get_async_session),
    limit : int = 10,
    page : int = 0,
    keyword : str = ''
    ):
    out_resp = await transaction_crud.get_list_buku(limit, page, keyword, db)
    return out_resp

@router.put("/create-pengembalian-pinjaman-buku", )
async def create_pengembalian_buku(
    data: Transactions, 
    user_info : dict = Depends(verify_token),
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await transaction_crud.create_pengembalian_buku(
        data, user_info, db
    )
    return out_resp

