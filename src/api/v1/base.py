from fastapi import APIRouter

from src.api.v1 import route_github_contributors

api_router = APIRouter()

api_router.include_router(
    router=route_github_contributors.router,
    prefix='/github_contributors',
    tags=['GitHub Contributors']
)

