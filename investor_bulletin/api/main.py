from api.routes import init_routes
from db.models.model_base import engine,Base
from fastapi import FastAPI
from uvicorn import run

# Create all tables in the database on startup
Base.metadata.create_all(bind = engine)

app = init_routes(FastAPI())

if __name__ == "__main__":
    run("api.main:app",reload = True)
