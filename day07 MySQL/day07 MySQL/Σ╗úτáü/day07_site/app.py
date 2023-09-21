import pymysql
from pymysql.cursors import DictCursor
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# 新增、删除、更新
def db_execute(sql, arg_list):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='shanghai', passwd='root123', charset="utf8",
                           db='day07_site')
    cursor = conn.cursor(cursor=DictCursor)
    cursor.execute(sql, arg_list)
    conn.commit()

    cursor.close()
    conn.close()


# 获取所有
def db_fetchall(sql, arg_list):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='shanghai', passwd='root123', charset="utf8",
                           db='day07_site')
    cursor = conn.cursor(cursor=DictCursor)
    cursor.execute(sql, arg_list)
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


@app.route('/phone/list')
def phone_list():
    data_list = db_fetchall("select id,mobile,city,name from phone order by id desc", [])

    # [{'id': 1, 'mobile': '15122233333', 'city': '北京', 'name': '武沛齐'}, {'id': 2, 'mobile': '15122233334', 'city': '上海', 'name': '罗浮'}, {'id': 3, 'mobile': '15122233335', 'city': '深圳', 'name': '光照'}, {'id': 4, 'mobile': '15122233336', 'city': '上海', 'name': '理解'}]
    # print(data_list)
    return render_template('phone_list.html', data_list=data_list)


# http://127.0.0.1:5000/add/phone?mobile=1&city=2&user=3
@app.route('/add/phone')
def add_phone():
    # 1.获取用户在页面上提交的数据
    mobile = request.args.get("mobile")
    city = request.args.get("city")
    user = request.args.get("user")
    # 2.保存到数据库中
    db_execute("insert into phone(mobile,city,name)values(%s,%s,%s)", [mobile, city, user])

    # 3.成功后，跳转到 /phone/list 页面
    return redirect("/phone/list")


# http://127.0.0.1:5000/delete/phone?pid=3
@app.route('/delete/phone')
def delete_phone():
    pid = request.args.get("pid")
    # 1.根据id的值对数据库中的数据进行删除
    db_execute("delete from phone where id=%s", [pid, ])

    # 2.跳转回到列表页面
    return redirect('/phone/list')


if __name__ == '__main__':
    app.run()
