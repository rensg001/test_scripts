#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^redirect/@@/(\d+)$', views.RedirectView.as_view(), name='redirect')
]