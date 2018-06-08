# -*- coding: utf8 -*-
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin

# Create your views here.
from first_app.models import FirstTest, Users
from first_app.serializers import UserSerializer, UserDetailSerializer


def index(request):
    print('request begin!')
    context = {"user": "第一个用户"}
    return render(request, "index.html", context)


def foo():
    rows = FirstTest.objects.all()
    for row in rows:
        print(row)


class CreateAPIView(GenericAPIView, CreateModelMixin):

    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)
        response['Location'] = response.data['url']
        return response


class UserDetailAPIView(GenericAPIView, RetrieveModelMixin):
    lookup_field = 'name'
    serializer_class = UserDetailSerializer

    def get_queryset(self):
        return Users.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
