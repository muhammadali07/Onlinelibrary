
from models import (
    users_model,
    book_model 
)
from schema import (
    Book, Users
)
from sqlalchemy.future import select
from sqlalchemy import and_, or_, desc, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from service import ResponseOutCustom, loging
from graphviz import Digraph,Graph

log = loging()

async def create_new_book(request: Book , db: AsyncSession):
    async with db as session:
        try:
            
            data = book_model.Book(
                book_name=request.book_name,
                book_category=request.book_category,
                book_status="available",
                book_qty=request.book_qty,
                book_price=request.book_price,
                book_desc=request.book_desc,
                created_at=datetime.now()
            )
            session.add(data)
            await session.commit()

            return ResponseOutCustom(message_id="00", status="Tambah data buku baru berhasil", list=request)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f"{str(e)}", list_data=[])


async def get_list_book(limit, page, keyword, db: AsyncSession):
    async with db as session:
        try:
            offset = page * limit
            terms = []

            if keyword not in (None, [],''):
                terms.append(
                    or_(
                        (book_model.Book.book_name.ilike(f'%{keyword}%')),
                        (book_model.Book.book_category.ilike(f'%{keyword}%'))
                    )
                )
                
            if terms not in (None, []):
                query_stmt = select(book_model.Book).filter(*(terms)).limit(limit).offset(offset).order_by(desc(book_model.Book.created_at))
            else:
                query_stmt = select(book_model.Book).limit(limit).offset(offset).order_by(desc(book_model.Book.created_at))
            
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().all()
            datas = jsonable_encoder(result)

            status = 'Berhasil' if datas not in (None, []) else 'Data tidak ditemukan'

            return ResponseOutCustom(message_id="00", status=status, list_data=datas)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])

async def get_book_by_id(request,db: AsyncSession):
    async with db as session:
        try:
            query_stmt = select(book_model.Book).where(book_model.Book.id == request)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()
            datas = jsonable_encoder(result)

            status = 'Berhasil' if datas not in (None, []) else 'Data tidak ditemukan'

            return ResponseOutCustom(message_id="00", status=status, list_data=datas)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])


async def update_book_by_id(data:Book,db: AsyncSession):
    async with db as session:
        try:
            
            # get data anak
            book = book_model.Book
            query_stmt = select(book).where(book.id==data.id)
            
            log.info(query_stmt)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()
            
            if result in (None, []):
                return ResponseOutCustom(message_id="02", status=f'Data buku dengan {data.id} tidak ditemukan', list_data=[])

            update_data_book = update(book).where(book.id==result.id).values(
                book_name = data.book_name,
                book_category = data.book_category,
                book_qty = data.book_qty,
                book_price = data.book_price,
                book_desc = data.book_desc

            )
            await session.execute(update_data_book)
            await session.commit()

            return ResponseOutCustom(message_id="00", status=f"Pembaharuan buku {data.id} berhasil", list_data=data)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])
        
async def delete_book_by_id(data,db: AsyncSession):
    async with db as session:
        try:
            book = book_model.Book
            query_stmt = select(book).where(book.id==data)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()

            if result in (None, []):
                return ResponseOutCustom(message_id="02", status=f'Data buku dengan ID {data} tidak ditemukan', list_data=[])

            delete_data_cucu = delete(book).where(book.id==result.id)
            await session.execute(delete_data_cucu)
            await session.commit()

            return ResponseOutCustom(message_id="00", status=f"Hapus data buku ID {data} berhasil", list_data=data)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])
