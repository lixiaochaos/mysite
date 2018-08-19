#!/usr/bin/env python
#-*- coding:utf8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_title, name="blog_title"),
    url(r'(?P<article_id>\d)/$', views.blog_articles, name="blog_detail"),
]