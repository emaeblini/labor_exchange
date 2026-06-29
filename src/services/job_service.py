from models.dto.job import JobCreateDTO, JobDTO
from models.dto.response import ResponseCreateDTO, ResponseDTO
from services.exceptions import ObjectDoesntExistsException, SystemLogicError
from bases.uows.job_uow import JobUOW


class JobService:
    def __init__(self, uow: JobUOW) -> None:
        self.uow = uow

    async def create_job(self, job_schema: JobCreateDTO) -> JobDTO:
        async with self.uow as uow:
            job = await uow.job_repository.create_job(job_schema)
            await uow.commit()

            return job

    async def get_all_jobs(self, limit: int = 100, skip: int = 0) -> list[JobDTO]:
        async with self.uow as uow:
            return await uow.job_repository.get_all_jobs(
                limit=limit,
                skip=skip,
            )

    async def get_job_by_id(self, job_id: int) -> JobDTO:
        async with self.uow as uow:
            job = await uow.job_repository.get_job_by_id(job_id)

            if job is None:
                raise ObjectDoesntExistsException("Вакансия не найдена")

            return job

    async def response_job(self, response_schema: ResponseCreateDTO) -> ResponseDTO:
        async with self.uow as uow:
            job = await uow.job_repository.get_job_by_id(response_schema.job_id)

            if job is None:
                raise ObjectDoesntExistsException("Вакансия не найдена")

            if not job.is_active:
                raise SystemLogicError("Нельзя откликнуться на неактивную вакансию")

            response = await uow.response_repository.response_job(response_schema)
            await uow.commit()

            return response

    async def get_responses_by_job_id(self, job_id: int) -> list[ResponseDTO]:
        async with self.uow as uow:
            job = await uow.job_repository.get_job_by_id(job_id)

            if job is None:
                raise ObjectDoesntExistsException("Вакансия не найдена")

            return await uow.response_repository.get_responses_by_job_id(job_id)