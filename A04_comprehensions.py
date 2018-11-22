#encoding:utf-8
"""
推导式comprehensions（又称解析式），是Python的一种独有特性。推导式是可以从一个数据序列构建另一个新的数据序列的结构体。 共有三种推导，在Python2和3中都有支持：

列表(list)推导式
字典(dict)推导式
集合(set)推导式
"""
#一、列表推导式

#表达式：[exp for val in collection if condition] #列表推导式

l = [1,2,3,4,5]

t = [i*i for i in l if i>2]
print t
eg1 = [i*i for i in range(0,30) if i % 3 ==0]
print eg1

#二字典推导式
#表达式 d = {key: value for (key, value) in iterable}
d = {"1":"Monday", "2":"Tuesday", "3":"Wendsday"}
d1 = {d[key]: key for key in d}
print d1

#三、集合推导式
l = [1,2,34,3]
s = {i*2 for i in l}
print s

