from fastapi import FastAPI
from incolume.py.fastapi.legis.routers.auth import router as user_router


app = FastAPI()


@app.get('/')
def home():
    return {'message': 'running..'}

app.include_router(user_router)
