#coding=utf8
import os
import requests
import sys
import unittest
parset = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parset)

class EventTidTest(unittest.TestCase):
    def setUp(self) -> None:
        self.base_url = "https://bbs.huaweicloud.com/forum/api/rest/index.php"

    def tearDown(self) -> None:
        #结束并获取参数所有的返回参数
        print(self.resurt_json)

    def test_null_parsemt(self):
        data = {"interface":"","tid":""}
        with requests.post(self.base_url,data=data) as req:
            self.resurt_json = req.json()
        self.assertEqual(self.resurt_json['rtnCode'],10003)
        self.assertEqual(self.resurt_json['rtnDesc'],'undefined_action')

    def test_ok_parsemt(self):
        data = {"interface": "get_open_thread", "tid": 45361}
        with requests.post(self.base_url, data=data) as req:
            self.resurt_json = req.json()
        self.assertEqual(self.resurt_json['rtnCode'],'10000')
        self.assertEqual(self.resurt_json['retList']['forum_name'],'回收站',msg='验证版块')
        self.assertEqual(self.resurt_json['retList']['author'],'镜子',msg='验证用户')

