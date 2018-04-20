#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from django.core.cache.backends.db import DatabaseCache
from django.db import connections, models, router
from django.utils import timezone


class TTLDatabaseCache(DatabaseCache):

    def get_ttl(self, key, default=None, version=None):
        key = self.make_key(key, version=version)
        self.validate_key(key)
        db = router.db_for_read(self.cache_model_class)
        connection = connections[db]
        table = connection.ops.quote_name(self._table)

        with connection.cursor() as cursor:
            cursor.execute("SELECT cache_key, value, expires FROM %s "
                           "WHERE cache_key = %%s" % table, [key])
            row = cursor.fetchone()
        if row is None:
            return default

        expires = row[2]
        expression = models.Expression(output_field=models.DateTimeField())
        for converter in (connection.ops.get_db_converters(expression) +
                              expression.get_db_converters(connection)):
            expires = converter(expires, expression, connection, {})

        now = timezone.now()
        if expires < now:
            return 0

        return (expires - now).seconds

class CacheRouter(object):
    """A router to control all database cache operations"""

    def db_for_read(self, model, **hints):
        "All cache read operations go to the replica"
        if model._meta.app_label == 'django_cache':
            return 'djangosecond'
        return None

    def db_for_write(self, model, **hints):
        "All cache write operations go to primary"
        if model._meta.app_label == 'django_cache':
            return 'djangosecond'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        "Only install the cache model on primary"
        if app_label == 'django_cache':
            return db == 'djangosecond'
        return None