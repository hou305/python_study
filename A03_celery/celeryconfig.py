# -*- encoding:utf-8 -*-

#celery用到的broker,result的redis配置信息
from celery import Celery
from celery.secdule import contrtab
from datetime import timedelta
BROKER_URL = "redis://localhost:6379/1"
CELERY_RESULT_BACKEND = "redis://localhost:6379/2"

#可以设置定时任务，需要导入模块
CELERY_IMPORTS = {
    'celery_study.task1',
    'celery_study.task2',
}


#定时任务
CELERYBEAT_SCHEDULE = {
    "task1":{
    'task':'celery_study.task1.add',
    'secdule':timedelta(seconds=10),
    'args':(2,2)
    }
}