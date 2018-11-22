#-*- encoding:utf-8 -*-
#date=2018-09-11
#author=jolting

import MySQLdb
import redis
import config
import time


def conn_mysql():
    """连接mysql数据库"""
    try:
        db = MySQLdb.connect(**config.db_config)
        cursor = db.cursor()
        print u"mysql连接成功"
        return cursor
    except Exception as e:
        print u"mysql连接异常"

def connect_redis():
    """连接redis"""
    try:
        pool = redis.ConnectionPool(**config.redis_config)
        redis_conn = redis.Redis(connection_pool=pool)
        print u"redis连接成功"
        return redis_conn
    except Exception as e:
        print u"redis连接异常"
        return False

def sel_trans():
    """数据库查询数据"""
    mdb = conn_mysql()
    sql = "select waybill_number from wb_logink_data"
    mdb.execute(sql)
    trans_numbers = mdb.fetchall()
    return trans_numbers

def insert_trans_to_redis1():
    """塞入运单号到redis"""
    trans = sel_trans()
    re = connect_redis()
    if re:
        for tr in trans:
            re.lpush("camel:waybill:trans:list", tr)
        print re.llen("camel:waybill:trans:list")
        print u"执行时间1为：%s"%time.ctime()
        time.sleep(5)
        print u"结束时间1%s"%time.ctime()

def insert_trans_to_redis2():
    """塞入运单号到redis"""
    trans = sel_trans()
    re = connect_redis()
    if re:
        for tr in trans:
            re.lpush("camel:waybill:trans:list", tr)
        print re.llen("camel:waybill:trans:list")
        print u"执行时间2为：%s"%time.ctime()
        time.sleep(3)
        print u"结束时间2%s"%time.ctime()