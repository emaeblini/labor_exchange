from types import TracebackType

from bases.uows.base_uow import BaseAsyncUOW
from repositories.job_repository import JobRepository
from repositories.response_repository import ResponseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from storage.sqlalchemy.connection_proxy import AlchemyAsyncConnectionProxy


class JobUOW(BaseAsyncUOW):
    def __init__(self, connection_proxy: AlchemyAsyncConnectionProxy) -> None:
        self.connection_proxy = connection_proxy
        self.session: AsyncSession | None = None

        self.job_repository: JobRepository | None = None
        self.response_repository: ResponseRepository | None = None

        self._is_transaction_commited = False

    async def __aenter__(self) -> "JobUOW":
        self.session = await self.connection_proxy.connect()

        if not self.session.in_transaction():
            await self.session.begin()

        self.job_repository = JobRepository(self.session)
        self.response_repository = ResponseRepository(self.session)

        self._is_transaction_commited = False

        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_type is not None:
            await self.rollback()

        await self.connection_proxy.disconnect()

    async def commit(self) -> None:
        if self.session is None:
            raise ValueError("Сессия БД не инициализирована")

        await self.session.commit()
        self._is_transaction_commited = True

    async def rollback(self) -> None:
        if self.session is None:
            raise ValueError("Сессия БД не инициализирована")

        if not self._is_transaction_commited:
            await self.session.rollback()