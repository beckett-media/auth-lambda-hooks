from hooks import post_confirmation

if __name__ == "__main__":
    post_confirmation.lambda_handler({"username": "testuser"}, None)