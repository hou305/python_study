# -*- coding:utf-8 -*-
__author__ = "jolting"
__date__ = "$2018-10-16$"
__doc__ = "generate dfc_data to tms:vehicle:unload30"
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('../../')

import random
import redis
import datetime
import json
from datetime import timedelta
import time
import logging
#get jg redis object, db select different
#get camel redis object,db select different

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB0 = 0
REDIS_DB1 = 1
r_jg = redis.StrictRedis(host = REDIS_HOST,port = REDIS_PORT, db = REDIS_DB0)

# REDIS_URL ="redis://:%s@%s:%s/%s"%(REDIS_PASSWORD,REDIS_HOST,REDIS_PORT,REDIS_DB)
# redis = redis.form_url(REDIS_URL)

jg_list = "JG_DFC_QUEUE"
camel_list = "camel:success:list:dfc"


def get_key(r,key):
    return r.get(key)

def lpush_key(r,key,value):
    return r.lpush(key,value)

def lpop_key(r,key):
    r.lpop(key)

def set_key(r,key,value):
    return r.set(key,value)


def generate_data():
    """生成到发车测试数据"""
    data_list = []
    for i in range(0,3000):
        cq_number = "CQ" + str(random.randint(1000000000,9999999999))
        op_code = random.choice(["140","160"])
        code = ["000111","210901","571901","000225","000212","574901"]
        location_code = random.choice(code)
        line_no = "MOT" + random.choice(code[:2]) + "TO" + random.choice(code[3:]) + "01"
        line_frequency_no = line_no + random.choice(["1100","1200"])
        now = datetime.datetime.now()
        pda_upload_time = datetime.datetime.strftime(now,"%Y-%m-%d %H:%M:%S")
        op_time = datetime.datetime.strftime(now + datetime.timedelta(minutes=-20),"%Y-%m-%d %H:%M:%S")
        vehicle_plate_no = random.choice(["粤","赣","陕", "皖","黑","浙","沪"]) + random.choice(["A","B","C", "D","E","F","H"]) + str(random.randint(11111,99999))
        fileds = [('waybillNo', 'cq_number'), ('orgCode', 'location_code'), ('opCode', 'op_code'),
                  ('lineNo', 'line_no'),
                  ('createTime', 'op_time'), ('uploadTime', 'pda_upload_time'), ('frequencyNo', 'line_frequency_no'),
                  ('lineFrequencyNo', 'line_frequency_no'), ('vehiclePlateNo', 'vehicle_plate_no')]
        data = dict(waybillNo=cq_number, opCode=op_code, lineNo=line_no, uploadTime=pda_upload_time, createTime=op_time,
                    lineFrequencyNo=line_frequency_no, vehiclePlateNo=vehicle_plate_no, orgCode=location_code)
        redis_data = json.dumps(data)
        data_list.append(redis_data)
    return data_list

def run():
    """将测试数据塞入jg队列"""
    redis_data = generate_data()
    for key,value in enumerate(redis_data):
        try:
            set_key(r_jg,key,value)
            lpush_key(r_jg,jg_list, key)
            print "插入数据成功"
        except Exception,e:
            print e

if __name__== "__main__":
    run()


