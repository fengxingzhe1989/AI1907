import pymysql


class User():
    def __init__(self,database):
        self.db=pymysql.connect(host='localhost',
                   port=3306,
                   user='root',
                   password='123456',
                   database='Trade',
                   charset='utf8')
        self.cur=self.db.cursor()
    def regester(self,name,passwd):
        sql="select * from user where name=%s;"
        self.cur.execute(sql,[name])
        r=self.cur.fetchone()

        if r:
            print('此用户名已经被占用，请重新注册')
            return False
        sql="insert into user (name,passwd) values (%s,%s) ;"
        try:
            self.cur.execute(sql,[name,passwd])
            self.db.commit()
            return True
        except:
            self.db.rollback()

    def login(self,name,passwd):
        sql="select * from user where name=%s and passwd=%s ;"
        self.cur.execute(sql,[name,passwd])
        r=self.cur.fetchone()
        if r:
            return True
        else:
            print('账号密码错误请重新登录')


if __name__ == '__main__':
    user=User('Trade')
    if user.regester('fdh','1234'):
        print('注册成功')

    if user.login('gfdsjh','748573'):
        print('登录成功')
