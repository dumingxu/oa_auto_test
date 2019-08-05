# coding=utf-8
from time import sleep
from TestCase.Test_GM_Form import Test_Document
import unittest
from public.Common.Doexcel import *
from config.globalconfig import *
from public.Common.function import send_mail        # 导入发送邮件模块
from public.Common.function import latest_report    # 导入获取最新报告模块
from HTMLTestRunner import HTMLTestRunner           # 导入HTMLTestRunner模块
import time

Case_path = TestCase_path       # 测试用例存放路径


# 获取所有测试用例
def get_allcase():
    discover = unittest.defaultTestLoader.discover(Case_path, pattern="test*.py")
    suite = unittest.TestSuite()
    suite.addTest(discover)
    return suite

if __name__ == '__main__':
    # 顺序加载用例使用此方法
    # suit = unittest.TestSuite()
    # suit.addTest(Tets_Document("test_SendToSign"))
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suit)
    # 加载测试  用例下所有以test开头的测试用例

## ========   下面代码为运行所有测试用例并将最新报告已邮件形式发送  ======= ##

    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = report_path + '\\' + now + 'result.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='OA单据自动化测试报告',
                            description='用例执行情况: ')
    # runner = unittest.TextTestRunner(verbosity=2)
    runner.run(get_allcase())
    fp.close()

    new_report = latest_report(report_path)  # 获取最新测试报告
    send_mail(new_report)                    # 发送测试报告