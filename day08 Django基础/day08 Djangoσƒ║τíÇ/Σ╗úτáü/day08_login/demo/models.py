from django.db import models


class UserInfo(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=16)  # varchar
    # 可以为空
    # pwd = models.CharField(verbose_name="密码", max_length=64, null=True, blank=True)
    # 默认值
    # pwd = models.CharField(verbose_name="密码", max_length=64, default="11111")
    # 提供默认值
    pwd = models.CharField(verbose_name="密码", max_length=64)

    age = models.IntegerField(verbose_name="姓名")  # int
    email = models.CharField(verbose_name="邮箱", max_length=32)  # varchar


class Department(models.Model):
    caption = models.CharField(verbose_name="标题", max_length=32)
