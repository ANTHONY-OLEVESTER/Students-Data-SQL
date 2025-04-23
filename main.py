from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from models import Student
from database import SessionLocal, engine, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/students/")
def create_student(name: str, grade: str, db: Session = Depends(get_db)):
    student = Student(name=name, grade=grade)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

@app.get("/students/")
def read_students(db: Session = Depends(get_db)):
    return db.query(Student).all()
