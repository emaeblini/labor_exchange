from bases.services.base_service import BaseService
from bases.uows.job_uow import JobUOW
from bases.uows.response_uow import ResponseUOW
from models.dto.response import ResponseCreateDTO, ResponseDTO
from services.exceptions import ObjectDoesntExistsException, SystemLogicError


class ResponseService(BaseService):
    def __init__(
        self,
        response_uow: ResponseUOW,
        job_uow: JobUOW,
    ) -> None:
        self.response_uow = response_uow
        self.job_uow = job_uow

    async def response_job(self, response_create_data: ResponseCreateDTO) -> ResponseDTO:
        """
        Создать отклик на вакансию.
        """

        async with self.job_uow as job_uow:
            job = await job_uow.repository.retrieve(id=response_create_data.job_id)

            if job is None:
                raise ObjectDoesntExistsException("Вакансия не найдена")

            if not job.is_active:
                raise SystemLogicError("Нельзя откликнуться на неактивную вакансию")

        async with self.response_uow as response_uow:
            response = await response_uow.repository.create(response_create_data)
            await response_uow.commit()

            return response

    async def get_responses_by_job_id(self, job_id: int) -> list[ResponseDTO]:
        """
        Получить список откликов по идентификатору вакансии.
        """

        async with self.job_uow as job_uow:
            job = await job_uow.repository.retrieve(id=job_id)

            if job is None:
                raise ObjectDoesntExistsException("Вакансия не найдена")

        async with self.response_uow as response_uow:
            responses = await response_uow.repository.list(job_id=job_id)

            return list(responses)