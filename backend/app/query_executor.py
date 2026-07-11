from sqlalchemy import text

from app.database import SessionLocal


def execute_sql(sql_query: str):
    """Execute a read-only SQL query and return the results as a list of dictionaries."""

    db = SessionLocal()

    try:
        result = db.execute(text(sql_query))
        rows = result.mappings().all()
        return [dict(row) for row in rows]
    finally:
        db.close()