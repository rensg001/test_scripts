#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os

import celery
from celery.schedules import crontab
from kombu import Exchange, Queue

from django_sites import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_sites.settings')

mq = celery.Celery('task_worker')

mq.conf.update(
    CELERY_ACCEPT_CONTENT=['json'],
    BROKER_HEARTBEAT=10,
    BROKER_HEARTBEAT_CHECKRATE=2,
    CELERY_TIMEZONE=settings.TIME_ZONE,
    BROKER_URL='amqp://127.0.0.1:5672//',
    CELERYBEAT_SCHEDULE={
        'my-foo-task': {
            'task': 'wechat.tasks.foo',
            'schedule': crontab(minute='*'),
        },
    }
)

default_exchange = Exchange('default', type='direct')

mq.conf.CELERY_QUEUES = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('hard_work', default_exchange, routing_key='hard_work')
)

mq.conf.CELERY_DEFAULT_QUEUE = 'default'
mq.conf.CELERY_DEFAULT_EXCHANGE = 'default'
mq.conf.CELERY_DEFAULT_ROUTING_KEY = 'default'

mq.conf.CELERY_ROUTES = {
    'wechat.tasks.foo': {
        'queue': 'default',
        'routing_key': 'default'
    },
    'wechat.tasks.hard_work': {
        'queue': 'hard_work',
        'routing_key': 'hard_work'
    }
}

mq.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
