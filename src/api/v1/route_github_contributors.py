from fastapi import APIRouter, Request, Query
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import status

from src.services.github_contributors import GitHubContributorsService

router = APIRouter()

templates = Jinja2Templates(directory='templates')


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
def get_contributors_by_repo_link(
        request: Request,
        github_url: str = Query(None)
):
    list_contributors = GitHubContributorsService().get_top_5_contributors(
        github_url=github_url
    ) if github_url else []

    return templates.TemplateResponse(
        name="base.html",
        context={
            'request': request,
            'list_contributors': list_contributors
        }
    )
