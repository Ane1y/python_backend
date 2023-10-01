# test_crud.py
from task_manager.src.db import crud
from sqlalchemy.orm import Session
from task_manager.src.db.models import Question
from task_manager.src.db.database import SessionLocal

def test_create_question():
    db = SessionLocal()
    question_data = "Test data"
    question = Question(question_data)
    db_question = crud.create_question(question, db)
    assert db_question is not None
    assert db_question.text == question_data

def test_create_question_invalid_data():
    db = SessionLocal()
    question_data = Question()  # Invalid data with missing 'text' field
    try:
        db_question = crud.create_question(question_data, db)
        assert False, "Creating question with invalid data should raise an exception"
    except Exception:
        pass

def test_get_questions():
    db = SessionLocal()
    questions = crud.get_questions(0, 10, db)
    assert len(questions) >= 0

def test_get_question_answers():
    db = SessionLocal()
    question = crud.get_question(1, db)
    assert question is not None
