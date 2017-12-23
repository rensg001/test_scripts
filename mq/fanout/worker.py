#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import sys

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.exchange_declare("first_fanout", exchange_type="fanout")

channel.queue_declare(queue="q_one")
channel.queue_declare(queue="q_two")
channel.queue_bind("q_one", exchange="first_fanout")
channel.queue_bind("q_two", exchange="first_fanout")

def message_handler(ch, method, properties, body):
    print("receive message: %s" % body.decode('utf8'))
    print("process message done.")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    whoami = sys.argv[1]
    if whoami == "one":
        q_name = "q_one"
    else:
        q_name = "q_two"
    channel.basic_consume(message_handler, q_name)
    channel.start_consuming()

if __name__ == "__main__":
    main()