import os

def is_in_lambda():
    return os.environ.get("AWS_EXECUTION_ENV") is not None
