from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    ENV: str
    DATABASE_URL: str
    REDIS_HOST: str
    REDIS_PORT: int

    class Config:
        env_file = ".env.local"  # default


env = os.getenv("ENV", "local")

if env == "prod":
    settings = Settings(_env_file=".env.prod")
else:
    settings = Settings(_env_file=".env.local")