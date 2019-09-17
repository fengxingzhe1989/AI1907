import pymysql
#连接数据库

db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='book',
                   charset='utf8')
#获取游标（用于操作数据库，执行sql语句，得到执行结果（
cur=db.cursor()
#执行语句
sql="insert into book values (5,'大海',20,'2018-10-01 00:00:01','中国教育出版社','gogogo');"
# 执行语句
cur.execute(sql)
#提交数据库
db.commit()

# 关闭语句
cur.close()
