from sqlalchemy.orm import Session

from app.db.models import Question
from app.db.schemas import QuestionCreate


def get_questions(skip, limit, db: Session):
    """
    Get a list of all the questions.

    Parameters:
    - skip (int): Number of questions to skip
    - limit (int): Maximum number of questions to return
    - db (Session): Database session

    Returns:
    - List[Question]: A list of recent questions.
    """
    questions = db.query(Question).offset(skip).limit(limit).all()
    return questions


def create_question(question: QuestionCreate, db: Session):
    """
    Create a new question.

    Parameters:
    - question (QuestionCreate): The data for the new question.
    - db (Session): Database session
    Returns:
    - Question: The created question with its unique identifier.
    """
    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


# Get answers to a specific question by question_id
def get_question(question_id: int, db: Session):
    """
    Get answers to a specific question.

    Parameters:
    - question_id (int): The unique identifier of the question.
    - db (Session): Database session

    Returns:
    - List[Answer]: A list of answers to the question.
    """
    question = db.query(Question).filter(Question.id == question_id).first()
    return question
