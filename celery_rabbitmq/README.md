# Wallpaper Download Service

The Wallpaper Download Service is a simple application that provides endpoints for fetching wallpapers for PCs and phones. It uses the FastAPI framework for handling HTTP requests and Celery for asynchronous task processing.

## Features

- Retrieve random PC and phone wallpapers.
- Asynchronous wallpaper retrieval using Celery.
- The wallpapers are chosen randomly from a set of images.

## Prerequisites

- Python 3.6 or higher
- Docker (if you want to run RabbitMQ using a Docker container)
- RabbitMQ (You can use the provided Docker command to run it)

## Installation

1. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

2.Run RabbitMQ:

   ```shell
   docker run -d -p 5672:5672 rabbitmq
   ```

3. Start a Celery worker to process wallpaper retrieval tasks:

   ```shell
   celery -A celery_rabbitmq.main worker -l info
   ```

4. Start the FastAPI application:

   ```shell
   python celery_rabbitmq/main.py
   ```

## Usage

Once the application is running, you can access the following endpoints:

- **Get a PC Wallpaper:** `http://localhost:8000/pc`
- **Get a Phone Wallpaper:** `http://localhost:8000/phone`

The wallpapers are returned as image files.

## Task Monitoring

You can monitor Celery tasks by accessing the Celery Flower web interface. To run Flower, use the following command:

```shell
celery -A celery_rabbitmq.main flower
```

Then, visit `http://localhost:5555` in your web browser to monitor the tasks.
