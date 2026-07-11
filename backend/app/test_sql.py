from app.sql_generator import generate_sql

question = "Show all employees"

sql = generate_sql(question)

print(sql)