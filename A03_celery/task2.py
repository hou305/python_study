# -*- encoding:utf-8 -*-


@celery.task
def multiply(x, y):
    return x * y