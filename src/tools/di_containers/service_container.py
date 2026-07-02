from dependency_injector import containers, providers

import services
from tools.di_containers.alchemy_container import AlchemyAsyncContainer


class ServiceContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(packages=["web.entrypoints"])

    alchemy_container = providers.Container(
        AlchemyAsyncContainer,
    )

    job_service = providers.Factory(
        services.JobService,
        uow=alchemy_container.job_uow,
    )

    response_service = providers.Factory(
        services.ResponseService,
        response_uow=alchemy_container.response_uow,
        job_uow=alchemy_container.job_uow,
    )