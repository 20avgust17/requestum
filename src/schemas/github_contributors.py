from urllib.parse import urlparse

from pydantic import BaseModel, validator


class GitHubUrl(BaseModel):
    github_url: str | None

    @validator('github_url')
    def validate_github_url(cls, value):
        if value and urlparse(value).netloc != 'github.com':
            raise ValueError('URL must be from GitHub domain')
        return value
