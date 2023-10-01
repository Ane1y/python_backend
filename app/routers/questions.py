from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import crud
from app.db.database import get_db
from app.db.schemas import QuestionCreate, QuestionDb, AnswerCreate

router = APIRouter()


@router.get("/questions/")
def get_questions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get a list of all the questions.

    Parameters:
    - skip (int): Number of questions to skip
    - limit (int): Maximum number of que    stions to return
    - db (Session): Database session

    Returns:
    - List[Question]: A list of recent questions.
    """
    questions = crud.get_questions(skip, limit, db)
    return questions


@router.post("/questions/", response_model=QuestionDb)
def create_question(question: QuestionCreate, db: Session = Depends(get_db)):
    """
    Create a new question.

    Parameters:
    - question (QuestionCreate): The data for the new question.
    - db (Session): Database session
    Returns:
    - Question: The created question
    """
    q = crud.create_question(question, db)
    return QuestionDb(text=q.text, id=q.id, answer=q.answer)


# Get answers to a specific question by question_id
@router.get("/questions/{question_id}/answers/")
def get_question_answers(question_id: int, db: Session = Depends(get_db)):
    """
    Get answers to a specific question.

    Parameters:
    - question_id (int): The unique identifier of the question.
    - db (Session): Database session

    Returns:
    - List[Answer]: A list of answers to the question.
    """
    question = crud.get_question(question_id, db)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    return question.answer

# Create an answer to a specific question by question_id
@router.post("/questions/{question_id}/answer/", response_model=QuestionDb)
def add_answer_to_question(
    question_id: int,
    answer_data: AnswerCreate,
    db: Session = Depends(get_db)
):
    """
    Add an answer to a specific question.

    Parameters:
    - question_id (int): The unique identifier of the question.
    - answer_data (AnswerCreate): The data for the answer.
    - db (Session): Database session.

    Returns:
    - QuestionDb: The updated question with the added answer.
    """
    question = crud.get_question(question_id, db)

    if not question:
        raise HTTPException(status_code=404, detail="Question not found")

    question.answer = answer_data.text
    db.commit()
    return question