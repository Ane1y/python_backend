# test_crud.py
from app.db import crud
from app.db.models import Question
from app.db.schemas import QuestionCreate
from app.tests.conftest import TestingSessionLocal

db = TestingSessionLocal()


# Tests for create questions
def test_create_question():
    question_data = "Test data"
    question = QuestionCreate(text=question_data)
    db_question = crud.create_question(question, db)
    assert db_question is not None
    assert db_question.text == question_data


def test_create_question_invalid_data():
    question_data = Question()  # Invalid data with missing 'text' field
    try:
        crud.create_question(question_data, db)
        assert False, "Creating question with invalid data should raise an exception"
    except Exception:
        pass


# nTests for get questions
def test_get_questions():
    questions = crud.get_questions(0, 10, db)
    assert len(questions) >= 0


# Tests for get question by id
def test_get_question_answers_invalid_id():
    question = crud.get_question(999, db)  # Non-existent ID
    assert question is None


def test_get_question_answers_negative_id():
    question = crud.get_question(-1, db)  # Negative ID
    assert question is None
