# Student Records API (SQL Demo)

A simple FastAPI-based backend that demonstrates structured data handling using SQL (SQLite) and Python.

## 🚀 Tech Stack
- Python 3.10+
- FastAPI
- SQLite (via SQLAlchemy)
- Uvicorn

## 📦 Features
- Add new students with name + grade
- Fetch student records
- Lightweight SQL backend
- Easily portable to Postgres/MySQL

## 📚 API Endpoints

| Method | Endpoint       | Description           |
|--------|----------------|-----------------------|
| GET    | `/`            | Welcome route         |
| POST   | `/students/`   | Add a student         |
| GET    | `/students/`   | Get all students      |

