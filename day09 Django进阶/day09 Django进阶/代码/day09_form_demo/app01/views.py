from django.shortcuts import render, HttpResponse
from django import forms
from django.core.validators import RegexValidator


class RoleForm(forms.Form):
    user = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), ]
    )

    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={"class": "form-control"}, render_value=True)
    )

    email = forms.CharField(
        label="邮箱",
        required=False,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )

    city = forms.ChoiceField(
        choices=[(1, "北京"), (2, "上海"), (3, "深圳"), ],
        widget=forms.Select(attrs={"class": "form-control"})
    )


def add_role(request):
    if request.method == "GET":
        form = RoleForm()
        # form = RoleForm(initial={'user': "武沛齐", 'password': "123123", "email": "xx", 'city': 3})
        return render(request, 'add_role.html', {"form": form})

    # POST请求，对用户提交的数据进行校验
    form = RoleForm(data=request.POST)
    if form.is_valid():
        print("成功", form.cleaned_data)
        return HttpResponse("成功")
    else:
        # form.errors 包含了所有的错误信息
        # form对象
        print("失败", form.errors)
        return render(request, 'add_role.html', {'form': form})
