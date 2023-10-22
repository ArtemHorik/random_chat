import os


class Config:
    TOKEN = os.getenv('TOKEN')

    REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)
    REDIS_USER = os.getenv('REDIS_USER')
    REDIS_PASSWORD = os.getenv('REDIS_PASS')

    WEBHOOK_PATH = f'/bot/{TOKEN}'
    WEBHOOK_URL = os.getenv('WEBHOOK_URL') + WEBHOOK_PATH

    WEBAPP_HOST = '0.0.0.0'
    WEBAPP_PORT = os.getenv('WEBAPP_PORT', '80')