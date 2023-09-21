import random
from flask import Flask, render_template

app = Flask(__name__)

# http://127.0.0.1:5000/index
@app.route("/index")
def index():
    # return "你<h1 style='color:red;'>好</h1> <a href='https://www.baidu.com'>中国移动</a>"

    # 假设从数据库中获取数据
    #  name = "上海移动"
    name = random.choice(["上海移动", "北京移动", "山东移动", "广州移动"])

    # 1.去templates目录中找 index.html 文件
    # 2.文件内容读取
    # 3.内容返回给用户浏览器
    return render_template("index.html", n1=name)

# http://127.0.0.1:5000/login
@app.route("/login")
def login():
    return "登录"


if __name__ == '__main__':
    app.run()
