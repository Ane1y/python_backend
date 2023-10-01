# test_app.py
from starlette.testclient import TestClient

from main import app
import app.tests.conftest as conftest
from app.db import crud
from app.db.schemas import AnswerCreate

client = TestClient(app)


# Test on creating questions
def test_create_question():
    test_question = "Test question"
    response = client.post("/questions/", json={"text": test_question})
    assert response.status_code == 200
    assert response.json()["text"] == test_question


def test_create_invalid_question():
    response = client.post("/questions/")
    assert response.status_code == 422  # Validation error


# Test on getting questions
def test_get_questions():
    response = client.get("/questions/")
    assert response.status_code == 200


# Tests on getting answers
def test_get_question_answers():
    question_id = 1
    response = client.get(f"/questions/{question_id}/answers/")
    assert response.status_code == 200
    question = crud.get_question(question_id, conftest.TestingSessionLocal())
    assert response.json() == question.answer


def test_get_invalid_answer_idx():
    question_id = 900
    response = client.get(f"/questions/{question_id}/answers/")
    assert response.status_code == 404


# Tests on create answer
def test_create_answer_to_question():
    question_id = 1
    answer_data = "Test answer"
    AnswerCreate(text=answer_data)
    response = client.post(
        f"/questions/{question_id}/answer/", json={"text": answer_data}
    )
    assert response.status_code == 200
    question = crud.get_question(question_id, conftest.TestingSessionLocal())
    assert question.answer == answer_data


def test_create_answer_to_question_nonexistent_question():
    question_id = 999  # Non-existent question ID
    answer_data = {"text": "Test answer"}
    response = client.post(f"/questions/{question_id}/answer/", json=answer_data)
    assert response.status_code == 404
