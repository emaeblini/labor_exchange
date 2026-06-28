from models.dto.job import JobCreateDTO, JobDTO
from models.dto.response import ResponseCreateDTO, ResponseDTO
from repositories.job_repository import JobRepository
from repositories.response_repository import ResponseRepository
from services.exceptions import ObjectDoesntExistsException, SystemLogicError
from sqlalchemy.ext.asyncio import AsyncSession


class JobService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.job_repository = JobRepository(db)
        self.response_repository = ResponseRepository(db)

    async def create_job(self, job_schema: JobCreateDTO) -> JobDTO:
        job = await self.job_repository.create_job(job_schema)
        await self.db.commit()
        return job

    async def get_all_jobs(self, limit: int = 100, skip: int = 0) -> list[JobDTO]:
        return await self.job_repository.get_all_jobs(limit=limit, skip=skip)

    async def get_job_by_id(self, job_id: int) -> JobDTO:
        job = await self.job_repository.get_job_by_id(job_id)

        if job is None:
            raise ObjectDoesntExistsException("Вакансия не найдена")

        return job

    async def response_job(self, response_schema: ResponseCreateDTO) -> ResponseDTO:
        job = await self.job_repository.get_job_by_id(response_schema.job_id)

        if job is None:
            raise ObjectDoesntExistsException("Вакансия не найдена")

        if not job.is_active:
            raise SystemLogicError("Нельзя откликнуться на неактивную вакансию")

        response = await self.response_repository.response_job(response_schema)
        await self.db.commit()

        return response

    async def get_responses_by_job_id(self, job_id: int) -> list[ResponseDTO]:
        job = await self.job_repository.get_job_by_id(job_id)

        if job is None:
            raise ObjectDoesntExistsException("Вакансия не найдена")

        return await self.response_repository.get_responses_by_job_id(job_id)