from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    # OpenAI Configuration
    openai_api_key: str = Field(..., env="OPENAI_API_KEY")
    
    # Company Information
    company_name: str = Field(default="Relego AI Solutions", env="COMPANY_NAME")
    company_email: str = Field(default="support@ndezwa.dev", env="COMPANY_EMAIL")
    company_website: str = Field(default="https://ndezwa.dev", env="COMPANY_WEBSITE")
    business_hours_start: str = Field(default="08:00", env="BUSINESS_HOURS_START")
    business_hours_end: str = Field(default="18:00", env="BUSINESS_HOURS_END")
    business_timezone: str = Field(default="UTC", env="BUSINESS_TIMEZONE")
    
    # API Configuration
    api_host: str = Field(default="0.0.0.0", env="API_HOST")
    api_port: int = Field(default=8000, env="API_PORT")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Global settings instance
settings = Settings()