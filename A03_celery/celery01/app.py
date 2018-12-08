# -*- encoding:utf-8 -*-
from send_task import app

if __name__ == '__main__':
    print "start task"
    app.send_task('send_task.add', queue='for_one',args=[56,311])
    app.send_task('send_task.multiply',queue='for_two',args=[55,2])
    #任务生产者，将add任务发送至for_add队列，args是该任务执行所需的参数
    """
    参数解析:
    ①任务路径及任务名称：给定该参数，会去这个路径下找该任务，并将该任务添加至后一个指定的队列；send_task.add:表示将哪个文件下的哪个任务放置队列中，如果给定一个错误的或者没有定义的任务，那么找不到，那就没有办法将这个任务放在队列中了
    ②队列名称：给定该参数，会将任务放置在该队列中，当worker启动中，会自动检测到该队列有任务并执行；
    ③任务所需参数：该参数执行，执行的任务所需的参数，即：add方法是需要两个参数的，如果缺少时，在添加任务至队列时，代码不会报错，在执行时报错
    """
    print 'end task..'
