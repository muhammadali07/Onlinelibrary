from pydantic import BaseModel

class Book(BaseModel): #buat test create user
    book_name : str = "Python Programming"
    book_category : str = "Computer Science"
    book_qty : int = 10
    book_price : float = 100000
    book_desc : str = ""

class UpdateBook(BaseModel): #buat test create user
    id : int = 1
    book_name : str = "Python Programming"
    book_category : str = "Computer Science"
    book_qty : int = 10
    book_price : float = 100000
    book_desc : str = ""


