#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare("hello")

def callback(ch, method, properties, body):
    print("receive message {}".format(body))

channel.basic_consume(callback, "hello", no_ack=True)

print("ready to receive message from hello queue.")

channel.start_consuming()