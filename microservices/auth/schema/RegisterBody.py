from typing import Union
from pydantic import BaseModel

class RegisterBody (BaseModel):
    email: str
    password: str
    
    
    