from django.shortcuts import render, HttpResponse, redirect
from app01 import models


def depart(request):
    """ 部门列表 """
    # queryset = [obj,obj,obj]
    # queryset = models.Department.objects.all()
    # queryset = models.Department.objects.all().order_by("id") # asc
    queryset = models.Department.objects.all().order_by("-id")  # desc
    return render(request, 'depart.html', {'queryset': queryset})


def add_depart(request):
    """ 添加部门 """

    # 显示添加部门页面
    if request.method == "GET":
        return render(request, 'add_depart.html')
    # 提交部门信息，新建
    title = request.POST.get("title")
    count = request.POST.get("count")

    models.Department.objects.create(title=title, count=count)

    # 跳转会列表页面
    return redirect("/depart/")


def delete_depart(request):
    """ 删除 """
    # http://127.0.0.1:8000/delete/depart/?id=3
    # http://127.0.0.1:8000/delete/depart/?id=4
    depart_id = request.GET.get('id')

    models.Department.objects.filter(id=depart_id).delete()

    return redirect("/depart/")


def edit_depart(request):
    """ 编辑页面 """
    # http://127.0.0.1:8000/edit/depart/?id=3

    # 从列表页面跳转过来的时候
    if request.method == "GET":
        depart_id = request.GET.get("id")
        depart_object = models.Department.objects.filter(id=depart_id).first()
        return render(request, 'edit_depart.html', {'depart_object': depart_object})

    # 编辑&提交数据
    depart_id = request.GET.get("id")
    title = request.POST.get("title")
    count = request.POST.get("count")

    models.Department.objects.filter(id=depart_id).update(title=title, count=count)

    return redirect("/depart/")
