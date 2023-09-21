from django.db import models


class Department(models.Model):
    title = models.CharField(verbose_name="标题", max_length=32)


class User(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=12)
    age = models.IntegerField(verbose_name="年龄")
    salary = models.IntegerField(verbose_name="工资")
    depart = models.ForeignKey(verbose_name="关联部门", to="Department", on_delete=models.CASCADE)
