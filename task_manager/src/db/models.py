from sqlalchemy import Column, Integer, String

from task_manager.src.db.database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, index=True)
    answer = Column(String)
