from datetime import datetime

from bases.base_alchemy_model import Base
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)

    name: Mapped[str] = mapped_column(String, nullable=False)

    hashed_password: Mapped[str] = mapped_column(String, nullable=False)

    is_company:Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    jobs = relationship('Job', back_populates='user', cascade='all, delete-orphan')

    responses = relationship('Response', back_populates='user', cascade='all, delete-orphan')