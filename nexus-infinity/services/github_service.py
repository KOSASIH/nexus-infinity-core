import os
import requests
from config import get_config

class GitHubService:
    def __init__(self, config):
        self.config = config
        self.github_token = None

    def _get_github_token(self):
        if not self.github_token:
            self.github_token = self.config.get_config("github", "access_token")
        return self.github_token

    def create_issue(self, repo_owner, repo_name, title, body):
        """
        Creates a new issue on a GitHub repository.

        :param repo_owner: The owner of the repository
        :param repo_name: The name of the repository
        :param title: The title of the issue
        :param body: The body of the issue
        :return: The response from the GitHub API
        """
        github_token = self._get_github_token()
        headers = {"Authorization": f"Bearer {github_token}"}
        data = {"title": title, "body": body}
        response = requests.post(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues", headers=headers, json=data)
        return response.json()

    def create_pull_request(self, repo_owner, repo_name, title, body, head, base):
        """
        Creates a new pull request on a GitHub repository.

        :param repo_owner: The owner of the repository
        :param repo_name: The name of the repository
        :param title: The title of the pull request
        :param body: The body of the pull request
        :param head: The head branch of the pull request
        :param base: The base branch of the pull request
        :return: The response from the GitHub API
        """
        github_token = self._get_github_token()
        headers = {"Authorization": f"Bearer {github_token}"}
        data = {"title": title, "body": body, "head": head, "base": base}
        response = requests.post(f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls", headers=headers, json=data)
        return response.json()

    def get_repo_id(self, repo_owner, repo_name):
        """
        Gets the ID of a GitHub repository.

        :param repo_owner: The owner of the repository
        :param repo_name: The name of the repository
        :return: The ID of the repository
        """
        github_token = self._get_github_token()
        headers = {"Authorization": f"Bearer {github_token}"}
        response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}", headers=headers)
        return response.json()["id"]

    def get_user_id(self, username):
        """
        Gets the ID of a GitHub user.

        :param username: The username to get the ID for
        :return: The ID of the user
        """
        github_token = self._get_github_token()
        headers = {"Authorization": f"Bearer {github_token}"}
        response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
        return response.json()["id"]
