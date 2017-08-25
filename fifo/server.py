#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

import os
import errno

fifo_name = "/tmp/fifo.serv"


def listen_fifo():
    with open(fifo_name, mode="r") as fifo:
        while True:
            data = fifo.read()
            if len(data) == 0:
                return
            print("receive data: {}".format(data))


def main():
    try:
        os.mkfifo(fifo_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("create fifo fail because: {}".format(e))

    while True:
        listen_fifo()


if __name__ == "__main__":
    main()
