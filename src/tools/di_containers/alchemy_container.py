from config import pg_config
from dependency_injector import containers, providers
from repositories import JobRepository, ResponseRepository
from bases.uows import JobUOW, ResponseUOW
from storage.sqlalchemy.connection_proxy import AlchemyAsyncConnectionProxy
from tools.factories.alchemy_engine_factory import AlchemyAsyncEngineFactory

config = pg_config.pg_config


class AlchemyAsyncContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=["services"])

    engine_factory = providers.Singleton(
        AlchemyAsyncEngineFactory,
        config.postgres_async_dsn,
        config.connection_pool_size,
    )

    connection_proxy = providers.Factory(
        AlchemyAsyncConnectionProxy,
        engine_factory,
    )

    job_repository = providers.Factory(
        JobRepository,
        connection_proxy,
    )

    response_repository = providers.Factory(
        ResponseRepository,
        connection_proxy,
    )

    job_uow = providers.Factory(
        JobUOW,
        repository=job_repository,
    )

    response_uow = providers.Factory(
        ResponseUOW,
        repository=response_repository,
    )