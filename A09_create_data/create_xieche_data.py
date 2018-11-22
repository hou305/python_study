# -*- coding:utf-8 -*-
__author__ = "jolting"
__date__ = "$2018-10-16$"
__doc__ = "generate xieche_data to tms:vehicle:unload30"
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append('../../')

import traceback
import redis
import uuid
import datetime
import time
#get jg redis object, db select different
#get camel redis object,db select different

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB0 = 0
REDIS_DB1 = 1
r_jg = redis.StrictRedis(host = REDIS_HOST,port = REDIS_PORT, db = REDIS_DB0)

# REDIS_URL ="redis://:%s@%s:%s/%s"%(REDIS_PASSWORD,REDIS_HOST,REDIS_PORT,REDIS_DB)
# redis = redis.form_url(REDIS_URL)
jg_list = "tms:vehicle:unload30"
camel_list = "camel:success:list:unload30"

# redis_obj = dict(jg =lambda:redis.StrictRedis(host = REDIS_HOST, port = REDIS_PORT, db =REDIS_DB0)
#     ,camel = lambda:redis.StrictRedis(host = REDIS_HOST, port = REDIS_PORT, db =REDIS_DB1))
#需要切换连接redis对象的时候，可以直接使用dict对象，将redis连接用lambda定义函数，返回一个函数对象

# def get_redis(source):
#     return redis_obj[source]()

def get_key(r,key):
    return r.get(key)

def lpush_key(r,key,value):
    return r.lpush(key,value)

def lpop_key(r,key):
    r.lpop(key)

def set_key(r,key,value):
    return r.set(key,value)

def run():
    updateTime = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
    xieche_data = [
    {"containerNo":'',#车签为空
    "isUp30":'1',
    "orgCode":"000111",
    "updateTime":updateTime
    },
    {"containerNo":'CQ0000003173',
    "isUp30":'',#是否超过30为空
    "orgCode":"000111",
    "updateTime":updateTime
    },
    {
    "containerNo":'CQ0000003172',
    "isUp30":'1',
    "orgCode":"",#操作中心为空
    "updateTime":updateTime
    },
    {"containerNo":'CQ0000003171',
    "isUp30":'1',#是否超过30为空
    "orgCode":"000111",
    "updateTime":""#更新时间为空
    },
    {"containerNo":'CQ0000003456',#不存在的车签号
    "isUp30":'1',
    "orgCode":"000111",
    "updateTime":updateTime
    },
    {"containerNo":'CQ0000003170',#不存在的车签号
    "isUp30":'1',
    "orgCode":"210901",#操作中心与运单操作中心不符
    "updateTime":updateTime
    },
    {"containerNo":"CQ0000003169",
    "isUp30":'1',#超过30件
    "orgCode":"000111",
    "updateTime":updateTime
    },
    {"containerNo":"CQ0000003168",
    "isUp30":'1',#未超过30件
    "orgCode":"000111",
    "updateTime":updateTime
    }]
    print "jg redis insert data"
    for data in xieche_data:
        print type(data)
        try:
            key = uuid.uuid1()
            set_key(r_jg,key,str(data))
            lpush_key(r_jg,jg_list, key)
            print "插入数据成功"
        except Exception,e:
            print e



if __name__== "__main__":
    run()


