from typing import Final
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings
import logging


DB_URL: Final = settings.DB_URL
engine = create_engine(DB_URL, pool_pre_ping=True)
Session = sessionmaker(bind=engine)

def get_db_session():
    try:
        session = Session()
        yield session
    finally:
        session.close()
        

if __name__ == '__main__':
    logging.debug(DB_URL)
