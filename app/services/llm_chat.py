from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.core.config import GROQ_API_KEY

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama3-8b-8192"  # Or llama3-8b-8192
)

async def ask_llm(prompt: str) -> str:
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content
