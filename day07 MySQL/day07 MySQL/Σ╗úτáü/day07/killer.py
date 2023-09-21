import pymysql
from pymysql.cursors import DictCursor

username = input("用户名：")
password = input("密码：")

# 1.连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root123', charset="utf8", db='cmcc')
cursor = conn.cursor(cursor=DictCursor)

# 2.执行SQL语句（指令）
#   注意：SQL语句不要用之前的字符串格式化来进行操作。
cursor.execute("select * from userinfo where user=%s and pwd=%s", [username, password])
result = cursor.fetchone()

# 3.关闭连接
cursor.close()
conn.close()

if result:
    print("登录成功")
else:
    print("登录失败")
