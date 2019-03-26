import pymysql
from sshtunnel import SSHTunnelForwarder

server = SSHTunnelForwarder(
    ssh_address_or_host=('222.85.150.247', 10037),  # 指定ssh登录的跳转机的address
    ssh_username='root',  # 跳转机的用户
    ssh_password='123456',  # 跳转机的密码
    remote_bind_address=('172.16.25.13', 3306)  # 数据库的地址及端口
)
# 启动服务
server.start()
# 连接数据库
db = pymysql.connect(
    host='127.0.0.1',  # 必须为127.0.0.1
    port=server.local_bind_port,
    user='zcsupervise',
    passwd='zcsupervise',
    db='fmsmp'
)
# 创建游标对象
cur = db.cursor()
sql = "SELECT COUNT(DISTINCT identity_card) FROM `m_manual_audit_verify` WHERE exam_date ='%s'"
prams = '2019-03-15'
cur.execute(sql % prams)

data = cur.fetchall()
# print(type(data))
result_manal_audit = data[0][0]  # 直接显示查询的数据结果，方便后续比较
print(result_manal_audit)
# data_json = json.dumps(data)
# print(type(data_json))
# print(data_json)
# pattern = re.compile(r'[^\d]+(\d+)[^\d]+') # 正则匹配数字
# res = re.findall(pattern, data_json)
# print(type(res))
# print(res[0])

cur.close()
db.close()
