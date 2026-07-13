from sqlalchemy import inspect
from app.database import get_engine
from app.logger import logger



def get_database_schema(db_path: str):
    engine = get_engine(db_path)
    inspector = inspect(engine)

    schema = "Database Schema\n\n"

    for table in inspector.get_table_names():
        schema += f"Table: {table}\n"

        columns = inspector.get_columns(table)

        for column in columns:
            schema += f"- {column['name']}\n"

        schema += "\n"
    logger.info(f"Database schema retrieved successfully from {db_path}.")

    return schema