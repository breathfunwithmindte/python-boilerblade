from fastapi import APIRouter, Request, Depends
from core.exceptions import *
from core.utils import *
from microservices.admin.dependencies import *
from config import settings


questionnaire_router = APIRouter()



@questionnaire_router.get("/read", dependencies=[Depends(passport), Depends(admin_only)])
async def readQuestionnaires (req: Request):
    return {
        "questionnaires": []
    }

