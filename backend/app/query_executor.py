from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from app.database import get_engine
from app.logger import logger



def execute_sql(sql_query: str, db_path: str | None = None):
    """Execute a read-only SQL query and return the results as a list of dictionaries."""
    engine = get_engine(db_path)
    SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
    db = SessionLocal()

    try:
        result = db.execute(text(sql_query))
        rows = result.mappings().all()
        return [dict(row) for row in rows]
    finally:
        db.close()

logger.info("Query results executed successfully.")