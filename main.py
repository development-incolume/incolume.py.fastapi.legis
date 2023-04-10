import uvicorn
import logging
from incolume.py.fastapi.legis.server import app


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0')
