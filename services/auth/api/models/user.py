from uuid import uuid4

from sqlalchemy import TIMESTAMP, UUID, Boolean, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid4)
    username = Column(String(140), nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String(140), nullable=False, unique=True)
    is_active = Column(Boolean, default=False)
    profile_id = Column(Integer, ForeignKey('profiles.id'), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('NOW()'))
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False, default=text('NOW()'), onupdate=text('NOW()'))

    profile = relationship('Profile', back_populates='user')
