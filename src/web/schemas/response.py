from bases.base_web_schema import BaseWebSchema, ConfigMixin
from models.dto.response import ResponseCreateDTO, ResponseDTO


class ResponseCreate(BaseWebSchema):
    user_id: int
    message: str

    def to_dto(self, job_id: int) -> ResponseCreateDTO:
        return ResponseCreateDTO(
            job_id=job_id,
            user_id=self.user_id,
            message=self.message,
        )


class Response(BaseWebSchema, ConfigMixin):
    id: int
    job_id: int
    user_id: int
    message: str

    @classmethod
    def from_dto(cls, response: ResponseDTO) -> "Response":
        return cls.model_validate(response)