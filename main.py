from hooks import post_confirmation, pre_signup


def post_confirmation_lambda_handler(event, context):
    return post_confirmation.lambda_handler(event, context)


def pre_signup_lambda_handler(event, context):
    return pre_signup.lambda_handler(event, context)
