from django.shortcuts import render, redirect


# http://127.0.0.1:8000/login/  GET
# http://127.0.0.1:8000/login/  POST
def login(request):
    # 判断到底是POST还是GET请求
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 去请求体中获取数据，再进行校验 {user:....,pwd:....}
        username = request.POST.get('user')
        password = request.POST.get('pwd')

        # 去数据库中校验，用户名&密码的合法性
        # 成功，跳转到后台管理界面 http://127.0.0.1:8000/index/     /index/
        # return redirect('/index/')
        # 不成功，再次让用户看到 login.html页面 -> 用户名或密码错误
        # return render(request, 'login.html', {"error": "用户名或密码错误"})
        if username == 'root' and password == "123":
            return redirect('/index/')
        else:
            return render(request, 'login.html', {"error": "用户名或密码错误"})


def index(request):
    # 1.数据库获取
    queryset = [
        {"id": 1, 'phone': "1888888888", "city": "上海"},
        {"id": 2, 'phone': "1888888882", "city": "北京"},
        {"id": 3, 'phone': "1888888883", "city": "上海"},
        {"id": 4, 'phone': "1888888884", "city": "上海"},
    ]

    # 2.展示渲染
    return render(request, 'index.html',{"queryset":queryset})
