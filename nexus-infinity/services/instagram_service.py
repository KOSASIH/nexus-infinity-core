import requests
from config import get_config

class InstagramService:
    def __init__(self, config):
        self.config = config
        self.instagram_token = None

    def _get_instagram_token(self):
        if not self.instagram_token:
            self.instagram_token = self.config.get_config("instagram", "access_token")
        return self.instagram_token

    def post_on_instagram(self, image_path, caption):
        """
        Posts an image on Instagram with a caption.

        :param image_path: The path to the image to post
        :param caption: The caption for the post
        :return: The response from the Instagram API
        """
        instagram_token = self._get_instagram_token()
        data = {"access_token": instagram_token, "image": open(image_path, 'rb'), "caption": caption}
        response = requests.post("https://graph.instagram.com/v13.0/me/media", files=data)
        return response.json()

    def get_instagram_user_id(self, username):
        """
        Gets the ID of an Instagram user.

        :param username: The username to get the ID for
        :return: The ID of the user
        """
        instagram_token = self._get_instagram_token()
        data = {"access_token": instagram_token, "fields": "id"}
        response = requests.get(f"https://graph.instagram.com/v13.0/{username}", params=data)
        return response.json()["id"]

    def get_instagram_account_info(self):
        """
        Gets the information of the authenticated Instagram account.

        :return: The information of the authenticated account
        """
        instagram_token = self._get_instagram_token()
        data = {"access_token": instagram_token, "fields": "id,username,account_type"}
        response = requests.get("https://graph.instagram.com/v13.0/me", params=data)
        return response.json()
