import os

from dotenv import load_dotenv
from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Settings"""
    # Twelve API Configurations
    # Twelve Data API Base URL
    TWELVE_DATA_BASE_URL: AnyHttpUrl = os.environ.get("TWELVE_DATA_BASE_URL")
    # RapidAPI Key
    RapidAPI_Key: str = os.environ.get("RAPIDAPI_KEY")
    # RapidAPI Host
    RapidAPI_Host: str = os.environ.get("RAPIDAPI_HOST")
    # Twelve Data API Timeout
    TWELVE_DATA_API_TIMEOUT: int = os.environ.get("TWELVE_DATA_API_TIMEOUT")

    # RabbitMQ Configurations
    # RabbitMQ Host
    RABBITMQ_HOST: str = os.environ.get("RABBITMQ_HOST")
    # RabbitMQ User
    RABBITMQ_USER: str = os.environ.get("RABBITMQ_USER")
    # RabbitMQ Password
    RABBITMQ_PASSWORD: str = os.environ.get("RABBITMQ_PASSWORD")

    # Celery Configurations
    # Celery Broker URL
    CELERY_BROKER_URL: str = os.environ.get("CELERY_BROKER_URL")
    # Celery Result Backend
    CELERY_RESULT_BACKEND: str = os.environ.get("CELERY_RESULT_BACKEND")

    class Config:
        """Config"""

        env_file = ".env"


settings = Settings()
