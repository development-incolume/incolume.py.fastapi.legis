import re
from typing import Optional
from pydantic import BaseModel, validator


class UserBase(BaseModel):
    username: str
    pw_hash: Optional[str]

    @validator('username')
    def check_username(cls, value):
        if not re.match('^([a-z]|[0-9]|_){8,15}$', value):
            raise ValueError('Invalide format for username')
        return value
    
    class Config:
        orm_mode = True
    
class UserIn(UserBase):
    password: str

