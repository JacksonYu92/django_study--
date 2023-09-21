from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/register")
def register():
    return render_template("register.html")


# http://127.0.0.1:5000/do/register?user=wupeiqi&pwd=123&gender=%E7%94%B7&city=%E6%9D%AD%E5%B7%9E&hobby=1&hobby=2&more=%E5%8F%91%E6%96%B9%E6%B3%95
@app.route("/do/register")
def do_register():
    # 1.在URL中获取数据
    username = request.args.get('user')
    password = request.args.get('pwd')
    gender = request.args.get('gender')
    city = request.args.get('city')
    hobby = request.args.getlist('hobby')
    more = request.args.get('more')

    # 2.写入文件
    line = "{}|{}|{}\n".format(username, password, gender)
    file_object = open("db.txt", mode='a', encoding='utf-8')
    file_object.write(line)
    file_object.close()

    # return "执行了注册"
    return redirect("/user/list")


# http://127.0.0.1:5000/user/list
@app.route('/user/list')
def user_list():

    # wupeiqi|123|男
    # 光照|123333|女
    # 熊试听|qweqwe|男
    # ["wupeiqi|123|男", "光照|123333|女", "熊试听|qweqwe|男"]
    data_list = []
    # 1.读取文件中的所有用户
    file_object = open("db.txt", mode='r', encoding='utf-8')
    for line in file_object:
        line = line.strip()
        data_list.append(line)
    file_object.close()
    # print(data_list)

    # [  ["wupeiqi", 123,男"], ["wupeiqi", 123,男"], ["wupeiqi", 123,男"] ]
    data_list_list = []
    # 1.读取文件中的所有用户
    file_object = open("db.txt", mode='r', encoding='utf-8')
    for line in file_object:
        line = line.strip()
        data_list_list.append(line.split("|"))
    file_object.close()
    # print(data_list)

    # 2.在页面上展示出来
    return render_template('user_list.html',v1=data_list,v2=data_list_list)


if __name__ == '__main__':
    app.run()
