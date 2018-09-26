#encoding:utf-8
from lxml import etree
import lxml.html.soupparser as soupparser

"""
lxml框架解析html页面
from lxml import etree
一、etree
1.etree.HTML方法,把html的文本内容解析成html对象
2.etree.tostring方法,打印html内容，可以设置encoding="utf-8"参数，pretty_print=True,
以标准格式输出

"""

#html解析
htmldemo = '''
<meta charset="UTF-8"> <!-- for HTML5 -->
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<html><head><title>yoyo ketang</title></head>
<body>
<b><!--Hey, this in comment!--></b>
<p class="title"><b>yoyoketang</b></p>
<p class="yoyo">这里是我的微信公众号：yoyoketang
<a href="http://www.cnblogs.com/yoyoketang/tag/fiddler/" class="sister" id="link1">fiddler教程</a>,
<a href="http://www.cnblogs.com/yoyoketang/tag/python/" class="sister" id="link2">python笔记</a>,
<a href="http://www.cnblogs.com/yoyoketang/tag/selenium/" class="sister" id="link3">selenium文档</a>;
快来关注吧！</p>
<p class="story">...</p>
'''


#etree.HTML解析html内容
demo = etree.HTML(htmldemo)
t = etree.tostring(demo,encoding="utf-8",pretty_print=True)
print type(t)
print "---------------------------"
print type(t.decode('utf-8'))

"""
二、soupparser解析器
import lxml.html.soupparser
soupparser解析器比上面的etree.HTML容错性要好一点.
因为其处理不规范的html的能力比etree强太多。
执行之后报错，原来必须用到beautifulsoup模块，所以如果没有安装beautifulsoup，此方法是不行的
"""
demo1 = soupparser.fromstring(htmldemo)
t1 = etree.tostring(demo1, encoding="utf-8", pretty_print=True)
print type(demo1),t


"""
三、xpath方法查找html中元素以及文本
1.解析html，返回html对象,还是用上面的demo
2.通过xpath的方法去定位元素，必须要对xpath定位元素的方法比较熟悉
3.二次查找的话可以将返回的html再通过xpath的方式定位
"""
# #定位"这里是我的微信公众号：yoyoketang"
# nodes = demo.xpath('//p[@class="yoyo"]')
# # print type(nodes),nodes[0].text
# #返回的nodes是一个list对象,class下的所有元素，每一个都是html元素对象
for ele in nodes:
    print etree.tostring(ele, encoding="utf-8", pretty_print=True)
    node1s = ele.xpath('//a[@class="sister"]')
    for i in range(len(node1s)):
        print node1s[i].text


# #二次查找
nodes_child = nodes[0].xpath('//a[@class="sister"]')



