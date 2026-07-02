import bcrypt

from bases.services.base_service import BaseService
from bases.uows.user_uow import UserUOW
from models.dto.user import UserCreateDBDTO, UserCreateDTO, UserDTO
from services.exceptions import ObjectDoesntExistsException, ObjectExistsException


class UserService(BaseService):
    def __init__(self, uow: UserUOW) -> None:
        self.uow = uow

    def _hash_password(self, password: str) -> str:
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)

        return hashed_password.decode("utf-8")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        password_bytes = plain_password.encode("utf-8")
        hashed_password_bytes = hashed_password.encode("utf-8")

        return bcrypt.checkpw(password_bytes, hashed_password_bytes)

    async def register_user(self, user_create_data: UserCreateDTO) -> UserDTO:
        """
        Зарегистрировать нового пользователя.
        """

        async with self.uow as uow:
            existing_user = await uow.repository.get_by_email(user_create_data.email)

            if existing_user is not None:
                raise ObjectExistsException("Пользователь с таким email уже существует")

            user_db_data = UserCreateDBDTO(
                email=user_create_data.email,
                name=user_create_data.name,
                hashed_password=self._hash_password(user_create_data.password),
                is_company=user_create_data.is_company,
            )

            user = await uow.repository.create(user_db_data)
            await uow.commit()

            return UserDTO.model_validate(user)

    async def get_user_by_id(self, user_id: int) -> UserDTO:
        """
        Получить пользователя по идентификатору.
        """

        async with self.uow as uow:
            user = await uow.repository.retrieve(id=user_id)

            if user is None:
                raise ObjectDoesntExistsException("Пользователь не найден")

            return UserDTO.model_validate(user)

    async def get_user_by_email(self, email: str) -> UserDTO:
        """
        Получить пользователя по email.
        """

        async with self.uow as uow:
            user = await uow.repository.get_by_email(email)

            if user is None:
                raise ObjectDoesntExistsException("Пользователь с таким email не найден")

            return UserDTO.model_validate(user)

    async def authenticate_user(self, email: str, password: str) -> UserDTO | None:
        """
        Проверить email и пароль пользователя.
        """

        async with self.uow as uow:
            user = await uow.repository.get_by_email(email)

            if user is None:
                return None

            if not self.verify_password(password, user.hashed_password):
                return None

            return UserDTO.model_validate(user)