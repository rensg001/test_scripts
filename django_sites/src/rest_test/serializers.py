#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from rest_framework import serializers
from .models import RestTest


class TestSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestTest
        fields = ('name', )
