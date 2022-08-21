import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str = "us-west-1"
    USER_POOL_ID: str

class DevSettings(Settings):
    USER_POOL_ID: str  = "us-west-1_YLyATgtQd"

class QASettings(Settings):
    ...

class ProdSettings(Settings):
    USER_POOL_ID: str  = "us-west-1_ElMUH3zGV"

def get_config():
    env_name = os.environ.get('ENV', "dev")
    envs = {
        "dev": DevSettings,
        "qa": QASettings,
        "prod": ProdSettings
    }
    return envs[env_name]()