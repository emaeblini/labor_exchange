from bases.base_alchemy_model import Base
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Response(Base):
    __tablename__ = 'responses'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    job_id: Mapped[int] = mapped_column(Integer, ForeignKey('jobs.id'), nullable=False)

    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), nullable=False)

    message: Mapped[str] = mapped_column(String, nullable=False)

    job = relationship('Job', back_populates='responses')

    user = relationship('User', back_populates='responses')