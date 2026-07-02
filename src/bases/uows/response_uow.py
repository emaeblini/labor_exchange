from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from models.alchemy.response import Response
from models.dto.response import ResponseCreateDTO, ResponseDTO, ResponseUpdateDTO


class ResponseUOW(
    AlchemyAsyncGenericUOW[
        Response,
        ResponseDTO,
        ResponseCreateDTO,
        ResponseUpdateDTO,
    ]
):
    pass