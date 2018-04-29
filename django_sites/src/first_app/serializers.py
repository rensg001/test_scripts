# -*- coding: utf-8 -*-

from rest_framework import serializers
from first_app.models import Users


class UserSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, instance):
        request = self.context['request']
        return request.data.get('url', '')

    class Meta:
        model = Users
        fields = ('id', 'name', 'url')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'name')
