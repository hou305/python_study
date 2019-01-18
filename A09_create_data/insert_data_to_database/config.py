# -*- coding:utf-8 -*-

_author__ = "jolting"
__date__ = "2018-05-11"

import random
import collections
import os
"""test data"""
db_config = {
        "host":"127.0.0.1",
        "user":"root",
        "passwd":"root",
        "db":"test",
        "port":3306,
        "charset":"utf8"
}

root = r"E:\Global_Transport"
file_name = "0.2.1test.xlsx"
path = os.path.abspath(os.path.join(root, file_name))
print path
