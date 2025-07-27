from pydantic import BaseModel
from datetime import datetime
from typing import List

class ChatLog(BaseModel):
    prompt: str
    response: str
    timestamp: datetime

class ChatLogsResponse(BaseModel):
    logs: List[ChatLog]
