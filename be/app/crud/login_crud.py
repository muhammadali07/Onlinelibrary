
from models import (
    users_model,
    book_model 
)
from schema import (
    UsersInLogIn
)
from sqlalchemy.future import select
from sqlalchemy import and_, or_, desc, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from service import ResponseOutCustom, loging, create_access_token, refresh_token
from datetime import timedelta

log = loging()

#* SET TIME FOR TOKEN
ACCESS_TOKEN_EXPIRE_MINUTES = 30

async def login(request: UsersInLogIn , db: AsyncSession):
    async with db as session:
        try:
            
            getUser = await get_user_exist(request.email, db)
            print(getUser)
            if not getUser:
                return ResponseOutCustom(
                    message_id="02",
                    status="User tidak ditemukan",
                    list_data=[]
                )
            if request.password != getUser['password']:
                return ResponseOutCustom(
                    message_id="03",
                    status="Password salah",
                    list_data=[]
                )
            else:
                dt = {
                        "username": getUser['email'],
                        "password": getUser['password'],
                        "role": getUser['role'],
                        "access_date": str(datetime.now())
                    }
                
                _token = create_access_token(data=dt, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))


                return ResponseOutCustom(message_id="00", status="Login berhasil", list={"token_bearer": _token})
            
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f"{str(e)}", list_data=[])
        
async def create_refresh_token(request:dict):
    try:
        dt = {
            "username": request.get('username', ''),
            "password": request.get('password', ''),
            "role": request.get('role', ''),
            "access_date": str(datetime.now())
        }
        refreshToken = await refresh_token(dt)
        return refreshToken
        
        
    except Exception as e:
        return ResponseOutCustom(message_id="03", status=f"{str(e)}", list_data=[])
    

async def get_user_exist(request, db: AsyncSession):
    async with db as session:
        try:
            users = users_model.Users
            query_stmt = select(users).where(users.email == request)
            proxy_row = await session.execute(query_stmt)
            result = proxy_row.scalars().first()

            return jsonable_encoder(result)
        
        except Exception as e:
            return ResponseOutCustom(message_id="03", status=f"{str(e)}", list_data=[])


