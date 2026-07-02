from fastapi import FastAPI

from config import app_config as app_config_module
from web.entrypoints import index_router, job_router, response_router

_config = app_config_module.app_config


def register_routers(app: FastAPI) -> None:

    prefix = f"/api/{_config.app_version}"

    app.include_router(index_router, prefix=prefix)
    app.include_router(job_router, prefix=prefix)
    app.include_router(response_router, prefix=prefix)