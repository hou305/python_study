# -*- encoding:utf-8 -*-
from task1 import add


#这里是触发task中函数的方法，想象就像金刚到发车接口，触发之后，然后将任务在放入队列，丢给规则引擎
if __name__ == '__main__':
    print "start task"
    result  = add.delay(2,4)
    #这里只是将任务放置在队列中了，函数还未从队列中取出执行
    print 'end task..'
    print result