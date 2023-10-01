from fastapi import FastAPI
import uvicorn

from app.routers.questions import router as question_router

app = FastAPI()
app.include_router(question_router)
if __name__ == "__main__":
    # create_initial_data()
    uvicorn.run(app, host="localhost", port=8000)
