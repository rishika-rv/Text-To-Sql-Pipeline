from pydantic import BaseModel


class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    salary: int
    city: str
    department_id: int

    class Config:
        from_attributes = True

class QueryRequest(BaseModel):
    question: str