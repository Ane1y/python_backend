import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

from celery_rabbitmq.tasks import pc_wallpaper, phone_wallpaper, app

some_file_path = "large-video-file.mp4"
fastapiApp = FastAPI()



@fastapiApp.get("/pc", response_class=FileResponse)
async def main():
    """
    Get a PC wallpaper

    Returns:
        FileResponse: A PC wallpaper file in the response.
    """
    res = pc_wallpaper.delay()
    return res.get()


@fastapiApp.get("/phone", response_class=FileResponse)
async def main():
    """
    Get a phone wallpaper

    Returns:
        FileResponse: A phone wallpaper file in the response.
    """
    res = phone_wallpaper.delay()
    return res.get()

if __name__ == "__main__":
    uvicorn.run("main:fastapiApp")