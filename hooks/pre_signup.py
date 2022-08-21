import logging
from cognito_utils.cognito import CognitoService
from cognito_utils.config import get_config

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    config = get_config()
    congito_service = CognitoService(config)

    email = event["request"]["userAttributes"]["email"]
    user = congito_service.get_verified_user_by_email(email)
    if user is not None:
        raise Exception("There is already a user associated with this email")
    
    return event