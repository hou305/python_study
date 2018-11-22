# -*- coding: utf-8 -*-
import redis

"""lambda表达式，通常是在需要一个函数，但是又不想费神去命名一个函数的场合下使用，也就是指匿名函数。
语法：
lambda argument_list:expression
解释：
lambda是Python预留的关键字，argument_list和expression由用户自定义。
具体介绍如下。
argument_list：是参数列表。它的结构与Python中函数(function)的参数列表是一样的。
expression：是一个关于参数的表达式。表达式中出现的参数需要在argument_list中有定义，并且表达式只能是单行的。
lambda argument_list: expression表示的是一个函数。这个函数叫做lambda函数。
"""

#例1：在后端代码中看到过用lamnda用于连接两个redis
redis_object = dict(r1 = lambda:redis.StrictRedis(host='127.0.0.1',port=6379,db=0),r2 = lambda:redis.StrictRedis(host=localhost,port=6379,db=1))

#方式1
get_redis = lambda source :redis_object['source']()

#方式二
def get_redis(source):
    """获取redis连接"""
    return redis_object['source']()

"""
方式一和方式二都是获取redis连接，那么通过lambda一行代码就可以解决，不需要def定义函数
其中因为redis_object是一个字典，redis_object['souce']是为了获取对应key的值，即redis_object['r1']就是获取到连接到redis:db=0的库的函数
因为lambda表示的一个函数，当前我们需要获取redis的连接，而不是一个函数，所以需要在redis_object['source']后面加上()表示执行这个连接函数
"""

#例子2：与if else嵌套
exp1 = lambda x : x+1 if 2 == 1 else 0
print exp1(2)
exp2 = lambda x : x+1 if 1==1 else 0
print exp2(2)
#if 条件为真的时候返回if前面内容，否则返回0
"""lambda就是简单函数的速写，不用专门的去def定义，所有用法与def函数无差异，没什么特别神秘的"""