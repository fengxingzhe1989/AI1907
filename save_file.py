"""
save_file.py
二进制文件存取示例
"""

import pymysql

# 连接数据库
db = pymysql.connect(user='root',
                     password = '123456',
                     database = 'stu',
                     charset='utf8')

# 获取游标 (操作数据库,执行sql语句,得到执行结果)
cur = db.cursor()

# 执行语句

# 存入图片
# with open('0.jpg','rb') as f:
#     data = f.read()
#
# sql = "insert into images values (1,%s,%s)"
# cur.execute(sql,[data,'初恋'])
# db.commit()

# 提取图片
sql = "select photo from images \
where comment='初恋'"
cur.execute(sql)
data = cur.fetchone()[0]
with open('1.jpg','wb') as f:
    f.write(data)

# 关闭游标
cur.close()

# 关闭数据库
db.close()

