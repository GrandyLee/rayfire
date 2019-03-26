import pymysql
import json
f = open('entrance_statics.sql', 'r')
sql_test=[]
for line in f:
    sql_test.append(line.strip('\n'))
print(sql_test)

# 连接数据库
connect = pymysql.Connect(host='10.197.236.152',    # 远程主机的IP地址
                          user='root',    # mysql用户名
                          db='fmsmp', # 数据库名字
                          passwd='123456',  # 数据库密码
                          port=3306,  # 数据库端口
                          charset='utf8')  # 指定编码

# 创建游标对象
cursor = connect.cursor()
i = 0
while i < len(sql_test):
    print(i)
    print(sql_test[i])
    cursor.execute(sql_test[i])
    connect.commit()  # 提交保存
    i += 1
f.close()

cursor.close()
connect.close()
try:
    cursor.execute(sql_test)
    data = cursor.fetchall()
    data1 = json.loads(data)
    print(data1)

# noinspection PyBroadException
except:
    connect.rollback()

cursor.execute(sql_test)
data = cursor.fetchall()
print(data)
