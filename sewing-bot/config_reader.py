from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    bot_token: SecretStr
    host: SecretStr
    database: SecretStr
    user_base: SecretStr
    password: SecretStr
    redis_host: SecretStr
    redis_port: SecretStr
    redis_password: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

config = Settings()