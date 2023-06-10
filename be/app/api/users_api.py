import re
from schema import Users, UsersUpdate
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from service import get_async_session, ResponseOutCustom
from crud import users_crud

router = APIRouter()

def validate_email(email: str) -> str:
    allowed_domains = ["gmail.com", "hotmail.com"]  # Daftar domain yang diizinkan

    regex_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(regex_pattern, email):
        raise ValueError("Format email tidak valid")

    domain = email.split("@")[1]
    if domain not in allowed_domains:
        raise ValueError("Domain email tidak diizinkan")

    return email

def validate_password(password: str) -> str:
    if len(password) < 8:
        raise ValueError("Password harus memiliki panjang minimal 8 karakter")

    regex_pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])[A-Za-z0-9]+$"
    if not re.match(regex_pattern, password):
        raise ValueError("Password harus terdiri dari minimal 1 huruf kapital, 1 huruf kecil, dan 1 angka")
    
    if any(char.isalnum() is False for char in password):
        raise ValueError("Password tidak boleh mengandung karakter khusus")
    return password

@router.post("/create-new-users", )
async def create_new_user(
    data: Users, 
    db: AsyncSession = Depends(get_async_session)
    ):
    try:
        data.email = validate_email(data.email)
        data.password = validate_password(data.password)
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
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.get_users_by_email(email, db)
    return out_resp

@router.put("/update-user-by-email", )
async def update_user_by_email(
    data: UsersUpdate, 
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.update_user_by_email(data, db)
    return out_resp


@router.delete("/delete-data-users", )
async def delete_data_uses(
    email:str,
    db: AsyncSession = Depends(get_async_session)
    ):
    out_resp = await users_crud.delete_user_by_email(email,db)
    return out_resp

