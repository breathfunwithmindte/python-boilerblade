from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from http import HTTPStatus

# @interface
class BaseException(Exception):
    status: int
    status_type: str
    message: str
    data: object
    
    def __init__(self, data: object={}) -> None:
        self.data = data
        super().__init__()
    
    def response (self):
        return {
            "status": self.status,
            "status_type": self.status_type,
            "message": self.message,
            "data": self.data
        }
    
# @implements BaseException - 400
class BadRequestException(BaseException):
    status = HTTPStatus.BAD_REQUEST.value
    status_type = HTTPStatus.BAD_REQUEST.name
    message = HTTPStatus.BAD_REQUEST.phrase
       
# @implements BaseException - 511
class AuthenticationRequiredException(BaseException):
    status = HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED.value
    status_type = HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED.name
    message = HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED.phrase
    
    
# @implements BaseException - 401
class NonAuthenticatedException(BaseException):
    status = HTTPStatus.UNAUTHORIZED.value
    status_type = HTTPStatus.UNAUTHORIZED.name
    message = HTTPStatus.UNAUTHORIZED.phrase
    
# @implements BaseException - 403
class ForbiddenException(BaseException):
    status = HTTPStatus.FORBIDDEN.value
    status_type = HTTPStatus.METHOD_NOT_ALLOWED.name
    message = HTTPStatus.METHOD_NOT_ALLOWED.phrase
    
class InternalServerErrorException(BaseException):
    status = HTTPStatus.INTERNAL_SERVER_ERROR.value
    status_type = HTTPStatus.INTERNAL_SERVER_ERROR.name
    message = HTTPStatus.INTERNAL_SERVER_ERROR.phrase
    
    
    
def register_exceptions (_app: FastAPI):
    @_app.exception_handler(BadRequestException)
    async def bad_request_exception(request: Request, exc: BadRequestException):
        return JSONResponse(status_code=exc.status, content=exc.response())
    
    @_app.exception_handler(AuthenticationRequiredException)
    async def authentication_required_exception(request: Request, exc: AuthenticationRequiredException):
        return JSONResponse(status_code=exc.status, content=exc.response())
    
    @_app.exception_handler(NonAuthenticatedException)
    async def non_authenticated_exception(request: Request, exc: NonAuthenticatedException):
        return JSONResponse(status_code=exc.status, content=exc.response())
    
    @_app.exception_handler(ForbiddenException)
    async def forbidden_exception(request: Request, exc: ForbiddenException):
        return JSONResponse(status_code=exc.status, content=exc.response())
    
    @_app.exception_handler(InternalServerErrorException)
    async def internal_server_error_exception(request: Request, exc: InternalServerErrorException):
        return JSONResponse(status_code=exc.status, content=exc.response())
