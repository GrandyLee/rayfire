import cx_Oracle
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ssh_address_or_host=('222.85.150.247', 10037),  # 指定ssh登录的跳转机的address
    ssh_username='root',  # 跳转机的用户
    ssh_password='123456',  # 跳转机的密码
    remote_bind_address=('172.16.17.82', 1521)
)

server.start()

db = cx_Oracle.connect('gyjg_zckj/zckj2018@127.0.0.1/gyjg')

cur = db.cursor()

