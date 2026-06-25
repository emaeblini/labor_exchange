from datetime import datetime
from decimal import Decimal

from bases.base_alchemy_model import Base
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Job(Base):
    __tablename__ = 'jobs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)

    title: Mapped[str] = mapped_column(String, nullable=False)

    description: Mapped[str] = mapped_column(String, nullable=False)

    salary_from: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    salary_to: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)

    user = relationship('User', back_populates='jobs')

    responses = relationship('Response', back_populates='job', cascade='all, delete-orphan')