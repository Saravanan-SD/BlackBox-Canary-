from celery_app import celery_app
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from app.core.config import GROQ_API_KEY
import re
from app.models.chat_log import save_chat_log
import time
from celery import states
from celery.exceptions import Ignore, Retry

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama3-8b-8192"  # Or llama3-8b-8192
)

def detect_pii(text: str) -> list:
    pii_matches = []

    if re.search(r"\b\d{10}\b", text):
        pii_matches.append("phone")

    if re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text):
        pii_matches.append("email")

    if re.search(r"\b\d{1,3}\s+\w+\s+\w+|\d{6}", text):
        pii_matches.append("address or pincode")

    return pii_matches



@celery_app.task(name="app.tasks.enrich_task.enrich_chat",bind=True, max_retries=3, default_retry_delay=5)
def enrich_chat(self, prompt: str, response: str):
    try:
        full_text = f"User: {prompt}\nBot: {response}"

        # Simulate a failure for testing
        if "fail" in prompt.lower():
            raise ValueError("Simulated failure!")

        pii = detect_pii(full_text)
        summary_prompt = f"Summarize this chat:\n\n{full_text}"
        summary = llm.invoke([HumanMessage(content=summary_prompt)]).content

        save_chat_log(prompt, response, summary, pii)

        print("✅ Chat saved to DB with summary + PII")

    except Exception as exc:
        print(f"❌ Error in enrich_chat: {exc}")
        try:
            self.retry(exc=exc)
        except Retry:
            pass  # Retry raised internally, ignore
        raise Ignore()  # prevent further error propagation


