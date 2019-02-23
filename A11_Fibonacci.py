# -*-encoding:utf-8 -*-
import sys
import requests

"""
迭代器与生成器，以及Fibonacci序列
迭代器两个基本的方法：
iter():创建迭代器对象
next()：输出迭代的下一个元素
"""

# list_a = [1, 2,  3, 4]
# iter_a = iter(list_a)
# print iter_a
# for i in iter_a:
#     print i
# print next(iter_a)


# #创建一个迭代器
# def MyClass(object):
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
#
# myiter = MyClass() #返回一个迭代器实例,迭代器对象，
# for i in range(5):
#     print myiter.__next__()


def fibonacci(n):#生成器函数-斐波那契
    #fibonacci算是一个生成器函数，返回一个迭代器对象
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield b
        a, b = a, a+b
        counter += 1

f = fibonacci(10) #返回一个生成器，可迭代对象
print f
