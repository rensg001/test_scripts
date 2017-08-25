#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import os

from fifo.server import fifo_name


def main():
    if not os.path.exists(fifo_name):
        print("fifo does not exists. client exit.")
        return

    with open(fifo_name, mode="w") as fifo:
        fifo.write("hello")


if __name__ == "__main__":
    main()
