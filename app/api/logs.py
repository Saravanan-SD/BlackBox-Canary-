from fastapi import APIRouter
from app.db.mongo import chat_collection
from app.schemas.logs import ChatLogsResponse, ChatLog

router = APIRouter()

@router.get("/logs", response_model=ChatLogsResponse)
async def get_chat_logs():
    logs_cursor = chat_collection.find().sort("timestamp", -1).limit(10)  # latest 10 logs
    logs = [
        ChatLog(
            prompt=doc["prompt"],
            response=doc["response"],
            timestamp=doc["timestamp"]
        )
        for doc in logs_cursor
    ]
    return {"logs": logs}
