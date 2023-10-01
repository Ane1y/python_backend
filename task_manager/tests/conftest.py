import os

import pytest
import tempfile
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task_manager.src.db.database import Base, SessionLocal
from task_manager.main import app
from task_manager.src.db.database import engine
from task_manager.src.db.models import Question


@pytest.fixture(scope="module")
def test_db_url():
    db_fd, db_name = tempfile.mkstemp()
    db_url = f"sqlite:///{db_name}"
    init_db()
    yield db_url
    Base.metadata.drop_all(bind=engine)
    os.close(db_fd)
    os.unlink(db_name)

@pytest.fixture(scope="module")
def test_db_session(test_db_url):
    engine = create_engine(test_db_url)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define a fixture to create a TestClient for testing FastAPI endpoints
@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)

def init_db():
    db = SessionLocal()

    question1 = Question(text="What is the capital of France?")
    db.add(question1)

    question2 = Question(text="How does photosynthesis work?")
    db.add(question2)

    db.commit()
    db.close()