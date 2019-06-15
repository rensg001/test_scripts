#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

import time

from queue import Queue
from threading import Thread, current_thread
from contextlib import contextmanager

DEFAULT_QUEUE_SIZE = 10
DEFAULT_THREAD_NUM = 10


class StopThread(object):
    pass


stop_thread = StopThread()


class ThreadPool(object):
    def __init__(self, max_threads=DEFAULT_THREAD_NUM, name=''):
        self.max_threads = max_threads
        self.name = name
        self.queue = Queue(DEFAULT_QUEUE_SIZE)
        self.workers = []
        self.waiters = []
        self.working = []

    def produce(self, func, callback=None, *args, **kwargs):
        task = (func, callback, args, kwargs)
        self.queue.put(task)

    def start(self):
        for i in range(self.max_threads):
            t = Thread(target=self._worker)
            self.workers.append(t)

        for thread in self.workers:
            thread.start()

    @contextmanager
    def state_context(self, state_list, tid):
        state_list.append(tid)
        yield
        state_list.remove(tid)

    def _worker(self):
        task = self.queue.get()
        tid = current_thread()
        while task is not stop_thread:
            with self.state_context(self.working, tid):
                func, callback, args, kwargs = task
                mark = kwargs.pop('mark', None)
                try:
                    result = func(*args, **kwargs)
                except:
                    success = False
                    result = None
                else:
                    success = True
                if callback:
                    if mark is not None:
                        callback(success, result, mark)
                    else:
                        callback(success, result)

            with self.state_context(self.waiters, tid):
                task = self.queue.get()

    def stop(self):
        for i in range(len(self.workers)):
            self.queue.put(stop_thread)

    def join(self):
        # while self.workers:
        #     for worker in self.workers:
        #         if not worker.is_alive():
        #             self.workers.remove(worker)
        #     time.sleep(1)
        for worker in self.workers:
            worker.join()

        self.workers = []


results = {}


def foo(x, y):
    time.sleep(5)
    raise ValueError
    return x + y


def callback(success, result, mark=None):
    if mark is not None:
        results[mark] = result
    else:
        print('succsss: %s, result: %s' % (success, result))


thread_pool = ThreadPool(5)

if __name__ == '__main__':
    for i in range(10):
        thread_pool.produce(foo, callback, 1, i, mark=i)

    thread_pool.start()
    thread_pool.stop()
    thread_pool.join()
    print('results:')
    print(results)
    print('program done.')
