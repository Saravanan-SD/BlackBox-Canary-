from celery import Celery
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

celery_app = Celery(
    "blackbox_canary",
    broker="redis://localhost:6379/0",  # Change if using a remote Redis
    backend="redis://localhost:6379/0"

)

# celery_app.autodiscover_tasks(["app.tasks"])

from app.tasks import log_task, enrich_task