# -*- encoding:utf-8 -*-
from kombu import Queue
BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND= "redis://localhost:6379/2"
CELERY_TIMEZONE='Aisa/shanghai'

CELERY_DEFULT_QUEUE = 'default' #request queue and custom queue
#创建任务队列
CELERY_QUEUES = (
    Queue('default', routing_key='default'),#不指定这行代码会报错
    Queue('for_one', routing_key='for_one'),
    Queue('for_two', routing_key='for_two')
)
#任务路由，相当于告诉worker，从哪里取获取要执行的哪个任务函数，当找不到任务对应的函数方法时，会报错
CELERY_ROUTES = {
    'send_task.tasks.add':{
        "queue":"for_one",
        "routing_key":"for_one"
    },
    'send_task.tasks.multiply': {
        "queue": "for_two",
        "routing_key": "for_two"
    }
}


