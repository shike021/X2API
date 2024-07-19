from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI Example"
    database_url: str = "sqlite:///./test.db"

settings = Settings()
