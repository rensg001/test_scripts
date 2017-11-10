#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import pika

conn = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

channel = conn.channel()

channel.queue_declare("hello")

channel.basic_publish(exchange="", routing_key="hello", body="hello world")

print("[x] send hello world.")

conn.close()