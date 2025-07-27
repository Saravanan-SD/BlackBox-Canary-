from celery_app import celery_app
from app.tasks.enrich_task import enrich_chat

@celery_app.task(name="app.tasks.log_task.log_chat")
def log_chat(prompt: str, response: str):
    print("📦 Logging Chat:")
    print("Prompt:", prompt)
    print("Response:", response)

    # Chain enrichment task
    enrich_chat.delay(prompt, response)
