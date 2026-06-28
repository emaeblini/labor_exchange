from models.alchemy.response import Response
from models.dto.response import ResponseCreateDTO, ResponseDTO
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class ResponseRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def response_job(self, response_schema: ResponseCreateDTO) -> ResponseDTO:
        response = Response(**response_schema.model_dump())

        self.db.add(response)
        await self.db.flush()
        await self.db.refresh(response)

        return ResponseDTO.model_validate(response)

    async def get_responses_by_job_id(self, job_id: int) -> list[ResponseDTO]:
        query = select(Response).where(Response.job_id == job_id)

        result = await self.db.execute(query)
        responses = result.scalars().all()

        return [ResponseDTO.model_validate(response) for response in responses]