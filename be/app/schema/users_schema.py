from pydantic import BaseModel

class Users(BaseModel): #buat test create user
    email : str = "muhalibakhtiar@gmail.com"
    username : str = "muhalibakhtiar"
    password : str = "muhalibakhtiar070194"
    


