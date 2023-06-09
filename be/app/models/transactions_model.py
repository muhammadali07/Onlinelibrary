from sqlalchemy import (
    Column, String, 
    BigInteger, Text, 
    DateTime, ForeignKey
    )
from datetime import datetime
from service import Base

import uuid

class Transactions(Base):
    __tablename__ = 'transactions'
    id = Column(BigInteger, primary_key=True)
    book_id = Column(BigInteger)
    jenis_transaksi = Column(String(50))
    id_user = Column(String(50))
    status = Column(String(50))
    keterangan = Column(Text)
    created_at = Column(DateTime, default=datetime.now())