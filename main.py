from fastapi import FastAPI
from app.api import chat
from app.api import history  

app = FastAPI(title="BlackBox Canary")

app.include_router(chat.router)
app.include_router(history.router, prefix="/history")