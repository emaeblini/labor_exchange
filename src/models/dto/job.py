from datetime import datetime
from decimal import Decimal
from bases.base_dto import BaseDTO


class JobCreateDTO(BaseDTO):
    user_id: int
    title: str
    description: str
    salary_from: Decimal
    salary_to: Decimal

class JobDTO(BaseDTO):
    id: int
    user_id: int
    title: str
    description: str
    salary_from: Decimal
    salary_to: Decimal
    is_active: bool
    created_at: datetime