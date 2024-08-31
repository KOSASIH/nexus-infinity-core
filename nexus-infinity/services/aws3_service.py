import os
import boto3
from botocore.exceptions import NoCredentialsError
from config import get_config

class AWSS3Service:
    def __init__(self, config):
        self.config = config
        self.s3_client = None
        self.s3_resource = None

    def _get_s3_client(self):
        if not self.s3_client:
            aws_access_key_id = self.config.get_config("aws_s3", "access_key_id")
            aws_secret_access_key = self.config.get_config("aws_s3", "secret_access_key")
            self.s3_client = boto3.client("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        return self.s3_client

    def _get_s3_resource(self):
        if not self.s3_resource:
            aws_access_key_id = self.config.get_config("aws_s3", "access_key_id")
            aws_secret_access_key = self.config.get_config("aws_s3", "secret_access_key")
            self.s3_resource = boto3.resource("s3", aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        return self.s3_resource

    def upload_file(self, file_path, bucket_name, key):
        """
        Uploads a file to AWS S3.

        :param file_path: The path to the file to upload
        :param bucket_name: The name of the S3 bucket
        :param key: The key to store the file under
        :return: The result of the upload operation
        """
        s3_client = self._get_s3_client()
        try:
            with open(file_path, "rb") as file:
                response = s3_client.put_object(Body=file, Bucket=bucket_name, Key=key)
                return response
        except NoCredentialsError:
            print("Error: AWS credentials not found.")
            return None

    def download_file(self, bucket_name, key, file_path):
        """
        Downloads a file from AWS S3.

        :param bucket_name: The name of the S3 bucket
        :param key: The key of the file to download
        :param file_path: The path to save the file to
        :return: The result of the download operation
        """
        s3_client = self._get_s3_client()
        try:
            with open(file_path, "wb") as file:
                s3_client.download_fileobj(bucket_name, key, file)
                return True
        except NoCredentialsError:
            print("Error: AWS credentials not found.")
            return False

    def list_buckets(self):
        """
        Lists all AWS S3 buckets.

        :return: A list of bucket names
        """
        s3_client = self._get_s3_client()
        response = s3_client.list_buckets()
        buckets = [bucket["Name"] for bucket in response["Buckets"]]
        return buckets

    def list_objects(self, bucket_name, prefix=""):
        """
        Lists all objects in an AWS S3 bucket.

        :param bucket_name: The name of the S3 bucket
        :param prefix: The prefix to filter objects by (optional)
        :return: A list of object keys
        """
        s3_client = self._get_s3_client()
        response = s3_client.list_objects(Bucket=bucket_name, Prefix=prefix)
        objects = [obj["Key"] for obj in response["Contents"]]
        return objects

    def delete_object(self, bucket_name, key):
        """
        Deletes an object from AWS S3.

        :param bucket_name: The name of the S3 bucket
        :param key: The key of the object to delete
        :return: The result of the delete operation
        """
        s3_client = self._get_s3_client()
        try:
            response = s3_client.delete_object(Bucket=bucket_name, Key=key)
            return response
        except NoCredentialsError:
            print("Error: AWS credentials not found.")
            return None

    def create_bucket(self, bucket_name):
        """
        Creates a new AWS S3 bucket.

        :param bucket_name: The name of the bucket to create
        :return: The result of the create operation
        """
        s3_client = self._get_s3_client()
        try:
            response = s3_client.create_bucket(Bucket=bucket_name)
            return response
        except NoCredentialsError:
            print("Error: AWS credentials not found.")
            return None

    def delete_bucket(self, bucket_name):
        """
        Deletes an AWS S3 bucket.

        :param bucket_name: The name of the bucket to delete
        :return: The result of the delete operation
       
