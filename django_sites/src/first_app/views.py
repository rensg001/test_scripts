# -*- coding: utf8 -*-
from django.shortcuts import render

# Create your views here.
from first_app.models import Test


def index(request):
    print 'request begin!'
    context = {"user": "第一个用户"}
    return render(request, "index.html", context)


def foo():
    rows = Test.objects.using('djangosecond').all()
    for row in rows:
        print(row)
