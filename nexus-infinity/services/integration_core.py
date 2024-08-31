import os
import requests
from config import get_config

class IntegrationCore:
    def __init__(self):
        self.config = get_config()
        self.services = {}

    def register_service(self, service_name, service_class):
        """
        Registers an external service with the integration core.

        :param service_name: The name of the service (e.g., "aws_s3", "slack")
        :param service_class: The class implementing the service integration
        """
        self.services[service_name] = service_class(self.config)

    def get_service(self, service_name):
        """
        Returns an instance of the registered service.

        :param service_name: The name of the service
        :return: An instance of the service class
        """
        return self.services.get(service_name)

    def integrate_with_service(self, service_name, method, *args, **kwargs):
        """
        Integrates with an external service using the specified method.

        :param service_name: The name of the service
        :param method: The method to call on the service (e.g., "upload_file", "send_message")
        :param args: Additional arguments to pass to the method
        :param kwargs: Additional keyword arguments to pass to the method
        :return: The result of the method call
        """
        service = self.get_service(service_name)
        if service:
            return getattr(service, method)(*args, **kwargs)
        return None

class AWSS3Service:
    def __init__(self, config):
        self.config = config
        self.s3_client = None

    def upload_file(self, file_path, bucket_name, key):
        """
        Uploads a file to AWS S3.

        :param file_path: The path to the file to upload
        :param bucket_name: The name of the S3 bucket
        :param key: The key to store the file under
        :return: The result of the upload operation
        """
        if not self.s3_client:
            self.s3_client = self.config.get_config("aws_s3", "client")
        with open(file_path, "rb") as file:
            response = self.s3_client.put_object(Body=file, Bucket=bucket_name, Key=key)
            return response

class SlackService:
    def __init__(self, config):
        self.config = config
        self.slack_client = None

    def send_message(self, channel, message):
        """
        Sends a message to a Slack channel.

        :param channel: The name of the Slack channel
        :param message: The message to send
        :return: The result of the message send operation
        """
        if not self.slack_client:
            self.slack_client = self.config.get_config("slack", "client")
        response = self.slack_client.chat_postMessage(channel=channel, text=message)
        return response

# Example usage:
integration_core = IntegrationCore()
integration_core.register_service("aws_s3", AWSS3Service)
integration_core.register_service("slack", SlackService)

result = integration_core.integrate_with_service("aws_s3", "upload_file", "path/to/file.txt", "my-bucket", "file.txt")
print(result)

result = integration_core.integrate_with_service("slack", "send_message", "#general", "Hello, world!")
print(result)
