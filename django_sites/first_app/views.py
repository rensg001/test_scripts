# -*- coding: utf8 -*-
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"user": "第一个用户"}
    return render(request, "index.html", context)