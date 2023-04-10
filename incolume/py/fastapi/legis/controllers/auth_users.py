from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from incolume.py.fastapi.legis.db.models.user import UserModel
from incolume.py.fastapi.legis.schemas.user import UserIn
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status
from jose import jwt, JWTError
from datetime import datetime, timedelta
from config import settings
from typing import List


crypt_context = CryptContext(schemes=['sha256_crypt'])


class User:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def register(self, user: UserIn)->UserModel:
        new_user = UserModel(
            username=user.username,
            password=crypt_context.hash(user.password)
        )
        try:
            self.db_session.add(new_user)
            self.db_session.commit()
            self.db_session.refresh(new_user)
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='User already exists.')
        return new_user
    
    def login(self, user:UserSchema, expires_in: int = 30):
        user_login = self.db_session.query(UserModel).filter_by(username=user.username)

        if user_login is None or crypt_context.verify(user.username, user_login.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTORIZED, detail='Invalid username or password')
        
        exp = datetime.utcnow() + timedelta(minutes=expires_in)
        payload = {
            'sub': user.username,
            'exp': exp,
        }

        access_token = jwt.encode(payload, settings.secret_key, algorithm=settings.ALGORITHM)

    def all(self) -> List[UserModel]:
        pass

    def view(self) -> UserModel:
        pass

    def delete(self) -> UserModel:
        pass

    def update(self) -> UserModel:
        pass
    
