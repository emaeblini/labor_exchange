from pydantic import Field
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    """
    Класс настроек для приложения
    """

    project_name: str = Field(
        description="Название проекта", default="test_project"
    )
    app_name: str = Field(
        description="Название сервиса", default="test_service"
    )
    app_version: str = Field(
        description="Версия API", default="v1"
    )

    app_host: str = Field(
        description="Хост сервиса",
        default="0.0.0.0",
        alias="PROJECT_HOST",
    )
    app_port: int = Field(
        description="Порт сервиса",
        default="8080",  # type: ignore[assignment]
        alias="PROJECT_PORT",
    )

    okd_stage: str = Field(
        description="Состояние OKD", default="DEV"
    )


app_config = Config()
