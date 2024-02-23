from fastapi import FastAPI

from src.api.v1.base import api_router

app = FastAPI(title='Requestum Test')

app.include_router(api_router)
