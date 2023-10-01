from pydantic import BaseModel


class QuestionBase(BaseModel):
    text: str

class QuestionCreate(QuestionBase):
    """
    Model to create new question in database
    """
    pass


class QuestionDb(QuestionBase):
    """
    Model to read question from database
    """
    answer: str
    class Config:
        orm_mode = True



class AnswerCreate(BaseModel) :
    text: str