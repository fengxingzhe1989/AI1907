import pymysql
import re
#连接数据库

db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='stu',
                   charset='utf8')
#获取游标（用于操作数据库，执行sql语句，得到执行结果（
cur=db.cursor()
with open('stu.sql','rb')as f:
    data=f.read()

sql="insert into images  values (1,%s,%s);"

#执行语句
cur.execute(sql,[data,'初恋'])
try:
#提交数据库
    db.commit()
except:
    db.rollback()

# 关闭语句
cur.close()
db.close()
