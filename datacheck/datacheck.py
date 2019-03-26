import os
from sshtunnel import SSHTunnelForwarder
import pymysql

import paramiko
pwd = os.getcwd()

"""
通过跳板机，连接远程mysql数据库
author: liweixin
time: 2019-03-21
"""
server = SSHTunnelForwarder(
    ssh_address_or_host=('222.85.150.247', 10037),  # 指定ssh登录的跳板机的address
    ssh_username="root",  # 跳板机的用户
    ssh_password="123456",  # 跳板机用户的密码
    local_bind_address=('127.0.0.1', 3306),  # 本地绑定的端口
    remote_bind_address=('172.16.25.13', 3306)  # 远程绑定的端口
 )

server.start() # 启动服务
# 数据库连接配置，host默认127.0.0.1不用修改
conn = pymysql.connect(
    host='127.0.0.1',  # 此处必须为127.0.0.1
    port=3306,  # 数据库的端口
    user='zcsupervise',  # 用户名
    password='zcsupervise',  # 密码
    db='fmsmp',  # 数据库名
    )
# 创建游标
cursor = conn.cursor()

# 获取游标
cursor1 = conn.cursor(cursor=pymysql.cursors.DictCursor)
# 查询数据库，查询一条数据，其他CURD操作类似
sql = "SELECT * FROM `m_manual_audit_verify` WHERE exam_date ='%s'"
prams = '2019-03-15'
cursor1.execute(sql % prams)
info = cursor1.fetchone()
print(info)
# 关闭连接
cursor1.close()
conn.close()





