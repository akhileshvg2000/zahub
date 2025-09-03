from langchain_openai import ChatOpenAI
from app.core.config import settings

llm= ChatOpenAI(
        api_key= settings.openai_api_key,
        base_url= settings.openai_api_base,
        model= settings.openai_model,
        temperature= 0.1
        )

