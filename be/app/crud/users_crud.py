
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

async def create_new_user(request: Users , db: AsyncSession):
    async with db as session:
        try:
            
            data = users_model.Users(
                email=request.email,
                username=request.username,
                password=request.password,
                role="guest",
                created_at=datetime.now()
            )
            session.add(data)
            await session.commit()

            return ResponseOutCustom(message_id="00", status="Create User Successfully", list=request)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f"{str(e)}", list_data=[])


async def get_list_users(limit, page, keyword, db: AsyncSession):
    async with db as session:
        try:
            offset = page * limit
            terms = []

            if keyword not in (None, [],''):
                terms.append(
                    or_(
                        (users_model.Users.username.ilike(f'%{keyword}%')),
                        (users_model.Users.email.ilike(f'%{keyword}%'))
                    )
                )
                
            if terms not in (None, []):
                query_stmt = select(users_model.Users).filter(*(terms)).limit(limit).offset(offset).order_by(desc(users_model.Users.created_at))
            else:
                query_stmt = select(users_model.Users).limit(limit).offset(offset).order_by(desc(users_model.Users.created_at))
            
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().all()
            datas = jsonable_encoder(result)

            status = 'Success' if datas not in (None, []) else 'Data tidak ditemukan'

            return ResponseOutCustom(message_id="00", status=status, list_data=datas)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])

async def get_users_by_email(request,db: AsyncSession):
    async with db as session:
        try:
            query_stmt = select(users_model.Users).where(users_model.Users.email == request)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()
            datas = jsonable_encoder(result)

            status = 'Success' if datas not in (None, []) else 'Data tidak ditemukan'

            return ResponseOutCustom(message_id="00", status=status, list_data=datas)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])


async def update_user_by_email(data:Users,db: AsyncSession):
    async with db as session:
        try:
            
            # get data anak
            users = users_model.Users
            query_stmt = select(users).where(users.email==data.email)
            
            log.info(query_stmt)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()

            if result in (None, []):
                return ResponseOutCustom(message_id="02", status=f'Data user dengan {data.email} tidak ditemukan', list_data=[])

            update_data_users = update(users).where(users.email==data.email).values(
                username = data.username,
                role = data.role,
                password = data.password
            )
            await session.execute(update_data_users)
            await session.commit()

            return ResponseOutCustom(message_id="00", status=f"Update users {data.email} berhasil", list_data=data)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])
3

async def delete_data_cucu(data,db: AsyncSession):
    async with db as session:
        try:
            
            # get data anak
            users = users_model.Users
            query_stmt = select(users).where(users.email==data.email)
            
            log.info(query_stmt)
            proxy_rows = await session.execute(query_stmt)
            result = proxy_rows.scalars().first()

            if result in (None, []):
                return ResponseOutCustom(message_id="02", status=f'Data user dengan {data.email} tidak ditemukan', list_data=[])

            delete_data_cucu = delete(users).where(users.email==data)
            await session.execute(delete_data_cucu)
            await session.commit()

            return ResponseOutCustom(message_id="00", status=f"Delete Cucu anak dari {data.nama_anak} Success", list_data=data)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f'{e}', list_data=[])
