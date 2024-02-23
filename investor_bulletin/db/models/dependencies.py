from db.models.model_base import SessionLocal


def get_db ():
    """Get the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
