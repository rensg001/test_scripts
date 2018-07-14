#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os
import time

MAXLINE = 128


def client(readfd, writefd):
    result = []
    buff = input('请输入要打开的文件:')
    if isinstance(buff, str):
        buff = buff.encode('utf8')

    os.write(writefd, buff)

    while True:
        data = os.read(readfd, MAXLINE)
        if not data:
            break
        result.append(data)

    result = [item.decode('utf8') for item in result]
    result = ''.join(result)

    print('Server said {}'.format(result))


def server(readfd, writefd):
    path = os.read(readfd, MAXLINE)
    if not path:
        raise ValueError('empty path.')

    print('path: {}'.format(path))

    try:
        with open(path, 'r') as f:
            content = f.read()
    except IOError:
        content = 'exception'

    if isinstance(content, str):
        content = content.encode('utf8')

    print('content:{}'.format(content))
    time.sleep(3)
    os.write(writefd, content)


if __name__ == '__main__':
    readfd_1, writefd_1 = os.pipe()
    readfd_2, writefd_2 = os.pipe()

    child_pid = os.fork()
    if child_pid == 0:  # child
        os.close(readfd_2)
        os.close(writefd_1)

        server(readfd_1, writefd_2)
        exit(0)

    # parent
    os.close(readfd_1)
    os.close(writefd_2)

    client(readfd_2, writefd_1)

    os.waitpid(child_pid, 0)
    exit(0)
