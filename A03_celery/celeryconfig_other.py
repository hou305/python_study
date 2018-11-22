# -*- encoding:utf-8 -*-
from kombu import Queue

BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"


CELERY_DEFULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', routing_key='defalut'),
    Queue('custom', routing_key='custom')
)

CELERY_ROUTES = {
    'receive_task.tasks.get_values':{
        "queue":"custom",
        "routing_key":"custom"
    }
}
