"""
The cache object API for implementing caches. The default is a thread
safe in-memory dictionary.
"""
#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#

from threading import Lock


class BaseCache(object):

    def get(self, key):
        raise NotImplemented()

    def set(self, key, value):
        raise NotImplemented()

    def delete(self, key):
        raise NotImplemented()

    def close(self):
        pass


class DictCache(BaseCache):

    def __init__(self, init_dict=None):
        self.lock = Lock()
        self.data = init_dict or {}

    def get(self, key):
        return self.data.get(key, None)

    def set(self, key, value):
        with self.lock:
            self.data.update({key: value})

    def delete(self, key):
        with self.lock:
            if key in self.data:
                self.data.pop(key)
