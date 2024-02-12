from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings
import os

from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Settings"""

    # Twelve Data API Base URL
    TWELVE_DATA_BASE_URL: AnyHttpUrl = os.environ.get("TWELVE_DATA_BASE_URL")
    # RapidAPI Key
    RapidAPI_Key: str = os.environ.get("RAPIDAPI_KEY")
    # RapidAPI Host
    RapidAPI_Host: str = os.environ.get("RAPIDAPI_HOST")
    # Twelve Data API Timeout
    TWELVE_DATA_API_TIMEOUT: int = os.environ.get("TWELVE_DATA_API_TIMEOUT")

    class Config:
        """Config"""

        env_file = ".env"


settings = Settings()
