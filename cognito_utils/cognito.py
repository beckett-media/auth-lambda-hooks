import boto3

from cognito_utils.config import Settings
from cognito_utils.utils import is_in_lambda

class CognitoService():

    def __init__(self, config: Settings):
        if is_in_lambda():
            self._session = boto3.Session(region_name=config.AWS_REGION)
        else:
            self._session = boto3.Session(
                aws_access_key_id=config.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
                region_name=config.AWS_REGION
            )
        self.client = self._session.client('cognito-idp')
        self.config = config

    def add_user_to_group(self, username: str, group: str):
        return self.client.admin_add_user_to_group(
            UserPoolId=self.config.USER_POOL_ID,
            Username=username,
            GroupName=group
        )
    
    def get_users_by_email(self, email):
        response =  self.client.list_users(
            UserPoolId=self.config.USER_POOL_ID,
            Limit=60,
            Filter=f'email = "{email}"'
        )
        users = response["Users"]
        while response.get("PaginationToken", None) is not None:
            response =  self.client.list_users(
                UserPoolId=self.config.USER_POOL_ID,
                Limit=60,
                Filter=f'email = "{email}"',
                PaginationToken = response["PaginationToken"]
            )
            users += response["Users"]
        return users

    def get_verified_user_by_email(self, email):
        users = self.get_users_by_email(email)
        return next((user for user in users if user["UserStatus"] == "CONFIRMED"), None)