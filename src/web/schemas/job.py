from datetime import datetime
from decimal import Decimal

from bases.base_web_schema import BaseWebSchema, ConfigMixin
from models.dto.job import JobCreateDTO, JobDTO


class JobCreate(BaseWebSchema):
    user_id: int
    title: str
    description: str
    salary_from: Decimal
    salary_to: Decimal

    def to_dto(self) -> JobCreateDTO:
        return JobCreateDTO(
            user_id=self.user_id,
            title=self.title,
            description=self.description,
            salary_from=self.salary_from,
            salary_to=self.salary_to,
        )


class Job(BaseWebSchema, ConfigMixin):
    id: int
    user_id: int
    title: str
    description: str
    salary_from: Decimal
    salary_to: Decimal
    is_active: bool
    created_at: datetime

    @classmethod
    def from_dto(cls, job: JobDTO) -> "Job":
        return cls.model_validate(job)