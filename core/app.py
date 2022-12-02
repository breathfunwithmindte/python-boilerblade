from fastapi import FastAPI, status, Depends, HTTPException, Request, APIRouter
from fastapi.responses import JSONResponse
from config import settings
from http import HTTPStatus
from core.exceptions import register_exceptions, NonAuthenticatedException, ForbiddenException
from microservices.admin.admin import admin_app
from microservices.auth.auth import auth_app


def create_app() -> FastAPI: 
    
    _app = FastAPI(
        title=settings.PROJECT_TITLE,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        docs_url="/docs",
    )


    register_exceptions(_app)
    
    register_exceptions(admin_app)
    _app.mount(settings.ADMIN_API_V1_PREFIX, admin_app)
    _app.mount(settings.AUTH_API_V1_PREFIX, auth_app)
    

    return _app
    

    