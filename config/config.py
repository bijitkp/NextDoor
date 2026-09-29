# config/config.py

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    # Application
    app_env: str = "development"
    debug: bool = False

    # PostgreSQL
    postgres_host: str
    postgres_port: int = 5432
    postgres_admin_user: str
    postgres_admin_password: str

    # Database names
    auth_db_name: str = "auth_db"
    user_db_name: str = "user_db"

    # Storage
    storage_provider: str = "local"
    storage_local_path: str = "./data"

    # Logging
    log_level: str = "INFO"
    log_path: str = "./logs"

    # AI / LLM
    llm_provider: str = "groq"
    groq_api_key: str = ""
    groq_model_name: str = ""

    openai_api_key: str = ""
    openai_model_name: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


settings = Settings()