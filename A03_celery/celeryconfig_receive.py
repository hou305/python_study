# -*- encoding:utf-8 -*-
from kombu import Queue
BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"

CELERY_DEFULT_QUEUE = 'default'
CELERY_QUEUES = (
    Queue('default', routing_key='default'),
    Queue('for_receive', routing_key='for_receive')
)
# 任务路由，定义了这个，celery可以找到对应路由，然后放入队列
CELERY_ROUTES = {
    'celery02.receive_task.tasks.get_values':{
        "queue":"for_receive",
        "routing_key":"for_receive"
    }
}
