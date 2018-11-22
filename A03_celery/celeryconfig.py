# -*- encoding:utf-8 -*-
from kombu import Queue
BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"


CELERY_DEFULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', routing_key='defalut'),
    Queue('for_add', routing_key='for_add')
)

CELERY_ROUTES = {
    'send_task.TASKS.add':{
        "queue":"for_add",
        "routing_key":"for_add"
    }
}