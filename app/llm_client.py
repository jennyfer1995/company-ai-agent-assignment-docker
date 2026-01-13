import os
from openai import OpenAI, AzureOpenAI


def get_llm_client():
    """
    Returns OpenAI or Azure OpenAI client based on environment variables.
    """
    if os.getenv("AZURE_OPENAI_ENDPOINT"):
        return AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version="2024-02-01"
        )
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
