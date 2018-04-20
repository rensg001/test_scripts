# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Users


@receiver(request_finished)
def my_callback(sender, **kwargs):
    print('Request finished!')


@receiver(post_save, sender=Users)
def my_handler(sender, **kwargs):
    with open('xxx.txt', mode=b'w') as f:
        f.write('xxx')
