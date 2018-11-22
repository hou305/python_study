# -*- coding:utf-8 -*-
#author :jolting
import random
import time,datetime
import random
import json

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Generate_data(object):
    """生成测试数据"""
    def __init__(self):
        super(Generate_data, self).__init__()
        self.datas = []

    def generate_data(self, length = 5):
        """随机生成测试经纬度坐标"""
        latlngs = []
        for i in range(length):
            lat_num = str(random.randint(1, 74))
            lng_num = str(random.randint(1, 179))
            num = str(random.randint(100000000000, 9999999999999))
            lat1 = float(lat_num + '.' + num)
            lng1 = float(lng_num + '.' + num)
            latlngs.append([lat1,lng1])
        #print latlngs
        return latlngs

    def __random_plate(self, length = 5):
        """随机生成车牌几位"""
        __plate_source_alphabets = [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "J", "K",
        "L", "M", "N", "P", "Q",
        "R", "S", "T", "U", "V",
        "W", "X", "Y", "Z"]
        __plate_source_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        plate = []
        alphabet = random.randint(0, 1)
        for i in range(alphabet):
            plate.append(random.choice(__plate_source_alphabets))
        if length > alphabet:
            for i in range(length - alphabet):
                plate.append(random.choice(__plate_source_numbers))
        random.shuffle(plate)
        return "".join(plate)

    def __generate_trucks(self, number):
        """generate trucks configuration"""

        prefix = ["A", "B", "C", "D", "E", "F", "G", "H", "L"]
        range_provice = [
        u"京", u"津", u"沪", u"渝", u"蒙",
        u"新", u"藏", u"宁", u"桂", u"黑",
        u"冀", u"青", u"鲁", u"豫", u"苏",
        u"皖", u"浙", u"闽", u"赣", u"湘",
        u"鄂", u"粤", u"琼", u"甘", u"陕",
        u"贵", u"云", u"川", u"吉", u"辽",
        u"晋"
        ]
        trucks = []
        for i in range(1, number+1):
            _plate = random.choice(range_provice) + random.choice(prefix) + self.__random_plate(5)
            print _plate
            trucks.append(_plate)
        return trucks

    def generate_address(self, length):
        adrs = []
        province = [u"陕西省",u"浙江省",u"湖北省",u"福建省",u"甘肃省",u"山西省",u"河南省"]
        city = [u"西安市",u"信阳市",u"咸阳市",u"郑州市",u"新乡市",u"商洛市"]
        street = [u"距离xxxxxxxx37米",u"位于xxxxx国道",u"不明地址",u"位于隧道下"]
        for i in range(length):
            address = random.choice(province) + random.choice(city) + random.choice(street)
            print address
            adrs.append(address)
        return adrs

    def generaet_gps_data(self, length):
        """生成gps数据"""
        #time
        ti = int(time.mktime(datetime.datetime.now().timetuple()))
        plates = self.__generate_trucks(length)
        address = self.generate_address(length)
        latlngs = self.generate_data(length)
        lon,lat = latlngs[random.randint(0,length-1)][0],latlngs[random.randint(0,length-1)][1],


        for moid in plates:
            data ={
            "type":random.choice(['A','B','C']),#DataCategoryType A:LOC;B:EMS;C:ETC
            "version":"0.1",
            "provider":random.choice([1,2,3,4,5]),#ProviderType 1:G7;2:ZJXL;3:YL;4:ZQ;5:KMS
            "encode":random.choice([1,2,3]), # LocationEncodeType  1:WGS84,2:GCJ;3:BD
            "status":random.choice([1,2,3]),#状态 RUNNING:1,STOPPED:2,OFFLINE:3
            "moid":moid,
            "lon":lon,
            "lat":lat,
            "speed":round(random.randint(0,180),1),
            "direction":round(random.randint(0,180),1),
            "time":ti,
            "address":random.choice(address),
            "altitue":round(random.randint(0,180),2),
            "text":u"随机生成"
            }
            n_data = json.dumps(data)
            self.datas.append(n_data)
            #print n_data
        return self.datas
