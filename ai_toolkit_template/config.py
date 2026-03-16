from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Uygulama ayarları — .env dosyasından okunur."""

    # API Keys
    openai_api_key: str = Field(default="", description="OpenAI API key")
    anthropic_api_key: str = Field(default="", description="Anthropic API key")

    # App settings
    app_name: str = Field(default="AI Toolkit", description="Uygulama adı")
    debug: bool = Field(default=False, description="Debug modu")
    log_level: str = Field(default="INFO", description="Log seviyesi")

    model_config = {"env_file": ".env", "env_file_encoding": "utf-8"}


settings = Settings()
