from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse


def login(request):
    # return HttpResponse("登录页面")
    # return render(request, "login.html")
    # return redirect("https://www.baidu.com")
    return render(request, "login.html")


def user_list(request):
    # 1.数据库获取所有的用户列表
    data = ["武沛齐", "李立权", "张弛"]

    mapping = {"name": "武沛齐", "age": 19, "size": 18}

    # 2.打开文件并读取内容
    # 3.模板的渲染 -> 文本替换
    return render(request, "user_list.html", {"message": "标题来了", "data_list": data, "xx": mapping})


def phone_list(request):
    # 1.获取数据
    queryset = [
        {"id": 1, 'phone': "1888888888", "city": "上海"},
        {"id": 2, 'phone': "1888888882", "city": "北京"},
        {"id": 3, 'phone': "1888888883", "city": "上海"},
        {"id": 4, 'phone': "1888888884", "city": "上海"},
    ]

    # 2.通过页面渲染返回给用户（表格）
    return render(request, 'phone_list.html', {"data": queryset})
