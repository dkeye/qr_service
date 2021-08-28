from fastapi import FastAPI

from . import models
from .database import engine
from .errors import AppLogicException
from .handlers import app_logic_exception_handler
from .routes import router

models.Base.metadata.create_all(bind=engine)


def get_app():
    application = FastAPI(title='Abstract service')

    application.add_exception_handler(AppLogicException, app_logic_exception_handler)

    application.include_router(router)

    return application


app = get_app()
