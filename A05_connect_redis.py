#encoding:utf-8
import redis

"""
一、redis连接的几种方法
二、redis内几种数据类型常用的方法

"""
#一、redis连接有几种方式

REDIS_HOST = "127.0.0.1"
REDIS_DB = 0
REDIS_PASSWORD = "admin"
REDIS_PORT = 6379

"""第1种 redis.Redis()"""
redis_config = {
    "host":REDIS_HOST,
    "db":REDIS_DB,
    "port":REDIS_PORT,
    "charset":"utf-8"
}
try:
    r1 = redis.Redis(**redis_config)
    print "方式一连接成功%s"%r1
except:
    print "方式一：redis连接异常"

print "-"*50

"""第2种 redis.StrictRedis()------在Redis和StrictRedis两个中，官方推荐StrictRedis"""
try:
    r2 = redis.StrictRedis()
    #当不传参数的时候，默认连接本地的6379端口，db为0
    print "方式二连接成功%s"%r2
except:
    print "方式二：redis连接异常"

print "*"*50

"""第3种 redis.from_url()
首先需要构造url,而url构造方式有三种模式
redis://[:password]@host:port/db    # TCP连接（常用的）
rediss://[:password]@host:port/db   # Redis TCP+SSL 连接
unix://[:password]@/path/to/socket.sock?db=db    # Redis Unix Socket 连接
"""
# REDIS_URL = "redis://:{0}@{1}:{2}/{3}".format(REDIS_PASSWORD,REDIS_HOST,REDIS_PORT,REDIS_DB)
REDIS_URL = "redis://:%s@%s:%s/%s"%(REDIS_PASSWORD,REDIS_HOST,REDIS_PORT,REDIS_DB)
#redis_url格式化的两种方式
try:
    r3 = redis.from_url(REDIS_URL)
    print "方式三连接成功%s"%r3
except Exception,e:
    print "方式三：redis连接异常,e"%e

"""第4种：构造redis连接池
tip：为什么需要连接池？
打印r1,r2,r3发现建立连接之后，每一个都会维护自己的连接池，开销比较大，所以需要建立一个公共的连接池
"""
try:
    pool = redis.ConnectionPool(**redis_config)
    r4 = redis.Redis(connection_pool = pool)
    r5 = redis.Redis(connection_pool = pool)
    print "方式四连接redis成功：r4:%s,r5:%s"%(r4,r5)

except Exception, e:
    print "方式四：redis连接异常：%s"%e
#还是不知道如何查看具体连接池，应该会有一个分配类似于id的东西去区分吧，怎么打印出来这几个连接池的唯一标识呢