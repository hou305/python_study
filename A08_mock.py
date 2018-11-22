# -*- coding:utf-8 -*-
#author :jolting
import sys
import unittest
import mock

def send_to_jg():
    '''这里是一个数据推送至金刚的功能，别人的接口
    推送成功返回：{success: true; errorCode: null;errorMsg: null;retryLater: null}
    推送失败返回：{success: false;errorCode: "-3";errorMsg: "服务端异常";retryLater: true}
    # '''
    # r= requests.post("http://192.168.8.0:7777/"+'post_coreOfGps')
    # result = r.json()
    # return result
    # print result['success'],result['retray_later']
    pass
#这是我们自己的方法，调用这个方法，测试
def send_to_jg_status(result):
    '''根据推送结果success or fail，判断数据是否重推'''
    if result["success"] is True and  result['retryLater'] =="null":
        return "send ok "
    elif result["success"] is False and result['retryLater'] is True:
        print (u"fail reason：%s" % result["errorMsg"])
        retry_num = result['errorCode']
        return u"send fail"
    else:
        return u"unknow exception"


class Test_send_to_jg_status(unittest.TestCase):
    '''单元测试用例'''
    def test_01(self):
        '''测试推送成功场景'''
        # mock一个推送成功的数据
        send_to_jg = mock.Mock(return_value={"success": True, "errorCode": "null", "errorMsg": "null", "retryLater": "null"})
        # 根据推送结果测试是否会重试数据推送
        status = send_to_jg_status(send_to_jg())
        print "测试推送成功的结果%s"%status
        self.assertEqual(status, u"send ok ")

    def test_02(self):
        '''测试推送失败场景'''
        # mock一个支付成功的数据
        send_to_jg = mock.Mock(return_value={"success": False,"errorCode": "-3", "errorMsg": u"服务端异常", "retryLater": True})
        # 根据推送结果测试是否会重试数据推送
        status = send_to_jg_status(send_to_jg())
        print u"测试推送失败的结果%s" % status
        self.assertEqual(status, u"send fail")


if __name__ == '__main__':
    unittest.main()


