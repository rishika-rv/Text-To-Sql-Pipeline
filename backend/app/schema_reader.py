from sqlalchemy import inspect
from app.database import engine


def get_database_schema():
    inspector = inspect(engine)

    schema = "Database Schema\n\n"

    for table in inspector.get_table_names():
        schema += f"Table: {table}\n"

        columns = inspector.get_columns(table)

        for column in columns:
            schema += f"- {column['name']}\n"

        schema += "\n"

    return schema