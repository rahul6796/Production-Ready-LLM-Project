from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file= "../.env", env_file_config="utf-8")

    MONGO_DATABASE_HOST: str = "mongodb://localhost:27017"
    MONGO_DATABASE_NAME: str = "scrabble"


setting = Settings()
