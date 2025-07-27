from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_chat import ask_llm

from app.tasks.log_task import log_chat

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
async def chat(request: ChatRequest):
    reply = await ask_llm(request.prompt)

    log_chat.delay(request.prompt, reply)
    return {"response": reply}
