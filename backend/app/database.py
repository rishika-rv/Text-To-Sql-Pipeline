import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path


# DATABASE_URL = "sqlite:///data/company.db"


DATABASE_PATH = os.getenv("DATABASE_PATH", "data/company.db")
DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


print("Current working directory:", Path.cwd())
print("Database path:", Path("data/company.db").resolve())
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
 