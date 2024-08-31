import os
import requests
from config import get_config

class SlackService:
    def __init__(self, config):
        self.config = config
        self.slack_token = None

    def _get_slack_token(self):
        if not self.slack_token:
            self.slack_token = self.config.get_config("slack", "bot_token")
        return self.slack_token

    def send_message(self, channel, message):
        """
        Sends a message to a Slack channel.

        :param channel: The channel to send the message to
        :param message: The message to send
        :return: The response from the Slack API
        """
        slack_token = self._get_slack_token()
        headers = {"Authorization": f"Bearer {slack_token}"}
        data = {"channel": channel, "text": message}
        response = requests.post("https://slack.com/api/chat.postMessage", headers=headers, json=data)
        return response.json()

    def send_file(self, channel, file_path, filename):
        """
        Sends a file to a Slack channel.

        :param channel: The channel to send the file to
        :param file_path: The path to the file to send
        :param filename: The filename to use when sending the file
        :return: The response from the Slack API
        """
        slack_token = self._get_slack_token()
        headers = {"Authorization": f"Bearer {slack_token}"}
        files = {"file": (filename, open(file_path, "rb"))}
        data = {"channels": channel}
        response = requests.post("https://slack.com/api/files.upload", headers=headers, files=files, data=data)
        return response.json()

    def get_channel_id(self, channel_name):
        """
        Gets the ID of a Slack channel.

        :param channel_name: The name of the channel to get the ID for
        :return: The ID of the channel
        """
        slack_token = self._get_slack_token()
        headers = {"Authorization": f"Bearer {slack_token}"}
        response = requests.get("https://slack.com/api/conversations.list", headers=headers)
        channels = response.json()["channels"]
        for channel in channels:
            if channel["name"] == channel_name:
                return channel["id"]
        return None

    def get_user_id(self, username):
        """
        Gets the ID of a Slack user.

        :param username: The username to get the ID for
        :return: The ID of the user
        """
        slack_token = self._get_slack_token()
        headers = {"Authorization": f"Bearer {slack_token}"}
        response = requests.get("https://slack.com/api/users.list", headers=headers)
        users = response.json()["members"]
        for user in users:
            if user["name"] == username:
                return user["id"]
        return None
