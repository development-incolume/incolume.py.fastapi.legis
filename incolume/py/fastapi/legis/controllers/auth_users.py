from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from incolume.py.fastapi.legis.db.models.user import UserModel
from incolume.py.fastapi.legis.schemas.user import User as UserSchema
from passlib.context import CryptContext
from fastapi.exceptions import HTTPException
from fastapi import status


crypt_context = CryptContext(schemes=['sha256_crypt'])


class User:
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def register(self, user: UserSchema):
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
