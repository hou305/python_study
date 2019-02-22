# -*- coding:utf-8 -*-

__author__ = "jolting"
__date__ = "2018-05-11"

import config
import MySQLdb
import config
import sys
import json
import time
import xlrd
from xlrd import xldate_as_tuple
from collections import OrderedDict
from datetime import datetime


reload(sys)
sys.setdefaultencoding( "utf-8" )

class Performer(object):
    """数据形式转化"""
    def __init__(self):
        super(Performer, self).__init__()

    def create_transport(self):
        """数据库批量插入数据"""
        data = self.read_data(config.path,0,2,3)
        new_mysql_value = []
        for i in range(len(data)):
            mysql_value = []
            for key in data[i]:
                # print "%s:%s"%(key, data[i][key])
                mysql_value.append(data[i][key])
            new_mysql_value.append(mysql_value)
        print new_mysql_value

        db = MySQLdb.connect(**config.db_config)
        cursor = db.cursor()

        print "————————————————————————————————————————————————————————————————————"

        sql = 'INSERT INTO wb_logink_data(telephone,actual_departured_at,consigned_at,\
                                        origin_name,destination_address,origin_address,\
                                        actual_arrived_at,destination_name,car_sign,origin_encode,\
                                        destination_encode,line_number,plate_number,driver_name,\
                                        waybill_number,created_at,updated_at,\
                                        carrier_name,vehicle_type) \
                                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

        try:
            cursor.executemany(sql, new_mysql_value)
            print "提交数据"
            db.commit()
            print "数据库插入成功"
        except Exception,e:
            print e
            db.rollback()
        db.close()

    def read_data(self, path, sheet = 0, row = 5, col = 0):
        """读取表格测试数据"""
        try:
            workbook = xlrd.open_workbook(path, 'rb')
            sheet = workbook.sheet_by_index(sheet)
        except Exception, e:
            print str(e)

        data_list = []
        title = sheet.row_values(1)
        for i in range(row, sheet.nrows):
            data_values = OrderedDict()
            row_value = sheet.row_values(i)
            #从第二行开始遍历，根据行数获得每行的数据list
            for j in range(col, len(row_value)):
                if title[j] in ['actual_departured_at','consigned_at','actual_arrived_at','created_at','updated_at']:
                    if row_value[j] == "":
                        print i,j
                    else:
                        #将表格中读取出来日期的序列号转化为时间戳
                        date_format = xlrd.xldate.xldate_as_datetime(row_value[j], 0)
                        # date_stru= time.mktime(date_format.timetuple())
                        #datetime转化为时间戳
                        row_value[j] = date_format.strftime("%Y-%m-%d %H:%M:%S")
                        #datetime转化为字符串
                data_values[title[j]] = row_value[j]
            data_list.append(data_values)
        return data_list


if __name__ == '__main__':
    Performer().create_transport()