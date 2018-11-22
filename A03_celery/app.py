# -*- encoding:utf-8 -*-
from send_task import add


if __name__ == '__main__':
    print "start task"
    #这里只是将任务放置在队列中了
    result = add.delay(45,34)
    t =result.get()
    print 'end task..'
