from sqlalchemy import Column, String, BigInteger, Text, DateTime
from datetime import datetime
from service import Base

class Users(Base):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    email = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    password = Column(Text)
    created_at = Column(DateTime, default=datetime.now())