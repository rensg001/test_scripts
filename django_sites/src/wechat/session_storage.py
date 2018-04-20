#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from wechatpy.session import SessionStorage

class DatabaseStorage(SessionStorage):

    def __init__(self, cache):
        self._cache = cache

    def get(self, key, default=None):
        return self._cache.get(key, default)

    def set(self, key, value, ttl=None):
        self._cache.set(key, value, ttl)

    def delete(self, key):
        self._cache.delete(key)

    def get_ttl(self, key, default=None, version=None):
        return self._cache.get_ttl(key, default, version)