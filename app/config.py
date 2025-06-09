from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    ALGORITHM: str = "HS256" 
    SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()
