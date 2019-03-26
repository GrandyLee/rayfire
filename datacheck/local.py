import pymysql


db = pymysql.connect(host='127.0.0.1',  # 数据库地址
                     user='root',  # 用户名
                     db='test',  # 应用的数据库名
                     passwd='123456',  # 用户密码
                     port=3306,  # 端口
                     charset='utf8'  # 编码规则
                     )

# 创建游标
cursor = db.cursor()
search_stu = "SELECT * FROM `students` where sno = %s"
prams = '108'
cursor.execute(search_stu % prams)
info = cursor.fetchone()
print(info)
# 关闭连接
cursor.close()
db.close()
