import re

def validate_sql(sql: str):
    sql = sql.strip()

    # Must start with SELECT
    if not re.match(r"^SELECT\b", sql, re.IGNORECASE):
        raise ValueError("Only SELECT queries are allowed.")

    # Block dangerous keywords
    forbidden = [
        "INSERT",
        "UPDATE",
        "DELETE",
        "DROP",
        "ALTER",
        "CREATE",
        "TRUNCATE",
        "REPLACE",
        "ATTACH",
        "DETACH",
        "PRAGMA"
    ]

    upper_sql = sql.upper()

    for keyword in forbidden:
        if keyword in upper_sql:
            raise ValueError(f"{keyword} queries are not allowed.")

    return sql