from pydantic import BaseModel

class Book(BaseModel): #buat test create user
    book_name : str = "Python Programming"
    book_category : str = "Computer Science"
    book_date_brw : str = ""
    book_date_rtn : str = ""
    book_date_drs : int = 0
    book_qty : int = 10
    book_price : float = 100000


