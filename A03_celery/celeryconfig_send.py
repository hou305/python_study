# -*- encoding:utf-8 -*-
from kombu import Queue
BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"

CELERY_DEFULT_QUEUE = 'default' #request queue and custom queue
#定义队列
CELERY_QUEUES = (
    Queue('default', routing_key='default'),
    Queue('for_add', routing_key='for_add'),
    Queue('for_receive',routing_key='for_receive')
)

# 定义哪个任务放置哪个队列
# CELERY_ROUTES = {
#     'send_task.task.add':{
#         "queue":"for_add",
#         "routing_key":"for_add"
#     },
#     'celery02.receive_task.task.get_values':{
#         "queue":"for_receive",
#         "routing_key":"for_receive"
#     }
# }
#根据路由找任务执行
CELERY_ROUTES = {
    'celery02.receive_task.task.get_values':{
        "queue":"for_receive",
        "routing_key":"for_receive"
    }
}





