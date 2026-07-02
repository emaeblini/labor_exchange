from http import HTTPStatus

from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from services import ResponseService
from tools.di_containers.service_container import ServiceContainer
from web import schemas

router = APIRouter(
    prefix="/jobs/{job_id}/responses",
    tags=["responses"],
)


@router.post(
    "",
    response_model=schemas.Response,
    status_code=HTTPStatus.CREATED,
)
@inject
async def response_job(
    job_id: int,
    response_create_data: schemas.ResponseCreate,
    response_service: ResponseService = Depends(
        Provide[ServiceContainer.response_service],
    ),
) -> schemas.Response:
    """
    Создать отклик на вакансию.
    """

    response_create_dto = response_create_data.to_dto(job_id)
    created_response = await response_service.response_job(response_create_dto)

    return schemas.Response.from_dto(created_response)


@router.get(
    "",
    response_model=list[schemas.Response],
    status_code=HTTPStatus.OK,
)
@inject
async def get_responses_by_job_id(
    job_id: int,
    response_service: ResponseService = Depends(
        Provide[ServiceContainer.response_service],
    ),
) -> list[schemas.Response]:
    """
    Получить список откликов по идентификатору вакансии.
    """

    responses = await response_service.get_responses_by_job_id(job_id)

    return [schemas.Response.from_dto(response) for response in responses]