#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   shanguiren
#   Date    :   17/4/13

import socket
import errno
import signal
import time
import os
import logging
import fcntl
import select

logging.basicConfig(level=logging.INFO)

socket_path = "/tmp/unix_domain_server.sock"


def signal_handler(signum, frame):
    if signum == signal.SIGINT:
        print("server is going to close.")
        time.sleep(3)
        exit(0)


def receive_data(conn, kqueue):
    data_buffer = []
    while True:
        try:
            data = conn.recv(1024)
            logging.info("data received: %s" % data)
            if not data:
                logging.info("The client has shut down")
                conn.close()
                break
        except socket.error as e:
            if e.args[0] in (errno.EAGAIN, errno.EWOULDBLOCK):
                logging.info("data read complete.")
                kevent = select.kevent(conn, filter=select.KQ_FILTER_READ,
                                       flags=select.KQ_EV_ADD)
                kqueue.control([kevent], 1)

                SOCKET_MAP.update({conn.fileno(): conn})
                break

            raise
        data_buffer.append(data)

    logging.info("".join(data_buffer))


SOCKET_MAP = {}


def main():
    signal.signal(signal.SIGINT, signal_handler)

    server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    SOCKET_MAP.update({server_socket.fileno(): server_socket})

    try:
        os.unlink(socket_path)
    except OSError:
        pass

    server_socket.bind(socket_path)
    server_socket.listen(10)

    kqueue = select.kqueue()
    kevent = select.kevent(server_socket, filter=select.KQ_FILTER_READ,
                           flags=select.KQ_EV_ADD)
    kqueue.control([kevent], 0, 0)
    while True:
        revents = kqueue.control(None, 1)
        for event in revents:
            if event.ident == server_socket.fileno():
                conn, address = server_socket.accept()
                logging.info("receive a client connection.")
                fcntl.fcntl(conn, fcntl.F_SETFL, os.O_NONBLOCK)
                receive_data(conn, kqueue)
            else:
                receive_data(SOCKET_MAP.get(event.ident), kqueue)


if __name__ == "__main__":
    main()
