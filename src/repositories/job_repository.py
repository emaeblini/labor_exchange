from bases.repositories.generic.base_alchemy_generic_repository import (
    BaseAlchemyGenericAsyncRepository,
)
from models.alchemy.job import Job
from models.dto.job import JobCreateDTO, JobDTO, JobUpdateDTO


class JobRepository(
    BaseAlchemyGenericAsyncRepository[
        Job,
        JobDTO,
        JobCreateDTO,
        JobUpdateDTO,
    ]
):
    alchemy_model = Job
    output_model = JobDTO
