from pydantic import BaseModel

class Transactions(BaseModel): #buat test create user
    book_id : int = 1
    jenis_transaksi : str = "P"
    keterangan : str = "Pinjam buku"
    


