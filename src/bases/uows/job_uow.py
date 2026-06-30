from bases.uows.generic_alchemy_uow import AlchemyAsyncGenericUOW
from models.alchemy.job import Job
from models.dto.job import JobCreateDTO, JobDTO, JobUpdateDTO


class JobUOW(
    AlchemyAsyncGenericUOW[
        Job,
        JobDTO,
        JobCreateDTO,
        JobUpdateDTO,
    ]
):
    pass