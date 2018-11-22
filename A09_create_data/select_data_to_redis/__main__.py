#-*- encoding:utf-8 -*-
#date=2018-09-11
#author=jolting
import threading
import time

from performer import insert_trans_to_redis1,insert_trans_to_redis2
threads = []
t1= threading.Thread(target=insert_trans_to_redis1)
threads.append(t1)
t2= threading.Thread(target=insert_trans_to_redis2)
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    #join()阻塞线程
    print u"all over %s"%time.ctime()
