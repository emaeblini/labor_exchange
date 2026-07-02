from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from models.alchemy.user import User
from models.dto.user import UserCreateDBDTO, UserInternalDTO, UserUpdateDTO


class UserRepository(
    BaseAlchemyGenericAsyncRepository[
        User,
        UserInternalDTO,
        UserCreateDBDTO,
        UserUpdateDTO,
    ]
):
    alchemy_model = User
    output_model = UserInternalDTO

    async def get_by_email(self, email: str) -> UserInternalDTO | None:
        return await self.retrieve(email=email)