from fastapi import FastAPI, status, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
from config import settings
from http import HTTPStatus
from core.exceptions import register_exceptions, NonAuthenticatedException, ForbiddenException

class MyExpection(Exception):
    def __init__ (self):
        self.hello = HTTPStatus.BAD_REQUEST.name
        self.hello1 = HTTPStatus.BAD_REQUEST.value
        self.hello2 = HTTPStatus.BAD_REQUEST.phrase
        print("something")


def create_app() -> FastAPI: 
    
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        version=settings.PROJECT_VERSION,
        docs_url="/docs"
    )
    
    register_exceptions(_app)
    
    @_app.get("/1")
    async def root1():
        raise ForbiddenException(data={"hello": "wowowo"})
        return JSONResponse(status_code=status.HTTP_200_OK, content={ "message": "Hello World1" })
    
    
    
    
    
    _public_app = FastAPI(
        
    )
    
    
    async def hello1 ():
        print("middleware is working")
        raise MyExpection()
    
    @_public_app.get("/wow", dependencies=[Depends(hello1)])
    async def hello ():
        
        return "hello world"
    
    
    _app.mount("", _public_app)
    
    return _app

    # app_ = FastAPI(
    #     title=settings.PROJECT_TITLE,
    #     description=settings.PROJECT_DESCRIPTION,
    #     version=settings.PROJECT_VERSION,
    #     docs_url=None if settings.ENV == "prod" else "/docs",
    #     redoc_url=None if settings.ENV == "prod" else "/redoc",
    # )

    # # Initializing required dependencies
    # init_listeners(app_=app_)
    # init_handlers(app_=app_)
    # init_middlewares(app_=app_)
    # init_routers(app_=app_)

    # return app_