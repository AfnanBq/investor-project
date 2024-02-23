from celery import Celery

# Create a celery app object to start your workers

def create_celery_app():
  return Celery(
    "worker",
    broker="pyamqp://guest@localhost//",
    include=["worker.tasks"],

  )

app = create_celery_app()
