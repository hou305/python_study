# -*- encoding:utf-8 -*-
from kombu import Queue
BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND= "redis://localhost:6379/2"
CELERY_TIMEZONE='Aisa/shanghai'

CELERY_DEFULT_QUEUE = 'default' #request queue and custom queue
#这个就是配置worker监控的队列地址，如果不指定，则无法从该队列取任务执行
#创建任务队列
CELERY_QUEUES = (
    Queue('default', routing_key='default'),#不指定这行代码会报错
    Queue('for_one', routing_key='for_one'),
    Queue('for_two', routing_key='for_two')
)
#配置路由，即告诉worker哪个任务从哪个队列中去取值执行
#这个配置起什么作用，当没有这个配置的时候，在send_task还是会指定任务放置的队列，并从对应的队列取值
# CELERY_ROUTES = {
#     'send_task.tasks.add':{
#         "queue":"for_one",
#         "routing_key":"for_one"
#     },
#     'send_task.tasks.multiply': {
#         "queue": "for_two",
#         "routing_key": "for_two"
#     }
# }

#当没有配置路由的时候，对应队列还是可以取出任务并执行

