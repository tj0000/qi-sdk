from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="QI_")

    API_KEY: str | None = None
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION: int = 30
