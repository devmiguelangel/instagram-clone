from sqlalchemy import TIMESTAMP, Column, Date, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from .database import Base


class Profile(Base):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    display_name = Column(String(140), nullable=False)
    phone = Column(String(15), nullable=False, default='')
    birth_date = Column(Date)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('NOW()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('NOW()'), onupdate=text('NOW()'))

    address = relationship('Address', back_populates='profile')
