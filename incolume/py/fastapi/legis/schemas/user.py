import re
from pydantic import BaseModel, validator


class User(BaseModel):
    username: str
    password: str

    @validator('username')
    def check_username(cls, value):
        if not re.match('^([a-z]|[0-9]|_){8,15}$', value):
            raise ValueError('Invalide format for username')
        return value
    
    class Config:
        orm_mode = True
    


