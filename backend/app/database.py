import os

from app.logger import logger

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path


DEFAULT_DB = "company.db"
DATABASE_PATH = os.getenv("DATABASE_PATH", f"data/{DEFAULT_DB}")

def get_engine(db_path: str | None = None):
    database_path = db_path or DATABASE_PATH
    database_url = f"sqlite:///{database_path}"

    logger.info(f"Using database: {database_path}")

    return create_engine(
        database_url,
        connect_args={"check_same_thread": False}
    )

engine = get_engine()

logger.info(f"Current working directory: {Path.cwd()}")

logger.info(f"Database path: {Path('data/company.db').resolve()}")


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 