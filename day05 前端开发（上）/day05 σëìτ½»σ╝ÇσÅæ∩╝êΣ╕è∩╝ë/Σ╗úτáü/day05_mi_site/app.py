from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index")
def index():
    return render_template('index.html')


# http://127.0.0.1:5000/search
# http://127.0.0.1:5000/search?keyword=123
@app.route("/search")
def search():
    # 获取到要搜索的关键字
    data = request.args.get('keyword')
    print(data)

    # 数据集中根据关键字搜索到数据，在页面上展示
    db1 = "中国上海移动分公司"
    db2 = "中国北京移动分公司"

    return render_template("search.html", v1=db1, v2=db2)


if __name__ == '__main__':
    app.run()
