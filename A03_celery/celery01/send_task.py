# -*- encoding:utf-8 -*-
import time
from celery import Celery
app = Celery('task')
app.config_from_object('celeryconfig_send')

@app.task
def add(x, y):
    print "add"
    return x+y

@app.task
def multiply(a, b):
    print "multiply"
    return a * b