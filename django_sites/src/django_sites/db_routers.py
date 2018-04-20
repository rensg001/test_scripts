#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

class DBRouter(object):
    def db_for_read(self, model, **hints):
        "All cache read operations go to the replica"
        if model._meta.app_label == 'trees':
            return 'djangofirst'
        return None

    def db_for_write(self, model, **hints):
        "All cache write operations go to primary"
        if model._meta.app_label == 'trees':
            return 'djangofirst'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        "Only install the cache model on primary"
        print(db, app_label, model_name, hints)
        if app_label == 'trees':
            return db == 'djangofirst'
        return None