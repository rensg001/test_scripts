#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user/new', views.CreateAPIView.as_view(), name='user_new'),
    url(r'^user/(?P<name>\w+)', views.UserDetailAPIView.as_view(), name='user_name')
]
