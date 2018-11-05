# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    # uname is email
    uname = models.CharField(max_length=50)
    upwd = models.CharField(max_length=20)
    uchname = models.CharField(max_length=20, null=True)
    uenname = models.CharField(max_length=20, null=True)
    # uemail = models.CharField(max_length=30, default='')
    # ushou = models.CharField(max_length=20, default='')
    # uaddress = models.CharField(max_length=100, default='')
    # uyoubian = models.CharField(max_length=6, default='')
    # uphone = models.CharField(max_length=11, default='')

    def __str__(self):
        return self.uname

# 这个表记录了上传的用户名和上传的文件信息
class UpInfo(models.Model):
    uname = models.CharField(max_length=50)
    uploadFile = models.FileField(upload_to='upapp/upload/', )

    def __str__(self):
        return self.uname