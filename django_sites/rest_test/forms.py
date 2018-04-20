#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from django import forms

class TestForm(forms.Form):

    name = forms.CharField(required=True)
