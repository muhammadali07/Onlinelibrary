from schema import Book, UpdateBook
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from service import get_async_session
from crud import book_crud

router = APIRouter()

@router.post("/create-new-book", )
async def create_new_user(
    data: Book, 
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await book_crud.create_new_book(
        data, db
    )
    return out_resp
    
@router.get("/get-list-book", )
async def get_list_book(
    db: AsyncSession = Depends(get_async_session),
    limit : int = 10,
    page : int = 0,
    keyword : str = ''
    ):
    out_resp = await book_crud.get_list_book(limit, page, keyword, db)
    return out_resp

@router.get("/get-book-by-id", )
async def get_user_by_email(
    id: int,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await book_crud.get_book_by_id(id, db)
    return out_resp

@router.put("/update-book-by-id", )
async def update_user_by_id(
    data: UpdateBook, 
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await book_crud.update_book_by_id(data, db)
    return out_resp


@router.delete("/delete-book-by-id", )
async def delete_data_uses(
    id:int,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await book_crud.delete_book_by_id(id,db)
    return out_resp

