from pydantic import BaseSettings


class Settings(BaseSettings):

    db_password: str
    db_user: str
    db_name: str
    db_url: str


settings = Settings()
