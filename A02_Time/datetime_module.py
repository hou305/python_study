# -*- coding:utf-8 -*-
import datetime
import time
"""
datetime模块 对于日期和时间进行简单或复杂的操作,相对于time模块，它主要有5大类,每个类包含了不同的方法

这五大类分别为：
datetime.MINYEAR 和 datetime.MAXYEAR 模块常量表示datetime接受的范围
class datetime.date: 一个理想化的日期, 提供year, month, day属性
class datetime.time: 一个理想化的时间, 提供hour, minute, second, microsecond, tzinfo.
class datetime.datetime: 日期和时间的组合.提供year, month, day, hour, minute, second, microsecond, tzinfo.
class datetime.timedelta: 表达两个date,time和datetime持续时间内的微妙差异.
class datetime.tzinfo: 时间对象的抽象基类.
"""
#一、date类

#   1: date对象由 year, month, day三部分组成; date(year, month, day)
a = datetime.date.today()
b = datetime.date(2017, 12, 12)
c = datetime.date(2017, 12, 13)
print "1.1: datetime.date, year: {0}, month: {1}, day: {2}".format(a.year, a.month, a.day)
print "1.1: 返回datetime.timedelta对象, {0}".format(c.__sub__(b))

#   2: ISO标准化日期
e = a.isocalendar()  # 一个包含三个值的元组
f = a.isoweekday()
print "1.2: ISO标准化日期, isocalendar, 返回一个元组: {0}; 元组的值依次为: {1}, {2}, {3}".format(e, e[0], e[1], e[2])
print "1.2: ISO标准化日期, isoweekday, 返回星期数, 周一为1: {0}".format(f)

#   3: 其他属性和方法
g = a.timetuple()  # 为了兼容time.localtime(...), 返回一个类型为time.struct_time的数组, 但有关时间的部分元素值为0
h = a.replace(year=2017, month=10, day=10)
# 返回一个替换指定日期字段的新date对象。参数3个可选参数，分别为year,month,day。注意替换是产生新对象，不影响原date对象。
i = time.time()
j = datetime.date.fromtimestamp(i)  # 根据一个指定的时间戳, 返回date对象
print "1.3: timetuple: {0}; ".format(g)
print "1.3: 各个属性值: {0}, {1}, {2}; 一年的天数: {3}".format(g.tm_year, g.tm_mon, g.tm_mday, g.tm_yday)
print "1.3: replace: {0}".format(h)
print "1.3: fromtimestamp, 时间戳: {0}, date对象: {1}".format(i, j)
print "1.3: format: {0}; strftime: {1}; __str__: {2}; ctime: {3}". \
    format(a.__format__("%Y--%m--%d"), a.strftime("%Y--%m--%d"), a.__str__(), a.ctime())


print "\n======二: datetime.time======\n"
# 二: time类
# time类由hour小时、minute分钟、second秒、microsecond毫秒和tzinfo五部分组成
# 相应的，time类中就有上述五个变量来存储应该的值
a_time = datetime.time(12, 20, 50, 900)
print "2.1: time: {0}, hour: {1}, minute: {2}".format(a_time, a_time.hour, a_time.minute)
# 格式化输出, 比较大小, ISO等与datetime.date 相同


print "\n======三: datetime.datetime======\n"
# 三: datetime类
# 类其实是可以看做是date类和time类的合体，其大部分的方法和属性都继承于这二个类;
# 相关的操作方法请参阅，本文上面关于二个类的介绍。其数据构成也是由这二个类所有的属性所组成的
a_datetime = datetime.datetime.now()
b_datetime = datetime.datetime.combine(a, a_time)
print "3.1: datetime: {0};".format(a_datetime)
print "3.1: date部分: {0}; 类型: {1}".format(a_datetime.date(), type(a_datetime.date()))
print "3.1: time部分: {0}; 类型: {1}".format(a_datetime.time(), type(a_datetime.time()))
print "3.1: 返回UTC时间元组: {0}".format(a_datetime.utctimetuple())
print "3.1: 将一个date对象与一个time对象合并为一个datetime对象: {0}, 类型: {1}".format(b_datetime, type(b_datetime))

# 与date和time对象相同的属性或方法
c_datetime = datetime.datetime.fromtimestamp(i)
d_datetime = a_datetime.strftime("%Y-%m-%d %H:%M:%S")
e_datetime = datetime.datetime.strptime(d_datetime, "%Y-%m-%d %H:%M:%S")
f_datetime = a_datetime.replace(month=10, day=20, hour=2, second=50)
print "3.2: 星期几: {0}".format(a_datetime.isoweekday())
print "3.2: 时间戳返回datetime对象; 时间戳: {0}, datetime对象: {1}, 类型: {2}".format(i, c_datetime, type(c_datetime))
print "3.2: timetuple: {0}".format(a_datetime.timetuple())
print "3.2: replace: {0};".format(f_datetime)
print "3.2: strftime: {0}; 类型: {1}".format(d_datetime, type(d_datetime))
print "3.2: strptime: {0}; 类型: {1}".format(e_datetime, type(e_datetime))

print "\n======四: datetime.timedelta======\n"
# 四: timedelta类
# 用来计算两个datetime对象的差值
# 差值不只是可以查看相差多少秒，还可以查看天(days), 秒(seconds), 微秒(microseconds).
a_timedelta = a_datetime - f_datetime
print "4.1: timedelta: {0}".format(a_timedelta)
print "4.1: timedelta.days: {0}; timedelta.seconds: {1} ".format(a_timedelta.days, a_timedelta.seconds)

a_datetime = datetime.datetime.now()
b_timedelta = datetime.timedelta(days=100, hours=12, minutes=20, seconds=12)
print "4.2: 初始datetime: {0};".format(a_datetime)
print "4.2: 加上timedelta后的时间: {0};".format(a_datetime + b_timedelta)
