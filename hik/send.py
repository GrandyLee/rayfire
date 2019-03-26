# -*- coding: UTF-8 -*-
import requests
import json

header = {"content-type": "application/json",
          "Cache-Control": "no-cache",
          "token": "6dbba9d2dc2f7c839ab4a9a31cd89b66"
          }

def send_get(url, data):
    """ 定义send_get函数，用来接收参数，发送get请求 """
    r = requests.get(url=url, params=data)
    result = r.json()
    return result


def send_post(url, data):
    """ 定义send_post函数，用来接收参数，发送post请求 """
    r = requests.post(url=url, data=data, headers=header)
    result = r.json()
    return result


def main(url, method, data):
    """ 定义一个主函数，根据method是get或post，来调用send_post()或send_get() """
    if method == 'POST'or 'post':
        r = send_post(url, data)  # 如果是POST请求，则调用send_post()
    else:
        r = send_get(url, data)   # 如果是GET请求，则调用send_get()
    return r   # 将结果返回出去


url1 = "http://222.85.150.247:10011/dmsmp/login"
reqparams = json.dumps({"userCode": "root", "userPwd": "25d55ad283aa400af464c76d713c07ad"})

print(reqparams)

demo1 = main(url1, 'post', reqparams)
#
# token = demo['result']['token']
print(demo1)
# print(token)


url2 = "http://222.85.150.247:10011/dmsmp/sysUser/pageInfo"
reqparams2 = json.dumps({"orgCode": "", "pageNum": "1", "pageSize": "10", "userCode": ""})
demo = main(url2, 'post', reqparams2)

print(demo)




