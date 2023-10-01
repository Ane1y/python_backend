# test_app.py
from fastapi.testclient import TestClient
from task_manager.main import app

client = TestClient(app)

def test_create_question():
    response = client.post("/questions/", json={"text": "Test question"})
    assert response.status_code == 200

def test_get_questions():
    response = client.get("/questions/")
    assert response.status_code == 200

def test_get_question_answers():
    # Assuming you have a question with ID 1 in your database
    response = client.get("/questions/1/answers/")
    assert response.status_code == 200
