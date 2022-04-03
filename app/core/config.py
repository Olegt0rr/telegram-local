from pydantic import BaseSettings, SecretStr


class TelegramConfig(BaseSettings):
    """Represents the Telegram bot configuration."""

    class Config:
        env_prefix = "TELEGRAM_"

    token: SecretStr
    local_server_url: str = "http://api"

    webhook_url: str = "http://bot"
    webhook_path: str = "/webhook"


class WebAppConfig(BaseSettings):
    """Represents the webapp configuration."""

    class Config:
        env_prefix = "WEBAPP_"

    host: str = "0.0.0.0"
    port: int = 80


class LoggingConfig(BaseSettings):
    """Represents the logging configuration."""

    class Config:
        env_prefix = "LOGGING_"

    level: str = "INFO"
    format: str = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    datefmt: str = "%Y-%m-%d %H:%M:%S"
