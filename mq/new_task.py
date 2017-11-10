#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import sys

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare("task_queue", durable=True)

message = " ".join(sys.argv[1:]) or "hello world"

channel.basic_publish(exchange="",
                      routing_key="hello",
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))

print("[x] sent message {}".format(message))

conn.close()