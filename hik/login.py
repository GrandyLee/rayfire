import requests
import data
# import paramunittest
import sys
import unittest
import json
baseurl = data.base_url
interface = "/dmsmp/login"
# url1 = "http://localhost:8080/dist/index.html#/homePage"
requrl = baseurl+interface
# print(requrl)

header = {"content-type": "application/json",
          "Cache-Control": "no-cache",
          "token": "c9709fe4-9689-433c-93a0-e7bfec6e2cec"
          }
reqparams = {"userCode": data.usrname, "userPwd": "25d55ad283aa400af464c76d713c07ad"}
timeout = 10
# def login():
#     # post request exp
#     postrep = requests.post(url=requrl, headers=header, data=json.dumps(reqparams), timeout=timeout)
#     asw = json.loads(postrep.text)
#     mytoken = asw['result']['token']
#     return mytoken
#
# if __name__ == '__main__':
#     login()

postrep = requests.post(url=requrl, headers=header, data=json.dumps(reqparams), timeout=timeout)
print(postrep.status_code)
asw = json.loads(postrep.text)
mytoken = asw['result']['token']
print(mytoken)

