#coding=utf-8
import unittest
import os,sys
import requests
parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parent)

class AIbig_apiTest(unittest.TestCase):
    base_url = "https://bbs.huaweicloud.com/forum/api/rest/index.php?interface=ai_threadrank"

    def setUp(self) -> None:
        self.url = self.base_url

    def tearDown(self) -> None:
        print(self.rest_json)

    def test_api_1(self):
        with requests.get(self.url) as tr:
            self.rest_json = tr.json()
        self.assertEqual(self.rest_json['ver'],1)
        self.assertEqual(self.rest_json['rtnDesc'],'success')
if __name__ == '__main__':
    unittest.main()