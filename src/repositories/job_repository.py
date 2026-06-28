from models.alchemy.job import Job
from models.dto.job import JobCreateDTO, JobDTO
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class JobRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_job(self, job_schema: JobCreateDTO) -> JobDTO:
        job = Job(**job_schema.model_dump())

        self.db.add(job)
        await self.db.flush()
        await self.db.refresh(job)

        return JobDTO.model_validate(job)

    async def get_all_jobs(self, limit: int = 100, skip: int = 0) -> list[JobDTO]:
        query = (
            select(Job)
            .where(Job.is_active == True)
            .offset(skip)
            .limit(limit)
        )

        result = await self.db.execute(query)
        jobs = result.scalars().all()

        return [JobDTO.model_validate(job) for job in jobs]

    async def get_job_by_id(self, job_id: int) -> JobDTO | None:
        query = select(Job).where(Job.id == job_id)

        result = await self.db.execute(query)
        job = result.scalars().first()

        if job is None:
            return None

        return JobDTO.model_validate(job)