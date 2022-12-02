from typing import Union
from pydantic import BaseModel


class LoginBody (BaseModel):
    login_value: str
    password: str
    wow: object