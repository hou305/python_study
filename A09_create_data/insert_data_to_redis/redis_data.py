#/usr/bin/env python
# -*- coding:utf-8 -*-
#author :jolting

import redis
import random
from config import Generate_data as G
import requests
import json
import uuid


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
class Performer(object):
    """连接redis 存入测试数据之后在取出推送"""
    def __init__(self):
        super(Performer, self).__init__()

    def connect_redis(self):
        """连接redis"""
        try:
            redis_config = {
            "host":"127.0.0.1",
            "port":6379
            }
            redis_conn = redis.Redis(**redis_config)
            print u"redis连接成功"
            return redis_conn
        except Exception as e:
            print u"redis连接异常"
            return False

    def insert_data_redis(self):
        """连接redis并插入数据"""
        re = self.connect_redis()
        if not re:
            print "failed"
            return False
        results = G().generaet_gps_data(5)
        for data in results:
            re.lpush("java.monitor.gpstojg",data)
        return re

#分为两部分，第一步部分是为了实现往redis插入数据，本地如果只为了测试接口，则不需要插入redis这一步骤
    def post_data(self):
        """redis取数据,并推送数据"""
        re = self.insert_data_redis()
        if re:
            llen = re.llen('java.monitor.gpstojg')
            results = re.lrange('java.monitor.gpstojg', 0, llen-1)
            for i in range(0,llen):
                pa = json.loads(re.lpop('java.monitor.gpstojg'))
                try:
                    body = {
                    "bizCode":"50001",
                    "coordinfo":{
                        "deviceId":pa['moid'],
                        "gpstime":pa['time'],
                        "coordType":pa['encode'],
                        "lon":pa['lon'],
                        "lat":pa['lat'],
                        "hight":pa['altitue'],
                        "speed":pa['speed'],
                        "direct":pa['direction'],
                        "accuracy":"127.0",
                        "status":pa['status'],
                        "address":pa['address'],
                        "providerType":pa['provider']
                        },
                    "requestId":uuid.uuid4()
                    }
                    headers = {
                    "content-type":"application/json",
                    "yunmeng.decrypt.key":"anNjLnl0bzU2LmNvbQ1234",
                    "yunmeng.signkey.key":"bG1fdG9fanNjLnl0bzU2LmNvbQ=="
                    }
                    print body

                    # r= requests.post("http://58.32.246.70:7777"+'/post_coreOfGps',data = body,headers=headers)
                    # print "金刚返回接口结果：%s"%：r.json()
                except Exception as e:
                    print u"http请求失败"
