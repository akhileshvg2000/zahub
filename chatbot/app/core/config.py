from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    secret_key: str
    openai_api_key: str
    openai_api_base: str | None= None
    openai_model: str

    zahub_mcp_host: str
    zahub_mcp_port: int

settings= Settings()
