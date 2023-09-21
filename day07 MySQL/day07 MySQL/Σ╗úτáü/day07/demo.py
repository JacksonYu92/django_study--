import pymysql
from pymysql.cursors import DictCursor

# 连接MySQL（socket）
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root123', charset="utf8", db='day07')
# cursor = conn.cursor()
cursor = conn.cursor(cursor=DictCursor)

# 1.新增数据
# cursor.execute("insert into tb5(name,email,age) values('武沛齐','xx',19);")
# conn.commit()

# 2.删除
# cursor.execute("delete from tb5 where id=8;")
# conn.commit()

# 3.更新
# cursor.execute("update tb5 set age=20 where id>7;")
# conn.commit()

# 4.查询
# cursor.execute("select * from tb5")
# data_list = cursor.fetchall()
# # ( (6, 'x', 'x', 10), (9, 'wupeiqi', 'xxx@livec.om', 20), (10, '武沛齐', 'xx', 20) )
# # [{'id': 6, 'name': 'x', 'email': 'x', 'age': 10}, {'id': 9, 'name': 'wupeiqi', 'email': 'xxx@livec.om', 'age': 20}, {'id': 10, 'name': '武沛齐', 'email': 'xx', 'age': 20}]
# print(data_list)


cursor.execute("select * from tb5")
data_list = cursor.fetchone()

# {'id': 6, 'name': 'x', 'email': 'x', 'age': 10}
print(data_list)

# 关闭连接
cursor.close()
conn.close()
