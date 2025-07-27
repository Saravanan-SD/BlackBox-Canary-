from fastapi import APIRouter
from app.models.chat_log import get_all_chats

router = APIRouter()

@router.get("/", tags=["History"])
def view_history():
    return get_all_chats()
