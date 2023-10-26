import random

from celery import Celery

app = Celery('celery_rabbitmq',
                   broker='amqp://',
                   backend='rpc://',
                   include=['celery_rabbitmq.tasks'])

app.conf.update(
    result_expires=3600,
)

@app.task
def pc_wallpaper():
    """
      Get a random PC wallpaper path.

      Returns:
          str: A string representing the path to a PC wallpaper image.
      """
    num = random.randint(1, 3)
    return f"pc_wallpaper/{num}.{'png' if num == 3 else 'jpg'}"


@app.task
def phone_wallpaper():
    """
      Get a random phone wallpaper path.

      Returns:
          str: A string representing the path to a phone wallpaper image.
      """
    num = random.randint(1, 3)
    return f"phone_wallpaper/{num}.jpg"
