#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/13

import socket
import time
import signal
import argparse

server_socket_path = "/tmp/unix_domain_server.sock"


def signal_handler(signum, frame):
    clean()


def clean():
    for client in sockets:
        client.close()
    exit(0)


sockets = []


def main():
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser()
    parser.add_argument("name", action="store", help="usage: client.py name")
    parser.add_argument("--sleep", action="store", help="usage: client.py 10")
    args = parser.parse_args()

    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sockets.append(s)
    s.connect(server_socket_path)
    while True:
        s.send("hello, i am client %s." % args.name)
        time.sleep(float(args.sleep))


if __name__ == "__main__":
    main()
