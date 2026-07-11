from app.database import SessionLocal
from app.models import Department, Employee

db = SessionLocal()

# Don't insert data again if it already exists
if db.query(Department).first():
    print("Database already contains data.")
    db.close()
    exit()

# Create dep 
hr = Department(name="HR")
engineering = Department(name="Engineering")
sales = Department(name="Sales")
finance = Department(name="Finance")

db.add_all([hr, engineering, sales, finance])
db.commit()

# Refresh to get IDs
db.refresh(hr)
db.refresh(engineering)
db.refresh(sales)
db.refresh(finance)

# Create emp 
employees = [
    Employee(name="Alice", age=28, salary=50000, city="Indore", department_id=hr.id),
    Employee(name="Bob", age=32, salary=70000, city="Bhopal", department_id=engineering.id),
    Employee(name="Charlie", age=26, salary=45000, city="Indore", department_id=sales.id),
    Employee(name="David", age=35, salary=90000, city="Delhi", department_id=engineering.id),
    Employee(name="Emma", age=30, salary=65000, city="Mumbai", department_id=finance.id),
    Employee(name="Frank", age=29, salary=55000, city="Pune", department_id=hr.id),
]

db.add_all(employees)
db.commit()

print("Sample data inserted successfully!")

db.close()