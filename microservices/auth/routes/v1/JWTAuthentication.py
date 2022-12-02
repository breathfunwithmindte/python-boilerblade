from fastapi import APIRouter, Request, Depends
from core.exceptions import *
from core.utils import *
from microservices.auth.dependencies import *
from microservices.auth.schema.LoginBody import *
from microservices.auth.schema.RegisterBody import *
from config import settings

jwtauthentication_router = APIRouter()

@jwtauthentication_router.post("/login", dependencies=[])
async def login (req: Request, loginBody: LoginBody):
    return {
        "login": [],
        "Asdasd": loginBody
    }

@jwtauthentication_router.post("/register", dependencies=[])
async def register (req: Request, registerBody: RegisterBody):
    return {
        "login": [],
        "Asdasd": registerBody
    }