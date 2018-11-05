#/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^$', index),
    # url(r'^register$', register),
    url(r'^login/$', login),
    url(r'^login_handle/$', login_handle),
    url(r'^logout/$', logout),
]

