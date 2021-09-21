from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from . import models
from abstract_service.api.admin.admin_routes import router as admin_router
from .api.routes import router as api_router
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

    application.include_router(api_router)
    application.include_router(admin_router)

    return application


app = get_app()
