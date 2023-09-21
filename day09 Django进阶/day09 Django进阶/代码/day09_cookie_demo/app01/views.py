from django.shortcuts import render, redirect, HttpResponse
from app01 import models


def login(request):
    """ 用户登录 """
    if request.method == "GET":
        return render(request, 'login.html')

    user = request.POST.get('user')
    pwd = request.POST.get('pwd')

    # 数据库中校验...
    #    - MySQL，创建库&mysqlclient
    #    - sqlite，文件数据，类似于access
    user_object = models.UserInfo.objects.filter(username=user, password=pwd).first()
    if user_object:
        """
        1.生成随机字符串
        2.返回到用户浏览器的cookie中
        3.存储到网站的session中 随机字符串+用户标识
        """
        request.session["info"] = {"name": user_object.username, 'id': user_object.id}
        return redirect("/home/")
    else:
        # 如果失败，展示错误信息
        return render(request, 'login.html', {'error': "用户名或密码错误"})


def home(request):
    # 判断用户是否已登录，未登录跳转回登录页面
    info_dict = request.info_dict
    return render(request, "home.html", {"info_dict": info_dict})


def order(request):
    return render(request, 'order.html')
