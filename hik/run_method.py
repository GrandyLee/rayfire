import requests
import json



class RunMain:
    """无构造器"""
    def send_get(self, url, data):
        header = {"content-type": "application/json",
                  "Cache-Control": "no-cache",
                  "token": "cf6d9457aebf573353ca06f033a329d8"
                  }
        res = requests.get(url=url, params=data, headers=header).json()
        return res

    def send_post(self, url, data):
        header = {"content-type": "application/json",
                  "Cache-Control": "no-cache",
                  "token": "c10b1736bfd4e2883e2c56ce74b2dcc6"
                  }
        res = requests.post(url=url, data=data, headers=header).json()
        return res

    def run_main(self, url, method, data=None):
        res = None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    # url1 = "http://222.85.150.247:10011/dmsmp/login"
    # reqparams = json.dumps({"userCode": "root", "userPwd": "25d55ad283aa400af464c76d713c07ad"})
    # url2 = "http://222.85.150.247:10011/dmsmp/sysUser/pageInfo"
    # reqparams2 = json.dumps({"orgCode": "", "pageNum": "1", "pageSize": "10", "userCode": ""})
    run = RunMain()
    # resullt1 = run.run_main(url1, "POST", reqparams)
    # result2 = run.run_main(url2, "POST", reqparams2)
    # print(resullt1)
    # print(resullt1['result']['token'])
    # print(result2)

