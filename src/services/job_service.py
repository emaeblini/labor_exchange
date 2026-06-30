from bases.services.base_service import BaseService
from bases.uows.job_uow import JobUOW
from models.dto.job import JobCreateDTO, JobDTO
from services.exceptions import ObjectDoesntExistsException


class JobService(BaseService):
    def __init__(self, uow: JobUOW) -> None:
        self.uow = uow

    async def create_job(self, job_create_data: JobCreateDTO) -> JobDTO:
        """
        Создать вакансию.
        """

        async with self.uow as uow:
            job = await uow.repository.create(job_create_data)
            await uow.commit()

            return job

    async def get_all_jobs(self, limit: int = 100, skip: int = 0) -> list[JobDTO]:
        """
        Получить список всех активных вакансий.
        """

        async with self.uow as uow:
            jobs = await uow.repository.list(
                limit=limit,
                skip=skip,
                is_active=True,
            )

            return list(jobs)

    async def get_job_by_id(self, job_id: int) -> JobDTO:
        """
        Получить вакансию по идентификатору.
        """

        async with self.uow as uow:
            job = await uow.repository.retrieve(id=job_id)

            if job is None:
                raise ObjectDoesntExistsException("Вакансия не найдена")

            return job