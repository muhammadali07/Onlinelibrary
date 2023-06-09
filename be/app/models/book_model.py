from sqlalchemy import (
    Column, String, 
    BigInteger, Text, 
    Integer, Float,
    DateTime, ForeignKey
    )
from datetime import datetime
from service import Base

class Book(Base):
    __tablename__ = 'book'
    id = Column(BigInteger, primary_key=True)
    book_name = Column(String(50), nullable=False)
    book_category = Column(String(50), nullable=False)
    book_status = Column(String(50))
    book_date_brw = Column(DateTime)
    book_date_rtn = Column(DateTime)
    book_date_drs = Column(Integer)
    book_qty = Column(Integer)
    book_price = Column(Integer)
    book_desc = Column(Text)
    created_at = Column(DateTime, default=datetime.now())