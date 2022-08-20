from hooks import post_confirmation


def post_confirmation_lambda_handler(event, context):
    return post_confirmation.lambda_handler(event, context)
