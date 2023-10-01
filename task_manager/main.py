from fastapi import FastAPI
import uvicorn

from task_manager.src.db import models
from task_manager.src.db.database import engine, SessionLocal
from task_manager.src.db.models import Question
from task_manager.src.routers.questions import router as question_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()




app.include_router(question_router)
if __name__ == "__main__":

    uvicorn.run(app, host="0.0.0.0", port=8000)
