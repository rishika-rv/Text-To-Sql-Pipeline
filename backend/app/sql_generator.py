from langchain_core.messages import HumanMessage, SystemMessage

from app.llm import llm
from app.prompt import SYSTEM_PROMPT


def generate_sql(question: str):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=question)
    ]

    response = llm.invoke(messages)

    return response.content.strip()