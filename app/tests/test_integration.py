import requests

BASE_URL = "http://localhost:8000"

def test_create_question():
    question_data = "Test Question"
    question = {"text": question_data}
    response = requests.post(f"{BASE_URL}/questions/", json=question)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["text"] == question_data

def test_get_questions():
    response = requests.get(f"{BASE_URL}/questions/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_question_answers():
    # Assuming you have a question with ID 1 in your database
    question_id = 1
    response = requests.get(f"{BASE_URL}/questions/{question_id}/answers/")
    assert response.status_code == 200
    assert isinstance(response.json(), str)

def test_add_answer_to_question():
    # Assuming you have a question with ID 1 in your database
    question_id = 1
    answer_data = {"text": "Integration Test Answer"}
    response = requests.post(f"{BASE_URL}/questions/{question_id}/answer/", json=answer_data)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["answer"] == "Integration Test Answer"
