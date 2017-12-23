#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import pika
import time

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.exchange_declare("first_direct", exchange_type="direct")

channel.queue_declare("direct_q")

channel.queue_bind("direct_q", exchange="first_direct", routing_key="nimei")

def message_handler(ch, method, properties, body):
    print("开始处理消息{msg}。。。。".format(msg=body.decode("utf8")))
    time.sleep(10)
    print("消息处理完成")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(message_handler, "direct_q")
channel.start_consuming()