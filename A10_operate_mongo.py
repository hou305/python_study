# -*-coding:utf-8 -*-

import pymongo
from pymongo import MongoClient

myclient = MongoClient('localhost',27017)
#连接mongo

db = myclient.admin
#选择数据库
db.authenticate('admin','gps-admin')

#上面的是mongo数据库连接以及用户认证

col_names = db.collection_names()
#获取集合名称，类似于mysql的表名
print cols

col = db.col_names[0]
#切换至某个集合
#获取集合下的数据
for i in col.find():
    print i

#以上是通过python直接连接mongo,操作mongo，类似于python直接连接mysql,如果需要插入数据，会使用到原生的sql语句，后面
#找资料，通过orm操作mongo db,可以不使用原生的mongo数据库语句
