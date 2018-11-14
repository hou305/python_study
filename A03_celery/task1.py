# -*- encoding:utf-8 -*-

import time
from celery import Celery
#这里是需要执行的任务
broker='redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
app = Celery('my_task', broker=broker, backend = backend)
#实例化一个celery
#相当于注册为一个任务，到时候执行的时候会将这个任务发送至broker里面
@app.task
def add(x, y):
    time.sleep(4)
    return x+y