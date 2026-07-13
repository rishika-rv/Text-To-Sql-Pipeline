from dotenv import load_dotenv
from langchain_groq import ChatGroq
import os
from app.logger import logger



load_dotenv()


logger.info("Initializing Groq LLM")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

logger.info("Groq LLM initialized successfully")