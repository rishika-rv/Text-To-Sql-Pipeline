from langchain_core.messages import HumanMessage, SystemMessage

from app.llm import llm
from app.prompt import SYSTEM_PROMPT
from app.schema_reader import get_database_schema
from app.logger import logger



def generate_sql(question: str, db_path: str):

    schema = get_database_schema(db_path)

    messages = [
        SystemMessage(
            content=f"{SYSTEM_PROMPT}\n\nDatabase Schema:\n{schema}"
        ),
        HumanMessage(content=question)
    ]
    logger.info(f"Generating SQL for question: {question}")

    response = llm.invoke(messages)

    return response.content.strip()