from fastapi import FastAPI
from app.db import models
from app.db.database import engine
from app.routers.questions import router as question_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(question_router)
