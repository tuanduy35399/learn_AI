from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv
import os
load_dotenv()

def get_llm():
    return ChatNVIDIA(model="openai/gpt-oss-20b", nvidia_api_key= os.getenv("OPENAI_API_KEY"), top_p=1)


