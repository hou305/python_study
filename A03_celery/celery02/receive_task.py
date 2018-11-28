# -*- encoding:utf-8 -*-
from celery import Celery
celery = Celery('tasks')
celery.config_from_object('celeryconfig_receive')

@celery.task
def get_values(data):
    try:
        print "receive data is %s"%data
    except Exception,e:
        print e
