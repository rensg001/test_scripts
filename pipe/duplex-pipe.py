#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os
import time
import multiprocessing

MAXLINE = 128


if __name__ == '__main__':
    left, right = multiprocessing.Pipe(True)

    child_pid = os.fork()
    if child_pid == 0:
        time.sleep(3)
        data = right.recv()

        if isinstance(data, bytes):
            data = data.decode('utf8')
        print('child read {}'.format(data))

        right.send(b'c')
        exit(0)

    left.send(b'p')
    data = left.recv()
    if isinstance(data, bytes):
        data = data.decode('utf8')
    print('parent receive {}'.format(data))

    os.waitpid(child_pid, 0)
    exit(0)