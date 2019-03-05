# -*- coding:utf-8 -*-
__author__ = "jolting"
__date__ = "2018-05-22"

import traceback
import sys
import requests
import logging
from logging import handlers
import time, datetime
import os
import hashlib

class BasePerformer(object):
    """接口测试的所需要的底层方法"""

    def __init__(self):
        current_path = os.getcwd()
        sys.path.append(current_path)
        reload(sys)
        super(BasePerformer, self).__init__()

    @staticmethod
    def post(url, path, data, files=None):
        """post请求方法"""
        try:
            r = requests.post(url + path, data=data, files=files)
            return r.json()
        except Exception, e:
            print "http请求异常%s" % str(e)
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def get(url, path, data):
        """get请求方法"""
        try:
            r = requests.get(url = url + path, data=data)
            return r.json()
        except Exception, e:
            print "http请求异常%s" % str(e)
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def put(url, path, data):
        try:
            r = requests.put(url = url + path, data=data)
            return r.json()
        except Exception, e:
            print "http请求异常%s" % str(e)
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def setup(self):
        pass

    @staticmethod
    def teardown(self):
        pass


    def md5(self, text):
        """将MD5方法封装"""
        hl = hashlib.md5()
        hl.update(text.encoding("utf-8"))
        return hl.hexdigest()