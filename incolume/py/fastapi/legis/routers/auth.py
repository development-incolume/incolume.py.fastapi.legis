from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from incolume.py.fastapi.legis.db.connection import get_db_session
from incolume.py.fastapi.legis.controllers.auth_users import User
from incolume.py.fastapi.legis.schemas.user import User as UserSchema


router = APIRouter(prefix='/auth')


@router.post('/signin', status_code=status.HTTP_201_CREATED, response_model=UserSchema)
def user_register(user: UserSchema, db_session: Session = Depends(get_db_session)):
    user = User(db_session=db_session).register(user=user)
    # return JSONResponse(content=user, status_code=status.HTTP_201_CREATED)
    return user


