import logging
from cognito_utils.cognito import CognitoService
from cognito_utils.config import get_config

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    config = get_config()
    congito_service = CognitoService(config)

    try:
        err = None
        username = event['username']
        group = "vaulting"
        congito_service.add_user_to_group(username, group)
    except congito_service.client.exceptions.InvalidParameterException:
        err = {"error": True, "success": False, "message": "Username doesnt exists"}
    except congito_service.client.exceptions.ResourceNotFoundException:
        err = {"error": True, "success": False, "message": "Resource not found!"}
    except congito_service.client.exceptions.NotAuthorizedException:
        err = {"error": True, "success": False, "message": "Not authorized"}
    except Exception as e:
        err = {"error": True, "success": False, "message": f"Unknown error {e.__str__()} "}
    finally:
        if err:
            logger.error(err)

    return event