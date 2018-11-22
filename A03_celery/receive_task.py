# -*- encoding:utf-8 -*-
from celery import Celery

celery = Celery('task')
celery.config_from_object('celeryconfig')

@celery.task
def get_values(data):
    try:
        print "receive data is %s"%data
    except Exception,e:
        print e
