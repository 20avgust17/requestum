from typing import Dict, List

import requests
from fastapi import HTTPException, status

from src.schemas.github_contributors import GitHubUrl


class GitHubContributorsService:

    def get_top_5_contributors(
            self,
            github_url: str,
    ) -> List:

        try:
            GitHubUrl(github_url=github_url)
        except Exception as error:
            raise HTTPException(
                detail=str(error),
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            )

        # Split url by parts
        parts = str(github_url).strip('/').split('/')
        owner, repo_name = parts[-2], parts[-1]

        # Get list if contributors by repo and owner
        contributors_data = self.get_result_api_request(
            url=f"https://api.github.com/repos/{owner}/{repo_name}/contributors"
        )
        projects_data = self.get_result_api_request(
            url=f"https://api.github.com/users/{owner}/repos"
        )

        # To make set of contributors
        contributors = {contributor['login'] for contributor in contributors_data}

        # Create dict of contributed_projects and iter
        contributed_projects = {}
        for project in projects_data:
            project_name = project['name']
            project_contributors_data = self.get_result_api_request(
                url=f"https://api.github.com/repos/{owner}/{project['name']}/contributors"
            )

            # Get contributors each projects
            project_contributors = {contributor['login'] for contributor in project_contributors_data}

            # Counting union contributors
            contributed_projects[project_name] = len(contributors & project_contributors)

        return sorted(contributed_projects.items(), key=lambda x: x[1], reverse=True)[:5]

    @staticmethod
    def get_result_api_request(
            url: str
    ) -> List[Dict]:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                raise NotImplementedError('There was an unexpected response from the GitHub Api')
        except requests.exceptions.HTTPError as error:
            raise HTTPException(
                detail=f'An error occurred while executing the query. Contact technical support. Detail: {error}',
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
