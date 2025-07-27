from datetime import datetime
from app.db.mongo import chat_logs

def save_chat_log(prompt, response, summary, pii):
    chat_logs.insert_one({
        "prompt": prompt,
        "response": response,
        "summary": summary,
        "pii": pii,
        "timestamp": datetime.utcnow()
    })

def get_all_chats():
    return list(chat_logs.find({}, {"_id": 0}))
