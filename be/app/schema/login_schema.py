from pydantic import BaseModel, EmailStr

class UsersInLogIn(BaseModel):
    email: EmailStr = 'muhalibakhtiar@gmail.com'
    password: str = 'muhalibakhtiar070194'



class RefreshInLogIn(BaseModel):
    email: EmailStr