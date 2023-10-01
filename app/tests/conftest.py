from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.db.database import Base, get_db
from main import app
from app.db.models import Question

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    # poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


def init_db(db: Session):

    question1 = Question(text="What is the capital of France?")
    db.add(question1)

    question2 = Question(text="How does photosynthesis work?")
    db.add(question2)

    db.commit()
    db.close()


app.dependency_overrides[get_db] = override_get_db

