import time,sys,os
sys.path.append('./interface')
from HtmlTestRunner import HTMLTestRunner
import unittest
import datetime
os.path.dirname(__file__)
#指定测试用例
test_dir = "./interface"
test_dir_path = unittest.defaultTestLoader.discover(test_dir,pattern="*_test.py")
if __name__ == '__main__':
    now = datetime.datetime.now()
    file_time = now.strftime("%Y-%m-%d-%H-%M")
    time_report = os.path.dirname(__file__) + "/report/" + file_time +'.html'
    fp = open(time_report,'wb')
    run = HTMLTestRunner(
        stream=fp,
        title='huaweicloud_API',
        description='接口测试报告'
    )
    run.run(test_dir_path)