from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Employee
from app.schemas import EmployeeResponse, QueryRequest
from app.sql_generator import generate_sql
from app.query_executor import execute_sql

router = APIRouter()


@router.get("/employees", response_model=list[EmployeeResponse])
def get_employees():

    db: Session = SessionLocal()
    try:
        employees = db.query(Employee).all()
        return employees
    finally:
        db.close()

@router.post("/query")
def query_database(request: QueryRequest):
    sql_query = generate_sql(request.question)

    if not sql_query.strip().lower().startswith("select"):
        raise HTTPException(
            status_code=400,
            detail="Only SELECT queries are allowed."
        )

    try:
        results = execute_sql(sql_query)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    return {
        "question": request.question,
        "generated_sql": sql_query,
        "results": results,
    }