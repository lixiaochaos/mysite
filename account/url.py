#!/usr/bin/env python
#-*- coding:utf8 -*-


from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^login/$', views.url_login, name='url_login'),
]