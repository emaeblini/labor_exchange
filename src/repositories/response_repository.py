from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from models.alchemy.response import Response
from models.dto.response import ResponseCreateDTO, ResponseDTO, ResponseUpdateDTO


class ResponseRepository(
    BaseAlchemyGenericAsyncRepository[
        Response,
        ResponseDTO,
        ResponseCreateDTO,
        ResponseUpdateDTO,
    ]
):
    alchemy_model = Response
    output_model = ResponseDTO