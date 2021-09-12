from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from abstract_service.api.routes import router
from . import models
from .database import engine
from .errors import AppLogicException
from .handlers import app_logic_exception_handler
from .settings import get_settings

models.Base.metadata.create_all(bind=engine)


def get_app():
    application = FastAPI(title='Abstract service')
    application.add_middleware(
        CORSMiddleware,
        allow_origins=get_settings().allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(AppLogicException, app_logic_exception_handler)

    application.include_router(router)

    return application


app = get_app()
