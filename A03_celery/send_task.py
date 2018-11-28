# -*- encoding:utf-8 -*-
import time
from celery import Celery
app = Celery('task')
app.config_from_object('celeryconfig_send')

receive_celery = Celery('task')
receive_celery.config_from_object('celeryconfig_receive')
#t同一个celery实例，不同队列
#同一个celery实例，不同队列
#不同实例，不同队列
#不同实例，同一个队列
@app.task
def add(x, y):
    print "action"
    t = x+y
    receive_celery.send_task('receive_task.get_values', args=[t], queue="for_receive")
    """在add任务执行过程中，重新发一个任务到for_receive队列，给定一个该任务所需要的参数"""
    print "over"
    return t


