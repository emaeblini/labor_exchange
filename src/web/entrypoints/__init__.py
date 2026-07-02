from web.entrypoints.index_entrypoint import router as index_router
from web.entrypoints.job_entrypoint import router as job_router
from web.entrypoints.response_entrypoint import router as response_router

__all__ = [
    "index_router",
    "job_router",
    "response_router",
]