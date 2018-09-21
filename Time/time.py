# -*- coding:utf-8 -*-
"""
python处理时间主要有两个模块：time和dateime,time模块是包含各方面对时间操作的函数
https://www.jb51.net/article/87721.htm

time模块提供的函数：
    time.time(): 返回一个时间戳,数据类型是float
    time.asctime([t]): 转换gmtime()和localtime()返回的元组或struct_time为string.
    time.clock(): 在第一次调用的时候, 返回程序运行的时间. 第二次之后返回与之前的间隔.
    time.ctime([secs]): 将时间戳转换为时间字符串, 如没有提供则返回当前的时间字符串,并与asctime(localtime())一样.
    time.gmtime([secs]): 将时间戳转化为, UTC 时区的struct_time.
    time.localtime([secs]): 类似gmtime()但会把他转换成本地时区.
    time.mktime(t): struct_time 转化为时间戳.
    time.sleep(secs): 线程推迟指定时间, 以秒为单位.
    time.strftime(format[,t]): 根据参数转换一个sturc_time或元组为字符串.
    time.strptime(string[, format]): 与strftime相反,返回一个struct_time.

"""
import time

#1.返回时间戳
a = time.time()
print "数据类型为:{0},返回数据为：{1}".format(type(a),a)

#2.返回格式为字符串的时间
b1 = time.asctime() #不传参数
b2 = time.asctime(time.localtime())  #传参
print "数据类型为：{0}，不传参数返回当前时间：{1}，传参返回时间：{1}".format(type(b1),b1,b2)

#3.时间转化为字符串
b1 = time.asctime() #不传参数
b2 = time.asctime(time.localtime()) #传参：参数要为时间元组或struct_time
c1 = time.ctime()  #不传参数，这时c1==b1的
c2 = time.ctime(time.time())  #时间戳转化时间字符串
#ctime和asctime传参时，参数要求的数据类型不一致
d = time.strftime("%Y:%m:%d %H:%M:%S",time.localtime()) #时间字符串格式化  参数为：struct_time或时间元组

print "asctime返回：{0}，asctime转化时间返回：{1}，ctime时间返回：{2}，ctime时间转化：{3}，strftime时间格式化返回：{4}".format(b1,b2,c1,c2,d)
#4.返回struct_time
e = time.localtime()  #本地时间
f = time.gmtime()  #UTC时间

#5.struct_time转化为时间戳
g = time.mktime(time.localtime())

print g





