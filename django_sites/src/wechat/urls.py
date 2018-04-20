# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^callback$', csrf_exempt(views.TestView.as_view()), name='callback'),
    url(r'^auth$', views.AuthTestView.as_view(), name='auth')
]
