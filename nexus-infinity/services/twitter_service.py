import os
import requests
from config import get_config

class TwitterService:
    def __init__(self, config):
        self.config = config
        self.twitter_token = None
        self.twitter_token_secret = None

    def _get_twitter_token(self):
        if not self.twitter_token:
            self.twitter_token = self.config.get_config("twitter", "access_token")
        return self.twitter_token

    def _get_twitter_token_secret(self):
        if not self.twitter_token_secret:
            self.twitter_token_secret = self.config.get_config("twitter", "access_token_secret")
        return self.twitter_token_secret

    def send_tweet(self, message):
        """
        Sends a tweet on Twitter.

        :param message: The message to send
        :return: The response from the Twitter API
        """
        twitter_token = self._get_twitter_token()
        twitter_token_secret = self._get_twitter_token_secret()
        auth = requests.auth.OAuth1(twitter_token, twitter_token_secret, self.config.get_config("twitter", "consumer_key"), self.config.get_config("twitter", "consumer_secret"))
        data = {"status": message}
        response = requests.post("https://api.twitter.com/1.1/statuses/update.json", auth=auth, json=data)
        return response.json()

    def get_user_id(self, username):
        """
        Gets the ID of a Twitter user.

        :param username: The username to get the ID for
        :return: The ID of the user
        """
        twitter_token = self._get_twitter_token()
        twitter_token_secret = self._get_twitter_token_secret()
        auth = requests.auth.OAuth1(twitter_token, twitter_token_secret, self.config.get_config("twitter", "consumer_key"), self.config.get_config("twitter", "consumer_secret"))
        response = requests.get(f"https://api.twitter.com/1.1/users/show.json?screen_name={username}", auth=auth)
        return response.json()["id"]

    def get_tweet_id(self, tweet_url):
        """
        Gets the ID of a Twitter tweet.

        :param tweet_url: The URL of the tweet to get the ID for
        :return: The ID of the tweet
        """
        twitter_token = self._get_twitter_token()
        twitter_token_secret = self._get_twitter_token_secret()
        auth = requests.auth.OAuth1(twitter_token, twitter_token_secret, self.config.get_config("twitter", "consumer_key"), self.config.get_config("twitter", "consumer_secret"))
        response = requests.get(f"https://api.twitter.com/1.1/statuses/show.json?id={tweet_url.split('/')[-1]}", auth=auth)
        return response.json()["id"]
