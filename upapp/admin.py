#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import *


# Register your models here.
class UserInfoAdmin(admin.ModelAdmin):
	list_display = ['uname', 'upwd', 'uchname', 'uenname']
	list_per_page = 10

class UpInfoAdmin(admin.ModelAdmin):
	list_display = ['uname', 'uploadFile']
	list_per_page = 10


admin.site.register(UserInfo, UserInfoAdmin)
admin.site.register(UpInfo, UpInfoAdmin)
