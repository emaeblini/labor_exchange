from datetime import datetime

from bases.base_dto import BaseDTO


class UserCreateDTO(BaseDTO):
    email: str
    name: str
    password: str
    is_company: bool = False


class UserCreateDBDTO(BaseDTO):
    email: str
    name: str
    hashed_password: str
    is_company: bool = False


class UserUpdateDTO(BaseDTO):
    email: str | None = None
    name: str | None = None
    hashed_password: str | None = None
    is_company: bool | None = None


class UserInternalDTO(BaseDTO):
    id: int
    email: str
    name: str
    hashed_password: str
    is_company: bool
    created_at: datetime


class UserDTO(BaseDTO):
    id: int
    email: str
    name: str
    is_company: bool
    created_at: datetime