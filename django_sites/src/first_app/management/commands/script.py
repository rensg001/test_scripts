#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from django.core.management import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('--flag', default='aa', action='store_const', const='bb')

    def handle(self, *args, **kwargs):
        print(kwargs['flag'])