import requests
from config import get_config

class FacebookService:
    def __init__(self, config):
        self.config = config
        self.facebook_token = None

    def _get_facebook_token(self):
        if not self.facebook_token:
            self.facebook_token = self.config.get_config("facebook", "access_token")
        return self.facebook_token

    def post_on_facebook(self, message):
        """
        Posts a message on Facebook.

        :param message: The message to post
        :return: The response from the Facebook API
        """
        facebook_token = self._get_facebook_token()
        data = {"access_token": facebook_token, "message": message}
        response = requests.post("https://graph.facebook.com/v13.0/me/feed", data=data)
        return response.json()

    def get_facebook_user_id(self, username):
        """
        Gets the ID of a Facebook user.

        :param username: The username to get the ID for
        :return: The ID of the user
        """
        facebook_token = self._get_facebook_token()
        data = {"access_token": facebook_token, "fields": "id"}
        response = requests.get(f"https://graph.facebook.com/v13.0/{username}", params=data)
        return response.json()["id"]

    def get_facebook_page_id(self, page_name):
        """
        Gets the ID of a Facebook page.

        :param page_name: The name of the page to get the ID for
        :return: The ID of the page
        """
        facebook_token = self._get_facebook_token()
        data = {"access_token": facebook_token, "fields": "id"}
        response = requests.get(f"https://graph.facebook.com/v13.0/{page_name}", params=data)
        return response.json()["id"]
