from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from services import JobService
from tools.di_containers.service_container import ServiceContainer
from web import schemas

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"],
)


@router.post(
    "",
    response_model=schemas.Job,
    status_code=HTTPStatus.CREATED,
)
@inject
async def create_job(
    job_create_data: schemas.JobCreate,
    job_service: JobService = Depends(Provide[ServiceContainer.job_service]),
) -> schemas.Job:
    """
    Создать вакансию.
    """

    job_create_dto = job_create_data.to_dto()
    created_job = await job_service.create_job(job_create_dto)

    return schemas.Job.from_dto(created_job)


@router.get(
    "",
    response_model=list[schemas.Job],
    status_code=HTTPStatus.OK,
)
@inject
async def get_all_jobs(
    limit: int = 100,
    skip: int = 0,
    job_service: JobService = Depends(Provide[ServiceContainer.job_service]),
) -> list[schemas.Job]:
    """
    Получить список всех активных вакансий.
    """

    jobs = await job_service.get_all_jobs(
        limit=limit,
        skip=skip,
    )

    return [schemas.Job.from_dto(job) for job in jobs]


@router.get(
    "/{job_id}",
    response_model=schemas.Job,
    status_code=HTTPStatus.OK,
)
@inject
async def get_job_by_id(
    job_id: int,
    job_service: JobService = Depends(Provide[ServiceContainer.job_service]),
) -> schemas.Job:
    """
    Получить вакансию по идентификатору.
    """

    job = await job_service.get_job_by_id(job_id)

    return schemas.Job.from_dto(job)