#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

from django.conf.urls import url, include

from . import views

v1_urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^redirect/@@/(\d+)$', views.RedirectView.as_view(), name='redirect'),
    url(r'^bad$', views.BadRequestAPIView.as_view(), name='bad')
]

urlpatterns = [
    url(r'rest/', include(v1_urlpatterns, namespace='rest_v1'))
]