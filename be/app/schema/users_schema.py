from pydantic import BaseModel, constr, validator, EmailStr

class Users(BaseModel): #buat test create user
    email: EmailStr
    username: str
    password: str
    

class UsersUpdate(BaseModel): #buat test create user
    email : str = "muhalibakhtiar@gmail.com"
    username : str = "muhalibakhtiar"
    password : str = "muhalibakhtiar070194"
    role : str = "admin"
    


