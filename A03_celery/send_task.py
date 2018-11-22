# -*- encoding:utf-8 -*-
import time
from celery import Celery
import celeryconfig
celery = Celery('Tasks')
celery.config_from_object('celeryconfig')
# #
# # real_celery = Celery('Tasks')
# # real_celery.config_from_object('celeryconfig_other')


# brokers = "redis://localhost:6379/1"
# backend = "redis://localhost:6379/2"
# celery = Celery('send_task',broker =brokers,backend=backend)
# @celery.task
# def add(x, y):
#     try:
#         t = x + y
#         real_celery.send_task('receive_task.get_values',args=[t], queue = 'custom')
#         print "celery task ok"
#
#     except Exception,e:
#         print e


@celery.task
def add(x, y):
    print "action"
    time.sleep(60)
    print "over"
    return x+y
