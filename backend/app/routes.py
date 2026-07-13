from fastapi import APIRouter, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.sql_validator import validate_sql
from app.database import SessionLocal
from app.models import Employee
from app.schemas import EmployeeResponse, QueryRequest
from app.sql_generator import generate_sql
from app.query_executor import execute_sql
from app.logger import logger


from pathlib import Path
import shutil

router = APIRouter()


DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)
CURRENT_DB_PATH = str(DATA_DIR / "company.db")


@router.get("/employees", response_model=list[EmployeeResponse])
def get_employees():

    db: Session = SessionLocal()
    try:
        employees = db.query(Employee).all()
        return employees
    finally:
        db.close()


@router.post("/upload-db")
def upload_database(file: UploadFile = File(...)):
    global CURRENT_DB_PATH
    if not (file.filename.endswith(".db") or file.filename.endswith(".sqlite")):
        raise HTTPException(
            status_code=400,
            detail="Only SQLite database files (.db, .sqlite) are allowed."
        )

    file_path = DATA_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    CURRENT_DB_PATH = str(file_path)

    return {
        "message": "Database uploaded successfully.",
        "filename": file.filename,
        "path": str(file_path)
    }

@router.post("/query")
def query_database(request: QueryRequest):
    sql_query = generate_sql(request.question, CURRENT_DB_PATH)

    validated_sql = validate_sql(sql_query)
    logger.info(f"Generated and validated SQL: {validated_sql}")

    # if not sql_query.strip().lower().startswith("select"):
    #     raise HTTPException(
    #         status_code=400,
    #         detail="Only SELECT queries are allowed."
    #     )

    try:
        results = execute_sql(validated_sql, CURRENT_DB_PATH)
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    return {
        "question": request.question,
        "generated_sql": validated_sql,
        "results": results,
    }