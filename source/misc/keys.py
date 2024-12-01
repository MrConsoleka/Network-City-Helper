from pydantic_settings import BaseSettings, SettingsConfigDict
from .paths import Paths


class keys(BaseSettings):
    model_config = SettingsConfigDict(env_file=Paths.env)

    BOT_TOKEN: str
    LOGGER: str
    SECRET_KEY: str
    PARSE_MODE: str
    ADMINS_ID: list[int]
    DB_SQL: str
    DB_LIB: str
    DB_LOGIN: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str


def get_keys() -> keys:
    return keys()
