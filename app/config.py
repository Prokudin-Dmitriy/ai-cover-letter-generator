from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    ollama_api_key: str
    debug: bool = False

    model_config = ConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )


settings = Settings()
