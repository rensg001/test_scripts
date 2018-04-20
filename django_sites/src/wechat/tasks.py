#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import random
from time import sleep

from django_sites.mq import mq
from .models import TaskModel


@mq.task
def foo():
    TaskModel.objects.create(num=random.randint(0, 100))

@mq.task
def hard_work():
    sleep(5)
