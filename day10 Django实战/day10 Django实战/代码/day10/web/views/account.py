from io import BytesIO

from django import forms
from django.core.validators import RegexValidator
from django.shortcuts import render, HttpResponse, redirect

from web import models
from utils.encrypt import md5
from utils.helper import check_code


class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "输入用户名"}),
        # validators=[RegexValidator(r'^\w{6,}$', '用户名格式错误')]
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={'class': "form-control", 'placeholder': "输入密码"}, render_value=True),
    )

    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': "输入验证码"}),
    )


def login(request):
    """ 用户登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'login.html', {"form": form})

    # 判断验证码是否正确
    image_code = request.session.get("image_code")
    if not image_code:
        form.add_error("code", "验证码已过期")
        return render(request, 'login.html', {"form": form})
    if image_code.upper() != form.cleaned_data['code'].upper():
        form.add_error("code", "验证码错误")
        return render(request, 'login.html', {"form": form})

    # 验证码正确，去数据库校验用户名和密码
    user = form.cleaned_data['username']
    pwd = form.cleaned_data['password']
    encrypt_pasword = md5(pwd)
    print(user, encrypt_pasword)
    admin_object = models.Admin.objects.filter(username=user, password=encrypt_pasword).first()
    if not admin_object:
        return render(request, 'login.html', {"form": form, 'error': "用户名或密码错误"})

    request.session['info'] = {"id": admin_object.id, 'name': admin_object.username}
    request.session.set_expiry(60 * 60 * 24 * 7)

    return redirect("/home/")


def img_code(request):
    # 1.生成图片
    image_object, code_str = check_code()

    # 2.图片内容返回写入内存，从内存读取并返回
    stream = BytesIO()
    image_object.save(stream, 'png')

    # 3.图片的内容写入session中 + 60s
    request.session['image_code'] = code_str
    request.session.set_expiry(60)

    return HttpResponse(stream.getvalue())


def logout(request):
    request.session.clear()
    return redirect('/login/')


def home(request):
    # request.info_dict['name']
    return render(request, 'home.html')
