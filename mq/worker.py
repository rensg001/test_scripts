#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import time

import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare("task_queue", durable=True)

def callback(ch, method, properties, body):
    print("[x] receive {}".format(body))

    time.sleep(str(body).count("."))

    print("[x] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback, queue="hello")

print("[x] start consuming.")

channel.start_consuming()