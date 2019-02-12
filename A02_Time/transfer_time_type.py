# -*- coding:utf-8 -*-
import time
import datetime
from datetime import timedelta


class TimeTransfer(object):
    """时间转化工具"""
    def str_to_dt(self, data):
        """字符串转化为datetime类型"""
        print "字符串转化为datetime"
        print type(datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S"))
        return datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")

    def dt_to_str(self, data):
        """datetime转化为字符串"""
        print "datetime转化为字符串"
        return data.strftime("%Y-%m-%d %H:%M:%S")

    def dt_to_ts(self, data):
        """datetime转化为时间戳"""
        print "datetime转化为时间戳"
        return time.mktime(data.timetuple())

    def ts_to_dt(self, data):
        """时间戳转化为datetime"""
        return datetime.datetime.fromtimestamp(data)

    def str_to_ts(self,data):
        """字符串转化为时间戳"""
        return self.dt_to_ts(self.str_to_dt(data))

    # def select_transfer_type(self, source, result, data):
    #     """转化方法切换选择"""
    #     if source == 'str' and result == "dt":
    #         return self.str_to_dt(data)
    #     elif source == 'dt' and result == "str":
    #         return self.dt_to_str(data)
    #     elif source == 'dt' and result == "ts":
    #         return self.dt_to_ts(data)
    #     elif source == 'ts' and result == "dt":
    #         return self.ts_to_dt(data)
    #     elif source =="str" and result=="ts":
    #         return self.str_to_ts(data)
    #     else:
    #         print "需要转化的类型错误"

if  __name__=="__main__":
    data = "2018-12-07 21:40:35"
    d1 = TimeTransfer().str_to_ts(data)
    print d1