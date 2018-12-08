# -*-coding:utf-8 -*-

import pymongo
from pymongo import MongoClient

myclient = MongoClient('localhost',27017)
#连接mongo

# db = myclient.admin
# 或者写法
db = myclient['admin']
#选择数据库
db.authenticate('admin','gps-admin')

#上面的是mongo数据库连接以及用户认证

col_names = db.collection_names()
#获取集合名称，类似于mysql的表名
print col_names

locations = db.col_names[0]
#切换至某个集合
#获取集合下的数据
for i in locations.find():
    print i

#以上是通过python直接连接mongo,操作mongo，类似于python直接连接mysql,如果需要插入数据，会使用到原生的sql语句，后面
#找资料，通过orm操作mongo db,可以不使用原生的mongo数据库语句
#后面表示需要查询返回的字段，mongo规定除过id可以随意设定为0或者1，表示不返回和返回，其他的字段不允许交叉出现设置有为0和1的情况设置为
#除了 _id 你不能在一个对象中同时指定 0 和 1，如果你设置了一个字段为 0，则其他都为 1，反之亦然。
for data in locations.find({},{"__id":0}):
    print data


"""3.1 条件操作符
"$lt"===================>"<"
"$lte"==================>"<="
"$gt"===================>">"
"$gte"==================>">="
"$ne"===================>"!="
"""
fixtime = ""
import time
import datetime
timearry = time.strptime("fixtime","%Y-%m-%d %H:%M:%S" )
data = locations.find({"x":{"gt":10}})