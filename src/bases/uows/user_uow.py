from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from models.alchemy.user import User
from models.dto.user import UserCreateDBDTO, UserInternalDTO, UserUpdateDTO


class UserUOW(
    AlchemyAsyncGenericUOW[
        User,
        UserInternalDTO,
        UserCreateDBDTO,
        UserUpdateDTO,
    ]
):
    pass