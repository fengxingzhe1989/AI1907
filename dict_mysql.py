import pymysql
import re
#连接数据库
f=open('dict.txt','r')
db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='dict',
                   charset='utf8')
#获取游标（用于操作数据库，执行sql语句，得到执行结果（
cur=db.cursor()
sql="insert into words (word,means) values (%s,%s);"
for line in f:
    tmp=line.split(' ',1)
    word=tmp[0]
    mean=tmp[1].strip()
#执行语句
    cur.execute(sql,[word,mean])
try:
#提交数据库
    db.commit()
except:
    db.rollback()

# 关闭语句
cur.close()
db.close()
