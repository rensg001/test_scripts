#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import wait


WORK_NUM = 5
CURENT_TIME = int(time.time())
WORKS = [
    ["worker1", CURENT_TIME + 10, CURENT_TIME + 30, 3],
    ["worker2", CURENT_TIME + 15, CURENT_TIME + 30, 4],
    ["worker3", CURENT_TIME + 20, CURENT_TIME + 30, 3],
    ["worker4", CURENT_TIME + 13, CURENT_TIME + 30, 5],
    ["worker5", CURENT_TIME + 25, CURENT_TIME + 30, 2],
]

def worker(args):
    worker_name, start_time, end_time, interval = args
    current_time = int(time.time())
    if current_time < start_time:
        time.sleep(start_time - current_time)
    print("thread name:{}, started, start time:{}".format(worker_name, start_time))
    while current_time < end_time:
        time.sleep(interval)
        current_time = int(time.time())
        print("thread name:{}, work done. current time:{}".format(worker_name, current_time))
    print("worker {} finished".format(worker_name))

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=len(WORKS)) as executor:
        # futures = executor.map(worker, WORKS)
        futures = [executor.submit(worker, work)for work in  WORKS]
        wait(futures)
