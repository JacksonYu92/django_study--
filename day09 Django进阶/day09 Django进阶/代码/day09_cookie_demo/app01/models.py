from django.db import models


class UserInfo(models.Model):
    """ 用户信息表 """
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="用户名", max_length=64)
    age = models.IntegerField(verbose_name="年龄")
    mobile = models.CharField(verbose_name="手机号", max_length=11)

