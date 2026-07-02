from bases.base_dto import BaseDTO


class ResponseCreateDTO(BaseDTO):
    job_id: int
    user_id: int
    message: str

class ResponseUpdateDTO(BaseDTO):
    message: str | None = None

class ResponseDTO(BaseDTO):
    id: int
    job_id: int
    user_id: int
    message: str
