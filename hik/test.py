import unittest
from hik.run_method import RunMain
from hik import HTMLTestRunner
import json


class TestMethod(unittest.TestCase):
    def setUp(self):
        self.run = RunMain()


    def test01(self):
        # 超级管理员登录系统
        url1 = "http://222.85.150.247:10011/dmsmp/login"
        reqparams = json.dumps({"userCode": "root", "userPwd": "25d55ad283aa400af464c76d713c07ad"})
        res1 = self.run.run_main(url1, 'POST', reqparams)
        print(res1)
        # re = json.loads(res1)
        self.assertEqual(res1['code'], 200, '测试失败')


    def test02(self):
        # 机构管理查询
        header = {"content-type": "application/json",
                  "Cache-Control": "no-cache",
                  "token": "c10b1736bfd4e2883e2c56ce74b2dcc6"
                  }
        url2 = "http://222.85.150.247:10011/dmsmp/sysUser/pageInfo"
        params2 = json.dumps({"orgCode": "", "pageNum": "1", "pageSize": "10", "userCode": ""})
        res2 = self.run.run_main(url2, 'POST', params2)
        print(res2)
        # re2 = json.loads(res2)
        self.assertEqual(res2['code'], 200, '测试失败')

    # def test03(self):
    #     header = {"content-type": "application/json",
    #               "Cache-Control": "no-cache",
    #               "token": "48eeba9eda8062e6e5f0e23fa13d2c33"
    #               }
    #     url3 = "http://222.85.150.247:10011/dmsmp/projectOne/overview/getAbnWarnProcessOverview"
    #     # reqparams3 = json.dumps({"orgCode": "", "pageNum": "1", "pageSize": "10", "userCode": ""})
    #     res3 = self.run.run_main(url3, 'POST', '')
    #     print(res3)
    #     # re2 = json.loads(res2)
    #     self.assertEqual(res3['code'], 200, '测试失败')


if __name__ == '__main__':
    file_name = 'G:/rayfire/hik/result/test_result.html'
    fp = open(file_name, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test01'))
    suite.addTest(TestMethod('test02'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='接口测试报告', description='测试报告如下：')
    runner.run(suite)
    fp.close()
    # unittest.main()




