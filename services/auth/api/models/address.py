from sqlalchemy import Column, Integer, String

from .database import Base


class Address(Base):
    __tablename__ = 'addresses'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    country = Column(String(140), nullable=False)
    city = Column(String(140), nullable=False)
    zip_code = Column(String(10), nullable=False, default='')
    street = Column(String(140), nullable=False, default='')
    number = Column(Integer, nullable=True)
