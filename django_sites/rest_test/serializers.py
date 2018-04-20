#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from rest_framework import serializers

class TestSerilalizer(serializers.Serializer):

    name = serializers.CharField()
